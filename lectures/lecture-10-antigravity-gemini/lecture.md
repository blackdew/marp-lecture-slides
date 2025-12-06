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

![bg left:35%](images/img_title_ai_agent.svg)

# Gemini CLI
## AI 에이전트 활용 마스터 클래스

**비개발자를 위한 실무 자동화 + 코딩**

---

## 오늘의 여정

### 전체 일정 (6시간)

| Part | 주제 | 시간 |
|------|------|------|
| **1** | AI Agent 소개 + 환경 설정 | 50분 |
| **2** | JavaScript 기초 with Gemini | 45분 |
| **3** | 파일 자동화 + AI 시대 우리의 역할 | 90분 |
| **4** | 웹 정보 수집 + 콘텐츠 생성 | 60분 |
| **5** | 나만의 프로토타입 만들기 | 70분 |
| **6** | AI 윤리 + 마무리 | 50분 |

**산출물**: 자동화 솔루션 프로토타입 5개 이상

---

<!--
_class: lead
-->

# Part 1

## AI Agent 소개 + 환경 설정

---

## 이번 시간에 배울 내용 (Part 1)

### Part 1: 시작하기 (50분)

- "AI Agent가 뭐죠?" - 챗봇과 다른 점
- Agent가 일하는 방법 (구조와 워크플로우)
- 내 컴퓨터에서 Agent 실행해보기

**핵심 메시지**: "Agent = 도구를 쓸 줄 아는 똑똑한 동료"

---

## AI Agent란?

### 챗봇 vs 에이전트

| 구분 | Chatbot | Agent |
|------|---------|-------|
| 역할 | 말만 함 (정보 제공) | **행동**을 함 (실무 수행) |
| 예시 | "여행 계획 텍스트 제공" | "비행기/호텔 예약 완료" |
| 한계 | 예약은 내가 직접 | 캘린더 등록, 메일 발송까지 |

> **"생각만 하던 AI에게, 실행하는 손발이 생겼습니다."**

---

## Agent의 구조 (4가지 요소)

### Agent = LLM + Memory + Planning + Tools

| 요소 | 역할 | 비유 |
|------|------|------|
| **LLM (Brain)** | 추론 및 결정 | 똑똑한 두뇌 |
| **Memory (Context)** | 기억 및 맥락 | 업무 수첩 |
| **Planning (Strategy)** | 계획 수립 | 업무 매뉴얼 |
| **Tools (Action)** | 실제 행동 | 손과 발 |

> "단순 반복은 AI에게 맡기고, 우리는 **결정**과 **기획**에 집중합시다."

---

## Agent 워크플로우

### 6단계 작업 흐름

1. **요구사항 (User)**: 사용자가 목표 제시
2. **계획 (Planning)**: Memory를 참조하여 단계별 계획 수립
3. **확인 (Confirm)**: 사용자에게 계획 승인 요청 (피드백 루프)
4. **실행 (Execution)**: 도구(Tools)를 사용하여 작업 수행
5. **검증 (Verification)**: 결과 확인 (실패 시 재계획)
6. **완료 (Completion)**: 최종 결과 전달

---

## Agent 워크플로우 (시각화)

![width:1100px](images/img_agent_workflow.svg)

---

## Agent 워크플로우 핵심 포인트

### User → Agent → Tools → Result

| 단계 | 설명 |
|------|------|
| **Planning** | Memory를 참조해 계획 수립 |
| **Confirm** | 사용자에게 확인 요청 |
| **Execution** | Tools를 사용해 실제 작업 수행 |
| **Verify** | 결과 검증 (실패 시 재계획) |

> 핵심: 피드백 루프를 통한 지속적 개선

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

---

## Node.js 설치 (필요한 경우)

### 설치 방법

1. https://nodejs.org/ 접속
2. **LTS 버전** 다운로드 (안정화 버전)
3. 설치 프로그램 실행
4. 터미널 재시작 후 다시 확인

### 확인

```bash
node --version   # v18 이상 권장
npm --version    # npm도 함께 설치됨
```

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

## 터미널 기초

### 필수 명령어

| 명령어 | 설명 | 예시 |
|--------|------|------|
| `cd` | 폴더 이동 | `cd Documents` |
| `ls` (Mac) / `dir` (Win) | 파일 목록 | `ls` |
| `pwd` | 현재 위치 | `pwd` |
| `mkdir` | 폴더 생성 | `mkdir project` |

### 팁

- **Tab 키**: 자동 완성
- **위/아래 화살표**: 이전 명령어
- **Ctrl + C**: 실행 중단

---

## 실습: 작업 폴더 만들기

### 터미널에서 실행

```bash
# Mac
cd ~/Desktop
mkdir ai-workshop
cd ai-workshop
pwd

# Windows
cd %USERPROFILE%\Desktop
mkdir ai-workshop
cd ai-workshop
```

### 확인

폴더가 생성되었으면 다음 단계로!

---

## 실습: 첫 번째 대화

### Gemini CLI 실행

```bash
gemini
```

