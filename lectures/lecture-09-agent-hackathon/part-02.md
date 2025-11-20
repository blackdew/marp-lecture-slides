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

## Part 2 개요

### 목표

**성공 경험을 통한 자신감 확보**

### 3가지 실습 (40분)

- **실습 1**: 환영 페이지 만들기 (15분)
- **실습 2**: 다운로드 폴더 정리 (10분)
- **실습 3**: Plan 모드 체험 (10분)
- 회고: 첫 실습 마무리 (5분)

**설계 철학**: "복잡한 이론보다 먼저 체험하기!"

---

## 실습 전 준비: 프로젝트 폴더 만들기

### 프로젝트 = 폴더

**Agent는 현재 폴더 안에서만 작업합니다**

- 각 프로젝트는 별도 폴더에서 작업
- Agent는 해당 폴더의 파일들만 보고 수정
- 다른 프로젝트와 파일이 섞이지 않음

**비유**: 책상 서랍처럼, 프로젝트마다 서랍(폴더)을 따로 쓰기

---

## 실습용 폴더 만들기

### 단계별 진행

```bash
# 1. 오늘 실습용 폴더 만들기
mkdir ai-hackathon

# 2. 폴더로 이동
cd ai-hackathon

# 3. 현재 위치 확인
pwd
# 출력: /Users/내이름/ai-hackathon

# 4. Agent 실행
claude
```

<div class="highlight">
<strong>중요!</strong> 앞으로 모든 실습은 이 폴더 안에서 진행합니다
</div>

**프로젝트가 끝나면**: 터미널 종료 (Ctrl+C) → 나중에 다시 `cd ai-hackathon` → `claude` 로 이어서 작업

---

## 실습 1: 환영 페이지 만들기

### 목표

**Agent에게 HTML 파일을 만들어달라고 요청하기**

- 파일명: `welcome.html`
- 내용: 오늘 날짜 + 환영 메시지

### 왜 이 실습을 할까요?

1. **성공 경험**: 프롬프트 한 번에 결과 나오는 체험
2. **자신감**: "개발자 아니어도 만들 수 있다!"
3. **Tools 경험**: Agent가 실제로 파일을 만드는 것 보기

**난이도**: ⭐ (매우 쉬움)

---

## 실습 1: 프롬프트 및 실행

### 기본 과제 (15분)

터미널에서 `claude` (또는 `gemini`, `codex`) 실행 후 다음처럼 입력하세요:

```
오늘 날짜와 환영 메시지를 보여주는 HTML 파일을 만들어줘.
파일명은 welcome.html로 해줘.
```

**Agent가 할 일**:
1. `welcome.html` 파일 생성
2. HTML 코드 작성
3. 결과 알려주기

**여러분이 할 일**:
1. 파일이 생성되었는지 확인
2. 브라우저로 파일 열어보기

---

## 실습 1: 도전 과제 & 확인

### 향후 도전 과제

파일을 만들었다면 수정해볼까요?

```
배경색을 파란색으로 바꾸고, 현재 시간도 보여줘.
```

### HTML 파일 브라우저로 열기

**Mac**: 파일 우클릭 → 연결 프로그램 → Chrome
**Windows**: 파일 더블클릭

<div class="highlight">
<strong>실패해도 괜찮습니다!</strong> Agent도 실수합니다. 다시 시도하면 됩니다.
</div>

**성공했나요?** 축하합니다!

---

## 실습 2: 다운로드 폴더 정리

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

<div>

### 목표

**Agent에게 다운로드 폴더를 정리하도록 요청하기**

- 실제 업무에서 자주 쓰는 작업
- 불필요한 파일 삭제
- 년도별 아카이빙

### 기본 과제 (5분)

```
내 다운로드 폴더를 정리해줘.

1. 먼저 어떤 파일들이 있는지 확인해줘
2. 중복 파일과 임시 파일을 찾아서 삭제해줘
3. 나머지 파일들을 생성 년도별로 폴더를 만들어서 정리해줘
   (예: 2023년, 2024년, 2025년)
```

</div>

<div>

### Agent가 할 일

1. 다운로드 폴더 스캔
2. 중복/임시 파일 식별
3. 삭제 대상 확인 요청
4. 년도별 폴더 생성
5. 파일 이동 및 결과 보고

### 향후 도전 과제

