# Part 4: 웹 정보 수집 + 콘텐츠 생성

## 웹 크롤링이란?

### 정의

웹 페이지에서 원하는 정보를 자동으로 추출하는 기술

### 활용 사례

- 뉴스 헤드라인 모으기
- 상품 가격 비교
- 취업 공고 수집
- 부동산 매물 정보

> **"수동으로 복사-붙여넣기 하던 일을 자동화"**

---

## 웹 페이지의 구조: HTML 기초

### HTML이란?

웹 페이지를 만드는 마크업 언어

### 기본 구조

```html
<html>
  <head>
    <title>페이지 제목</title>
  </head>
  <body>
    <h1>큰 제목</h1>
    <p>문단 내용</p>
    <a href="https://...">링크</a>
  </body>
</html>
```

### 핵심 태그

| 태그 | 의미 |
|------|------|
| `<h1>~<h6>` | 제목 |
| `<p>` | 문단 |
| `<a>` | 링크 |
| `<div>` | 구역 |
| `<span>` | 인라인 구역 |

---

## Node.js 크롤링 라이브러리

### axios

웹 페이지 가져오기 (HTTP 요청)

```bash
npm install axios
```

### cheerio

HTML 파싱 (jQuery 스타일)

```bash
npm install cheerio
```

### 설치

```bash
npm install axios cheerio
```

---

## 기본 크롤링 패턴

```javascript
const axios = require('axios');
const cheerio = require('cheerio');

async function crawl() {
  // 1. 페이지 가져오기
  const response = await axios.get('https://example.com');

  // 2. HTML 파싱
  const $ = cheerio.load(response.data);

  // 3. 원하는 요소 찾기
  const titles = $('h1').text();
  console.log(titles);
}

crawl();
```

---

## 윤리적 크롤링 원칙

### 반드시 지켜야 할 것

| 원칙 | 설명 |
|------|------|
| **robots.txt 확인** | 크롤링 허용 여부 확인 |
| **적절한 간격** | 요청 사이 1-2초 대기 |
| **서버 부하 고려** | 과도한 요청 금지 |
| **저작권 존중** | 수집한 데이터 사용 범위 |

### robots.txt 확인 방법

```
https://example.com/robots.txt
```

---

## 실습 4-1: 웹 정보 수집기

### 시나리오

뉴스 사이트에서 오늘의 헤드라인을 수집

### 목표

1. 뉴스 제목 추출
2. 링크 추출
3. CSV 파일로 저장

---

## 실습 4-1: Gemini에게 요청

```
다음 작업을 수행하는 Node.js 스크립트를 만들어줘:

1. https://news.ycombinator.com/ 페이지에서
2. 뉴스 제목과 링크를 추출하고
3. news_headlines.csv 파일로 저장해줘

컬럼: 제목, 링크, 수집일시

axios와 cheerio, csv-writer 패키지를 사용해줘.
파일명: news_crawler.js
```

---

## 생성된 코드 예시

```javascript
const axios = require('axios');
const cheerio = require('cheerio');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

async function crawlNews() {
  // 페이지 가져오기
  const url = 'https://news.ycombinator.com/';
  const response = await axios.get(url);
  const $ = cheerio.load(response.data);

  // 뉴스 제목과 링크 추출
  const newsData = [];
  $('.titleline > a').each((index, element) => {
    const title = $(element).text();
    const link = $(element).attr('href');
    newsData.push({
      제목: title,
      링크: link,
      수집일시: new Date().toISOString().slice(0, 16).replace('T', ' ')
    });
  });

  // CSV 저장
  const csvWriter = createCsvWriter({
    path: 'news_headlines.csv',
    header: [
      {id: '제목', title: '제목'},
      {id: '링크', title: '링크'},
      {id: '수집일시', title: '수집일시'}
    ]
  });

  await csvWriter.writeRecords(newsData);
  console.log(`완료! ${newsData.length}개의 뉴스를 수집했습니다.`);
}

crawlNews();
```

