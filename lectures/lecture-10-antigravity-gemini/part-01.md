# Part 1: AI Agent 소개 + 환경 설정

## AI Agent란?

- **Chatbot vs Agent**:
  - **Chatbot**: 말만 함 (정보 제공)
  - **Agent**: **행동(Action)**을 함 (실무 수행)

- **AI Agent**:
  > **"생각만 하던 AI에게, 실행하는 손발이 생겼습니다."**

  - **LLM (뇌)**: 생각하고 계획함
  - **Tools (손발)**: 실제로 도구를 사용해 일을 처리함

> "단순 반복은 AI에게 맡기고, 우리는 **결정**과 **기획**에 집중합시다."

---

## 챗봇 vs 에이전트: 비교

| 구분 | Chatbot (기존) | Agent (미래) |
|------|---------------|--------------|
| **예시 요청** | "여행 계획 짜줘" | "여행 계획 짜줘" |
| **결과** | 텍스트로 된 계획표 | 비행기/호텔 **예약 완료** |
| **한계/특징** | 예약은 내가 직접 | 캘린더 등록, 메일 발송까지 수행 |

---

## Agent의 구조 (4가지 요소)

> **Agent = LLM + Memory + Planning + Tools**

| 요소 | 역할 | 비유 |
|------|------|------|
| **LLM (Brain)** | 추론 및 결정 | 똑똑한 두뇌 |
| **Memory (Context)** | 기억 및 맥락 | 업무 수첩 |
| **Planning (Strategy)** | 계획 수립 | 업무 매뉴얼 |
| **Tools (Action)** | 실제 행동 | 손과 발 |

---

## Agent 워크플로우

1. **요구사항 (User)**: 사용자가 목표 제시
2. **계획 (Planning)**: Memory를 참조하여 단계별 계획 수립
3. **확인 (Confirm)**: 사용자에게 계획 승인 요청 (피드백 루프)
4. **실행 (Execution)**: 도구(Tools)를 사용하여 작업 수행
5. **검증 (Verification)**: 결과 확인 (실패 시 재계획)
6. **완료 (Completion)**: 최종 결과 전달

---

## AI Agent CLI 도구 비교

### 어떤 Agent를 선택할까요?

| 도구 | 가격 | CLI 지원 | 특징 |
|------|------|----------|------|
| **Gemini CLI** | 무료 | O | 완전 무료. 빠른 응답. Google AI Studio API 기반 |
| **Claude Code** | 유료 | O | Plan 모드로 실행 전 계획 검토 가능. 한국어에 강함 |
| **Codex** | 유료/무료 | O | ChatGPT Plus 구독자는 무료. 코드 생성에 특화 |

**오늘 강의**: Gemini CLI를 중심으로 진행 (무료!)
**대안 옵션**: Claude Code (유료), Codex (ChatGPT Plus 구독자)

---

## 왜 Gemini CLI를 선택했나요?

### 비개발자를 위한 4가지 이유

| 이유 | 설명 |
|------|------|
| **완전 무료** | 별도 결제 없이 바로 사용 가능 |
| **빠른 응답** | Google 인프라 기반 빠른 처리 속도 |
| **파일 처리** | 다양한 파일 형식 읽기/쓰기 지원 |
| **쉬운 설치** | Node.js만 있으면 바로 설치 |

**다른 옵션**: 더 강력한 기능 → Claude Code / ChatGPT Plus 구독자 → Codex

---

## CLI(Command Line Interface)란?

### CLI vs GUI

| 구분 | CLI (명령어) | GUI (그래픽) |
|------|-------------|-------------|
| **사용 방법** | 키보드로 텍스트 입력 | 마우스 클릭 |
| **장점** | 빠르고 정확, 자동화 가능 | 직관적, 배우기 쉬움 |
| **예시** | 터미널, PowerShell | 웹 브라우저, 탐색기 |

### 왜 CLI를 사용할까요?

- **자동화**: 반복 작업을 스크립트로 처리
- **정확성**: 마우스 클릭 실수 방지
- **통합**: 개발 도구 대부분이 CLI 기반

### 터미널 여는 법

- **Mac**: Spotlight 검색 (⌘+Space) → "터미널" 입력
- **Windows**: 시작 메뉴 → "PowerShell" 또는 "cmd" 검색

---

## 설치 전 준비: Node.js 확인

### Node.js란?

- JavaScript를 컴퓨터에서 실행하게 해주는 런타임
- Gemini CLI를 포함한 대부분의 AI CLI 도구가 Node.js 기반

### 설치 확인

