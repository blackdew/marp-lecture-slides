# AI Agent 워크샵 실습 파일

Gemini CLI 중심의 AI 에이전트 활용 강의를 위한 실습 파일입니다.

## 시작하기

### Agent가 알아서 설치해줍니다!

**권장 방식**: 프롬프트만 주면 Agent가 필요한 패키지를 자동으로 설치합니다.

```
예시: "CSV 파일을 합쳐줘" → Agent가 csv-parser, csv-writer 자동 설치!
```

### (대안) 수동 설치

Agent가 설치하지 못하는 경우에만 직접 설치하세요:

```bash
cd samples
npm install
```

설치되는 패키지:
- `csv-parser` - CSV 파일 읽기
- `csv-writer` - CSV 파일 쓰기
- `axios` - HTTP 요청
- `cheerio` - HTML 파싱
- `express` - 웹 서버

## 폴더 구조

```
samples/
├── README.md           # 이 파일
├── package.json        # npm 패키지 설정
├── part-03-csv/        # Part 3: CSV 통합 실습용
├── part-03-organize/   # Part 3: 폴더 정리 실습용
└── part-05-express/    # Part 5: Express 프로토타입용
```

## Part별 실습 안내

### Part 3-1: CSV 데이터 통합

**목표**: 세 개의 월별 매출 파일을 하나로 합치기

**샘플 파일** (`part-03-csv/`):
- `sales_jan.csv` - 1월 매출 (날짜 형식: YYYY/MM/DD)
- `sales_feb.csv` - 2월 매출 (날짜 형식: MM-DD-YYYY)
- `sales_mar.csv` - 3월 매출 (날짜 형식: X월 X일)

**실습 프롬프트**:
```
다음 작업을 수행하는 Node.js 스크립트를 만들어줘:

1. part-03-csv 폴더의 sales_jan.csv, sales_feb.csv, sales_mar.csv 파일을 읽어서
2. 하나로 합치고
3. 날짜 컬럼을 YYYY-MM-DD 형식으로 통일하고
4. sales_merged.csv로 저장해줘

csv-parser와 csv-writer 패키지를 사용해줘.
```

**도전 과제**:
```
담당자별 총 매출 합계도 계산해서 sales_summary.csv로 저장해줘.
```

### Part 3-2: 폴더 자동 정리

**목표**: 파일들을 확장자별로 분류하기

**샘플 파일** (`part-03-organize/`):
- 문서: `.pdf`, `.docx`, `.xlsx`, `.pptx`, `.txt`
- 이미지: `.jpg`, `.jpeg`, `.png`, `.gif`
- 압축: `.zip`, `.tar.gz`
- 미디어: `.mp4`, `.mp3`

**실습 프롬프트**:
```
part-03-organize 폴더의 파일들을 확장자별로 분류하는 스크립트 만들어줘.

분류 규칙:
- images: jpg, jpeg, png, gif
- documents: pdf, doc, docx, xlsx, pptx, txt
- archives: zip, tar, gz
- media: mp4, mp3
- others: 나머지

파일명: organize_folder.js
```

**도전 과제**:
```
파일들을 날짜(수정일)별로도 정리해줘.
폴더 구조: images/2024-01-15/photo.jpg 형식으로 해줘.
```

### Part 4: 웹 정보 수집

**목표**: 웹 페이지에서 정보 추출하기

**실습 프롬프트**:
```
다음 작업을 수행하는 Node.js 스크립트를 만들어줘:

1. https://news.ycombinator.com/ 페이지에서
2. 뉴스 제목과 링크를 추출하고
3. news_headlines.csv 파일로 저장해줘

컬럼: 제목, 링크, 수집일시
파일명: news_crawler.js
```

### Part 5: Express 프로토타입

**목표**: 웹 애플리케이션 만들기

`part-05-express/` 폴더에서 작업하세요.

**템플릿 1: 보고서 자동 생성기**
```
Express로 보고서 자동 생성기를 만들어줘.

기능:
1. 주제 입력 (text input)
2. 보고서 유형 선택 (select: 일일보고, 주간보고, 프로젝트보고)
3. "생성" 버튼 클릭 시 개요/본문 표시

파일명: report_generator.js
```

**템플릿 2: 수업 노트 요약기**
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

**템플릿 3: 취업 공고 비교 도구**
```
Express로 취업 공고 비교 도구를 만들어줘.

기능:
1. 취업 공고 정보 입력 (회사명, 직무, 연봉, 위치, 복리후생)
2. 최대 3개 공고 입력 가능
3. "비교" 버튼 클릭 시 비교표 생성

파일명: job_comparer.js
```

## 유용한 명령어

```bash
# 스크립트 실행
node 파일명.js

# Express 서버 실행 후
# 브라우저에서 http://localhost:3000 접속

# CSV 파일 내용 확인
cat 파일명.csv

# 폴더 내용 확인
ls -la 폴더명/
```

## 문제 해결

### "Cannot find module" 에러
```bash
npm install 패키지명
```

### "EADDRINUSE" 에러 (포트 사용 중)
다른 터미널에서 실행 중인 서버를 종료하거나, 포트 번호를 변경하세요.

### 경로 문제
상대 경로 대신 절대 경로를 사용하거나, 현재 작업 디렉토리를 확인하세요:
```bash
pwd
```

## 참고

- 강의 슬라이드: `../lecture.html`
- 강의 개요: `../outline.md`
