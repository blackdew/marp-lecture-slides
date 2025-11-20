---
marp: true
theme: default
size: 16:9
paginate: true
---

<style>
section {
  padding: 60px 80px;
  font-size: 1.1em;
}

section.lead {
  padding: 60px 80px;
  text-align: center;
}

h1 {
  color: #2c3e50;
  font-size: 2.5em;
}

h2 {
  color: #3498db;
  font-size: 1.8em;
}

h3 {
  font-size: 1.4em;
}

p, li {
  font-size: 1.1em;
  line-height: 1.5;
}

code {
  background: #f4f4f4;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 1.1em;
}

table {
  font-size: 1.1em;
}

.highlight {
  background: #fff3cd;
  padding: 15px;
  border-left: 4px solid #ffc107;
  margin: 15px 0;
  font-size: 1.2em;
}

.success {
  background: #d4edda;
  padding: 15px;
  border-left: 4px solid #28a745;
  margin: 15px 0;
  font-size: 1.2em;
}

.question {
  background: #e3f2fd;
  padding: 20px;
  border-left: 4px solid #2196f3;
  margin: 20px 0;
  font-size: 1.3em;
  font-weight: bold;
  color: #1565c0;
}
</style>

# Part 6

# 회고 및 다음 단계

**시간**: 20분 (회고 10분 + 한계 5분 + 다음 단계 5분)

---

## 이번 시간에 할 내용

**목표**: 배운 내용 정리 + 지속 가능한 학습 계획

| 단계 | 내용 | 시간 |
|------|------|------|
| **회고** | 오늘의 학습 돌아보기 | 10분 |
| **Agent의 한계** | 기대치 조정하기 | 5분 |
| **다음 단계** | 심화 학습 방법 | 5분 |

---

## 회고: 오늘 하루를 돌아보며

**3가지 질문**:

1. **가장 놀라웠던 순간은?**
   - Agent가 해낸 것 중 예상 밖이었던 것

2. **내일부터 써먹을 것은?**
   - 실무에 바로 적용할 수 있는 것

3. **더 배우고 싶은 것은?**
   - 오늘 시간이 부족했거나 궁금한 것

---

## 회고: 참가자 공유 (선택)

**자원자 환영!**

- 간단히 한 문장으로
- 또는 채팅/포스트잇으로

**강사 코멘트**:
- 공통 패턴 정리
- 자주 나온 질문 답변

---

## 오늘 배운 핵심 내용 요약

| Part | 핵심 내용 | 키워드 |
|------|----------|--------|
| **Part 1-2** | Agent 첫 만남 | 챗봇 vs Agent, Tools |
| **Part 3** | AI 시대 관점 | 선택, 계획, 문서화 |
| **Part 4** | 업무 자동화 | CSV, PDF, 메일, 도구 |
| **Part 5** | 팀 해커톤 | 프롬프트, 실용성, 창의성 |

**핵심 메시지**: "Agent = 도구를 쓸 줄 아는 똑똑한 동료"

---

## Agent의 한계

**핵심 메시지**: 기대치를 조정해야 실망이 없습니다

**Agent가 못 하는 것**:

- ❌ 보안/인증이 필요한 시스템 접근
- ❌ 외부 API 호출 (MCP 없이)
- ❌ 실시간 웹 검색 (기본 설정)
- ❌ 당신 대신 선택하기 (정보 제공만)

---

## Agent가 잘하는 것

**Agent가 잘하는 것**:

- ✅ 로컬 파일 읽기/쓰기
- ✅ 코드 생성 및 수정
- ✅ 문서 작성 및 요약
- ✅ 데이터 변환 및 정리
- ✅ 반복 작업 자동화

**팁**: Agent의 강점에 집중하세요!

---

## 실무에서 Agent 활용 팁

**효과적인 사용 패턴**:

| 상황 | 권장 방법 |
|------|----------|
| **데이터 정리** | CSV, Excel 변환 및 포맷 통일 |
| **문서 작성** | 초안 생성 → 사람이 검토 및 수정 |
| **코드 생성** | 간단한 스크립트, HTML 페이지 |
| **반복 작업** | 파일 이름 변경, 포맷 변환 |

**원칙**: Agent는 80%, 사람은 마지막 20% (검토 및 결정)

---

## 활용 팁 1: 문서 기반 작업 관리

<div class="highlight">
핵심: 프로젝트 상태를 문서로 관리하세요
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

<div>

### 왜 문서 관리가 중요한가?

**문제**: 세션이 길어지면
- 대화 기록이 너무 길어짐
- 맥락을 잃어버림
- Agent 성능이 떨어짐

