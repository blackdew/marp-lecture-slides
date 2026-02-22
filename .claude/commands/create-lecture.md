---
description: requirements.md로부터 완성된 Marp 강의를 자동 생성
argument-hint: <강의폴더경로> [--issue <번호>] [--plan-only] [--no-images] [--rebuild]
---

# Create Lecture - 강의 제작 파이프라인

`requirements.md`로부터 완성된 Marp 프레젠테이션까지 전체 워크플로우를 자동화합니다.
**7개의 전문 에이전트**가 10-Phase 파이프라인(학습 주입 → AC 추출 → 분석 → 교차 검증 → 설계 → 설계 평가 → 제작 → 콘텐츠 평가 → 검증 → 회고)으로 협업하며,
실행할 때마다 과거 교훈을 학습하여 점점 더 좋은 결과물을 만들어내는 **자기 개선 루프**를 갖추고 있습니다.

## 사용법

```
/create-lecture lectures/lecture-XX-주제명 [options]
```

### 옵션

| 옵션 | 설명 |
|------|------|
| `--issue <번호>` | GitHub 이슈 연동 (댓글·close 자동화) |
| `--plan-only` | Phase 1-2 (분석/설계)까지만 실행 |
| `--no-images` | SVG 이미지 생성 건너뛰기 (기존 이미지 재활용) |
| `--rebuild` | Phase 3-4만 재실행 (분석/설계 결과 재활용) |

> **`--issue` 사용 예시**:
> - `--issue 13` → 이슈 #13의 요구사항을 반영하여 강의 생성/수정, 완료 후 이슈 close
> - `--issue 13 --plan-only` → 설계까지만 진행하고 이슈에 설계 완료 댓글 (close 안 함)
> - `--issue 13 --rebuild` → 기존 분석/설계 재활용하여 재제작, 완료 후 이슈 close

## 워크플로우 개요

```
Pre-flight: 환경 검증 (+이슈 검증)
    ↓
Phase 0: 학습 주입 (Main Agent)  ← 자기 개선 루프
  ├── learnings/create-lecture.md 읽기 → 모든 에이전트 프롬프트에 주입
  └── 💬 이슈 시작 댓글 (--issue 시)
    ↓
Phase 0.5: Acceptance Criteria 추출 (Main Agent)  ← 신규
  └── requirements.md → .work/acceptance-criteria.md (MUST/SHOULD 체크리스트)
    ↓
Phase 1: 분석 (lecture-analyst ×3 병렬)
  ├── 1-1 Audience Analyst → .work/audience-analysis.md
  ├── 1-2 Topic Researcher → .work/topic-research.md
  ├── 1-3 Reference Analyzer → .work/reference-analysis.md
  └── 📎 이슈 본문을 추가 컨텍스트로 주입 (--issue 시)
    ↓ [품질 게이트 G1: 3개 분석 완성]
Phase 1.5: 교차 검증 (Main Agent)  ← 신규
  └── 3개 분석의 충돌/갭 → .work/cross-validation.md
    ↓
Phase 2: 설계 (instructional-designer ×1 순차)  ← 프롬프트 강화
  └── Instructional Designer → outline.md (갱신)
    ↓ [품질 게이트 G2: 시간 합계 = 강의 시간]
Phase 2.5: 설계 루브릭 평가 (rubric-evaluator ×1)  ← 신규
  └── rubric-evaluator (design 모드) → .work/rubric-report-design.md
    ↓ [루브릭 게이트 RG1: 80점 이상 합격]
    ↓ 💬 설계 완료 댓글 (--issue 시)
    ↓ [--plan-only 시 종료]
Phase 3: 제작 (slide-writer → visual-designer + lab 병렬)
  ├── 3-1 Slide Writer → lecture.md (먼저 실행)
  ├── 3-2 Visual Designer → images/*.svg (3-1 완료 후)
  └── 3-3 Lab Designer → .work/lab-sections.md (3-1 완료 후)
    ↓ [통합: lab-sections.md → lecture.md에 병합]
    ↓ [품질 게이트 G3: Marp 빌드 성공]
Phase 3.5: 콘텐츠 루브릭 평가 (rubric-evaluator ×1)  ← 신규
  └── rubric-evaluator (content 모드) → .work/rubric-report-content.md
    ↓ [루브릭 게이트 RG2: 80점 이상 합격]
Phase 4: 검증 & 빌드 (lecture-reviewer ×1 순차)  ← 검증 항목 확대
  ├── Quality Reviewer → .work/review-report.md (근본원인 분석 + MUST 충족 현황)
  └── 빌드: generate-presentation.sh
    ↓ [품질 게이트 G4: 리뷰 이슈 0건]
Phase 5: 회고 & 학습 (retrospective-agent ×1)  ← 자기 개선 루프 + 카테고리 확장
  ├── review-report.md + rubric-report-*.md에서 교훈 추출
  ├── .work/generated-lecture.md.snapshot 저장
  └── learnings/create-lecture.md 업데이트
    ↓
완료: HTML 파일 경로 출력 + 루브릭 점수 표시
  └── 💬 이슈 완료 댓글 + 커밋 + close (--issue 시)
```

---

## 전체 워크플로우

### Pre-flight: 환경 검증

다른 Phase에 앞서 반드시 실행. **검증 실패 시 사용자에게 보고하고 중단**.

#### 인자 파싱

`$ARGUMENTS`에서 다음을 추출합니다:

**첫 번째 인자** (필수): 강의 폴더 경로
- 예: `lectures/lecture-12-new-topic`
- `LECTURE_DIR` 변수로 저장

**옵션 플래그** (선택, 순서 무관):
- `--issue <번호>` → `ISSUE_NUMBER=<번호>` (다음 인자를 번호로 취급)
- `--plan-only` → `PLAN_ONLY=true`
- `--no-images` → `NO_IMAGES=true`
- `--rebuild` → `REBUILD=true`

**파싱 예시**:
- 입력: `lectures/lecture-12-topic --plan-only` → `LECTURE_DIR=lectures/lecture-12-topic`, `PLAN_ONLY=true`
- 입력: `lectures/lecture-12-topic --rebuild --no-images` → `REBUILD=true`, `NO_IMAGES=true`
- 입력: `lectures/lecture-12-topic --issue 13` → `ISSUE_NUMBER=13`
- 입력: `lectures/lecture-12-topic --issue 13 --rebuild` → `ISSUE_NUMBER=13`, `REBUILD=true`

