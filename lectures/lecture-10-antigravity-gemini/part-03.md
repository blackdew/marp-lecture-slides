# Part 3: 파일 자동화 실습

## 파일 자동화란?

### 반복 작업의 자동화

- 매일 같은 형식의 파일 정리
- 여러 CSV 파일 합치기
- 파일 이름 일괄 변경

> **"한 번 스크립트를 만들면, 평생 쓸 수 있다"**

---

## Node.js의 파일 처리

### 핵심 모듈

| 모듈 | 용도 | 설치 |
|------|------|------|
| `fs` | 파일 읽기/쓰기 | 내장 (설치 불필요) |
| `path` | 경로 처리 | 내장 (설치 불필요) |
| `csv-parser` | CSV 읽기 | `npm install` |
| `csv-writer` | CSV 쓰기 | `npm install` |

### 패키지 설치

```bash
npm install csv-parser csv-writer
```

---

## fs 모듈 기초

### 파일 읽기

```javascript
const fs = require('fs');

// 동기식 읽기
const data = fs.readFileSync('hello.txt', 'utf8');
console.log(data);

// 비동기식 읽기
fs.readFile('hello.txt', 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
```

### 파일 쓰기

```javascript
fs.writeFileSync('output.txt', '안녕하세요!');
```

---

## 데이터 처리의 기본: CSV

### CSV란?

- **Comma-Separated Values**
- 엑셀 파일의 단순화 버전
- 텍스트 편집기로도 열 수 있음

### CSV 예시

```csv
이름,나이,부서
홍길동,25,개발팀
김철수,30,마케팅팀
```

### CSV vs 엑셀

| 구분 | CSV | 엑셀 (.xlsx) |
|------|-----|--------------|
| 형식 | 텍스트 | 바이너리 |
| 수식 | ❌ | ✅ |
| 호환성 | 모든 프로그램 | Office 필요 |
| **자동화** | **쉬움** | 복잡함 |

---

## 실습 3-1: CSV 데이터 통합

### 시나리오

3개월치 매출 데이터를 하나로 합쳐야 함

### 샘플 파일

- `sales_jan.csv` - 1월 매출
- `sales_feb.csv` - 2월 매출
- `sales_mar.csv` - 3월 매출

### 문제점

- 날짜 포맷 제각각
- 금액에 ₩ 기호 포함
- 일부 중복 데이터 존재

---

## 실습 3-1: Step by Step

### Step 1: Gemini에게 요청

```
다음 작업을 수행하는 Node.js 스크립트를 만들어줘:

1. sales_jan.csv, sales_feb.csv, sales_mar.csv 세 파일을 읽어서
2. 하나로 합치고
3. 날짜 컬럼을 YYYY-MM-DD 형식으로 통일하고
4. 금액 컬럼에서 ₩ 기호와 콤마를 제거하고
5. sales_merged.csv로 저장해줘

csv-parser와 csv-writer 패키지를 사용해줘.
파일명: merge_sales.js
```

---

## 생성된 코드 예시

```javascript
const fs = require('fs');
const csv = require('csv-parser');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

const files = ['sales_jan.csv', 'sales_feb.csv', 'sales_mar.csv'];
let allData = [];

// 날짜 포맷 통일 함수
function formatDate(dateStr) {
  const date = new Date(dateStr);
  return date.toISOString().split('T')[0];
}

// 금액 정리 함수
function cleanAmount(amount) {
  return Number(amount.replace(/[₩,]/g, ''));
}

// 파일 읽기 및 처리
async function processFiles() {
  for (const file of files) {
    await new Promise((resolve) => {
      fs.createReadStream(file)
        .pipe(csv())
        .on('data', (row) => {
          row['날짜'] = formatDate(row['날짜']);
          row['금액'] = cleanAmount(row['금액']);
          allData.push(row);
        })
        .on('end', resolve);
    });
  }

  // CSV 저장
  const csvWriter = createCsvWriter({
    path: 'sales_merged.csv',
    header: Object.keys(allData[0]).map(key => ({id: key, title: key}))
  });

  await csvWriter.writeRecords(allData);
  console.log('완료! sales_merged.csv 생성됨');
}

processFiles();
```

---

## csv-parser 사용법

### 기본 패턴

