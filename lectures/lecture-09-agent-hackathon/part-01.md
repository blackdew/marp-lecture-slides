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

<!-- _class: lead -->

# 비개발자를 위한
# AI 에이전트 해커톤

**Part 1: 시작하기**

환경 확인 및 AI Agent 첫 만남

---

## 이번 시간에 배울 내용 (Part 1)

### Part 1: 시작하기 (30분)

- 내 컴퓨터에서 Agent 실행해보기
- "AI Agent가 뭐죠?" - 챗봇과 다른 점
- Agent가 일하는 방법

**핵심 메시지**: "Agent = 도구를 쓸 줄 아는 똑똑한 동료"

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

## Part 1: AI Agent란?

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

<!-- _class: lead -->

# Part 1 마무리

다음은 **Part 2: 첫 실습**

실제로 Agent와 함께 작업해봅시다!