```bash
node --version
```

- 버전 번호가 나오면 → 이미 설치됨!
- `command not found` → Node.js 설치 필요

### Node.js 설치 (필요한 경우)

1. https://nodejs.org/ 접속
2. **LTS 버전** 다운로드 및 설치
3. 터미널 재시작 후 다시 확인

---

## 설치 옵션 1: Gemini CLI (권장, 무료)

### Gemini CLI 설치

```bash
npm install -g @google/gemini-cli
```

### 첫 실행

```bash
gemini
```

- 처음 실행 시 브라우저에서 Google 계정 인증
- 인증 완료 후 터미널에서 바로 사용 가능

### 비용

- **완전 무료** (Google AI Studio API 기반)
- 별도 API 키나 결제 정보 불필요

---

## 설치 옵션 2: Claude Code (유료)

### Claude Code CLI 설치

**설치 가이드**: https://getclaudecode.com/

```bash
npm install -g @anthropic-ai/claude-code
```

### 실행

```bash
claude --version
claude
```

### 비용

- Anthropic API 키 필요 (사용량 기반 과금)
- **Plan 모드**: 실행 전 계획 검토 가능 (안전장치)

---

## 설치 옵션 3: Codex (ChatGPT 구독자용)

### OpenAI Codex 설치

```bash
npm install -g @openai/codex
```

### 실행 및 인증

```bash
codex
# 처음 실행 시 브라우저에서 ChatGPT 계정으로 로그인
```

### 비용

- ChatGPT Plus/Pro 구독자: 포함된 크레딧 사용 (추천)
- API 키: `codex login --api-key <KEY>` (사용량 기반 과금)

**특징**: 프로그래밍 언어에 특화. 코드 생성 및 자동완성에 강함

---

## 설치 비교 요약

### 어떤 도구를 선택할까요?

| 상황 | 권장 도구 |
|------|-----------|
| 처음이고 무료로 시작하고 싶다 | **Gemini CLI** |
| 한국어 작업이 많다 | Claude Code |
| ChatGPT Plus를 이미 구독 중이다 | Codex |
| 코드 생성이 주 목적이다 | Codex |

### 오늘 강의 기준

- **메인**: Gemini CLI (모든 예시는 Gemini 기준)
- 다른 도구도 명령어만 다르고 사용법은 거의 동일!

---

## 터미널 기초 (처음이신 분들을 위해)

### 필수 명령어

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `cd` | 폴더 이동 | `cd Documents` |
| `ls` | 파일 목록 보기 | `ls` |
| `pwd` | 현재 위치 확인 | `pwd` |
| `mkdir` | 폴더 생성 | `mkdir project` |

### 팁

- **Tab 키**: 자동 완성
- **위/아래 화살표**: 이전 명령어
- **Ctrl + C**: 실행 중단

---

## 실습: 첫 번째 대화

### Gemini CLI에서 입력해보세요

```
안녕, 너는 누구니? 어떤 모델을 사용하고 있어?
```

### 확인할 점

| 항목 | 기대 결과 |
|------|-----------|
| 한국어 응답 | 자연스러운 한국어 답변 |
| 모델 정보 | Gemini 모델 이름 확인 |
| 응답 속도 | 빠른 응답 |

---

## 실습: 파일 생성 체험

### Gemini에게 요청

```
"안녕하세요"라고 적힌 hello.txt 파일을 만들어줘
```

### 확인

```bash
cat hello.txt
```

> **축하합니다!** AI Agent가 실제로 파일을 생성했습니다.

---

## 대안: AntiGravity (GUI 사용자용)

### CLI가 어렵다면?

- **AntiGravity**: GUI 기반 AI Agent 도구
- 마우스 클릭으로 동일한 기능 사용 가능
- 설치: https://antigravity.google/

### 언제 사용하나요?

| 상황 | 권장 도구 |
|------|-----------|
| 터미널이 익숙함 | Gemini CLI |
| GUI 선호 | AntiGravity |
| 빠른 시각적 확인 | AntiGravity |
| 자동화/스크립트 연동 | Gemini CLI |

---

## 체크포인트

| 단계 | 확인 사항 | 완료 |
|------|-----------|------|
| 1 | Node.js 설치 확인 (`node --version`) | ☐ |
| 2 | Gemini CLI 설치 (`gemini --version`) | ☐ |
| 3 | Google 계정 인증 완료 | ☐ |
| 4 | 첫 대화 성공 | ☐ |
| 5 | 파일 생성 체험 완료 | ☐ |

> **다음 시간**: Python 코드 생성 및 실행!
