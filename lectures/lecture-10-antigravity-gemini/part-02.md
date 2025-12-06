# Part 2: JavaScript 기초 with Gemini

## 왜 JavaScript인가?

### Node.js가 이미 설치되어 있습니다!

- Gemini CLI 설치할 때 Node.js를 설치했음
- **추가 설치 없이** 바로 코딩 시작 가능
- Windows에서도 문제없이 동작

### JavaScript의 장점

| 장점 | 설명 |
|------|------|
| **범용성** | 웹, 서버, 앱 모두 가능 |
| **인기** | 세계에서 가장 많이 사용되는 언어 |
| **AI 친화적** | AI가 잘 생성하는 언어 |
| **즉시 실행** | 브라우저에서도 실행 가능 |

> **"코드를 외울 필요 없이, AI에게 시키면 됩니다."**

---

## Node.js 실행 환경 확인

### 설치 확인

```bash
node --version
```

### 결과 예시

```
v20.10.0
```

> 버전이 나오면 OK!

---

## AI 시대의 3가지 키워드

> **"AI가 모든 걸 해도, 우리의 역할은 더 중요해집니다"**

| 키워드 | 핵심 개념 | 왜 중요한가? |
|--------|----------|--------------|
| **1. 선택** | 나의 가치와 선호 반영 | AI 결과물에 "나"를 담아야 내 것이 됨 |
| **2. 계획** | 컨텍스트 채우기 | 계획 없으면 엉뚱한 결과 |
| **3. 문서화** | 문서 = 프로젝트 | 문서화로 성찰하고 성장 |

---

## 1. 선택 (Selection): 의미 담기

- **과거**: 정보 부족으로 제한된 선택
- **AI 시대**: Agent가 정교한 비교 제공 → **더 나은 선택 가능**

### 핵심

- Agent는 정보와 옵션을 제공할 뿐
- **최종 선택은 인간의 몫**
- 나의 가치관이 반영된 선택이 결과물에 **"영혼"**을 불어넣음

> **Tip**: "A안과 B안의 장단점을 비교해줘"라고 요청하고, 최종 결정은 내가 내리세요.

---

## 2. 계획 (Planning): 의도 전달

### 문제

"보고서 써줘" (모호함) → AI가 마음대로 추론 → 엉뚱한 결과

### 해결

**계획에 시간 투자 (Work의 70%)**

### 좋은 계획의 3원칙

| 원칙 | 설명 | 예시 |
|------|------|------|
| **구체성** | 누가, 무엇을, 어떻게 | "마케팅팀 신입을 위한..." |
| **단계성** | 순서대로 지시 | "1단계는 조사, 2단계는 작성..." |
| **결과물 명시** | 최종 형태 지정 | "마지막엔 result.json으로 저장해줘" |

---

## 3. 문서화 (Documentation): 성장 도구

### Before AI

- 시간 부족으로 문서화 포기
- "일하기도 바쁜데..."

### After AI

- **Agent가 문서화 대행 (거의 무료)**
- 문서 = 프로젝트 그 자체
- 시작(계획서) → 진행(로그) → 완료(회고)

> **Action**: 작업을 마칠 때 "오늘 한 내용을 요약해서 회고 문서로 만들어줘"

---

## 실습 2-1: Hello World

### Step 1: Gemini에게 요청

```
Hello World를 출력하는 JavaScript 코드를 만들어서 hello.js로 저장해줘
```

### Step 2: 생성된 코드 확인

```javascript
console.log("Hello World");
```

### Step 3: 실행

```bash
node hello.js
```

### 결과

```
Hello World
```

---

## JavaScript 기초 개념 1: console.log()

### console.log() 함수

화면(터미널)에 텍스트를 출력하는 함수

```javascript
console.log("안녕하세요");
console.log("오늘 날짜는 2025년입니다");
```

### 여러 값 출력

```javascript
console.log("이름:", "홍길동");
console.log("나이:", 25);
```

---

## JavaScript 기초 개념 2: 변수

### 변수란?

데이터를 담는 상자

```javascript
const name = "홍길동";  // 변하지 않는 값
let age = 25;          // 변할 수 있는 값

console.log(name);  // 홍길동
console.log(age);   // 25
```

### const vs let

| 키워드 | 용도 | 예시 |
|--------|------|------|
| `const` | 변하지 않는 값 | `const PI = 3.14` |
| `let` | 변할 수 있는 값 | `let count = 0` |

---

## 실습 2-2: 간단한 계산기

### Step 1: Gemini에게 요청

```
두 숫자를 입력받아서 더하는 Node.js 프로그램을 만들어줘.
사용자가 터미널에서 직접 숫자를 입력할 수 있어야 해.
파일명은 calculator.js로 해줘.
```