```javascript
const fs = require('fs');
const csv = require('csv-parser');

const results = [];

fs.createReadStream('data.csv')
  .pipe(csv())
  .on('data', (row) => {
    // 각 행마다 실행
    results.push(row);
  })
  .on('end', () => {
    // 모든 행 읽기 완료
    console.log(results);
  });
```

### 행 데이터 형태

```javascript
// CSV의 각 행은 객체로 변환됨
{
  '이름': '홍길동',
  '나이': '25',
  '부서': '개발팀'
}
```

---

## csv-writer 사용법

### 기본 패턴

```javascript
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

const csvWriter = createCsvWriter({
  path: 'output.csv',
  header: [
    {id: 'name', title: '이름'},
    {id: 'age', title: '나이'}
  ]
});

const data = [
  {name: '홍길동', age: 25},
  {name: '김철수', age: 30}
];

csvWriter.writeRecords(data)
  .then(() => console.log('저장 완료!'));
```

---

## 도전 과제: 담당자별 매출 합계

### Gemini에게 추가 요청

```
merge_sales.js를 수정해서
담당자별 매출 합계를 계산하고
sales_summary.csv로 저장해줘
```

### 힌트: reduce로 집계

```javascript
const summary = allData.reduce((acc, row) => {
  const name = row['담당자'];
  acc[name] = (acc[name] || 0) + row['금액'];
  return acc;
}, {});
```

---

## 실습 3-2: 폴더 자동 정리 스크립트

### 시나리오

Downloads 폴더가 파일로 가득 참

- 이미지, 문서, 압축파일 등 뒤섞여 있음
- 확장자별로 자동 분류하고 싶음

### 목표

```
Downloads/
├── images/      # .jpg, .png, .gif
├── documents/   # .pdf, .docx, .xlsx
├── archives/    # .zip, .tar
└── others/      # 나머지
```

---

## 실습 3-2: Gemini에게 요청

```
Downloads 폴더의 파일들을 확장자별로 분류하는 Node.js 스크립트를 만들어줘.

분류 규칙:
- images: jpg, jpeg, png, gif, svg
- documents: pdf, doc, docx, xls, xlsx, ppt, pptx
- archives: zip, tar, gz, rar
- others: 나머지

각 폴더가 없으면 자동 생성하고,
파일을 해당 폴더로 이동시켜줘.

파일명: organize_folder.js
```

---

## 생성된 코드 예시

```javascript
const fs = require('fs');
const path = require('path');

// 분류 규칙 정의
const CATEGORIES = {
  images: ['jpg', 'jpeg', 'png', 'gif', 'svg'],
  documents: ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx'],
  archives: ['zip', 'tar', 'gz', 'rar']
};

function getCategory(filename) {
  const ext = path.extname(filename).slice(1).toLowerCase();
  for (const [category, extensions] of Object.entries(CATEGORIES)) {
    if (extensions.includes(ext)) {
      return category;
    }
  }
  return 'others';
}

function organizeFolder(folderPath) {
  const files = fs.readdirSync(folderPath);

  files.forEach(filename => {
    const filePath = path.join(folderPath, filename);

    // 폴더는 건너뛰기
    if (fs.statSync(filePath).isDirectory()) return;

    // 카테고리 결정
    const category = getCategory(filename);

    // 대상 폴더 생성
    const targetFolder = path.join(folderPath, category);
    if (!fs.existsSync(targetFolder)) {
      fs.mkdirSync(targetFolder);
    }

    // 파일 이동
    const targetPath = path.join(targetFolder, filename);
    fs.renameSync(filePath, targetPath);
    console.log(`이동: ${filename} → ${category}/`);
  });

  console.log('정리 완료!');
}

// 실행
organizeFolder('./Downloads');
```

---

## fs 모듈 핵심 메서드

### 파일/폴더 조작

| 메서드 | 설명 |
|--------|------|
| `readdirSync(path)` | 폴더 내 파일 목록 |
| `statSync(path)` | 파일/폴더 정보 |
| `existsSync(path)` | 존재 여부 확인 |
| `mkdirSync(path)` | 폴더 생성 |
| `renameSync(old, new)` | 이동/이름변경 |
| `copyFileSync(src, dest)` | 파일 복사 |
| `unlinkSync(path)` | 파일 삭제 |

---

## path 모듈 핵심 메서드