#### 환경 검증

Main agent가 Bash 도구로 다음 명령을 실행합니다:

```bash
# 1. 강의 폴더 존재 확인
ls ${LECTURE_DIR} 2>/dev/null || echo "ERROR: 폴더 없음: ${LECTURE_DIR}"

# 2. requirements.md 존재 확인
ls ${LECTURE_DIR}/requirements.md 2>/dev/null || echo "ERROR: requirements.md 없음"

# 3. .work 디렉토리 생성
mkdir -p ${LECTURE_DIR}/.work

# 4. images 디렉토리 생성
mkdir -p ${LECTURE_DIR}/images

# 5. Marp CLI 설치 확인
which marp || echo "WARNING: marp CLI 미설치. 빌드 단계에서 필요합니다."

# 6. generate-presentation.sh 확인
ls generate-presentation.sh 2>/dev/null || echo "WARNING: 빌드 스크립트 없음"
```

#### 이슈 검증 (ISSUE_NUMBER가 있을 때만)

```bash
# 1. 이슈가 현재 레포의 이슈인지 확인
gh issue view ${ISSUE_NUMBER} --json repository --jq '.repository.nameWithOwner'

# 2. 이슈 상태 확인 (이미 closed면 경고)
gh issue view ${ISSUE_NUMBER} --json state --jq '.state'
```

- 이슈가 존재하지 않으면 → 에러 보고 후 중단
- 이슈가 이미 CLOSED면 → 사용자에게 경고하고 확인 요청 (계속할지)
- 이슈의 레포가 현재 레포와 다르면 → 에러 보고 후 중단

**검증 체크리스트**:

- [ ] 강의 폴더가 존재하는가?
- [ ] `requirements.md`가 존재하는가?
- [ ] `.work/` 디렉토리가 생성되었는가?
- [ ] (--issue 시) 이슈가 현재 레포에 존재하고 OPEN 상태인가?

`--rebuild` 옵션인 경우:

- [ ] `.work/audience-analysis.md`, `.work/topic-research.md`, `.work/reference-analysis.md`가 존재하는가?
- [ ] `.work/acceptance-criteria.md`가 존재하는가?
- [ ] `outline.md`가 존재하는가?
- 모두 존재하면 Phase 3으로 건너뛰기 (Phase 0.5/1/1.5/2/2.5 건너뛰고, 기존 acceptance-criteria.md 재활용)
- acceptance-criteria.md가 없으면 Phase 0.5만 실행 후 Phase 3으로 진행
- Phase 3.5(콘텐츠 루브릭 평가)는 `--rebuild`에서도 실행

---

### Phase 0: 학습 주입

Pre-flight 이후, Phase 1 시작 전에 main agent가 실행합니다.

#### 학습 메모리 로드

1. `.claude/learnings/create-lecture.md`를 Read 도구로 읽기
2. 파일이 없거나 비어있으면 건너뛰기
3. 내용이 있으면 `LEARNINGS` 변수에 저장

#### 학습 주입 블록

이후 모든 Phase의 에이전트 프롬프트에 다음 블록을 추가합니다:

```
**과거 학습 (반드시 준수):**
{LEARNINGS 내용}

위 교훈들을 참고하여 같은 실수를 반복하지 마세요.
특히 "반복 패턴" 항목은 반드시 준수해야 합니다.
```

이 블록은 Phase 1~4의 모든 에이전트 프롬프트 하단에 삽입됩니다.
LEARNINGS가 비어있으면 이 블록을 생략합니다.

#### 이슈 시작 댓글 (ISSUE_NUMBER가 있을 때만)

학습 주입 완료 후, Phase 1 시작 전에 이슈에 작업 시작 댓글을 남깁니다:

```bash
gh issue comment ${ISSUE_NUMBER} --body "## 🚀 강의 제작 파이프라인 시작

이슈 내용을 반영하여 강의를 생성/수정합니다.

**강의 폴더:** \`${LECTURE_DIR}\`
**파이프라인:** 분석 → 설계 → 제작 → 검증 → 회고

진행 상황을 댓글로 업데이트하겠습니다."
```

#### 이슈 본문 로드 (ISSUE_NUMBER가 있을 때만)

Phase 1 에이전트들에게 추가 컨텍스트로 전달할 이슈 본문을 가져옵니다:

```bash
gh issue view ${ISSUE_NUMBER} --json title,body,labels --jq '{title: .title, body: .body, labels: [.labels[].name]}'
```

결과를 `ISSUE_CONTEXT` 변수에 저장합니다.

---

### Phase 0.5: Acceptance Criteria 추출

**`--rebuild` 옵션인 경우 건너뛰기** (기존 `.work/acceptance-criteria.md` 재활용)

Main agent가 `requirements.md`를 Read 도구로 읽고, MUST/SHOULD 체크리스트를 추출합니다.

#### 추출 규칙

1. **requirements.md**에서 다음을 MUST로 분류:
   - 강의 시간, 대상, 인원 등 기본 정보
   - 강의 목표의 각 항목
   - 시간 배분 비율 (이론/실습/Q&A)
   - 주요 도구 지정 및 제외 도구 목록
   - 성공 기준의 각 항목

2. **requirements.md**에서 다음을 SHOULD로 분류:
   - 고려사항 섹션의 권고 사항
   - 대안 도구 관련 사항
   - 난이도/환경 권고

3. **flow.md**가 강의 폴더에 존재하면 추가 추출:
   - 핵심 메시지와 배치 전략을 MUST로 추가
   - 시연/실습 설계 원칙을 SHOULD로 추가

#### 출력 형식

Write 도구로 `${LECTURE_DIR}/.work/acceptance-criteria.md`에 저장:

```markdown
## Acceptance Criteria

### MUST (필수 충족)
| # | 항목 | 출처 | 검증 방법 |
|---|------|------|----------|
| M1 | 강의 시간 120분 | requirements.md 기본 정보 | outline 시간 합산 |
| M2 | 주요 도구: Claude Desktop | requirements.md 도구 | 실습 슬라이드 확인 |
| ... | ... | ... | ... |

### SHOULD (권고)
| # | 항목 | 출처 |
|---|------|------|
| S1 | 무료/저비용 도구 우선 | requirements.md 고려사항 |
| ... | ... | ... |
```

---

### Phase 1: 분석 (병렬 3개)

**`--rebuild` 옵션인 경우 건너뛰기**