**해결책**: 문서로 상태 관리
- 세션을 자유롭게 시작/종료
- 언제든 작업 재개 가능
- Agent에게 정확한 맥락 전달

</div>

<div>

### 문서 예시

```markdown
# project-status.md

## 현재 진행 상황
- [완료] 데이터 수집
- [진행중] 데이터 정리
- [대기] 보고서 작성

## TODO 리스트
1. CSV 중복 제거
2. 날짜 포맷 통일
3. 결측치 처리

## 결정사항
- 결측치: 0으로 처리
```

</div>

</div>

---

## 활용 팁 2: 세션 관리

<div class="highlight">
세션은 짧게, 자주 종료하세요
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

<div>

### 세션이 길어지면 문제

- Agent 응답 품질 저하
- 불필요한 맥락으로 혼란
- 비용 증가 (토큰 사용량)

### 권장: 30-60분 작업 사이클

1. 문서 읽고 시작
2. 한 가지 작업에 집중
3. 문서 업데이트
4. 세션 종료

</div>

<div>

### 프롬프트 예시

**세션 시작 시**:
```
project-status.md 읽어줘.
다음 TODO 진행:
CSV 중복 제거
```

**세션 종료 전**:
```
project-status.md 업데이트해줘.
완료: CSV 중복 제거
다음: 날짜 포맷 통일
```

</div>

</div>

---

## 활용 팁 3: 좋은 대화 원칙

<div class="highlight">
Agent와의 대화도 사람과의 대화처럼
</div>

| 원칙 | 설명 | 예시 |
|------|------|------|
| **서두르지 않기** | Agent가 계획을 세우도록 시간 주기 | "먼저 계획을 세워줘" |
| **꼼꼼하게 읽기** | Agent의 응답과 질문을 주의깊게 읽기 | 에러 메시지, 제안사항 놓치지 않기 |
| **구체적으로 답하기** | Agent 질문에 명확하게 답변 | ❌ "대충" → ✅ "YYYY-MM-DD 형식" |
| **추가 아이디어 요청** | Agent에게 제안 요청 | "다른 방법도 있을까?" |
| **이해 확인** | Agent가 제대로 이해했는지 확인 | "내 요청을 요약해줘" |

**나쁜 예**:
```
파일 정리해줘
```

**좋은 예**:
```
downloads 폴더의 PDF 파일들을 정리하고 싶어.
먼저 어떤 방식으로 정리할지 3가지 옵션을 제안해줘.
```

---

## 활용 팁 4: IDE로 작업 확인

<div class="highlight">
Agent의 결과를 직접 눈으로 확인하세요
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

<div>

### 추천 도구

| 도구 | 특징 |
|------|------|
| **VS Code** | 무료, 파일 탐색 |
| **Cursor** | AI 통합 에디터 |
| **AntiGravity** | 최신 IDE |

**설치 링크**:
- VS Code: https://code.visualstudio.com/
- Cursor: https://cursor.com/
- AntiGravity: https://antigravity.google/download

</div>

<div>

### 왜 IDE를 사용?

**1. 파일 구조 확인**
- Agent가 만든 파일들
- 폴더 구조 한눈에

**2. 직접 수정 가능**
- 놓친 부분 바로 수정
- 간단한 변경은 직접

**3. 동시 작업**
- Agent: 큰 작업
- 나: 작은 수정/확인

</div>

</div>

---

## 활용 팁 5: Git으로 작업 저장

<div class="highlight">
Agent에게 Git도 맡기세요
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

<div>

### 프롬프트 예시

**간단하게**:
```
깃 커밋해줘
```

**구체적으로**:
```
지금까지 작업을 git에 저장.
커밋 메시지:
"데이터 정리 완료"
```

**작업 흐름**:
작업 완료 -> "깃 커밋해줘" -> Agent가 커밋 -> 다음 작업 진행

</div>

<div>

### 왜 Git을 사용?

| 상황 | 도움 |
|------|------|
| **실수** | 이전 버전 복구 |
| **실험** | 안전하게 시도 |
| **공유** | 팀원과 협업 |
| **기록** | 자동 히스토리 |

**Git = 되돌리기 버튼**

실패해도 괜찮다는
안전감을 줍니다

</div>

</div>

---

## 활용 팁 5-1: 처음 Git 사용 시 초기화

<div class="highlight">
첫 커밋 전에 Git 사용자 정보 설정이 필요합니다
</div>

### 프롬프트 예시

**초기화 요청**:
```
Git을 처음 사용합니다.
내 이름과 이메일로 Git 초기화해줘.

이름: 홍길동
이메일: hong@example.com
```

**Agent가 실행하는 명령**:
```bash
git config --global user.name "홍길동"
git config --global user.email "hong@example.com"
git init
```