### Step 2: 생성된 코드 (예시)

```javascript
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('첫 번째 숫자: ', (num1) => {
  rl.question('두 번째 숫자: ', (num2) => {
    const result = Number(num1) + Number(num2);
    console.log(`결과: ${num1} + ${num2} = ${result}`);
    rl.close();
  });
});
```

---

## JavaScript 기초 개념 3: 입력받기 (readline)

### readline 모듈

Node.js에서 사용자 입력을 받는 내장 모듈

```javascript
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('이름을 입력하세요: ', (answer) => {
  console.log(`안녕하세요, ${answer}님!`);
  rl.close();
});
```

### 주의: 타입 변환

```javascript
// 입력은 항상 문자열(string)
const input = "25";        // 문자열
const num = Number(input); // 숫자로 변환
```

---

## JavaScript 기초 개념 4: 연산자

### 산술 연산자

| 연산자 | 의미 | 예시 |
|--------|------|------|
| `+` | 더하기 | `5 + 3` → `8` |
| `-` | 빼기 | `5 - 3` → `2` |
| `*` | 곱하기 | `5 * 3` → `15` |
| `/` | 나누기 | `5 / 3` → `1.666...` |
| `%` | 나머지 | `5 % 3` → `2` |

---

## 도전 과제: 사칙연산 계산기

### Gemini에게 요청

```
사칙연산을 선택할 수 있는 계산기를 만들어줘.
1. 두 숫자 입력
2. 연산 선택 (+, -, *, /)
3. 결과 출력
파일명: advanced_calculator.js
```

### 힌트: 조건문

```javascript
if (operation === "+") {
  result = num1 + num2;
} else if (operation === "-") {
  result = num1 - num2;
}
// ...
```

---

## JavaScript 기초 개념 5: 조건문

### if-else if-else 구조

```javascript
const score = 85;

if (score >= 90) {
  console.log("A학점");
} else if (score >= 80) {
  console.log("B학점");
} else if (score >= 70) {
  console.log("C학점");
} else {
  console.log("F학점");
}
```

### 비교 연산자

| 연산자 | 의미 |
|--------|------|
| `===` | 같다 (타입까지 비교) |
| `!==` | 다르다 |
| `>`, `<` | 크다, 작다 |
| `>=`, `<=` | 크거나 같다, 작거나 같다 |

---

## 템플릿 문자열 (백틱)

### 기존 방식

```javascript
const name = "홍길동";
console.log("안녕하세요, " + name + "님!");
```

### 템플릿 문자열 (권장)

```javascript
const name = "홍길동";
console.log(`안녕하세요, ${name}님!`);
```

> 백틱(`) 안에서 `${변수}`로 값 삽입 가능!

---

## 코드 읽는 법: AI가 만든 코드 이해하기

### 핵심 포인트

1. **주석(//)**: 코드 설명 - 먼저 읽기
2. **함수 이름**: 역할 추측 가능 (`console.log`, `readline`)
3. **변수 이름**: 데이터의 의미 파악
4. **들여쓰기**: 코드 블록 구분

### 모르는 코드가 있다면?

```
이 코드에서 Number()가 뭐하는 거야?
```

> AI에게 물어보세요!

---

## Python vs JavaScript 비교

### 같은 기능, 다른 문법

| 기능 | Python | JavaScript |
|------|--------|------------|
| 출력 | `print("Hello")` | `console.log("Hello")` |
| 변수 | `name = "홍길동"` | `const name = "홍길동"` |
| 조건문 | `if score >= 90:` | `if (score >= 90) {` |
| 타입변환 | `int("25")` | `Number("25")` |

> 문법만 다를 뿐, 개념은 같습니다!

---

## 학습 포인트 정리

### 오늘 배운 것

| 개념 | 설명 |
|------|------|
| `console.log()` | 출력 함수 |
| `const`, `let` | 변수 선언 |
| `readline` | 입력 받기 |
| 연산자 | 계산 수행 |
| 조건문 | 분기 처리 |
| 템플릿 문자열 | 문자열 조합 |

### 핵심 메시지

> **"코드를 직접 작성하지 않아도, AI가 만든 코드를 읽고 수정할 수 있다"**

---

## 체크포인트

| 단계 | 확인 사항 | 완료 |
|------|-----------|------|
| 1 | Node.js 버전 확인 완료 | ☐ |
| 2 | hello.js 실행 성공 | ☐ |
| 3 | calculator.js 실행 성공 | ☐ |
| 4 | 도전 과제 (사칙연산) 완료 | ☐ |

> **다음 시간**: 파일 자동화 실습 (CSV, 폴더 정리)