**데이터 준비 (Main Agent 실행)**: `requirements.md`를 Read 도구로 읽어 내용을 파악합니다.

3개의 Explore 에이전트를 Task 도구로 **병렬 호출**합니다. 읽은 requirements 내용을 각 에이전트 프롬프트의 `{requirements.md 전문}` 위치에 주입합니다.

**이슈 컨텍스트 주입 (ISSUE_NUMBER가 있을 때만)**: 각 에이전트 프롬프트에 다음 블록을 추가합니다:

```
**GitHub 이슈 #${ISSUE_NUMBER} 내용:**
{ISSUE_CONTEXT}

이슈의 요구사항을 requirements.md와 교차 검증하고, 이슈에서 명시한 수정 범위를 우선 반영하세요.
```

#### 1-1. Audience Analyst

```
subagent_type: Explore
description: "수강생 페르소나 분석"
prompt: |
  다음 강의의 수강생을 분석해주세요.

  **requirements.md 내용:**
  {requirements.md 전문}

  **분석 요청 사항:**
  1. requirements.md의 수강 대상 특성을 기반으로 페르소나 3개 작성
     - 각 페르소나: 이름(가상), 배경, AI 경험 수준, 기대사항, 이탈 위험 요인
  2. 전체 수강생의 기대 수준 분포 추정
  3. 난이도 권고 (기본/중급/고급 비율)
  4. 실습 환경 제약 사항 정리

  **출력 형식:**
  마크다운으로 작성. 파일 저장 없이 분석 결과만 반환.
```

분석 결과를 Write 도구로 `${LECTURE_DIR}/.work/audience-analysis.md`에 저장.

#### 1-2. Topic Researcher

```
subagent_type: Explore
description: "주제 리서치 및 최신 동향"
prompt: |
  다음 강의의 주제를 리서치해주세요.

  **requirements.md 내용:**
  {requirements.md 전문}

  **리서치 요청 사항:**
  1. 강의 목표에 언급된 핵심 주제에 대해 웹 검색으로 최신 동향 조사
  2. 관련 도구/서비스 현황 (무료/유료, 가격, 접근성)
  3. 수강생이 바로 활용 가능한 실용적 사례 5개 이상
  4. 강의에서 다루면 좋을 최신 트렌드
  5. 팩트체크가 필요한 주장이나 수치 검증

  **출력 형식:**
  마크다운으로 작성. 파일 저장 없이 리서치 결과만 반환.
```

리서치 결과를 Write 도구로 `${LECTURE_DIR}/.work/topic-research.md`에 저장.

#### 1-3. Reference Analyzer

```
subagent_type: Explore
description: "기존 강의 자료 분석"
prompt: |
  다음 강의 폴더의 기존 자료를 분석해주세요.

  **강의 폴더 경로:** ${LECTURE_DIR}
  **requirements.md 내용:**
  {requirements.md 전문}

  **분석 요청 사항:**
  1. 기존 `lecture.md`가 있다면: 강점/약점 분석
  2. 기존 `outline.md`가 있다면: requirements와의 정합성 검토
  3. 기존 `part-XX.md` 파일들: 재활용 가능한 콘텐츠 식별
  4. 기존 `images/` 폴더: 재활용 가능한 에셋 목록
  5. requirements.md 대비 갭 분석: 빠진 내용, 추가 필요 사항

  기존 파일이 없다면 "새 강의 - 기존 자료 없음"으로 보고하고,
  같은 저장소의 다른 강의(`lectures/` 하위)를 참조하여 패턴과 스타일을 분석해주세요.

  **출력 형식:**
  마크다운으로 작성. 파일 저장 없이 분석 결과만 반환.
```

분석 결과를 Write 도구로 `${LECTURE_DIR}/.work/reference-analysis.md`에 저장.

---

#### 품질 게이트 G1 (Main Agent 실행)

Phase 1의 3개 Task가 완료되면, main agent가 Bash 도구로 다음을 확인:

```bash
# 3개 분석 리포트 존재 확인
ls ${LECTURE_DIR}/.work/audience-analysis.md && \
ls ${LECTURE_DIR}/.work/topic-research.md && \
ls ${LECTURE_DIR}/.work/reference-analysis.md && \
echo "G1_PASS" || echo "G1_FAIL"
```

- **3개 모두 존재 (G1_PASS)**: Phase 2로 진행
- **누락 파일 있음 (G1_FAIL)**: 누락된 에이전트만 재실행 (1회). 재실행 후에도 실패하면 사용자에게 보고하고 중단

---

### Phase 1.5: 교차 검증

**`--rebuild` 옵션인 경우 건너뛰기**

G1 통과 후, main agent가 3개 분석 결과를 Read 도구로 읽고 다음을 검사합니다:

#### 검사 항목

1. **도구 충돌**: Topic Researcher가 추천한 도구와 requirements.md의 "제외 도구"가 겹치는지
2. **난이도 갭**: Audience Analyst의 난이도 권고와 Topic Researcher의 콘텐츠 깊이가 일치하는지
3. **커버리지 갭**: requirements.md의 강의 목표가 3개 분석에서 모두 다뤄졌는지
4. **가정 충돌**: 각 분석에서 암묵적으로 가정한 수강생 수준/환경이 일치하는지

#### 출력

Write 도구로 `${LECTURE_DIR}/.work/cross-validation.md`에 저장:

```markdown
## 교차 검증 결과

### 충돌 발견
| # | 유형 | 분석 A | 분석 B | 내용 | 해결 방향 |
|---|------|--------|--------|------|----------|
| 1 | 도구 충돌 | topic-research | requirements | CLI 도구 추천 vs 제외 | requirements 우선 |

### 갭 발견
| # | 유형 | 누락 영역 | 보완 제안 |
|---|------|----------|----------|
| 1 | 커버리지 | 강의 목표 #3 미다룸 | Phase 2에서 명시적 배치 |

### Phase 2 주입 사항
- {충돌 해결 방향 요약}
- {갭 보완 지시 요약}
```

충돌/갭이 없으면 "교차 검증 통과: 충돌/갭 없음"으로 기록합니다.

---

### Phase 2: 설계 (순차 1개)

**`--rebuild` 옵션인 경우 건너뛰기**

