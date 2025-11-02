# Part 2: 강의 자료 제작

Marp로 프레젠테이션 슬라이드 만들기

---

## 강의 자료 제작의 도전 과제

**강사들이 겪는 어려움**

- 슬라이드 내용 구성
- 시각 자료 준비
- 일관된 디자인 유지
- 여러 강의 버전 관리
- 반복 작업 (포맷팅, 이미지 삽입)

**Claude Code로 해결**

마크다운으로 작성하고 Marp로 변환, 모든 과정을 자동화

---

## 실제 사례: 이 강의 자료

**바로 이 강의가 Claude Code로 제작되었습니다!**

**프로젝트 구조**

```
lectures/
├── CLAUDE.md                    # 작업 컨텍스트
├── generate-presentation.sh     # 빌드 스크립트
├── lecture-01-ai-data-coding/
├── lecture-02-프로젝트공유/
├── lecture-03-ai-agent-intro/
├── lecture-04-claude-code-features/
└── lecture-05-문서작업-실전/   ← 지금 만드는 중!
    ├── part-01-novel-writing.md
    ├── part-02-lecture-creation.md
    ├── lecture.md
    └── images/
```

---

## 작업 흐름: 강의 기획

**1. 개요 작성**

```
"Claude Code를 활용한 문서 작업에 대한
강의 개요를 만들어줘.

대상: 비개발자 포함
주제: 소설, 강의, 논문, 개인 문서
시간: 60분"
```

**2. Claude의 제안**

```markdown
## 강의 구성안

Part 1: 소설 집필 (15분)
- 프로젝트 구조
- 캐릭터 일관성
- 플롯 관리

Part 2: 강의 자료 제작 (15분)
- Marp 활용
- 자동화
...
```

---

## Part 파일 분리 작업

**모듈화 전략**

각 Part를 별도 파일로 작성하고 나중에 통합

**요청**

```
"Part 1: 소설 집필에 대한 슬라이드를 작성해줘.
part-01-novel-writing.md 파일로 저장.

Marp 형식으로 작성하되:
- 슬라이드는 ---로 구분
- 각 슬라이드는 한 화면에 들어갈 분량
- 코드 예시와 실전 팁 포함"
```

---

## Plan Mode로 구조 검토

**큰 작업 전 계획 확인**

```
/plan

"Part 1부터 Part 4까지 모든 슬라이드를 작성해줘"
```

**Claude의 계획**

```
1. Part 1: 소설 집필 (20 슬라이드 예상)
2. Part 2: 강의 자료 (15 슬라이드)
3. Part 3: 논문 리뷰 (18 슬라이드)
4. Part 4: 개인 문서 (15 슬라이드)

각 Part는 별도 파일로 작성 후
lecture.md에 통합
```

**승인**

```
"좋아, 진행해줘"
```

---

## 이미지 생성: SVG 활용

**배경 이미지 필요**

각 Part마다 배경 이미지 필요

**요청**

```
"Part 1용 배경 이미지를 SVG로 만들어줘.
책과 펜을 상징하는 심플한 디자인.

파일명: images/img_1_novel.svg
크기: viewBox="0 -80 600 1160"
콘텐츠는 중앙 배치"
```

**중요: SVG 디자인 원칙**

- 콘텐츠는 항상 중앙 배치
- 내부 여백 충분히 확보
- 세로 방향으로 긴 디자인

---

## SVG 자동 생성

**Claude가 생성한 SVG**

```xml
<svg viewBox="0 -80 600 1160" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea"/>
      <stop offset="100%" style="stop-color:#764ba2"/>
    </linearGradient>
  </defs>

  <!-- 책 아이콘 -->
  <rect x="200" y="400" width="200" height="250"
        fill="white" stroke="#667eea" stroke-width="3"/>

  <!-- 펜 아이콘 -->
  <line x1="350" y1="300" x2="400" y2="400"
        stroke="#764ba2" stroke-width="4"/>
</svg>
```

---

## Custom Command: 슬라이드 생성

**`.claude/commands/new-slide.md`**

```markdown
# 새 슬라이드 섹션 생성

주어진 주제에 대해 5-7개 슬라이드를 생성해줘.

형식:
- Marp 마크다운 (--- 구분자)
- 각 슬라이드: 제목 + 3-5개 불릿 포인트
- 코드 예시는 ```로 감싸기
- 표가 적절한 경우 마크다운 표 사용

