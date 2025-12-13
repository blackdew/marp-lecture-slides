# Part 1: 인턴 입사 + 업무 환경 세팅

## AI Agent란?

### 챗봇 vs 에이전트

| 구분 | Chatbot | Agent |
|------|---------|-------|
| 역할 | 말만 함 (정보 제공) | **행동**을 함 (실무 수행) |
| 예시 | "여행 계획 텍스트 제공" | "비행기/호텔 예약 완료" |
| 한계 | 예약은 내가 직접 | 캘린더 등록, 메일 발송까지 |

> **"생각만 하던 관리자(Manager)에게, 실행하는 유능한 인턴(Intern)이 생겼습니다."**

---

## Agent의 구조 (4가지 요소)

### Agent = LLM + Memory + Planning + Tools

| 요소 | 역할 | 비유 |
|------|------|------|
| **LLM (Brain)** | 추론 및 결정 | 똑똑한 두뇌 |
| **Memory (Context)** | 기억 및 맥락 | 업무 수첩 |
| **Planning (Strategy)** | 계획 수립 | 업무 매뉴얼 |
| **Tools (Action)** | 실제 행동 | 손과 발 |

> "이 인턴의 잠재력은 엄청납니다. 단, <strong>좋은 사수(여러분을)</strong>를 만났을 때만 그렇습니다."

---

## Agent 워크플로우

### 6단계 작업 흐름

1. **요구사항 (User/Manager)**: "김 대리(Agent), 이번 달 매출 분석해줘." (목표 제시)
2. **계획 (Agent/Intern)**: "네, 그럼 파일 A, B를 열어서 합치면 될까요?" (계획 수립)
3. **확인 (User/Manager)**: "응, 맞아. 대신 날짜 형식은 꼭 맞춰." (승인 및 피드백)
4. **실행 (Agent/Intern)**: (열심히 작업 중...) (도구 사용)
5. **검증 (User/Manager)**: "어? 여기 합계가 틀렸는데?" (결과 검증)
6. **완료 (Completion)**: "수정했습니다. 여기 있습니다!" (최종 보고)

---

## AI Agent CLI 도구 비교

### 어떤 Agent를 선택할까요?

| 도구 | 가격 | 특징 |
|------|------|------|
| **Claude Code** | 유료 | Plan 모드로 계획 검토. 코드 품질 우수 |
| **Gemini CLI** | 무료 | 완전 무료. 빠른 응답. Google AI Studio 기반 |
| **Codex** | 유료/무료 | ChatGPT Plus 구독자 무료. OpenAI 기반 |

**오늘 강의**: Claude Code를 중심으로 진행 (코드 품질 우수!)
**대안 옵션**: Gemini CLI (무료), Codex (ChatGPT Plus 구독자)

---

## 왜 Claude Code를 선택했나요?

### 비개발자를 위한 4가지 이유

| 이유 | 설명 |
|------|------|
| **Plan 모드** | 실행 전 계획 검토 가능 (안전장치) |
| **코드 품질** | 정확하고 신뢰할 수 있는 코드 생성 |
| **파일 처리** | 다양한 파일 형식 읽기/쓰기 지원 |
| **쉬운 설치** | Node.js만 있으면 바로 설치 |

**다른 옵션**: 무료로 시작 → Gemini CLI / ChatGPT Plus 구독자 → Codex

---

## CLI(Command Line Interface)란?

### CLI vs GUI

| 구분 | CLI (명령어) | GUI (그래픽) |
|------|-------------|-------------|
| **사용 방법** | 키보드로 텍스트 입력 | 마우스 클릭 |
| **장점** | 빠르고 정확, 자동화 가능 | 직관적, 배우기 쉬움 |
| **예시** | 터미널, PowerShell | 웹 브라우저, 탐색기 |

### 터미널 여는 법

- **Mac**: Spotlight 검색 (⌘+Space) → "터미널" 입력
- **Windows**: 시작 메뉴 → "PowerShell" 또는 "cmd" 검색

---