**데이터 준비 (Main Agent 실행)**: Phase 1의 3개 분석 결과와 requirements.md, 그리고 Phase 0.5/1.5 산출물을 Read 도구로 읽어 변수에 저장합니다:
- `requirements` ← `${LECTURE_DIR}/requirements.md`
- `audience_analysis` ← `${LECTURE_DIR}/.work/audience-analysis.md`
- `topic_research` ← `${LECTURE_DIR}/.work/topic-research.md`
- `reference_analysis` ← `${LECTURE_DIR}/.work/reference-analysis.md`
- `acceptance_criteria` ← `${LECTURE_DIR}/.work/acceptance-criteria.md`
- `cross_validation` ← `${LECTURE_DIR}/.work/cross-validation.md`
- `flow_md` ← `${LECTURE_DIR}/flow.md` (존재하면)

읽은 내용을 Instructional Designer 에이전트의 프롬프트에 주입합니다.

#### Instructional Designer

```
subagent_type: general-purpose
description: "강의 설계 및 outline 작성"
prompt: |
  강의 아웃라인을 설계해주세요.

  **requirements.md 내용:**
  {requirements.md 전문}

  **Phase 1 분석 결과:**

  [수강생 분석]
  {audience-analysis.md 전문}

  [주제 리서치]
  {topic-research.md 전문}

  [기존 자료 분석]
  {reference-analysis.md 전문}

  **Acceptance Criteria (반드시 참조):**
  {acceptance-criteria.md 전문}

  **교차 검증 결과 (반드시 반영):**
  {cross-validation.md 전문}

  **강의 흐름 참조 (flow.md가 있을 때만):**
  {flow.md 전문 또는 "flow.md 없음"}

  **설계 요구사항:**

  1. **분 단위 타임라인 설계**
     - 총합이 반드시 requirements.md의 강의 시간과 일치해야 합니다
     - 각 Part의 시작/종료 시간 명시
     - 시간 배분: requirements.md의 비율 준수 (이론/실습/Q&A)

  2. **섹션별 학습 목표**
     - 각 Part에 1~2개의 명확한 학습 목표
     - Bloom's Taxonomy 기반 (이해 → 적용 → 분석)

  3. **활동 유형 명시**
     - 강의 (Lecture): 이론 설명
     - 시연 (Demo): 강사가 직접 보여주기
     - 실습 (Lab): 수강생이 직접 수행
     - Q&A: 질의응답 및 토론

  4. **난이도 계층**
     - 기본 (Basic): 모든 수강생 대상
     - 도전 (Challenge): 경험 있는 수강생 대상

  5. **비주얼 에셋 목록**
     - 각 Part에 필요한 SVG 이미지 목록
     - 파일명과 간단한 설명

  6. **슬라이드 구성 예상**
     - 각 Part의 예상 슬라이드 수

  7. **휴식 배치** ← 신규
     - 60분 이하: 없음 / 61-90분: 1회 / 91-120분: 50-60분 지점에 10분
     - 타임라인에 명시적으로 포함

  8. **시연 도구 검증** ← 신규
     - requirements.md의 "제외 도구"가 시연/실습에 포함되지 않았는지 확인
     - 시연 테이블에 도구명 명시

  9. **AC 매핑 테이블** ← 신규
     - outline 하단에 MUST 항목별 반영 위치(Part/슬라이드)와 반영 방식을 기록

  10. **교차 검증 반영** ← 신규
      - cross-validation.md의 충돌/갭 해결을 outline에 반영
      - 해결 방법을 AC 매핑 테이블 또는 해당 Part에 명시

  **기존 outline.md가 있다면:**
  기존 구조를 최대한 존중하되, requirements와 Phase 1 분석 결과, AC, 교차 검증 결과를 반영하여 갱신.

  **출력:**
  1. 먼저 `${LECTURE_DIR}/outline.md` 존재 여부를 확인 (Read 도구로 시도)
  2. 파일이 존재하면: 기존 내용을 읽고, Edit 도구로 수정
  3. 파일이 없으면: Write 도구로 새로 작성
```

#### 품질 게이트 G2 (Main Agent 실행)

main agent가 outline.md를 Read 도구로 읽고 다음을 검증:

1. **시간 합계 검증**: 모든 Part의 시간을 합산 → requirements.md의 강의 시간과 일치하는지 확인
2. **필수 섹션 존재**: 학습 목표, 타임라인, 비주얼 에셋 목록이 모두 있는지

- **합계 불일치**: Instructional Designer를 다시 호출하여 재조정 요청 (1회)
- **필수 섹션 누락**: Instructional Designer를 다시 호출하여 해당 섹션 추가 요청 (1회)
- **2회 시도 후에도 실패**: 사용자에게 보고하고 수동 수정 요청

---

### Phase 2.5: 설계 루브릭 평가

**`--rebuild` 옵션인 경우 건너뛰기**

G2 통과 후, rubric-evaluator를 호출하여 outline.md의 품질을 정량 평가합니다.

#### 데이터 준비 (Main Agent 실행)

1. `${LECTURE_DIR}/outline.md`를 Read 도구로 읽기
2. `${LECTURE_DIR}/.work/acceptance-criteria.md`를 Read 도구로 읽기
3. `${LECTURE_DIR}/requirements.md`를 Read 도구로 읽기

#### Rubric Evaluator (설계 모드)

```
subagent_type: rubric-evaluator
description: "설계 루브릭 평가"
prompt: |
  outline.md를 설계 루브릭으로 평가해주세요.

  **평가 모드:** design
  **평가 대상:** outline.md

  **outline.md 내용:**
  {outline.md 전문}

  **acceptance-criteria.md 내용:**
  {acceptance-criteria.md 전문}

  **requirements.md 내용:**
  {requirements.md 전문}

  **출력:**
  ${LECTURE_DIR}/.work/rubric-report-design.md 파일을 Write 도구로 저장해주세요.
```

#### 루브릭 게이트 RG1 (Main Agent 실행)

rubric-report-design.md를 Read 도구로 읽고 총점과 등급을 확인:

- **A (90+) 또는 B (80-89)**: Phase 3로 진행 (B는 경고 사항을 로그)
- **C (70-79)**: 감점 사유를 Instructional Designer에 전달하여 재작업 요청 (최대 2회)
  - 재작업 후 rubric-evaluator 재호출
  - 2회 시도 후에도 C 이하면 사용자에게 보고하고 확인 요청
- **F (0-69)**: 즉시 사용자에게 보고하고 수동 개입 요청

---

#### 이슈 설계 완료 댓글 (ISSUE_NUMBER가 있을 때만)