### 경로 처리

```javascript
const path = require('path');

path.join('folder', 'file.txt')  // 'folder/file.txt'
path.extname('image.png')        // '.png'
path.basename('/home/file.txt')  // 'file.txt'
path.dirname('/home/file.txt')   // '/home'
```

### 왜 path를 사용하나요?

- Windows: `folder\file.txt`
- Mac/Linux: `folder/file.txt`
- `path.join()`이 자동으로 처리!

---

## 도전 과제: 날짜별 폴더 생성

### Gemini에게 추가 요청

```
organize_folder.js를 수정해서
파일의 수정 날짜를 기준으로 YYYY-MM 폴더를 먼저 만들고,
그 안에 확장자별 폴더를 만들어줘.

예시:
Downloads/
├── 2025-01/
│   ├── images/
│   └── documents/
└── 2025-02/
    └── archives/
```

### 힌트

```javascript
const stats = fs.statSync(filePath);
const mtime = stats.mtime;
const folderName = `${mtime.getFullYear()}-${String(mtime.getMonth() + 1).padStart(2, '0')}`;
```

---

## 실습 회고

### 질문

- 성공했나요?
- 에러가 났다면 어떤 에러?
- AI에게 어떻게 물어봤나요?

### 기억하세요

> **"에러는 무서운 게 아니라, AI가 알려주는 힌트예요"**

에러 메시지를 복사해서 Gemini에게 물어보세요!

---

## 흔한 에러와 해결법

| 에러 | 원인 | 해결 |
|------|------|------|
| `ENOENT: no such file` | 파일 경로 오류 | 경로 확인, `pwd` 명령어 |
| `EPERM: operation not permitted` | 권한 부족 | 관리자 모드 실행 |
| `Cannot find module` | 패키지 미설치 | `npm install 패키지명` |
| `SyntaxError` | 문법 오류 | AI에게 코드 검토 요청 |

---

## 산출물 체크

### 프로토타입 1: 폴더 정리 스크립트 ⭐

```bash
node organize_folder.js
```

- [ ] 스크립트 실행 성공
- [ ] 파일이 확장자별로 분류됨
- [ ] 에러 없이 완료

### 프로토타입 2: CSV 통합 분석기 ⭐⭐

```bash
node merge_sales.js
```

- [ ] 세 파일이 하나로 합쳐짐
- [ ] 날짜 포맷 통일됨
- [ ] 금액 정리됨

---

## 학습 포인트 정리

### 오늘 배운 것

| 개념 | 설명 |
|------|------|
| fs 모듈 | 파일 읽기/쓰기/이동 |
| path 모듈 | 경로 처리 |
| csv-parser | CSV 파일 읽기 |
| csv-writer | CSV 파일 쓰기 |

### 핵심 메시지

> **"반복되는 파일 작업은 스크립트로 자동화하세요"**

---

## 체크포인트

| 단계 | 확인 사항 | 완료 |
|------|-----------|------|
| 1 | csv-parser, csv-writer 설치 완료 | ☐ |
| 2 | CSV 통합 스크립트 실행 성공 | ☐ |
| 3 | 폴더 정리 스크립트 실행 성공 | ☐ |
| 4 | 도전 과제 1개 이상 완료 | ☐ |

---

# AI 시대, 우리의 역할

## 실습을 돌아보며

### 방금 경험한 것

```
"CSV 합쳐줘" → Gemini가 코드 생성 → 실행 → 완료!
```

### 질문

- Gemini가 만든 코드, 그대로 썼나요?
- 수정을 요청했나요? 왜?
- 결과물이 마음에 들었나요?

> **AI가 다 해줬는데, 우리는 뭘 한 걸까요?**

---

## AI 시대의 3가지 역할

> **"AI가 모든 걸 해도, 우리의 역할은 더 중요해집니다"**

| 키워드 | 핵심 | 왜 중요한가? |
|--------|------|--------------|
| **1. 선택** | 나의 가치와 선호 반영 | AI 결과물에 "나"를 담아야 내 것이 됨 |
| **2. 계획** | 비어있는 컨텍스트 채우기 | 계획 없으면 엉뚱한 결과 |
| **3. 문서화** | 문서 = 프로젝트 | 문서화로 성찰하고 성장 |

---

## 1. 선택: 의미 담기

