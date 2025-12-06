# Part 5: 나만의 프로토타입 만들기

## Express란?

### 정의

Node.js로 웹 서버를 쉽게 만드는 프레임워크

### 특징

- 가장 인기 있는 Node.js 웹 프레임워크
- 간단한 코드로 서버 구축
- HTML, API 모두 가능
- 수많은 예제와 자료

> **"Node.js로 웹앱을 만드는 가장 쉬운 방법"**

---

## Express 설치 및 실행

### 설치

```bash
npm install express
```

### 기본 서버 코드

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('서버 실행: http://localhost:3000');
});
```

### 실행

```bash
node app.js
```

### 결과

- 브라우저에서 `http://localhost:3000` 접속
- "Hello World!" 표시

---

## 첫 번째 Express 앱

### Gemini에게 요청

```
Express로 간단한 웹 서버를 만들어줘.
- 메인 페이지에 "나의 첫 웹앱" 제목 표시
- 이름을 입력받는 폼
- 제출하면 "안녕하세요, [이름]님!" 표시

파일명: app.js
```

---

## 생성된 코드 예시

```javascript
const express = require('express');
const app = express();

// 폼 데이터 파싱
app.use(express.urlencoded({ extended: true }));

// 메인 페이지
app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>나의 첫 웹앱</title>
      <meta charset="UTF-8">
    </head>
    <body>
      <h1>나의 첫 웹앱</h1>
      <form action="/greet" method="POST">
        <input type="text" name="name" placeholder="이름을 입력하세요">
        <button type="submit">인사하기</button>
      </form>
    </body>
    </html>
  `);
});

// 인사 페이지
app.post('/greet', (req, res) => {
  const name = req.body.name;
  res.send(`<h1>안녕하세요, ${name}님!</h1><a href="/">돌아가기</a>`);
});

app.listen(3000, () => {
  console.log('서버 실행: http://localhost:3000');
});
```

---

## Express 핵심 개념

### 라우팅 (Routing)

| 메서드 | 용도 | 예시 |
|--------|------|------|
| `app.get()` | 페이지 보여주기 | `app.get('/', ...)` |
| `app.post()` | 데이터 받기 | `app.post('/submit', ...)` |

### 요청과 응답

```javascript
app.get('/hello', (req, res) => {
  // req = 요청 (클라이언트 → 서버)
  // res = 응답 (서버 → 클라이언트)
  res.send('Hello!');
});
```

---

## HTML 기초: 폼 (Form)

### 입력 폼 구조

```html
<form action="/submit" method="POST">
  <input type="text" name="username">
  <button type="submit">제출</button>
</form>
```

### 주요 속성

| 속성 | 설명 | 예시 |
|------|------|------|
| `action` | 데이터 보낼 주소 | `/submit` |
| `method` | 전송 방식 | `GET`, `POST` |
| `name` | 입력 필드 이름 | `username` |

### 서버에서 데이터 받기

```javascript
app.post('/submit', (req, res) => {
  const username = req.body.username;  // 폼의 name 속성
  res.send(`받은 데이터: ${username}`);
});
```

---

## HTML 입력 요소

### 자주 사용하는 입력

| 태그 | 용도 | 예시 |
|------|------|------|
| `<input type="text">` | 한 줄 텍스트 | 이름, 제목 |
| `<textarea>` | 여러 줄 텍스트 | 내용, 설명 |
| `<input type="number">` | 숫자 | 나이, 수량 |
| `<select>` | 드롭다운 선택 | 카테고리 |

### 예시

```html
<input type="text" name="title" placeholder="제목">
<textarea name="content" rows="5"></textarea>
<input type="number" name="age" min="0" max="120">
<select name="category">
  <option value="1">옵션1</option>
  <option value="2">옵션2</option>
</select>
```

---

## 실습 5-1: 기본 웹앱 만들기

### Gemini에게 요청

```
Express로 간단한 계산기 웹앱을 만들어줘.

기능:
1. 두 숫자 입력 (number input)
2. 연산 선택 (select: +, -, *, /)
3. "계산" 버튼
4. 결과 표시

파일명: calculator_app.js
```

---

## 생성된 코드 예시

```javascript
const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>간단한 계산기</title>
      <meta charset="UTF-8">
      <style>
        body { font-family: sans-serif; padding: 20px; }
        input, select, button { padding: 10px; margin: 5px; }
      </style>
    </head>
    <body>
      <h1>간단한 계산기</h1>
      <form action="/calculate" method="POST">
        <input type="number" name="num1" placeholder="첫 번째 숫자" required>
        <select name="operation">
          <option value="+">+</option>
          <option value="-">-</option>
          <option value="*">×</option>
          <option value="/">÷</option>
        </select>
        <input type="number" name="num2" placeholder="두 번째 숫자" required>
        <button type="submit">계산</button>
      </form>
    </body>
    </html>
  `);
});

app.post('/calculate', (req, res) => {
  const num1 = parseFloat(req.body.num1);
  const num2 = parseFloat(req.body.num2);
  const op = req.body.operation;
  let result;

  switch(op) {
    case '+': result = num1 + num2; break;
    case '-': result = num1 - num2; break;
    case '*': result = num1 * num2; break;
    case '/': result = num2 !== 0 ? num1 / num2 : '0으로 나눌 수 없음'; break;
  }

  res.send(`
    <h1>계산 결과</h1>
    <p>${num1} ${op} ${num2} = ${result}</p>
    <a href="/">다시 계산하기</a>
  `);
});

app.listen(3000, () => console.log('http://localhost:3000'));
```