---

## cheerio 핵심 메서드

### 요소 찾기 (jQuery 스타일)

| 메서드 | 설명 | 예시 |
|--------|------|------|
| `$('태그')` | 태그 선택 | `$('h1')` |
| `$('.클래스')` | 클래스 선택 | `$('.title')` |
| `$('#아이디')` | 아이디 선택 | `$('#main')` |
| `.find()` | 하위 요소 찾기 | `$('div').find('a')` |
| `.each()` | 반복 처리 | 아래 예시 |

### 반복 처리 예시

```javascript
$('a').each((index, element) => {
  console.log($(element).text());
});
```

---

## 속성과 텍스트 접근

### 텍스트 가져오기

```javascript
const text = $('h1').text();
console.log(text);  // "제목 텍스트"
```

### 속성 가져오기

```javascript
const href = $('a').attr('href');
console.log(href);  // "https://..."

const className = $('div').attr('class');
```

### HTML 가져오기

```javascript
const html = $('div').html();
```

---

## CSS 선택자 기초

### 자주 쓰는 선택자

| 선택자 | 의미 | 예시 |
|--------|------|------|
| `태그` | 태그명 | `h1`, `p`, `a` |
| `.클래스` | class 속성 | `.news-title` |
| `#아이디` | id 속성 | `#main-content` |
| `태그.클래스` | 조합 | `div.article` |
| `부모 > 자식` | 직계 자식 | `ul > li` |
| `부모 자손` | 모든 자손 | `div a` |

### 개발자 도구 활용

1. 브라우저에서 F12 (개발자 도구)
2. 요소 선택 도구 클릭
3. 원하는 요소 클릭
4. HTML 구조 확인

---

## 도전 과제: 여러 페이지 크롤링

### Gemini에게 요청

```
news_crawler.js를 수정해서
1페이지부터 3페이지까지 크롤링해줘.
각 페이지 요청 사이에 1초 대기 시간을 넣어줘.
```

### 힌트: 대기 함수

```javascript
// 대기 함수
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

// 사용
for (let page = 1; page <= 3; page++) {
  const url = `https://news.ycombinator.com/news?p=${page}`;
  const response = await axios.get(url);
  // ... 처리 ...
  await sleep(1000);  // 1초 대기
}
```

---

## async/await 이해하기

### 비동기 처리란?

웹 요청처럼 시간이 걸리는 작업을 기다리는 방법

### 기본 패턴

```javascript
// async 함수 선언
async function fetchData() {
  // await로 응답 기다리기
  const response = await axios.get('https://...');
  console.log(response.data);
}

// 함수 실행
fetchData();
```

### try-catch로 에러 처리

```javascript
async function fetchData() {
  try {
    const response = await axios.get('https://...');
    console.log(response.data);
  } catch (error) {
    console.error('에러 발생:', error.message);
  }
}
```

---

## 콘텐츠 생성: Nano Banana

### Nano Banana란?

AI 기반 이미지/영상 생성 도구

### 활용 예시

- 썸네일 이미지 생성
- 짧은 영상 클립 제작
- 소셜 미디어 콘텐츠

### 사용법

1. https://nanobanana.com/ 접속
2. 프롬프트 입력
3. 스타일 선택
4. 생성 및 다운로드

---

## 실습 4-2: 홍보 콘텐츠 생성

### 시나리오

동아리/팀 행사를 홍보하는 콘텐츠 제작

### Step 1: Gemini에게 텍스트 생성 요청

```
우리 동아리 '코딩클럽'의 신입 환영회를 홍보하는 콘텐츠를 만들어줘.

일시: 2025년 3월 15일 토요일 오후 2시
장소: 학생회관 세미나실
대상: 코딩에 관심 있는 모든 학생

