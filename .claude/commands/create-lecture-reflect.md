---
description: 사용자 수정 후 피드백을 캡처하여 학습 메모리에 반영
argument-hint: <강의폴더경로>
---

# Create Lecture Reflect - 피드백 캡처 스킬

사용자가 `/create-lecture`로 생성된 `lecture.md`를 수동 수정한 뒤 실행하는 **피드백 캡처 스킬**입니다.
생성된 결과물과 사용자 수정본의 차이를 분석하여 교훈을 추출하고, 다음 파이프라인 실행 시 같은 실수를 반복하지 않도록 학습 메모리를 업데이트합니다.

## 사용법

```
/create-lecture-reflect lectures/lecture-XX-주제명
```

## 전제 조건

- `${LECTURE_DIR}/.work/generated-lecture.md.snapshot` 파일이 존재해야 합니다 (Phase 5에서 자동 생성)
- `${LECTURE_DIR}/lecture.md`에 사용자 수정이 반영되어 있어야 합니다

## 워크플로우

### Step 1: 인자 파싱 및 검증

`$ARGUMENTS`에서 강의 폴더 경로를 추출합니다:

```
LECTURE_DIR = $ARGUMENTS의 첫 번째 인자
```

**검증 (Bash 도구)**:

```bash
# 1. 스냅샷 존재 확인
ls ${LECTURE_DIR}/.work/generated-lecture.md.snapshot 2>/dev/null || echo "ERROR: 스냅샷 없음. /create-lecture를 먼저 실행하세요."

# 2. 현재 lecture.md 존재 확인
ls ${LECTURE_DIR}/lecture.md 2>/dev/null || echo "ERROR: lecture.md 없음"

# 3. learnings 파일 존재 확인
ls .claude/learnings/create-lecture.md 2>/dev/null || echo "ERROR: learnings 파일 없음"
```

검증 실패 시 사용자에게 보고하고 중단합니다.

### Step 2: 변경 사항 분석

**데이터 준비 (Main Agent 실행)**:

1. `${LECTURE_DIR}/.work/generated-lecture.md.snapshot`을 Read 도구로 읽기
2. `${LECTURE_DIR}/lecture.md`를 Read 도구로 읽기
3. 두 파일의 차이를 Bash 도구로 추출:

```bash
diff ${LECTURE_DIR}/.work/generated-lecture.md.snapshot ${LECTURE_DIR}/lecture.md || true
```

### Step 3: 교훈 추출 (retrospective-agent 호출)

```
subagent_type: retrospective-agent
description: "사용자 수정 피드백에서 교훈 추출"
prompt: |
  사용자가 자동 생성된 강의 슬라이드를 수정했습니다. 변경 사항을 분석하여 교훈을 추출해주세요.

  **강의 폴더:** ${LECTURE_DIR}
  **강의명:** ${LECTURE_DIR에서 추출한 강의명}

  **원본 (자동 생성본):**
  {generated-lecture.md.snapshot 전문}

  **수정본 (사용자 수정본):**
  {lecture.md 전문}

  **diff 결과:**
  {diff 출력}

  **기존 학습 메모리:**
  {learnings/create-lecture.md 전문}

  **분석 요청:**

  1. 변경 사항을 다음 카테고리로 분류:
     - 삭제된 슬라이드 → "불필요한 콘텐츠" 교훈
     - 추가된 슬라이드 → "누락된 콘텐츠" 교훈
     - 텍스트 수정 → "표현/톤 개선" 교훈
     - 레이아웃 변경 → "디자인 패턴 개선" 교훈

  2. 각 변경에서 일반화 가능한 교훈 추출
     - 이 강의에만 해당하는 내용은 제외
     - 향후 모든 강의에 적용 가능한 패턴만 추출

  3. 추출된 교훈을 learnings/create-lecture.md에 추가
     - 기존 항목과 중복 확인
     - 적절한 카테고리에 배치
     - 형식: `- [날짜 강의명] 문제 설명 → 재발방지 규칙`

  4. 반복 패턴 확인
     - 동일 교훈이 3회 이상이면 "반복 패턴"으로 승격
     - CSS/SVG/레이아웃 관련 반복 패턴은 create-lecture-templates.md 반영 제안

  **출력:**
  1. learnings/create-lecture.md를 Edit 도구로 업데이트
  2. 변경 요약을 반환 (감지된 변경 수, 추출된 교훈 수, 반복 패턴 승격 여부)
```

### Step 4: 완료 보고

retrospective-agent의 결과를 기반으로 사용자에게 보고합니다:

```
📝 피드백 캡처 완료!

감지된 변경: {N}건
- 삭제: {N} 슬라이드
- 수정: {N} 슬라이드
- 추가: {N} 슬라이드
- 레이아웃: {N} 슬라이드

추출된 교훈: {N}건
{각 교훈 요약}

learnings/create-lecture.md 업데이트 완료.
{반복 패턴 승격이 있으면 해당 내용 안내}
{create-lecture-templates.md 반영 제안이 있으면 안내}

💡 다음 /create-lecture 실행 시 이 교훈들이 자동으로 반영됩니다.
```

## 주의사항

- 스냅샷이 없으면 비교 불가 → `/create-lecture`를 먼저 실행해야 함
- 모든 출력은 **한국어**로 작성
- 교훈은 일반화 가능한 것만 추출 (강의별 특수 사항 제외)
- learnings 파일의 50줄 상한 유지