**참고**: 이 설정은 컴퓨터당 한 번만 하면 됩니다!

---

## Agent 활용 실제 프로젝트 사례

**실전에서 Agent를 어떻게 활용하고 있을까요?**

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 30px;">

<div>

**창작 & 콘텐츠**
- 음악 앨범 프로젝트
- 강의 생성 프로젝트

**생산성 & 도구**
- DailyFlow 프로젝트
- OTU 프로젝트

</div>

<div>

**데이터 & 분석**
- 캐글 컨테스트 참여
- 주식 신호 분석기

**연구 & 학습**
- 정책 및 논문 연구

</div>

</div>

**프로젝트 상세 내용**: [Agent 활용 프로젝트 7가지](https://docs.google.com/presentation/d/1_525QEweDZZS5LJC0roWzQaAkrp54Yn6XBI1-d9IWNQ/edit?usp=sharing)

---

## 다음 단계: 심화 학습

**1단계: 기본 활용**
- 실무에서 주 1회 이상 사용
- 프롬프트 패턴 익히기
- Plan 모드 습관화

**2단계: 프로젝트 컨텍스트**
- CLAUDE.md 파일 작성법 학습
- 프로젝트별 가이드라인 설정

**3단계: 고급 기능**
- Commands 활용법 (반복 작업 자동화)
- Skills 활용법 (전문 도구 활용)


---

## CLAUDE.md 작성 가이드 (미리보기)

**CLAUDE.md란?**
- Agent에게 프로젝트 컨텍스트를 알려주는 파일
- 매번 설명하지 않아도 Agent가 이해함

**기본 구조**:
```markdown
# 프로젝트 개요
이 프로젝트는 주간 매출 보고서를 자동 생성합니다.

# 파일 구조
data/ - CSV 원본 파일
reports/ - 생성된 보고서

# 작업 규칙
1. 날짜는 항상 YYYY-MM-DD 형식
2. 금액은 천 단위 쉼표
```

---

## Commands 활용법 (미리보기)

**Commands란?**
- 자주 쓰는 작업을 단축 명령어로 저장
- `/report` 입력하면 주간 보고서 자동 생성

**예시**:
```bash
# .claude/commands/report.md
주간 매출 데이터를 읽어서
경영진용 요약 보고서를 작성하고
reports/ 폴더에 저장해줘.
```

**사용**: `/report` 입력만으로 실행!

---

## Skills 활용하기 (미리보기)

**Skills란?**
- 특정 작업에 특화된 전문 도구 모음
- PDF, Excel, 이미지 처리 등 복잡한 작업을 쉽게 수행

**활용 예시**:
- PDF Skill: PDF 텍스트 추출, 병합, 분할
- Excel Skill: 데이터 분석, 차트 생성, 피벗 테이블
- 이미지 Skill: 이미지 편집, 포맷 변환, 썸네일 생성

**사용법**: Agent가 필요시 자동으로 적절한 Skill 선택!

---

## 과제

**강의 후 미션**:

1. **실무에서 Agent 1회 이상 사용**
   - 어떤 작업이든 OK

2. **사용 후기 간단히 작성**
   - 무엇을 했는가?
   - 얼마나 시간을 절약했는가?
   - 어려웠던 점은?

3. **회사 채널/메일로 공유** (선택)
   - 다른 팀원들에게도 도움이 됩니다!

---

## 마지막 메시지

**축하합니다!**

오늘 하루 동안:
- Agent를 처음 만나고
- 실습을 통해 체험하고
- AI 시대 관점을 배우고
- 실무 자동화를 경험하고
- 팀 프로젝트를 완성했습니다

**이제 시작입니다!**

---

## Agent와 함께하는 미래

**AI 시대의 일하는 방식**:

- **Before**: 모든 것을 직접
- **After**: Agent와 협업

**핵심**:
- Agent는 도구를 쓸 줄 아는 동료
- 명확한 지시가 성공의 열쇠
- 실패해도 다시 시도하면 됨

**당신의 역할**: 선택하고, 계획하고, 검토하기

---

## 연락처 및 피드백

**공식 문서**:
- Claude Code 공식 문서: https://code.claude.com/docs
- Claude.ai: https://claude.ai

**강의 관련 문의**:
- GitHub: https://github.com/blackdew
- 이메일: blackdew7@gmail.com

**피드백 환영**:
- 오늘 강의에 대한 의견
- 개선 제안
- 추가로 듣고 싶은 내용

---

<!-- _class: lead -->

# 감사합니다!

**AI Agent와 함께하는**
**새로운 업무 방식의 시작**

**질문이 있으시면 언제든지!**

---