**도전 1**: 파일 크기 확인
```
10MB 이상 큰 파일들을 별도로
"대용량_파일" 폴더로 분류해줘
```

**도전 2**: 정리 리포트
```
정리 결과를 report.txt로 만들어줘:
- 삭제한 파일 수와 용량
- 년도별 파일 수
```

</div>

</div>

---

## Plan 모드란?

### 안전장치: 실행 전에 계획 검토하기

**Plan 모드**: Agent가 실행하기 **전에** 계획을 보여줌

| 일반 모드 | Plan 모드 |
|----------|-----------|
| 프롬프트 → 바로 실행 | 프롬프트 → **계획 확인** → 승인 → 실행 |
| 빠르지만 위험 | 느리지만 안전 |

**비유**: "일 시키기 전에 보고받기"

### Plan 모드 진입 방법

**Claude Code**: 키보드에서 `Shift + Tab` 두 번 누르기
**Gemini, Codex**: Plan 모드 미지원 (일반 모드에서 신중하게 프롬프트 작성)

**표시**: `[Plan Mode]` 라는 표시가 나타남 (Claude만)

---

## 실습 3: Plan 모드 체험

### 목표

**Plan 모드로 간단한 카운터 만들기** (Claude 사용자)
**신중한 프롬프트로 카운터 만들기** (Gemini, Codex 사용자)

### 기본 과제 (10분)

**Claude 사용자**:
1. `Shift + Tab` 두 번 눌러 Plan 모드 진입
2. 다음 프롬프트 입력:

```
간단한 카운터 HTML을 만들어줘.
버튼을 누르면 숫자가 1씩 증가하는 기능.
파일명은 counter.html로 해줘.
```

3. **Agent의 계획 확인** (여기가 핵심!)
4. 괜찮으면 `Y`, 수정하려면 추가 지시
5. 실행 후 브라우저로 확인

**Gemini, Codex 사용자**: 위 프롬프트를 그대로 입력 → 바로 실행

---

## 실습 3: 향후 도전 과제

### 향후 도전 과제

계획을 확인했는데 뭔가 추가하고 싶다면?

**예시**:
- Agent 계획: "카운터 HTML 생성"
- 여러분: "색상 선택 버튼도 추가해줘"

**학습 포인트**:
- Plan 모드 = 실행 전 검토
- 계획 단계에서 수정 가능
- 안전하게 작업할 수 있음

<div class="highlight">
중요한 파일 작업 시 Plan 모드를 습관화하세요!
</div>

---

## 회고: 첫 실습 마무리

### 질문

1. **성공했나요?**
   - 실습 1, 2, 3을 모두 완료했나요?

2. **어떤 점이 놀라웠나요?**
   - "프롬프트 한 번에 파일이 만들어졌어요" (실습 1)
   - "Agent가 내 컴퓨터 파일을 직접 정리했어요" (실습 2)
   - "Plan 모드로 미리 확인할 수 있다니!" (실습 3, Claude)

3. **어디에 써먹을 수 있을까요?**
   - 파일 정리, 문서 생성, 간단한 웹 도구, 반복 작업 자동화...

<div class="highlight">
<strong>오늘의 메시지</strong>: 개발자가 아니어도 Agent와 함께라면 만들 수 있습니다!
</div>

---

<!-- _class: lead -->

# 휴식 시간 (15분)

다음 시간에는 **AI 시대의 3가지 키워드**를 배웁니다:

**선택 · 계획 · 문서화**

지금까지 체험한 내용이 왜 중요한지 이해하게 됩니다!

---
<!-- _class: lead -->

# Just Plan It!

**Part 3: AI 시대 3가지 키워드**

선택 · 계획 · 문서화

---

<div class="question">
AI가 모든 것을 만들어주는 시대, 어떻게 '내 것'으로 만드는가?
</div>

### Part 1-2에서의 경험

Agent가 정말 많은 걸 해줬습니다:

- 코드 작성, 파일 생성, 스타일 디자인...
- 질문에 답하고, 문제를 해결하고, 실수를 고치고...

### 그런데 핵심 질문

- Agent가 만든 결과물은 누구의 것인가요?
- 어떻게 하면 "내가 만든 것"이 될까요?
- AI 시대에 인간의 역할은 무엇일까요?

**AI가 다 만들어줘도, "나의 의미"를 담아야 내 것이 됩니다**

---