### 입력해보세요

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
| 터미널이 익숙함 | Gemini CLI |
| GUI 선호 | AntiGravity |
| 빠른 시각적 확인 | AntiGravity |
| 자동화/스크립트 연동 | Gemini CLI |

---

## 체크포인트 (Part 1)

### 확인 사항

| 단계 | 확인 사항 | 완료 |
|------|-----------|------|
| 1 | Node.js 버전 확인 (`node --version`) | ☐ |
| 2 | Gemini CLI 설치 (`gemini --version`) | ☐ |
| 3 | Google 계정 인증 완료 | ☐ |
| 4 | 첫 대화 성공 | ☐ |
| 5 | 파일 생성 체험 완료 | ☐ |

> **다음 시간**: JavaScript 코드 생성 및 실행!

---

<!--
_class: lead
-->

# Part 2

## JavaScript 기초 with Gemini

---

## 이번 시간에 배울 내용 (Part 2)

### Part 2: JavaScript 기초 (45분)

- 왜 JavaScript인가?
- Gemini가 생성한 코드 실행하기
- 간단한 프로그램 만들기

**핵심 메시지**: "코드를 외울 필요 없이, AI에게 시키면 됩니다"

---

## 왜 JavaScript인가?

### Node.js가 이미 설치되어 있습니다!

- Gemini CLI 설치할 때 Node.js를 설치했음
- **추가 설치 없이** 바로 코딩 시작 가능

### JavaScript의 장점

| 장점 | 설명 |
|------|------|
| **범용성** | 웹, 서버, 앱 모두 가능 |
| **인기** | 세계에서 가장 많이 사용되는 언어 |
| **AI 친화적** | AI가 잘 생성하는 언어 |

> **"코드를 외울 필요 없이, AI에게 시키면 됩니다."**

---

## JavaScript 기본 개념: 변수

### 변수란?

데이터를 담는 상자

```javascript
const name = "홍길동";  // 변하지 않는 값
let age = 25;          // 변할 수 있는 값
```

### const vs let

| 키워드 | 용도 | 예시 |
|--------|------|------|
| `const` | 고정 값 | 이름, 설정값 |
| `let` | 변하는 값 | 나이, 점수 |

---

## JavaScript 기본 개념: 출력

### console.log()

화면에 결과를 출력하는 함수

```javascript
console.log("안녕하세요");
console.log(`이름: ${name}`);  // 템플릿 문자열
```

### 템플릿 문자열