---

## 해커톤: 프로토타입 제작

### 3개 템플릿 중 선택

| # | 프로토타입 | 난이도 | 주요 기능 |
|---|-----------|--------|----------|
| 1 | 보고서 자동 생성기 | ⭐⭐ | 주제 → 개요/본문 생성 |
| 2 | 수업 노트 요약기 | ⭐⭐ | 텍스트 → 요약 + 퀴즈 |
| 3 | 취업 공고 비교 도구 | ⭐⭐⭐ | 정보 입력 → 비교표 |

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
2. 보고서 유형 선택 (select: 기획안, 제안서, 분석 보고서)
3. 분량 선택 (select: 500자, 1000자, 2000자)
4. "생성" 버튼 클릭 시:
   - 개요 (bullet points)
   - 본문 초안
   - 참고 키워드

파일명: report_generator.js

참고: 실제 AI 생성 대신 템플릿 텍스트를 사용해도 됨
```

---

## 템플릿 1: 코드 예시

```javascript
const express = require('express');
const app = express();
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html>
    <head><title>보고서 자동 생성기</title><meta charset="UTF-8"></head>
    <body>
      <h1>보고서 자동 생성기</h1>
      <form action="/generate" method="POST">
        <p>주제: <input type="text" name="topic" required></p>
        <p>유형: <select name="type">
          <option>기획안</option>
          <option>제안서</option>
          <option>분석 보고서</option>
        </select></p>
        <p>분량: <select name="length">
          <option value="500">500자</option>
          <option value="1000">1000자</option>
          <option value="2000">2000자</option>
        </select></p>
        <button type="submit">생성</button>
      </form>
    </body>
    </html>
  `);
});

app.post('/generate', (req, res) => {
  const { topic, type, length } = req.body;
  res.send(`
    <h1>📋 ${topic} - ${type}</h1>
    <h2>개요</h2>
    <ul>
      <li>주제: ${topic}</li>
      <li>유형: ${type}</li>
      <li>예상 분량: ${length}자</li>
    </ul>
    <h2>📝 본문 초안</h2>
    <h3>1. 서론</h3>
    <p>${topic}에 대한 ${type}입니다...</p>
    <h3>2. 본론</h3>
    <p>주요 내용을 여기에 작성합니다...</p>
    <h3>3. 결론</h3>
    <p>요약 및 제안사항...</p>
    <h2>🔑 참고 키워드</h2>
    <p>#${topic.replace(/ /g, '')} #AI자동화 #업무효율</p>
    <a href="/">다시 작성하기</a>
  `);
});

app.listen(3000, () => console.log('http://localhost:3000'));
```

---

## 템플릿 2: 수업 노트 요약기

### Gemini에게 요청

```
Express로 수업 노트 요약기를 만들어줘.

기능:
1. 수업 노트 입력 (textarea)
2. 요약 길이 선택 (radio: 짧게/보통/길게)
3. "요약하기" 버튼 클릭 시:
   - 핵심 내용 요약 (3-5줄)
   - 키워드 추출 (5개)
   - 퀴즈 생성 (객관식 2문제)

파일명: note_summarizer.js
```

---

## 템플릿 2: 코드 예시

```javascript
const express = require('express');
const app = express();
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html>
    <head><title>수업 노트 요약기</title><meta charset="UTF-8"></head>
    <body>
      <h1>수업 노트 요약기</h1>
      <form action="/summarize" method="POST">
        <p>수업 노트:</p>
        <textarea name="notes" rows="10" cols="50" required></textarea>
        <p>요약 길이:
          <label><input type="radio" name="length" value="short"> 짧게</label>
          <label><input type="radio" name="length" value="medium" checked> 보통</label>
          <label><input type="radio" name="length" value="long"> 길게</label>
        </p>
        <button type="submit">요약하기</button>
      </form>
    </body>
    </html>
  `);
});

app.post('/summarize', (req, res) => {
  const { notes, length } = req.body;
  const wordCount = notes.length;

  res.send(`
    <h1>📌 핵심 내용 요약</h1>
    <p>입력된 노트: ${wordCount}자</p>
    <ol>
      <li>첫 번째 핵심 포인트</li>
      <li>두 번째 핵심 포인트</li>
      <li>세 번째 핵심 포인트</li>
    </ol>
    <h2>🔑 키워드</h2>
    <p>키워드1, 키워드2, 키워드3, 키워드4, 키워드5</p>
    <h2>❓ 퀴즈</h2>
    <p><strong>Q1. 이 수업의 핵심 주제는?</strong></p>
    <p>① 옵션1 ② 옵션2 ③ 옵션3 ④ 옵션4</p>
    <p><strong>Q2. 다음 중 올바른 설명은?</strong></p>
    <p>① 옵션1 ② 옵션2 ③ 옵션3 ④ 옵션4</p>
    <a href="/">다시 요약하기</a>
  `);
});