확인 사항:
- 한 슬라이드에 너무 많은 내용 X
- 시각적 여백 확보
- 핵심만 간결하게
```

---

## Command 활용

**새 섹션 추가 시**

```
/new-slide "Git을 활용한 버전 관리"
```

**자동 생성 결과**

```markdown
---

## Git으로 버전 관리

**강의 자료도 코드처럼**

- 각 수정사항을 커밋으로 기록
- 이전 버전으로 되돌리기 쉬움
- 여러 버전 실험 가능

---

## Git 초기화

**명령어**

```bash
git init
git add .
git commit -m "Initial lecture slides"
```
...
```

---

## 일관성 검사: Todo 활용

**긴 강의 제작 시**

```
여러 Part를 작성하는 Todo:

☑ Part 1: 소설 집필 완료
☑ Part 2: 강의 자료 완료
→ Part 3: 논문 리뷰 작성 중
☐ Part 4: 개인 문서
☐ 이미지 생성
☐ lecture.md 통합
☐ HTML 빌드 및 테스트
```

**진행 상황을 한눈에 파악**

---

## 파일 통합: lecture.md 생성

**모든 Part가 완성되면**

```
"part-01부터 part-04까지 모든 파일을
순서대로 lecture.md에 통합해줘.

맨 앞에 다음 프런트매터 추가:
---
marp: true
theme: default
size: 16:9
paginate: true
---

그리고 CSS 스타일도 추가:
section { padding: 60px 80px; }"
```

---

## 자동 통합 작업

**Claude가 수행하는 작업**

1. 프런트매터 생성
2. CSS 스타일 추가
3. 표지 슬라이드 생성
4. part-01.md 내용 삽입
5. part-02.md 내용 삽입
6. part-03.md 내용 삽입
7. part-04.md 내용 삽입
8. 마무리 슬라이드 추가

**결과: lecture.md 완성**

---

## 빌드: HTML 생성

**빌드 스크립트 활용**

```bash
./generate-presentation.sh lecture-05-문서작업-실전 lecture.md
```

**스크립트가 수행하는 작업**

```bash
#!/bin/bash
FOLDER=$1
FILE=$2

cd "$FOLDER"
marp "$FILE" -o "${FILE%.md}.html" --html --allow-local-files
cp -r images ./
echo "Generated: $FOLDER/${FILE%.md}.html"
```

---

## 검토: 브라우저 테스트

**HTML 파일 열기**

```bash
open lecture-05-문서작업-실전/lecture.html
```

**확인 항목**

| 항목 | 확인 사항 |
|-----|---------|
| 여백 | 텍스트가 가장자리에 붙지 않는지 |
| 배경 이미지 | 35% 크기, 잘리지 않는지 |
| 오버플로우 | 슬라이드 하단이 잘리지 않는지 |
| 이미지 | 모든 이미지가 로드되는지 |
| 폰트 | 한글이 깨지지 않는지 |

---

## 문제 발견 시

**슬라이드 오버플로우**

```
"Part 2의 5번째 슬라이드가 너무 길어서
내용이 잘려요. 두 슬라이드로 나눠줘"
```

**배경 이미지 여백 부족**

```
"images/img_2_lecture.svg가
슬라이드 가장자리에 붙어있어.
마크다운에서 35%로 줄여줘"
```

**Claude가 즉시 수정**

---

## 반복 작업 자동화

**Custom Command: 빌드 및 검토**

**`.claude/commands/build-and-review.md`**

```markdown
# 빌드 및 검토

1. generate-presentation.sh 실행
2. HTML 파일 생성 확인
3. 주요 체크리스트:
   - 슬라이드 개수 확인
   - 이미지 경로 확인
   - 마지막 슬라이드 확인

4. 문제 발견 시 보고
```

**실행**

```
/build-and-review
```

---

## 버전 관리

**Git으로 강의 버전 관리**

```
"현재까지의 강의 자료를 Git에 커밋해줘.
커밋 메시지는 'feat: Part 1-2 완성'"
```

**Claude 실행**

```bash
git add .
git commit -m "feat: Part 1-2 완성

- Part 1: 소설 집필 사례 추가
- Part 2: 강의 자료 제작 사례 추가
- 배경 이미지 2개 생성
"
```

---

## 강의 업데이트 시나리오

**6개월 후 내용 업데이트 필요**

**Claude Code 활용**

```
"Part 3: 논문 리뷰 섹션에
최신 AI 논문 리뷰 도구 정보를 추가해줘.