다음 형식으로 출력해줘:
1. 포스터 문구 (간결하게)
2. SNS 게시글 (친근하게)
3. 해시태그 10개
```

---

## Step 2: Nano Banana로 이미지 생성

### 프롬프트 예시

```
A modern, colorful poster for a coding club welcome party.
Include icons of laptops, code, and happy students.
Vibrant colors, clean design, flat illustration style.
```

### 팁

- 영어 프롬프트가 더 정확함
- 스타일 키워드 추가 (flat, 3D, cartoon 등)
- 색상 톤 지정 (vibrant, pastel, dark 등)

---

## Step 3: Canva로 완성하기

### Canva란?

무료 온라인 디자인 도구

### 워크플로우

```
Gemini (텍스트) + Nano Banana (이미지) → Canva (편집/완성)
```

### Canva에서 할 일

1. 적절한 템플릿 선택
2. Nano Banana 이미지 업로드
3. Gemini가 만든 문구 배치
4. 색상/폰트 조정
5. 다운로드

---

## 실습: 카드뉴스 만들기

### 3장 구성 예시

| 장 | 내용 |
|----|------|
| 1장 | 행사명 + 임팩트 있는 이미지 |
| 2장 | 일시, 장소, 대상 정보 |
| 3장 | 참가 방법 + QR코드/링크 |

### 체크리스트

- [ ] Gemini로 문구 생성
- [ ] Nano Banana로 이미지 생성
- [ ] Canva에서 3장 완성
- [ ] 다운로드 (PNG 또는 PDF)

---

## 크롤링 + AI 생성의 조합

### 가능한 시나리오

| 크롤링 대상 | AI 생성 결과 |
|-------------|--------------|
| 취업 공고 | 맞춤 자기소개서 초안 |
| 뉴스 기사 | 요약 브리핑 |
| 상품 리뷰 | 비교 분석 리포트 |
| 경쟁사 정보 | 마케팅 전략 제안 |

### 예시 워크플로우

```
웹 크롤링 (데이터 수집)
    ↓
Gemini (분석/요약)
    ↓
Nano Banana + Canva (시각화)
```

---

## 저작권 및 윤리적 고려사항

### 주의해야 할 점

| 항목 | 주의사항 |
|------|----------|
| **크롤링 데이터** | 상업적 사용 시 법적 검토 필요 |
| **AI 생성 이미지** | 각 서비스의 이용약관 확인 |
| **뉴스/기사** | 원문 출처 명시 |
| **개인정보** | 수집/저장 금지 |

### 안전한 사용

- 학습/연구 목적으로 제한
- 공개된 정보만 수집
- 원 저작자/출처 표시
- 서비스 이용약관 준수

---

## 산출물 체크

### 프로토타입 3: 웹 정보 수집기 ⭐⭐

```bash
node news_crawler.js
```

- [ ] 스크립트 실행 성공
- [ ] CSV 파일 생성됨
- [ ] 제목, 링크, 수집일시 포함

### 콘텐츠 생성 체험

- [ ] Gemini로 홍보 문구 생성
- [ ] Nano Banana로 이미지 생성
- [ ] Canva로 최종 완성

---

## 학습 포인트 정리

### 오늘 배운 것

| 개념 | 설명 |
|------|------|
| HTML | 웹 페이지 구조 |
| axios | HTTP 요청 (페이지 가져오기) |
| cheerio | HTML 파싱 (jQuery 스타일) |
| CSS 선택자 | 요소 찾기 |
| async/await | 비동기 처리 |
| Nano Banana | AI 이미지 생성 |
| Canva | 디자인 편집 |

### 핵심 메시지

> **"크롤링으로 데이터를 모으고, AI로 콘텐츠를 만든다"**

---

## 체크포인트

| 단계 | 확인 사항 | 완료 |
|------|-----------|------|
| 1 | axios, cheerio 설치 완료 | ☐ |
| 2 | 웹 크롤러 실행 성공 | ☐ |
| 3 | CSV 파일 생성 확인 | ☐ |
| 4 | 콘텐츠 생성 체험 완료 | ☐ |

> **다음 시간**: Express로 나만의 프로토타입 만들기
