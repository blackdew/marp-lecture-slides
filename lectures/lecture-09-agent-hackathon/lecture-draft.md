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
</style>

<!-- _class: lead -->

# 비개발자를 위한
# AI 에이전트 해커톤

**Part 1-2: 시작하기 & 첫 실습**

AI Agent와 첫 만남

---

## 오늘 배울 내용 (Part 1-2)

### Part 1: 시작하기 (50분)

- 환경 확인: Claude Code 실행 테스트
- AI Agent란 무엇인가?
- Agent의 구조: Tools의 힘

### Part 2: 첫 실습 (70분)

- **실습 1**: 환영 페이지 만들기 (20분)
- **실습 2**: 다운로드 폴더 정리 (20분)
- **실습 3**: Plan 모드 체험 (20분)
- 회고: 첫 실습 마무리 (10분)

**핵심 메시지**: "복잡한 이론보다 먼저 체험하기!"

---

## AI Agent CLI 도구 비교

### 어떤 Agent를 선택할까요?

| 도구 | 가격 | CLI 지원 | 특징 |
|------|------|----------|------|
| **Claude Code** | 유료 | O | Plan 모드로 실행 전 계획 검토 가능. 한국어 및 긴 문서 작업에 강함. 비개발자 친화적 프롬프트 이해력 |
| **Gemini** | 무료 | O | 완전 무료로 사용 가능. 빠른 응답 속도. 다양한 파일 형식 처리. Google AI Studio API 기반 |
| **Codex** | 유료/무료 | O | ChatGPT Plus 구독자는 무료 사용 가능. 프로그래밍 언어 특화. 코드 자동완성 및 생성에 강함 |

**오늘 강의**: Claude Code CLI를 중심으로 진행
**대안 옵션**: Gemini CLI (완전 무료), Codex (ChatGPT Plus 구독자 무료) - 설치 방법은 다음 슬라이드

---

## 왜 Claude Code를 선택했나요?

### 비개발자 친화적인 4가지 이유

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

<div>

**1. 한국어 지원 우수**
- 자연스러운 한국어 이해 및 생성
- 한국어 문서 작업에 강함

**2. Plan 모드 (안전장치)**
- 실행 전 계획 검토 가능
- 실수 방지, 학습에 유리

</div>

<div>

**3. 문서 작업 능력**
- 긴 문서 요약, 생성 우수
- 비개발 업무에 적합

**4. 비개발자 친화적**
- 자연어 프롬프트 이해력 높음
- 에러 메시지도 친절

</div>

</div>

**다른 옵션**: 완전 무료 → Gemini CLI / ChatGPT Plus 구독자 → Codex

---

## 실습 준비: CLI 환경 이해하기

### CLI(Command Line Interface)란?

**CLI**: 텍스트 명령어로 컴퓨터와 대화하는 방식
- GUI (그래픽): 마우스 클릭, 아이콘
- CLI (명령어): 키보드로 텍스트 입력

**왜 CLI를 사용할까요?**
- 빠르고 정확한 작업
- 반복 작업 자동화
- 개발 도구 대부분이 CLI 기반

### 터미널 여는 법

**Mac**: Spotlight 검색 (⌘+Space) → "터미널" 입력
**Windows**: 시작 메뉴 → "cmd" 또는 "PowerShell" 검색

---

## 설치 옵션: Claude Code

### 옵션 A: Claude Code CLI (권장, 유료)

**설치 가이드**: https://getclaudecode.com/

**설치 명령어**:
```bash
npm install -g @anthropic-ai/claude-code
```

**실행**:
```bash
claude --version
claude
```

**비용**: Anthropic API 키 필요 (사용량 기반 과금)

---

## 설치 옵션: Gemini (무료 대안)

### 옵션 B: Gemini CLI (무료)

**설치 가이드**: https://getclaudecode.com/

위 가이드의 **4번 Claude Code 설치** 단계에서 아래 명령어로 대체:

```bash
npm install -g @google/gemini-cli
```

**실행**:
```bash
gemini --version
gemini
```

**비용**: 완전 무료 (Google AI Studio API)

---

## 설치 옵션: Codex (ChatGPT 구독자용)

### 옵션 C: OpenAI Codex (ChatGPT Plus/Pro 구독자)

**설치 가이드**: https://getclaudecode.com/

위 가이드의 **4번 Claude Code 설치** 단계에서 아래 명령어로 대체:

```bash
npm install -g @openai/codex
```