- 백틱(`) 사용
- `${변수}` 형식으로 변수 삽입

```javascript
const item = "커피";
const price = 4500;
console.log(`${item}의 가격은 ${price}원입니다.`);
```

---

## JavaScript 기본 개념: 조건문

### if-else 문

조건에 따라 다른 동작 수행

```javascript
const score = 85;

if (score >= 90) {
  console.log("A학점");
} else if (score >= 80) {
  console.log("B학점");
} else {
  console.log("C학점");
}
```

### 비교 연산자

| 연산자 | 의미 |
|--------|------|
| `>=` | 크거나 같다 |
| `===` | 같다 |
| `!==` | 다르다 |

---

## 실습 2-1: Hello World

### Step 1: Gemini에게 요청

```
Hello World를 출력하는 JavaScript 코드를 만들어서 hello.js로 저장해줘
```

### Step 2: 실행

```bash
node hello.js
```

### 결과

```
Hello World
```

> **성공!** Gemini가 코드를 만들고, 우리가 실행했습니다!

---

## 실습 2-1: 코드 이해하기

### Gemini가 생성한 코드

```javascript
// hello.js
console.log("Hello World");
```

### 코드 분석

| 부분 | 설명 |
|------|------|
| `//` | 주석 (설명) |
| `console.log` | 출력 함수 |
| `"Hello World"` | 출력할 문자열 |
| `;` | 문장 끝 |

---

## 실습 2-2: 간단한 계산기

### Gemini에게 요청

```
두 숫자를 입력받아서 더하는 Node.js 프로그램을 만들어줘.
사용자가 터미널에서 직접 숫자를 입력할 수 있어야 해.
파일명은 calculator.js로 해줘.
```

### 실행

```bash
node calculator.js
```

### 확인

- 숫자 두 개를 입력할 수 있는가?
- 더한 결과가 나오는가?

---

## 실습 2-2: 코드 이해하기

### readline 모듈

사용자 입력을 받는 Node.js 내장 모듈

```javascript
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
```

### 숫자 변환

```javascript
const num = parseInt(input);  // 문자열 → 정수
```

> 코드를 외울 필요 없습니다. AI에게 물어보면 됩니다!

---

## 도전 과제: 사칙연산 계산기

### Gemini에게 요청

```
calculator.js를 수정해서 사칙연산(+, -, *, /)을 선택할 수 있게 해줘.
사용자가 연산자를 선택하면 그에 맞는 계산을 수행해줘.
```

### 기대 결과

```
첫 번째 숫자: 10
두 번째 숫자: 5
연산자 (+, -, *, /): *
결과: 50
```

---

## 체크포인트 (Part 2)

### 확인 사항

| 단계 | 확인 사항 | 완료 |
|------|-----------|------|
| 1 | hello.js 실행 성공 | ☐ |
| 2 | calculator.js 실행 성공 | ☐ |
| 3 | 도전: 사칙연산 계산기 완료 | ☐ |

### 핵심 배움

- JavaScript 기본 문법 (변수, 출력, 조건문)
- `node 파일명.js`로 실행
- AI가 코드를 생성하고, 우리가 실행하고 검증

---

<!--
_class: lead
-->

# Part 3

## 파일 자동화 실습

---

## 이번 시간에 배울 내용 (Part 3)

### Part 3: 파일 자동화 (90분)

- CSV 파일 처리 (읽기, 쓰기, 통합)
- 폴더 자동 정리 스크립트
- AI 시대 우리의 역할 (선택, 계획, 문서화)

**목표**: 2개 프로토타입 완성!

---

## Node.js의 파일 처리

### 핵심 모듈

| 모듈 | 용도 | 설치 |
|------|------|------|
| `fs` | 파일 읽기/쓰기 | 내장 |
| `path` | 경로 처리 | 내장 |
| `csv-parser` | CSV 읽기 | npm install |
| `csv-writer` | CSV 쓰기 | npm install |

### 설치

```bash
npm install csv-parser csv-writer
```

---

## fs 모듈: 파일 시스템

### 주요 함수

| 함수 | 설명 |
|------|------|
| `fs.readFileSync()` | 파일 읽기 |
| `fs.writeFileSync()` | 파일 쓰기 |
| `fs.readdirSync()` | 디렉토리 목록 |
| `fs.mkdirSync()` | 디렉토리 생성 |

### 예시

```javascript
const fs = require('fs');

// 파일 읽기
const data = fs.readFileSync('hello.txt', 'utf8');
console.log(data);
```

---

## 실습 3-1: CSV 데이터 통합

### 시나리오

세 개의 월별 매출 파일을 하나로 합치기

- `sales_jan.csv` - 1월 매출
- `sales_feb.csv` - 2월 매출
- `sales_mar.csv` - 3월 매출

### 요구사항

1. 세 파일 통합
2. 날짜 포맷 통일 (YYYY-MM-DD)
3. `sales_merged.csv`로 저장

---

## 실습 3-1: Gemini에게 요청

### 프롬프트

```
다음 작업을 수행하는 Node.js 스크립트를 만들어줘:

1. sales_jan.csv, sales_feb.csv, sales_mar.csv 세 파일을 읽어서
2. 하나로 합치고
3. 날짜 컬럼을 YYYY-MM-DD 형식으로 통일하고
4. sales_merged.csv로 저장해줘

csv-parser와 csv-writer 패키지를 사용해줘.
파일명: merge_csv.js
```

---

## 실습 3-1: 실행 및 확인

### 샘플 데이터 생성

먼저 테스트용 CSV 파일이 필요합니다:

```
Gemini에게: sales_jan.csv, sales_feb.csv, sales_mar.csv
테스트 데이터를 만들어줘. 각 파일에 날짜, 상품명, 금액 컬럼이 있어야 해.
```

### 스크립트 실행

```bash
node merge_csv.js
```

### 결과 확인

```bash
cat sales_merged.csv
```

---

## 실습 3-1: 도전 과제

### 담당자별 매출 합계 추가

```
merge_csv.js를 수정해서 담당자별 총 매출 합계도 계산해줘.
결과를 sales_summary.csv로 저장해줘.
```

### 기대 결과

```csv
담당자,총매출
김철수,1500000
이영희,2300000
박민수,1800000
```

---

## 실습 3-2: 폴더 자동 정리

### 시나리오

Downloads 폴더의 파일들을 확장자별로 분류

### 분류 규칙

| 폴더 | 확장자 |
|------|--------|
| images | jpg, jpeg, png, gif |
| documents | pdf, doc, docx, xlsx |
| archives | zip, tar, gz |
| others | 나머지 |

---

## 실습 3-2: Gemini에게 요청

### 프롬프트

```
Downloads 폴더의 파일들을 확장자별로 분류하는 스크립트 만들어줘.

분류 규칙:
- images: jpg, jpeg, png, gif
- documents: pdf, doc, docx, xlsx
- archives: zip, tar, gz
- others: 나머지

파일명: organize_folder.js
```

---

## 실습 3-2: 코드 이해하기

### path 모듈

파일 경로를 다루는 Node.js 내장 모듈

```javascript
const path = require('path');

const filePath = '/Users/me/Downloads/photo.jpg';
const ext = path.extname(filePath);  // '.jpg'
const name = path.basename(filePath);  // 'photo.jpg'
```

### 파일 이동

```javascript
fs.renameSync(oldPath, newPath);
```

---

## 실습 3-2: 도전 과제

### 날짜별 폴더 생성

```
organize_folder.js를 수정해서 파일들을 날짜(수정일)별로도 정리해줘.
폴더 구조: images/2024-01-15/photo.jpg 형식으로 해줘.
```

### 기대 결과

```
images/
  2024-01-15/
    photo1.jpg
    photo2.png
  2024-01-16/
    photo3.gif
```

---

## 산출물 체크 (Part 3 - 실습)

### 프로토타입 1: 폴더 정리 스크립트

- [ ] 스크립트 실행 성공
- [ ] 파일이 확장자별로 분류됨

### 프로토타입 2: CSV 통합 분석기

- [ ] 세 파일이 하나로 합쳐짐
- [ ] 날짜 포맷 통일됨
- [ ] (도전) 담당자별 합계 계산됨

---

<!--
_class: lead
-->

# AI 시대, 우리의 역할

실습을 돌아보며

---

## AI 시대의 3가지 역할

> **"AI가 모든 걸 해도, 우리의 역할은 더 중요해집니다"**

| 키워드 | 핵심 | 왜 중요한가? |
|--------|------|--------------|
| **1. 선택** | 나의 가치와 선호 반영 | AI 결과물에 "나"를 담아야 내 것이 됨 |
| **2. 계획** | 컨텍스트 채우기 | 계획 없으면 엉뚱한 결과 |
| **3. 문서화** | 문서 = 프로젝트 | 문서화로 성찰하고 성장 |

---

## 1. 선택: 의미 담기

### Agent가 정교한 비교 제공

```
주간 보고서 형식을 5가지 스타일로 비교해줘
```

→ Agent가 장단점 분석 → **내가 가치 기반 선택**

### 같은 비교표, 다른 선택

| 팀 | 가치 | 선택 |
|----|------|------|
| A팀 | "효율 중시" | 불릿 포인트 |
| B팀 | "공감 중시" | 스토리텔링 |

> **"선택에서 자기가 드러납니다"**

---

## 1. 선택: 실습에서의 예시

### 폴더 정리 스크립트

여러 분류 방법 중 선택:
- 확장자별 분류
- 날짜별 분류
- 크기별 분류
- 프로젝트별 분류

### CSV 통합

여러 날짜 형식 중 선택:
- YYYY-MM-DD (ISO 표준)
- DD/MM/YYYY (유럽식)
- MM/DD/YYYY (미국식)

---

## 2. 계획: 의도 전달

### 시간 배분의 변화

| 구분 | 과거 | AI 시대 |
|------|------|---------|
| 계획 | 20% | **70%** |
| 실행 | 80% | 30% |

> Agent가 실행을 대신하므로, **계획에 더 많은 시간을 투자**해야 합니다.

---

## 2. 계획: 좋은 프롬프트의 3원칙

| 원칙 | 나쁜 예 | 좋은 예 |
|------|--------|--------|
| **구체성** | "정리해줘" | "PDF를 년도별로 정리" |
| **단계성** | "분석해줘" | "1) 로드 2) 정제 3) 집계" |
| **결과물** | "요약해줘" | "3문장으로 요약해서 저장" |

### 오늘 실습에서

```
# 나쁜 프롬프트
"CSV 파일 합쳐줘"

# 좋은 프롬프트
"sales_jan.csv, sales_feb.csv, sales_mar.csv를 합치고,
날짜를 YYYY-MM-DD로 통일해서 sales_merged.csv로 저장해줘"
```

---

## 3. 문서화: 성장 도구

### Before vs After AI

| 단계 | Before AI | After AI |
|------|----------|----------|
| 작성 | 직접 (2시간) | Agent (5분) |
| 비용 | 30-50% | **5-10%** |

### 문서 중심 사고

```
문서(계획) → 작업(Agent) → 문서(회고) → 성장
```

> **"Agent 덕분에 문서화가 거의 무료가 되었습니다"**

---

## 3. 문서화: 실습에서의 예시

### 회고 문서 만들기

```
오늘 만든 폴더 정리 스크립트에 대한 회고 문서를 작성해줘.

포함할 내용:
1. 무엇을 만들었는지
2. 어떤 어려움이 있었는지
3. 다음에 개선할 점
```

### 결과

- 작업 내용 기록
- 학습 포인트 정리
- 개선 아이디어 보존

---

## 정리: AI 시대의 3가지 역할

### 1. 선택 = 의미 담기

Agent가 비교 제공 → **나의 가치로 선택**

### 2. 계획 = 의도 전달

**계획에 70% 시간 투자** → 정확한 결과

### 3. 문서화 = 성장 도구

**문서 = 프로젝트 = 성찰 = 성장**

> **"AI가 만들어줘도, 선택·계획·문서화는 우리의 몫입니다"**

---

<!--
_class: lead
-->

# Part 4

## 웹 정보 수집 + 콘텐츠 생성

---

## 이번 시간에 배울 내용 (Part 4)

### Part 4: 웹 크롤링 (60분)

- 웹 크롤링 기초 개념
- axios + cheerio 사용법
- 뉴스 헤드라인 수집기 만들기
- AI 콘텐츠 생성 체험

**목표**: 웹 정보 수집기 프로토타입 완성!

---

## 웹 크롤링이란?

### 정의

웹 페이지에서 원하는 정보를 자동으로 추출하는 기술

### 용도

| 용도 | 예시 |
|------|------|
| 가격 비교 | 여러 쇼핑몰 가격 수집 |
| 뉴스 모니터링 | 특정 키워드 뉴스 수집 |
| 연구 데이터 | 통계 데이터 수집 |
| 경쟁사 분석 | 제품/서비스 정보 수집 |

---

## 웹 크롤링 도구

### Node.js 크롤링 라이브러리

| 라이브러리 | 역할 |
|------------|------|
| `axios` | HTTP 요청 (페이지 가져오기) |
| `cheerio` | HTML 파싱 (jQuery 스타일) |

### 설치

```bash
npm install axios cheerio
```

---

## HTML 기초 이해

### 웹 페이지의 구조

```html
<html>
  <head>
    <title>페이지 제목</title>
  </head>
  <body>
    <h1 class="title">큰 제목</h1>
    <p id="content">내용</p>
    <a href="https://example.com">링크</a>
  </body>
</html>
```

### 선택자

| 선택자 | 설명 | 예시 |
|--------|------|------|
| 태그 | 요소 이름 | `h1`, `p`, `a` |
| 클래스 | `.클래스명` | `.title` |
| 아이디 | `#아이디` | `#content` |

---

## 윤리적 크롤링 원칙

### 반드시 지켜야 할 것

| 원칙 | 설명 |
|------|------|
| **robots.txt 확인** | 사이트의 크롤링 허용 범위 확인 |
| **요청 간격** | 1-2초 간격으로 요청 (서버 부하 방지) |
| **개인정보 주의** | 개인정보는 수집하지 않기 |
| **이용약관 확인** | 사이트 이용약관 준수 |

### robots.txt 예시

```
User-agent: *
Disallow: /private/
Allow: /public/
```

---

## 실습 4-1: 웹 정보 수집기

### 시나리오

Hacker News에서 뉴스 헤드라인 수집하기

### Gemini에게 요청

```
다음 작업을 수행하는 Node.js 스크립트를 만들어줘:

1. https://news.ycombinator.com/ 페이지에서
2. 뉴스 제목과 링크를 추출하고
3. news_headlines.csv 파일로 저장해줘

컬럼: 제목, 링크, 수집일시
파일명: news_crawler.js
```

---

## 실습 4-1: 코드 구조

### axios로 페이지 가져오기

```javascript
const axios = require('axios');
const response = await axios.get('https://example.com');
const html = response.data;
```

### cheerio로 파싱하기

```javascript
const cheerio = require('cheerio');
const $ = cheerio.load(html);

$('.title').each((index, element) => {
  const title = $(element).text();
  console.log(title);
});
```

---

## 실습 4-1: 실행 및 확인

### 스크립트 실행

```bash
node news_crawler.js
```

### 결과 확인

```bash
cat news_headlines.csv
```

### 기대 결과

```csv
제목,링크,수집일시
"첫 번째 뉴스 제목","https://...",2024-01-15T10:30:00
"두 번째 뉴스 제목","https://...",2024-01-15T10:30:00
```

---

## 실습 4-1: 도전 과제

### 여러 페이지 크롤링

```
news_crawler.js를 수정해서 1페이지부터 3페이지까지
모든 뉴스를 수집해줘.
페이지 간 1초 간격을 두고 요청해줘.
```

### 힌트

- 페이지 URL 패턴: `?p=1`, `?p=2`, `?p=3`
- 요청 간격: `await new Promise(r => setTimeout(r, 1000))`

---

## 실습 4-2: 콘텐츠 생성

### 시나리오

동아리 행사를 홍보하는 콘텐츠 제작

### 워크플로우

1. **Gemini**: 홍보 문구/해시태그 생성
2. **Nano Banana**: AI 이미지 생성
3. **Canva**: 카드뉴스 완성

---

## 실습 4-2: Step 1 - 텍스트 생성

### Gemini에게 요청

```
우리 동아리 '코딩클럽'의 신입 환영회를 홍보하는 콘텐츠를 만들어줘.

행사 정보:
- 일시: 2025년 3월 15일 오후 2시
- 장소: 학생회관 302호
- 내용: 동아리 소개, 간단한 코딩 체험

만들어줄 것:
1. 포스터 제목 (10자 이내)
2. 설명 문구 (3줄)
3. 해시태그 5개
```

---

## 실습 4-2: Step 2 - 이미지 생성

### Nano Banana 사용

1. https://nano-banana.ai/ 접속
2. 프롬프트 입력:

```
A colorful poster for a coding club welcome party,
modern flat design, friendly atmosphere,
includes laptop and coffee icons
```

3. 이미지 다운로드

---

## 실습 4-2: Step 3 - Canva로 완성

### Canva 작업

1. https://canva.com/ 접속
2. 인스타그램 포스트 템플릿 선택
3. 생성된 이미지 업로드
4. 텍스트 추가
5. 다운로드

### 완성!

- 텍스트: Gemini
- 이미지: Nano Banana
- 편집: Canva
- **기획**: 나!

---

## 산출물 체크 (Part 4)

### 프로토타입 3: 웹 정보 수집기

- [ ] 스크립트 실행 성공
- [ ] CSV 파일 생성됨
- [ ] (도전) 여러 페이지 수집

### 콘텐츠 생성 체험

- [ ] Gemini로 홍보 문구 생성
- [ ] Nano Banana로 이미지 생성
- [ ] Canva로 최종 완성

---

## 정리: 크롤링 + AI 생성의 가능성

### 활용 아이디어

| 수집 | 생성 | 결과 |
|------|------|------|
| 뉴스 헤드라인 | 요약 생성 | 뉴스레터 |
| 제품 리뷰 | 분석 리포트 | 시장 조사 |
| 채용 공고 | 비교표 생성 | 취업 준비 |
| 가격 정보 | 추천 생성 | 쇼핑 가이드 |

### 주의사항

- 저작권 확인 필수
- 개인정보 수집 금지
- 사이트 이용약관 준수

---

<!--
_class: lead
-->

# Part 5

## 나만의 프로토타입 만들기

---

## 이번 시간에 배울 내용 (Part 5)

### Part 5: 프로토타입 (70분)

- Express로 웹 서버 만들기
- 3개 템플릿 중 선택해서 구현
- 발표 및 공유

**목표**: 웹앱 프로토타입 완성!

---

## Express란?

### 정의

Node.js로 웹 서버를 쉽게 만드는 프레임워크

### 설치

```bash
npm install express
```

### 실행

```bash
node app.js
```

브라우저에서 `http://localhost:3000` 접속

---

## Express 기본 구조

### 최소한의 웹 서버

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('<h1>Hello World!</h1>');
});