Phase 2 완료 후 (G2 통과 후), `--plan-only` 종료 또는 Phase 3 진입 전에 이슈에 설계 완료 댓글을 남깁니다:

```bash
gh issue comment ${ISSUE_NUMBER} --body "## 📋 설계 완료

outline.md가 갱신되었습니다.

**강의 폴더:** \`${LECTURE_DIR}\`

### 주요 설계 사항
{outline.md의 Part 목록 및 시간 배분 요약}

제작 단계로 진행합니다."
```

**`--plan-only` 옵션인 경우 여기서 종료**

```
📋 설계 완료!

outline.md: ${LECTURE_DIR}/outline.md
분석 결과: ${LECTURE_DIR}/.work/

전체 파이프라인을 실행하려면:
/create-lecture ${LECTURE_DIR} --rebuild
```

> **`--plan-only` + `--issue` 조합 시**: 설계 완료 댓글만 남기고 이슈를 close하지 않습니다.

---

### Phase 3: 제작

**데이터 준비 (Main Agent 실행)**:
1. `create-lecture-templates.md`를 Read 도구로 읽어 CSS 템플릿, SVG 표준, 레이아웃 패턴을 파악
2. `outline.md`를 Read 도구로 읽기
3. Phase 1 분석 결과 3개를 Read 도구로 읽기

이 내용을 각 에이전트 프롬프트의 `{...}` 플레이스홀더에 주입합니다.

#### 3-1. Slide Writer (먼저 실행)

```
subagent_type: general-purpose
description: "lecture.md 슬라이드 작성"
prompt: |
  Marp 프레젠테이션 슬라이드를 작성해주세요.

  **outline.md 내용:**
  {outline.md 전문}

  **Phase 1 분석 결과 요약:**
  - 수강생: {audience-analysis.md 핵심 요약}
  - 주제: {topic-research.md 핵심 요약}
  - 참조: {reference-analysis.md 핵심 요약}

  **디자인 컨벤션 (반드시 준수):**
  {create-lecture-templates.md의 CSS 템플릿 + 레이아웃 패턴 전문}

  **작성 규칙:**

  1. **프런트매터**: 템플릿의 Marp CSS를 그대로 포함
  2. **슬라이드 구분**: `---`로 구분
  3. **배경 이미지 참조**: `![bg left:35%](images/img_파일명.svg)` 형식
     - outline의 비주얼 에셋 목록에 따라 이미지 참조 위치 배치
     - 이미지 파일은 아직 없어도 참조 경로만 먼저 작성
  4. **레이아웃 패턴**: 2단 그리드, 테이블, 하이라이트 박스 등 다양하게 활용
  5. **Part 전환**: 각 Part 시작 전에 `<!-- _class: lead -->` 타이틀 슬라이드 삽입
  6. **실습 슬라이드**: 프롬프트 예시, 확인 방법, 학습 포인트를 포함
     - 실습 내용은 outline 기반으로 기본 구조만 작성
     - `<!-- LAB_PLACEHOLDER: 실습명 -->` 주석으로 Lab Designer가 보강할 위치 표시
  7. **콘텐츠 밀도**: 슬라이드당 불릿 최대 5~6개, 테이블 최대 4행
  8. **한국어**: 모든 콘텐츠는 한국어로 작성

  **출력:**
  ${LECTURE_DIR}/lecture.md 파일을 Write 도구로 작성해주세요.
```

#### 3-2. Visual Designer (3-1 완료 후)

**`--no-images` 옵션인 경우 건너뛰기**