기존 내용은 유지하고,
'새로운 도구' 슬라이드 2개 추가"
```

**자동으로**

- 기존 내용 읽기
- 적절한 위치 파악
- 새 슬라이드 삽입
- 일관된 포맷 유지

---

## 여러 강의 시리즈 관리

**프로젝트 구조**

```
lectures/
├── lecture-01-기초/
│   ├── lecture.md
│   └── images/
├── lecture-02-중급/
│   ├── lecture.md
│   └── images/
└── lecture-03-고급/
    ├── lecture.md
    └── images/
```

**일관성 유지**

```
"lecture-01, 02, 03 모두에서
슬라이드 디자인이 일관되는지 확인하고
CSS 스타일을 통일해줘"
```

---

## Agent로 전체 검토

**Explore Agent 활용**

```
"lectures/ 디렉토리 전체를 분석해서:

1. 각 강의의 슬라이드 개수
2. 사용된 이미지 목록
3. 중복된 내용이 있는지
4. 일관되지 않은 표현

을 보고서로 정리해줘"
```

**Agent 보고서**

```
강의 시리즈 분석 결과:

lecture-01: 45 슬라이드, 8 이미지
lecture-02: 52 슬라이드, 10 이미지
lecture-03: 48 슬라이드, 9 이미지

중복 내용:
- "Git 기초" 설명이 01, 02에 중복
  → 02에서는 참조만 하도록 수정 권장
```

---

## PDF 변환

**인쇄용 PDF 생성**

**방법 1: 브라우저 인쇄**

1. HTML 파일을 브라우저로 열기
2. Cmd+P (인쇄)
3. "배경 그래픽" 옵션 활성화
4. PDF로 저장

**방법 2: Command 자동화**

```markdown
# .claude/commands/export-pdf.md

1. HTML 파일이 최신인지 확인
2. 브라우저 인쇄 방법 안내
```

---

## 협업: 피드백 반영

**동료 강사의 피드백**

```
"Part 2의 예시가 너무 기술적이에요.
비개발자도 이해할 수 있게 쉽게 바꿔주세요"
```

**Claude에게 요청**

```
"part-02-lecture-creation.md에서
기술 용어를 쉬운 말로 바꾸고,
비개발자도 이해할 수 있게 예시를 수정해줘"
```

**자동 수정 후 확인**

---

## 강의 자료 재사용

**다른 형식으로 변환**

```
"lecture.md를 블로그 포스트 형식으로 변환해줘.
blog-post.md로 저장하고:

- 슬라이드 구분(---) 제거
- 섹션별로 ## 헤딩으로 구분
- 코드 블록은 그대로 유지"
```

**결과**

강의 슬라이드 → 블로그 글 자동 변환

---

## CLAUDE.md: 작업 컨텍스트

**프로젝트 루트에 CLAUDE.md**

```markdown
# 강의 자료 제작 프로젝트

## 규칙
- Marp 형식 준수
- 이미지는 SVG, 중앙 배치
- 슬라이드당 5-7 불릿 포인트
- 배경 이미지는 35% 크기

## 구조
각 강의는 lecture-XX-주제/ 디렉토리
part-0X.md로 모듈화 후 lecture.md 통합
```

**Claude가 자동으로 규칙 준수**

---

## 실전 팁

| 단계 | Claude Code 활용 |
|-----|-----------------|
| 기획 | 개요 작성, 구조 제안 |
| 작성 | Part별 슬라이드 생성 |
| 이미지 | SVG 자동 생성 |
| 통합 | lecture.md 병합 |
| 빌드 | 스크립트 실행 |
| 검토 | 자동 체크리스트 |
| 업데이트 | 특정 섹션만 수정 |

---

## 강의 제작 시간 비교

**기존 방식 (PowerPoint)**

- 기획: 2시간
- 슬라이드 작성: 8시간
- 디자인: 4시간
- 이미지 준비: 3시간
- **총: 17시간**

**Claude Code + Marp**

- 기획: 1시간 (AI 도움)
- 마크다운 작성: 4시간
- 자동 디자인: 0시간
- SVG 생성: 1시간
- **총: 6시간** (65% 절약!)

---

## 강의 자료 제작 정리

**Claude Code의 이점**

- 마크다운으로 빠른 작성
- 버전 관리 용이
- 일관된 디자인 자동 유지
- 재사용 및 업데이트 쉬움
- 협업 편리

**강사가 얻는 것**

- 내용에 집중
- 시간 절약
- 체계적 관리
- 여러 형식으로 변환 가능

**다음: 논문 리뷰 및 작성**