app.listen(3000, () => {
  console.log('서버 실행: http://localhost:3000');
});
```

### 핵심 개념

| 개념 | 설명 |
|------|------|
| `app.get('/', ...)` | GET 요청 처리 |
| `req` | 요청 객체 |
| `res` | 응답 객체 |
| `res.send()` | 응답 보내기 |

---

## Express: 폼 처리

### HTML 폼

```html
<form action="/submit" method="POST">
  <input type="text" name="topic" placeholder="주제">
  <button type="submit">제출</button>
</form>
```

### Express에서 처리

```javascript
app.use(express.urlencoded({ extended: true }));

app.post('/submit', (req, res) => {
  const topic = req.body.topic;
  res.send(`주제: ${topic}`);
});
```

---

## 실습 5-1: 기본 웹앱 만들기

### Gemini에게 요청

```
Express로 간단한 웹앱을 만들어줘.

기능:
1. 메인 페이지에 제목과 입력창이 있어야 해
2. 사용자가 텍스트를 입력하면
3. 입력한 내용을 화면에 표시해줘

파일명: simple_app.js
```

### 실행

```bash
node simple_app.js
```

---

## 해커톤: 3개 템플릿 중 선택

### 선택지

| # | 프로토타입 | 난이도 | 설명 |
|---|-----------|--------|------|
| 1 | 보고서 자동 생성기 | ⭐⭐ | 주제 입력 → 개요/본문 생성 |
| 2 | 수업 노트 요약기 | ⭐⭐ | 텍스트 입력 → 요약 + 퀴즈 |
| 3 | 취업 공고 비교 도구 | ⭐⭐⭐ | 정보 입력 → 비교표 생성 |

### 시간 배분

- 선택 및 계획: 5분
- 기본 기능 구현: 25분
- 개선 및 디자인: 10분

---

## 템플릿 1: 보고서 자동 생성기

### Gemini에게 요청

```
Express로 보고서 자동 생성기를 만들어줘.