```
subagent_type: general-purpose
description: "SVG 이미지 생성"
prompt: |
  강의 프레젠테이션용 SVG 이미지를 생성해주세요.

  **outline.md의 비주얼 에셋 목록:**
  {outline.md에서 비주얼 에셋 목록 섹션}

  **lecture.md에서 이미지 참조 위치:**
  {lecture.md에서 `![bg` 패턴을 grep하여 추출한 이미지 참조 목록}

  **기존 이미지:**
  {images/ 폴더의 기존 파일 목록}

  **SVG 디자인 표준 (반드시 준수):**
  {create-lecture-templates.md의 SVG 표준 섹션 전문}

  **작성 규칙:**

  1. **기존 이미지 재활용**: 기존 images/ 폴더에 있는 이미지 중 outline과 맞는 것은 그대로 유지
  2. **새 이미지 생성**: outline에는 있지만 기존에 없는 이미지만 새로 생성
  3. **viewBox**: 배경 이미지용은 `viewBox="0 -80 600 960"` 사용
  4. **색상**: 팔레트 색상만 사용
  5. **중앙 배치**: 모든 콘텐츠는 viewBox 중앙에
  6. **단순 디자인**: 아이콘, 도형, 텍스트 조합으로 핵심 메시지 전달
  7. **한글 텍스트**: `font-family="sans-serif"` 사용
  8. **파일명**: outline의 에셋 목록에 명시된 파일명 사용

  **출력:**
  각 SVG 파일을 ${LECTURE_DIR}/images/ 디렉토리에 Write 도구로 저장해주세요.
```

#### 3-3. Lab Designer (3-1 완료 후, 3-2와 병렬)

```
subagent_type: general-purpose
description: "실습 섹션 설계"
prompt: |
  강의의 실습 섹션을 상세 설계해주세요.

  **outline.md 내용:**
  {outline.md 전문}

  **수강생 분석:**
  {audience-analysis.md 전문}

  **주제 리서치:**
  {topic-research.md 전문}

  **lecture.md의 실습 플레이스홀더:**
  {lecture.md에서 LAB_PLACEHOLDER 주석이 포함된 섹션}

  **설계 요구사항:**

  1. 각 실습에 대해:
     - **시나리오**: 수강생이 공감할 수 있는 상황 설정
     - **기본 과제**: 모든 수강생이 수행 가능한 수준
     - **도전 과제**: 경험 있는 수강생을 위한 확장
     - **프롬프트 예시**: 복사-붙여넣기 가능한 구체적 프롬프트
     - **결과물 확인 방법**: 체크리스트 형태
     - **학습 포인트**: 3가지 키워드(선택/계획/문서화)와 연결

  2. 실습 환경 고려:
     - 개인 노트북 기준
     - 무료/저비용 도구 우선
     - 네트워크 불안정 대비 오프라인 대안

  **출력 형식:**
  각 실습을 Marp 슬라이드 형태로 작성.
  ${LECTURE_DIR}/.work/lab-sections.md 파일을 Write 도구로 저장해주세요.
```

#### 3-4. Lab Integration (Main Agent 실행)

Visual Designer와 Lab Designer 완료 후, main agent가 실습 콘텐츠를 lecture.md에 통합합니다:

1. `lecture.md`를 Read 도구로 읽기
2. `.work/lab-sections.md`를 Read 도구로 읽기
3. `lecture.md`에서 `<!-- LAB_PLACEHOLDER: 실습명 -->` 패턴을 Grep 도구로 찾기
4. 각 플레이스홀더를 lab-sections.md의 해당 실습 콘텐츠로 교체 (Edit 도구)
5. 플레이스홀더와 실습명이 불일치하면 사용자에게 보고

#### 품질 게이트 G3 (Main Agent 실행, 최대 3회 시도)

main agent가 Marp 빌드 테스트를 실행합니다:

**시도 1:**
```bash
marp ${LECTURE_DIR}/lecture.md --html -o ${LECTURE_DIR}/lecture_test.html --allow-local-files 2>&1
echo "EXIT_CODE: $?"
```

- **빌드 성공 (exit code 0)**: 테스트 파일 삭제 후 Phase 4로 진행
  ```bash
  rm ${LECTURE_DIR}/lecture_test.html
  ```
- **빌드 실패**: 에러 메시지를 캡처하고, Slide Writer를 다시 호출하여 에러 내용을 전달하며 수정 요청

**시도 2 (재시도 1회차):**
- Slide Writer가 수정한 lecture.md로 빌드 재시도
- 성공하면 Phase 4로 진행

**시도 3 (재시도 2회차, 마지막):**
- 2회차에도 실패하면 한 번 더 재시도
- 3회 모두 실패 시: 에러 내용을 사용자에게 보고하고 중단

---

### Phase 3.5: 콘텐츠 루브릭 평가

G3 통과 후, rubric-evaluator를 호출하여 lecture.md의 품질을 정량 평가합니다.

#### 데이터 준비 (Main Agent 실행)

1. `${LECTURE_DIR}/lecture.md`를 Read 도구로 읽기
2. `${LECTURE_DIR}/.work/acceptance-criteria.md`를 Read 도구로 읽기
3. `${LECTURE_DIR}/requirements.md`를 Read 도구로 읽기
4. `${LECTURE_DIR}/images/` 폴더를 Glob 도구로 파일 목록 확인

#### Rubric Evaluator (콘텐츠 모드)

```
subagent_type: rubric-evaluator
description: "콘텐츠 루브릭 평가"
prompt: |
  lecture.md를 콘텐츠 루브릭으로 평가해주세요.

  **평가 모드:** content
  **평가 대상:** lecture.md

  **lecture.md 내용:**
  {lecture.md 전문}

  **acceptance-criteria.md 내용:**
  {acceptance-criteria.md 전문}

  **requirements.md 내용:**
  {requirements.md 전문}

  **images/ 파일 목록:**
  {Glob으로 images/*.svg 결과}

  **출력:**
  ${LECTURE_DIR}/.work/rubric-report-content.md 파일을 Write 도구로 저장해주세요.
```

#### 루브릭 게이트 RG2 (Main Agent 실행)

rubric-report-content.md를 Read 도구로 읽고 총점과 등급을 확인:

- **A (90+) 또는 B (80-89)**: Phase 4로 진행 (B는 경고 사항을 로그)
- **C (70-79)**: 감점 사유를 Slide Writer에 전달하여 재작업 요청 (최대 2회)
  - 재작업 후 rubric-evaluator 재호출
  - 2회 시도 후에도 C 이하면 사용자에게 보고하고 확인 요청
- **F (0-69)**: 즉시 사용자에게 보고하고 수동 개입 요청

---

### Phase 4: 검증 & 빌드

#### Quality Reviewer

```
subagent_type: general-purpose
description: "강의 품질 검증"
prompt: |
  완성된 강의 자료의 품질을 검증해주세요.

  **lecture.md 내용:**
  {lecture.md 전문}

  **outline.md 내용:**
  {outline.md 전문}

  **requirements.md 내용:**
  {requirements.md 전문}

  **images/ 폴더 파일 목록:**
  {Glob으로 images/*.svg 결과}

  **Acceptance Criteria:**
  {acceptance-criteria.md 전문}

  **루브릭 평가 결과 (참조):**
  {rubric-report-content.md 전문}

  **검증 항목:**

  1. **슬라이드 오버플로우 검사**
     - 각 슬라이드의 콘텐츠 양 추정
     - 불릿 6개 초과, 테이블 5행 초과, 코드 10줄 초과 시 경고
     - 슬라이드 분할 제안

  2. **시간 배분 검증**
     - 슬라이드 수 × 평균 시간 ≈ 강의 시간
     - 이론/실습 슬라이드 비율 검증

  3. **이미지 참조 유효성**
     - lecture.md의 모든 `![` 참조에 대해 실제 파일 존재 확인
     - 누락 이미지 목록 작성

  4. **한국어 텍스트 품질**
     - 문장이 지나치게 긴 경우 경고 (80자 초과)
     - 맞춤법/어색한 표현 지적

  5. **디자인 컨벤션 준수**
     - 프런트매터 CSS 포함 여부
     - 배경 이미지 35% 준수
     - 하이라이트 박스 적절 사용

  6. **학습 목표 달성 가능성**
     - requirements.md의 성공 기준 대비 커버리지

  7. **AC MUST 항목 충족 검증** ← 신규
     - acceptance-criteria.md의 MUST 항목을 lecture.md에서 하나씩 검증
     - 미충족 MUST 항목은 Critical 심각도로 보고
     - MUST 충족 현황 테이블을 리뷰 리포트에 포함

  8. **루브릭 감점 미수정 건 확인** ← 신규
     - rubric-report-content.md의 감점 항목이 lecture.md에서 수정되었는지 확인
     - 미수정 감점 건은 Warning 심각도로 재보고

  9. **실전 설계 규칙 준수** ← 신규
     - 휴식 배치: 91분 이상 강의에 휴식 슬라이드 존재 확인
     - 시연 도구: 제외 도구가 시연/실습에 사용되지 않았는지 확인
     - 역할 분기: 다중 역할 강의에서 선택 안내 슬라이드 존재 확인

  10. **근본원인 분석** (Phase 5 학습용)
      - 각 이슈에 대해 근본원인(왜 발생했는지)을 분석
      - 재발방지를 위한 일반화된 교훈 도출

  **출력 형식:**
  마크다운으로 리뷰 리포트 작성.
  각 이슈에 심각도(Critical/Warning/Info)와 수정 제안 포함.

  이슈 테이블은 다음 형식을 사용:
  ```
  | # | 심각도 | 이슈 | 근본원인 | 재발방지 교훈 |
  |---|--------|------|---------|-------------|
  ```
  "근본원인"과 "재발방지 교훈" 열은 Phase 5에서 learnings 파일에 기록됩니다.

  ${LECTURE_DIR}/.work/review-report.md 파일을 Write 도구로 저장해주세요.
```

#### 리뷰 이슈 해결

review-report.md를 Read 도구로 읽고:

- **Critical 이슈**: 즉시 수정 (Edit 도구로 lecture.md 수정)
- **Warning 이슈**: 가능하면 수정
- **Info 이슈**: 사용자에게 보고만

수정 완료 후 Critical 이슈가 남아있으면 Quality Reviewer를 한 번 더 실행 (최대 2회).

#### 최종 빌드

```bash
# LECTURE_DIR이 "lectures/lecture-12-topic"인 경우
# FOLDER_NAME = "lecture-12-topic" (lectures/ 접두사 제거)
FOLDER_NAME=$(echo ${LECTURE_DIR} | sed 's|^lectures/||')
./generate-presentation.sh ${FOLDER_NAME} lecture.md
```

> **주의**: `generate-presentation.sh`는 내부에서 `lectures/${FOLDER_NAME}/${MD_FILE}` 경로를 구성합니다.
> 따라서 첫 번째 인자에 `lectures/`를 포함하면 안 됩니다.

빌드 성공 확인:

```bash
ls ${LECTURE_DIR}/lecture.html && echo "BUILD_SUCCESS"
```

#### 품질 게이트 G4

- **빌드 성공 + Critical 이슈 0건**: Phase 5로 진행
- **빌드 실패**: 에러 분석 후 수정, 재빌드 (최대 2회)

---

### Phase 5: 회고 & 학습 추출

retrospective-agent를 호출하여 이번 실행에서 발견된 교훈을 학습 메모리에 기록합니다.

#### 데이터 준비 (Main Agent 실행)

1. `${LECTURE_DIR}/.work/review-report.md`를 Read 도구로 읽기
2. `${LECTURE_DIR}/.work/rubric-report-design.md`를 Read 도구로 읽기 (존재하면)
3. `${LECTURE_DIR}/.work/rubric-report-content.md`를 Read 도구로 읽기 (존재하면)
4. `.claude/learnings/create-lecture.md`를 Read 도구로 읽기
5. `${LECTURE_DIR}/lecture.md`를 Read 도구로 읽기

#### Retrospective Agent

```
subagent_type: retrospective-agent
description: "회고 및 학습 추출"
prompt: |
  이번 강의 제작 파이프라인의 실행 결과를 회고하고 교훈을 추출해주세요.

  **강의 폴더:** ${LECTURE_DIR}
  **강의명:** ${LECTURE_DIR에서 추출한 강의명}

  **리뷰 리포트:**
  {review-report.md 전문}

  **루브릭 평가 리포트 (설계):**
  {rubric-report-design.md 전문 또는 "없음"}

  **루브릭 평가 리포트 (콘텐츠):**
  {rubric-report-content.md 전문 또는 "없음"}

  **기존 학습 메모리:**
  {learnings/create-lecture.md 전문}

  **작업 요청:**

  1. review-report.md의 이슈 테이블에서 "근본원인 + 재발방지 교훈" 열을 추출
  2. rubric-report-*.md의 감점 사유에서 추가 교훈을 추출
  3. 추출된 교훈을 적절한 카테고리에 분류 (6개):
     - 슬라이드 작성 교훈 (레이아웃, 콘텐츠 밀도, 표현)
     - SVG 이미지 교훈 (viewBox, 색상, 배치)
     - 설계 교훈 (시간 배분, 구조, 목표)
     - 분석 교훈 (페르소나, 리서치, 참조)
     - 설계 원칙 (구조적 규칙: 휴식 배치, 도구 제약, 역할 분기 등)
     - 평가 교훈 (채점 기준 적절성, 오탐/미탐 사례)
  4. 기존 learnings와 중복 여부 확인 (의미가 같으면 스킵)
  5. 새 교훈을 learnings/create-lecture.md에 추가
     - 형식: `- [날짜 강의명] 문제 설명 → 재발방지 규칙`
  6. 3회 이상 반복된 교훈은 "반복 패턴" 섹션으로 승격
  7. 70줄 초과 시 가장 오래된 일회성 항목부터 제거

  **출력:**
  1. .claude/learnings/create-lecture.md를 Edit 도구로 업데이트
  2. ${LECTURE_DIR}/lecture.md를 ${LECTURE_DIR}/.work/generated-lecture.md.snapshot으로 복사 (Write 도구)
  3. 업데이트 요약을 반환
```

#### 학습 메모리 업데이트 확인

retrospective-agent 완료 후:

1. `learnings/create-lecture.md`가 업데이트되었는지 확인
2. `.work/generated-lecture.md.snapshot`이 생성되었는지 확인

```bash
ls .claude/learnings/create-lecture.md && ls ${LECTURE_DIR}/.work/generated-lecture.md.snapshot && echo "PHASE5_OK"
```

---

## 완료 보고

```
🎉 강의 제작 완료!

📁 강의 폴더: ${LECTURE_DIR}
📄 프레젠테이션: ${LECTURE_DIR}/lecture.html
📝 아웃라인: ${LECTURE_DIR}/outline.md
🖼️ 이미지: ${LECTURE_DIR}/images/ ({N}개 SVG)

📊 요약:
- 총 슬라이드: {N}장
- 예상 강의 시간: {N}분
- 이미지: {N}개
- 실습: {N}개
- 설계 루브릭: {N}점/{등급} | 콘텐츠 루브릭: {N}점/{등급}

📋 분석 산출물: ${LECTURE_DIR}/.work/
- acceptance-criteria.md (MUST/SHOULD 체크리스트)
- audience-analysis.md (수강생 분석)
- topic-research.md (주제 리서치)
- reference-analysis.md (기존 자료 분석)
- cross-validation.md (교차 검증)
- rubric-report-design.md (설계 루브릭 평가)
- lab-sections.md (실습 설계)
- rubric-report-content.md (콘텐츠 루브릭 평가)
- review-report.md (품질 리뷰)
- generated-lecture.md.snapshot (수정 전 스냅샷)

🧠 학습 메모리: .claude/learnings/create-lecture.md
- 이번 실행에서 {N}건의 교훈이 추가되었습니다

💡 다음 단계:
1. 브라우저에서 lecture.html 열어 검수
2. 필요시 lecture.md 직접 편집 후 재빌드
3. 수정 완료 후: /create-lecture-reflect ${LECTURE_DIR} 실행하여 피드백 캡처
4. PDF 필요 시: 브라우저 인쇄 → PDF 저장 (배경 그래픽 활성화)
```

### 이슈 완료 처리 (ISSUE_NUMBER가 있을 때만)

완료 보고 출력 후, 이슈 연동 마무리를 수행합니다:

#### 1. 커밋 (이슈 번호 포함)

```bash
git add ${LECTURE_DIR}/
git commit -m "feat: 강의 업데이트 - 이슈 #${ISSUE_NUMBER} 반영

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

#### 2. 이슈에 완료 댓글

```bash
gh issue comment ${ISSUE_NUMBER} --body "## ✅ 강의 제작 완료

### 변경 사항
{완료 보고의 요약 내용}

### 산출물
- 프레젠테이션: \`${LECTURE_DIR}/lecture.html\`
- 아웃라인: \`${LECTURE_DIR}/outline.md\`
- 이미지: {N}개 SVG

### 커밋
\`{commit_hash}\` - feat: 강의 업데이트 - 이슈 #${ISSUE_NUMBER} 반영

---
수정이 필요하면 \`/create-lecture ${LECTURE_DIR} --issue ${ISSUE_NUMBER} --rebuild\`로 재실행할 수 있습니다."
```

#### 3. 이슈 close

```bash
gh issue close ${ISSUE_NUMBER} --comment "강의 제작 파이프라인으로 해결됨"
```

---

## 에이전트 목록

### 전문 에이전트 (`.claude/agents/`)

| Phase | Agent | 에이전트 파일 | 역할 |
|-------|-------|-------------|------|
| 1 | Lecture Analyst | `lecture-analyst` | 수강생/주제/참조 분석 (×3 병렬) |
| 2 | Instructional Designer | `instructional-designer` | 강의 설계 및 outline 작성 |
| 2.5/3.5 | Rubric Evaluator | `rubric-evaluator` | 루브릭 기반 정량 평가 |
| 3 | Slide Writer | `slide-writer` | Marp 슬라이드 작성 |
| 3 | Visual Designer | `visual-designer` | SVG 이미지 생성 |
| 4 | Lecture Reviewer | `lecture-reviewer` | 품질 검증 + 근본원인 분석 + MUST 충족 |
| 5 | Retrospective Agent | `retrospective-agent` | 회고 & 학습 추출 (6개 카테고리) |

### 서브 에이전트 (Task 도구 호출)

| Phase | Agent | subagent_type | 역할 |
|-------|-------|--------------|------|
| 1-1 | Audience Analyst | `lecture-analyst` | 수강생 페르소나 분석 |
| 1-2 | Topic Researcher | `lecture-analyst` | 주제 리서치 및 최신 동향 |
| 1-3 | Reference Analyzer | `lecture-analyst` | 기존 강의 자료 분석 |
| 2 | Instructional Designer | `instructional-designer` | 강의 설계 및 outline 작성 |
| 2.5 | Rubric Evaluator | `rubric-evaluator` | 설계 루브릭 평가 (design 모드) |
| 3-1 | Slide Writer | `slide-writer` | Marp 슬라이드 작성 |
| 3-2 | Visual Designer | `visual-designer` | SVG 이미지 생성 |
| 3-3 | Lab Designer | `slide-writer` | 실습 섹션 설계 |
| 3.5 | Rubric Evaluator | `rubric-evaluator` | 콘텐츠 루브릭 평가 (content 모드) |
| 4 | Quality Reviewer | `lecture-reviewer` | 품질 검증 + 근본원인 분석 + MUST 충족 |
| 5 | Retrospective Agent | `retrospective-agent` | 회고 & 학습 추출 (6개 카테고리) |

## 자기 개선 루프

이 파이프라인은 **자기 개선 루프**를 내장하고 있습니다:

```
                    ┌─────────────────────────────────┐
                    │    learnings/create-lecture.md   │
                    │    (축적된 교훈 = 팀의 기억)       │
                    └──────┬──────────────┬────────────┘
                     읽기 ↓              ↑ 쓰기
              ┌────────────┴──┐   ┌──────┴───────────┐
              │  Phase 0      │   │  Phase 5          │
              │  학습 주입     │   │  회고 & 학습 추출   │
              └──────┬────────┘   └──────┬────────────┘
                     ↓                    ↑
    requirements.md → Phase 1-4 → lecture.html → 사용자 수정
                                                    ↓
                                        /create-lecture-reflect
                                        (diff 기반 교훈 추출)
```

- **Phase 0**: 매 실행마다 `learnings/create-lecture.md`를 읽어 모든 에이전트에 주입
- **Phase 5**: 리뷰 리포트의 근본원인에서 교훈 추출 → learnings 업데이트
- **reflect**: 사용자 수정 후 diff 기반으로 추가 교훈 캡처 (`/create-lecture-reflect`)

## 주의사항

- 모든 콘텐츠는 **한국어**로 작성
- `.work/` 디렉토리는 중간 산출물 저장소 (`.gitignore`에 추가됨)
- `.claude/learnings/` 디렉토리는 Git 추적 대상 (팀원 공유)
- 에이전트 간 데이터 전달은 **파일 기반** (Read/Write 도구 사용)
- Phase 간 품질 게이트를 반드시 통과해야 다음 단계 진행
- 빌드 실패 시 최대 **2회 재시도** 후 사용자에게 보고
- 이미지 참조 경로는 상대 경로 (`images/img_*.svg`)
- `create-lecture-templates.md`의 CSS/SVG 표준을 반드시 참조
- learnings 파일은 최대 70줄 유지 (retrospective-agent가 자동 관리)
- `--issue` 옵션은 **조건부 실행**: ISSUE_NUMBER가 없으면 모든 이슈 연동 로직을 건너뛰어 기존 동작과 완전히 동일
- `--issue` + `--plan-only` 조합 시 이슈를 close하지 않음 (설계 완료 댓글만)