app.listen(3000, () => console.log('http://localhost:3000'));
```

---

## 템플릿 3: 취업 공고 비교 도구

### Gemini에게 요청

```
Express로 취업 공고 비교 도구를 만들어줘.

기능:
1. 공고 정보 입력 (2개)
   - 각각: 회사명, 포지션, 연봉, 복지
2. "비교하기" 버튼 클릭 시:
   - 두 공고를 표로 비교
   - 장단점 분석

파일명: job_compare.js
```

---

## 템플릿 3: 코드 예시

```javascript
const express = require('express');
const app = express();
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html>
    <head><title>취업 공고 비교</title><meta charset="UTF-8">
    <style>
      .column { display: inline-block; width: 45%; vertical-align: top; }
      input, textarea { width: 100%; margin: 5px 0; }
    </style>
    </head>
    <body>
      <h1>취업 공고 비교 도구</h1>
      <form action="/compare" method="POST">
        <div class="column">
          <h3>공고 1</h3>
          <input name="company1" placeholder="회사명">
          <input name="position1" placeholder="포지션">
          <input name="salary1" placeholder="연봉">
          <textarea name="benefits1" placeholder="복지"></textarea>
        </div>
        <div class="column">
          <h3>공고 2</h3>
          <input name="company2" placeholder="회사명">
          <input name="position2" placeholder="포지션">
          <input name="salary2" placeholder="연봉">
          <textarea name="benefits2" placeholder="복지"></textarea>
        </div>
        <p><button type="submit">비교하기</button></p>
      </form>
    </body>
    </html>
  `);
});

app.post('/compare', (req, res) => {
  const { company1, position1, salary1, benefits1,
          company2, position2, salary2, benefits2 } = req.body;

  res.send(`
    <h1>📊 비교 결과</h1>
    <table border="1" cellpadding="10">
      <tr><th>항목</th><th>공고 1</th><th>공고 2</th></tr>
      <tr><td>회사명</td><td>${company1}</td><td>${company2}</td></tr>
      <tr><td>포지션</td><td>${position1}</td><td>${position2}</td></tr>
      <tr><td>연봉</td><td>${salary1}</td><td>${salary2}</td></tr>
      <tr><td>복지</td><td>${benefits1}</td><td>${benefits2}</td></tr>
    </table>
    <h2>💡 분석</h2>
    <p>두 공고의 장단점을 비교 분석합니다...</p>
    <a href="/">다시 비교하기</a>
  `);
});

app.listen(3000, () => console.log('http://localhost:3000'));
```

---

## 프로토타입 개선 아이디어

### 스타일 개선

```html
<style>
  body {
    font-family: sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  button {
    background: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    cursor: pointer;
  }
  button:hover {
    background: #45a049;
  }
</style>
```

### 기능 확장

- 결과를 파일로 저장
- 입력 검증 추가
- 히스토리 저장

---

## 발표 및 공유

### 발표 형식 (3분)

1. **무엇을 만들었나요?** (30초)
   - 프로토타입 이름과 목적

2. **어떻게 만들었나요?** (1분)
   - 사용한 프롬프트
   - 핵심 코드 설명

3. **시연** (1분)
   - 실제 작동 데모

4. **배운 점 / 어려웠던 점** (30초)

---

## 베스트 프로토타입 선정

### 평가 기준

| 항목 | 배점 | 설명 |
|------|------|------|
| **실용성** | 40점 | 실제로 사용할 수 있는가? |
| **프롬프트** | 30점 | 지시가 명확하고 구체적인가? |
| **창의성** | 30점 | 독창적인 아이디어인가? |

### 시상

- 🥇 베스트 프로토타입
- 🥈 베스트 프롬프트
- 🎨 베스트 디자인

---

## 산출물 체크

### 프로토타입 4 & 5

- [ ] Express 앱 실행 성공
- [ ] 템플릿 1개 이상 완성
- [ ] 기본 기능 작동 확인
- [ ] (도전) 스타일 개선

### 발표 준비

- [ ] 3분 발표 준비 완료
- [ ] 시연 가능한 상태

---

## 학습 포인트 정리

### 오늘 배운 것

| 개념 | 설명 |
|------|------|
| Express | Node.js 웹 서버 프레임워크 |
| 라우팅 | URL별 처리 (get, post) |
| HTML Form | 사용자 입력 받기 |
| req.body | 폼 데이터 접근 |
| res.send() | HTML 응답 보내기 |

### 핵심 메시지

> **"아이디어가 있으면 바로 프로토타입으로 만들 수 있다"**

---

## 체크포인트

| 단계 | 확인 사항 | 완료 |
|------|-----------|------|
| 1 | Express 설치 완료 | ☐ |
| 2 | 기본 웹앱 실행 성공 | ☐ |
| 3 | 템플릿 프로토타입 완성 | ☐ |
| 4 | 발표 준비 완료 | ☐ |

> **다음 시간**: AI 윤리 + 마무리