기능:
1. 주제 입력 (text input)
2. 보고서 유형 선택 (select: 일일보고, 주간보고, 프로젝트보고)
3. "생성" 버튼 클릭 시 개요/본문 표시

파일명: report_generator.js
```

### 확장 아이디어

- 마크다운 형식 출력
- 파일 다운로드 기능

---

## 템플릿 2: 수업 노트 요약기

### Gemini에게 요청

```
Express로 수업 노트 요약기를 만들어줘.

기능:
1. 수업 노트 입력 (textarea)
2. "요약" 버튼 클릭 시:
   - 3줄 요약
   - 핵심 키워드 5개
   - 퀴즈 3문제 생성

파일명: note_summarizer.js
```

### 확장 아이디어

- PDF 출력
- 플래시카드 생성

---

## 템플릿 3: 취업 공고 비교 도구

### Gemini에게 요청

```
Express로 취업 공고 비교 도구를 만들어줘.

기능:
1. 취업 공고 정보 입력 (회사명, 직무, 연봉, 위치, 복리후생)
2. 최대 3개 공고 입력 가능
3. "비교" 버튼 클릭 시 비교표 생성

파일명: job_comparer.js
```

### 확장 아이디어

- 점수 계산 기능
- 추천 기능

---

## 해커톤 진행

### 시간 배분

| 단계 | 시간 | 활동 |
|------|------|------|
| 계획 | 5분 | 템플릿 선택, 기능 정리 |
| 구현 | 25분 | Gemini와 함께 코딩 |
| 개선 | 10분 | 디자인, 추가 기능 |

### 팁

- **계획이 70%**: 먼저 기능을 명확히 정리
- **단계별 요청**: 한 번에 하나씩 구현
- **자주 테스트**: 작은 단위로 확인

---

## 발표 및 공유

### 발표 형식 (3분)

| 순서 | 내용 | 시간 |
|------|------|------|
| 1 | 무엇을 만들었나요? | 30초 |
| 2 | 어떻게 만들었나요? | 1분 |
| 3 | 시연 | 1분 |
| 4 | 배운 점 | 30초 |

### 평가 기준

| 항목 | 배점 | 설명 |
|------|------|------|
| **실용성** | 40점 | 실제로 쓸 수 있는가? |
| **프롬프트** | 30점 | 계획이 잘 되었는가? |
| **창의성** | 30점 | 독창적인 아이디어? |

---

## 산출물 체크 (Part 5)

### 프로토타입 4

선택한 템플릿:
- [ ] 보고서 자동 생성기
- [ ] 수업 노트 요약기
- [ ] 취업 공고 비교 도구

### 완성도

- [ ] 기본 기능 동작
- [ ] 웹 브라우저에서 확인
- [ ] 발표 준비 완료

---

<!--
_class: lead
-->

# Part 6

## AI 윤리 + 마무리

---

## 이번 시간에 배울 내용 (Part 6)

### Part 6: 마무리 (50분)

- AI 코드 검토 및 디버깅
- AI 활용 시 주의사항
- 오늘 배운 내용 정리
- 다음 단계 안내

**핵심 메시지**: "AI를 믿되, 검증하라"

---

## AI는 완벽하지 않다

### 흔한 문제들

| 유형 | 설명 |
|------|------|
| **논리적 오류** | 문법은 맞지만 논리가 틀림 |
| **오래된 방식** | 비효율적이거나 폐기된 코드 |
| **할루시네이션** | 존재하지 않는 함수/라이브러리 사용 |

### 핵심 원칙

> **"AI를 믿되, 검증하라"**

---

## AI가 생성한 코드 검토

### 3단계 검토 프로세스

| 단계 | 확인 사항 | 방법 |
|------|-----------|------|
| **1. 실행** | 코드가 동작하는가? | `node 파일.js` |
| **2. 결과** | 예상한 결과가 나오는가? | 직접 테스트 |
| **3. 이해** | 코드가 무슨 일을 하는지 이해되는가? | AI에게 설명 요청 |

### 코드 설명 요청

```
이 코드가 어떻게 작동하는지 한 줄씩 설명해줘:

[코드 붙여넣기]
```

---

## 흔한 에러와 해결법

### 자주 발생하는 에러

| 에러 메시지 | 원인 | 해결책 |
|-------------|------|--------|
| `Cannot find module` | 패키지 미설치 | `npm install 패키지명` |
| `SyntaxError` | 문법 오류 | AI에게 수정 요청 |
| `ENOENT: no such file` | 파일/폴더 없음 | 경로 확인 |
| `TypeError` | 타입 오류 | AI에게 질문 |
| `EADDRINUSE` | 포트 사용 중 | 다른 포트 사용 |

---

## 에러 해결 전략

### AI에게 에러 해결 요청

```
이 에러가 발생했어:

[에러 메시지 전체 복사]

어떻게 해결하면 될까?
```

### 디버깅 팁

```javascript
// 중간 값 확인하기
console.log('변수값:', variable);

// 코드 흐름 확인하기
console.log('여기까지 실행됨');
```

> **에러는 무서운 게 아니라, 문제를 알려주는 힌트!**

---

## AI 활용 시 주의사항

### 4가지 핵심 원칙

| 원칙 | 설명 |
|------|------|
| **개인정보 보호** | 민감한 정보를 입력하지 않기 |
| **저작권 인식** | AI 생성물의 권리 이해 |
| **할루시네이션 주의** | AI의 거짓말 검증 |
| **보안 관리** | API 키, 비밀번호 노출 금지 |

---

## 개인정보 보호

### 프롬프트에 넣으면 안 되는 정보

| 유형 | 예시 |
|------|------|
| **개인 식별 정보** | 주민번호, 전화번호, 주소 |
| **금융 정보** | 계좌번호, 카드번호 |
| **인증 정보** | 비밀번호, API 키 |
| **업무 기밀** | 내부 문서, 고객 데이터 |

### 안전한 사용법

```
# 나쁜 예
"김철수(010-1234-5678) 고객의 계약서를 분석해줘"