## 강의용 Claude Code 설치

### 1단계: 설치 가이드 따라하기

**설치 가이드**: https://getclaudecode.com/

**설치 명령어**:
```bash
npm install -g @anthropic-ai/claude-code
```

### 2단계: 강의용 계정 연결

**계정 공유 링크**: https://example.com/lecture-account (추후 공유 예정)

**실행**:
```bash
claude
```

> **참고**: 강의용 계정이 제공되므로 별도 결제가 필요 없습니다.

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

**실행**:
```bash
codex
```

**비용**: ChatGPT Plus/Pro 구독자 크레딧 사용 (추천)

---

## 설치 비교 요약

### 어떤 도구를 선택할까요?

| 상황 | 권장 도구 |
|------|-----------|
| 코드 품질과 안정성이 중요하다 | **Claude Code** |
| 무료로 시작하고 싶다 | Gemini CLI |
| ChatGPT Plus를 이미 구독 중이다 | Codex |

### 오늘 강의 기준

- **메인**: Claude Code (모든 예시는 Claude Code 기준)
- 다른 도구도 명령어만 다르고 사용법은 거의 동일!

---

## 터미널 기초

### 필수 명령어

| 작업 | Mac/Linux | Windows |
|------|-----------|---------|
| 폴더 이동 | `cd Documents` | `cd Documents` |
| 파일 목록 | `ls` | `dir` |
| 현재 위치 | `pwd` | `cd` (인자 없이) |
| 폴더 생성 | `mkdir project` | `md project` |

### 팁

- **Tab 키**: 자동 완성
- **위/아래 화살표**: 이전 명령어
- **Ctrl + C**: 실행 중단

---

## 실습: 작업 폴더 만들기

### Mac/Linux vs Windows

| Mac/Linux | Windows |
|-----------|---------|
| `cd ~/Desktop` | `cd %USERPROFILE%\Desktop` |
| `mkdir ai-workshop` | `md ai-workshop` |
| `cd ai-workshop` | `cd ai-workshop` |
| `pwd` | `cd` |

폴더가 생성되었으면 다음 단계로!

---

## 실습: 첫 번째 대화

### Claude Code 실행

```bash
claude
```

### 입력해보세요

```
안녕, 너는 누구니? 어떤 모델을 사용하고 있어?
```

### 확인할 점

| 항목 | 기대 결과 |
|------|-----------|
| 한국어 응답 | 자연스러운 한국어 답변 |
| 모델 정보 | Claude 모델 이름 확인 |
| 응답 속도 | 빠른 응답 |

---

## 실습: 파일 생성 체험

### Claude에게 요청

```
"안녕하세요"라고 적힌 hello.txt 파일을 만들어줘
```

### 확인

```bash
cat hello.txt   # Mac
type hello.txt  # Windows
```

### 성공!

> **축하합니다!** AI Agent가 실제로 파일을 생성했습니다.
> 이것이 바로 Agent의 **Tools** 기능입니다!

---

## 대안: AntiGravity (GUI 사용자용)

### CLI가 어렵다면?

- **AntiGravity**: GUI 기반 AI Agent 도구
- 마우스 클릭으로 동일한 기능 사용 가능
- 설치: https://antigravity.google/

### 언제 사용하나요?

| 상황 | 권장 도구 |
|------|-----------|
| 터미널이 익숙함 | Claude Code |
| GUI 선호 | AntiGravity |
| 빠른 시각적 확인 | AntiGravity |
| 자동화/스크립트 연동 | Claude Code |

---

## 체크포인트

| 단계 | 확인 사항 | 완료 |
|------|-----------|------|
| 1 | Node.js 설치 확인 (`node --version`) | ☐ |
| 2 | Claude Code 설치 (`claude --version`) | ☐ |
| 3 | Anthropic 계정 인증 완료 | ☐ |
| 4 | 첫 대화 성공 | ☐ |
| 5 | 파일 생성 체험 완료 | ☐ |

> **다음 시간**: JavaScript 코드 생성 및 실행!