### 선택은 비교로부터

**과거**: 정보 수집에 3시간 → 비교 1시간 → 선택 30분

**AI 시대**: Agent가 5분만에 정교한 비교 제공 → **더 나은 선택 가능**

### 예시: 보고서 형식 선택

```
주간 보고서 형식을 5가지 스타일로 비교해줘:
1. 불릿 포인트 (간결)
2. 스토리텔링 (상세)
3. 표 형식 (수치 중심)

각각의 장단점, 적합한 상황을 표로 정리해줘.
```

→ **Agent가 비교 제공 → 내가 가치 기반 선택**

---

## 선택에서 자기가 드러난다

### 같은 비교표, 다른 선택

| 팀 | 가치 | 선택 |
|----|------|------|
| A팀 | "효율 중시" | 불릿 포인트 |
| B팀 | "공감 중시" | 스토리텔링 |
| C팀 | "객관성 중시" | 표 형식 |

### 핵심

- Agent는 정보와 옵션을 제공할 뿐
- **최종 선택은 인간의 몫**
- 선택에서 나의 가치관이 드러남

> **"AI 도구 + 나의 선택 = 의미있는 결과물"**

---

## 2. 계획: 의도 전달

### 두 가지 지시의 차이

**지시 A**: "보고서 써줘"
→ 결과: ???

**지시 B**: "경영진용 주간 보고서를 불릿 포인트로, 주요 성과 3가지와 다음 주 계획 2가지 포함해서 써줘"
→ 결과: 정확히 원하는 대로!

### 비어있는 컨텍스트의 위험

"보고서 써줘"라고 하면 AI가 추론으로 채움:

- 누구를 위한? → "일반 대중용"
- 어떤 톤? → "중립적"
- 얼마나 길게? → "1000단어"

**→ 당신의 의도와 완전히 다른 결과**

---

## AI 시대는 계획의 시대

### 시간 배분의 변화

| 구분 | 과거 | AI 시대 |
|------|------|---------|
| 계획 | 20% | **70%** |
| 실행 | 80% | 30% |

### 좋은 계획의 3원칙

| 원칙 | 나쁜 예 | 좋은 예 |
|------|--------|--------|
| **구체성** | "정리해줘" | "다운로드 폴더의 PDF를 년도별로 정리" |
| **단계성** | "분석해줘" | "1) CSV 로드 2) 중복 제거 3) 집계" |
| **결과물 명시** | "요약해줘" | "3문장으로 summary.md로 저장" |

> **"계획에 시간을 투자할수록, 원하는 결과가 나옵니다"**

---

## 3. 문서화: 성장 도구

### 문서화가 중요한 이유

- 프로젝트 전체 이해
- 언제든 재개 가능
- Agent에게 맥락 전달
- **성찰과 성장의 기록**

### Before vs After AI

| 단계 | Before AI | After AI |
|------|----------|----------|
| 작성 | 내가 직접 (2시간) | Agent가 초안 (5분) |
| 비용 | 작업의 30-50% | **작업의 5-10%** |

> **Agent 덕분에 문서화가 거의 무료가 되었습니다**

---

## 문서 중심 사고

### 전통적 사고

```
결과물 완성 → (시간 있으면) 문서 작성
```

### 문서 중심 사고

```
1. 문서 먼저 (계획서)
2. 작업 수행 (Agent)
3. 문서 업데이트 (진행)
4. 문서로 마무리 (회고)
```

### 실천: 회고 요청

```
오늘 실습 내용을 회고하는 문서를 만들어줘.
- 무엇을 만들었는가
- 무엇을 배웠는가
- 다음에 적용할 점
```

> **"문서 = 프로젝트 = 성찰 = 성장"**

---

## 정리: AI 시대의 3가지 역할

### 1. 선택 = 의미 담기

Agent가 정교한 비교 제공 → **나의 가치로 선택**

### 2. 계획 = 의도 전달

비어있는 컨텍스트 → 엉뚱한 결과
**계획에 70% 시간 투자** → 정확한 결과

### 3. 문서화 = 성장 도구

Agent로 거의 무료 → **문서 = 프로젝트**

> **"AI가 만들어줘도, 선택·계획·문서화는 우리의 몫입니다"**

---

> **점심 후**: 웹 정보 수집 + 콘텐츠 생성