# 좋은 예
"고객 계약서 템플릿을 분석해줘 (개인정보 제거된 버전)"
```

---

## 저작권 이해하기

### AI 생성물의 권리

| 항목 | 현재 상황 |
|------|----------|
| **코드** | 대부분 자유롭게 사용 가능 |
| **이미지** | 서비스별 이용약관 확인 필요 |
| **텍스트** | 상업적 사용 시 주의 |

### 주의사항

- 각 AI 서비스의 이용약관 확인
- 상업적 사용 시 별도 확인
- 출처 명시 권장

---

## 할루시네이션 (AI의 거짓말)

### 정의

AI가 그럴듯하지만 **틀린 정보**를 자신있게 말하는 현상

### 자주 발생하는 사례

| 유형 | 예시 |
|------|------|
| **없는 함수** | `axios.fetchData()` (존재하지 않음) |
| **잘못된 문법** | 오래된 버전의 문법 사용 |
| **거짓 정보** | 잘못된 통계, 날짜, 인용 |

### 대처법

- 코드는 반드시 실행해서 확인
- 중요한 정보는 공식 문서에서 검증

---

## 보안 관리

### API 키 관리

```javascript
// 나쁜 예 (코드에 직접 입력)
const API_KEY = "sk-abc123...";

// 좋은 예 (환경 변수 사용)
const API_KEY = process.env.API_KEY;
```

### .gitignore 활용

```
# .gitignore 파일
.env
config.json
*_secret*
```

### 중요 원칙

- API 키는 절대 코드에 직접 작성 금지
- GitHub에 비밀 정보 올리지 않기

---

## 오늘 배운 내용 정리

### Part별 핵심

| Part | 주제 | 핵심 기술 |
|------|------|----------|
| 1 | AI Agent 소개 | Gemini CLI |
| 2 | JavaScript 기초 | console.log, 변수, 조건문 |
| 3 | 파일 자동화 | fs, csv-parser |
| 3 | 우리의 역할 | 선택, 계획, 문서화 |
| 4 | 웹 크롤링 | axios, cheerio |
| 5 | 프로토타입 | Express |
| 6 | AI 윤리 | 검증, 보안, 윤리 |

---

## 산출물 체크리스트

| # | 프로토타입 | 난이도 | 완료 |
|---|-----------|--------|------|
| 1 | 폴더 정리 스크립트 | ⭐ | ☐ |
| 2 | CSV 통합 분석기 | ⭐⭐ | ☐ |
| 3 | 웹 정보 수집기 | ⭐⭐ | ☐ |
| 4 | 보고서 생성기 / 노트 요약기 | ⭐⭐ | ☐ |
| 5 | 개인 선택 프로토타입 | ⭐⭐⭐ | ☐ |

> 3개 이상 완료했다면 성공!

---

## AI 시대의 3가지 키워드 (복습)

### 선택, 계획, 문서화

| 키워드 | 의미 | 실천법 |
|--------|------|--------|
| **선택** | AI 결과물에 나의 판단 반영 | "이것 vs 저것" 비교 요청 |
| **계획** | 구체적 지시로 원하는 결과 | 단계별 요청, 예시 제시 |
| **문서화** | 작업 과정을 기록으로 남기기 | 회고 문서 작성 요청 |

> **AI가 모든 걸 해도, 우리의 역할은 더 중요해집니다**

---

## 실무 적용 아이디어

### 당장 해볼 수 있는 것

| 업무 | AI 자동화 아이디어 |
|------|-------------------|
| 반복 파일 작업 | 폴더 정리 스크립트 커스텀 |
| 데이터 정리 | CSV 통합/분석 자동화 |
| 정보 수집 | 관심 분야 뉴스 크롤링 |
| 보고서 작성 | 초안 자동 생성 |

---

## 다음 단계

### 실천 계획

1. **이번 주**: 오늘 만든 스크립트 실제 업무에 적용
2. **다음 주**: 새로운 자동화 아이디어 1개 구현
3. **한 달 후**: 팀에 공유할 수 있는 도구 완성

### 심화 학습 경로

| 단계 | 주제 | 자료 |
|------|------|------|
| 1 | JavaScript 심화 | MDN Web Docs |
| 2 | Node.js | nodejs.org 공식 문서 |
| 3 | Express | expressjs.com |
| 4 | AI Agent | MCP (Model Context Protocol) |

---

## Q&A

### 자주 묻는 질문

**Q: AI가 코드를 다 만들어주면, 개발자는 필요 없나요?**

A: 아니요. AI는 도구입니다. 무엇을 만들지 결정하고, 결과를 검증하고, 문제를 해결하는 것은 사람의 역할입니다.

**Q: 어느 AI를 사용해야 하나요?**

A: 각 AI마다 장단점이 있습니다. 여러 개를 사용해보고 상황에 맞게 선택하세요.

**Q: 더 배우려면 어떻게 해야 하나요?**

A: 오늘 만든 것을 실제로 사용해보세요. 필요에 의해 배울 때 가장 빨리 배웁니다.

---

## 핵심 메시지

### 오늘의 성과

- Gemini CLI로 AI Agent 체험
- JavaScript 기초 코드 작성 및 실행
- 5개 이상의 자동화 프로토타입 제작
- AI 윤리 및 보안 인식

### 기억해야 할 것

> **"코드를 외우지 않아도, AI와 함께 문제를 해결할 수 있다"**

---

<!--
_class: lead
-->

# 감사합니다

## Q&A

질문이 있으시면 언제든 물어보세요!

> **"AI와 함께 성장하는 여러분을 응원합니다!"**