**실행 및 인증**:
```bash
codex
# 처음 실행 시 브라우저에서 ChatGPT 계정으로 로그인
```

**비용**:
- ChatGPT Plus/Pro 구독자: 포함된 크레딧 사용 (추천)
- API 키: `codex login --api-key <KEY>` (사용량 기반 과금)

**특징**: 프로그래밍 언어에 특화. 코드 생성 및 자동완성에 강함

---

## 실습 준비: 기본 명령어

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

<div>

### 알아두면 유용한 명령어

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `pwd` | 현재 위치 확인 | `pwd` |
| `ls` | 파일 목록 보기 | `ls` |
| `cd` | 디렉토리 이동 | `cd Documents` |
| `mkdir` | 폴더 만들기 | `mkdir my-project` |

### 작업 디렉토리 만들기

```bash
mkdir ai-hackathon
cd ai-hackathon
pwd    # 위치 확인
```

</div>

<div>

### Windows 사용자: Git Bash 권장

**PowerShell/cmd 대신 Git Bash를 사용하세요**

**이유**:
- Mac과 동일한 Unix 스타일 명령어 사용 가능
- 개발 도구 대부분이 Unix 기반으로 설계됨
- AI Agent CLI 도구들도 Unix 환경에 최적화

**설치**: [git-scm.com](https://git-scm.com) → Git 설치 시 Git Bash 자동 포함

</div>

</div>

**주의**: 강의 시연은 Claude 기준이지만, Gemini와 Codex도 대부분 동일하게 작동합니다!

---

## 실습 준비: Agent와 첫 대화

### Agent 실행 및 첫 대화

설치한 Agent를 실행해보세요:

```bash
claude    # 또는 gemini, codex
```

**프롬프트가 나타나면 입력**:
```
안녕? 자기소개 해줘.
```

**Agent가 응답하면 성공!**

**종료하기**: `Ctrl+C` 또는 `/exit`

---

## Part 1-2: AI Agent란?

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

<div>

### 챗봇 vs Agent - 무엇이 다를까요?

| 구분 | 챗봇 | Agent |
|------|------|-------|
| **할 수 있는 것** | 대화, 조언, 설명 | 대화 + **파일 조작** |
| **도구 사용** | 없음 | 파일 읽기/쓰기, 코드 실행 |
| **비유** | 똑똑한 친구 | **도구를 쓰는 비서** |
| **예시** | "Python 코드 알려줘" | "Python 파일 만들어줘" |

</div>

<div>

### CLI를 사용하는 이유

**CLI를 통해 Agent가 컴퓨터 기능에 직접 접근할 수 있습니다**

- **파일 시스템**: 내 컴퓨터의 파일을 읽고, 만들고, 수정
- **명령 실행**: 프로그램 실행, 데이터 처리, 작업 자동화
- **도구 연결**: Git, Python, 데이터베이스 등 개발 도구 활용

**웹 챗봇과의 차이**:
- 웹 챗봇: 브라우저 안에서만 작동 (복사/붙여넣기 필요)
- CLI Agent: 내 컴퓨터에서 직접 작업 (자동화 가능)

</div>

</div>

<div class="highlight">
핵심: CLI를 사용하면 Agent가 <strong>내 컴퓨터의 도구(Tools)를 직접 사용</strong>할 수 있습니다!
</div>

---

## Agent의 구조: Tools의 힘

### Agent = LLM + Memory + Planning + **Tools**

**AI Agent를 구성하는 4가지 요소:**

**1. LLM (뇌)**
- 언어 이해 및 생성

**2. Memory (기억)**
- 대화 맥락 유지

**3. Planning (계획)**
- 단계별 작업 계획

**4. Tools (도구) ← 핵심!**
- Read, Write, Edit, Bash...
- 실제 작업을 수행하는 능력

**비유**: 요리사에게 레시피만 vs **재료와 도구까지 준 것**

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

**난이도**: 매우 쉬움

---

## 실습 1: 프롬프트 및 실행

### 기본 과제 (20분)

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

### 도전 과제 (10분)

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

### 기본 과제 (20분)

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

### 도전 과제 (10분)

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

### 기본 과제 (20분)

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

## 실습 3: 도전 과제

### 도전 과제 (10분)

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

# 휴식 시간 (20분)

다음 시간에는 **AI 시대의 3가지 키워드**를 배웁니다:

**선택 · 계획 · 문서화**

지금까지 체험한 내용이 왜 중요한지 이해하게 됩니다!

