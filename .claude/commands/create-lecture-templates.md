# 강의 제작 템플릿 & 컨벤션 참조

이 파일은 `create-lecture` 스킬의 지원 파일입니다.
에이전트들이 강의 제작 시 참조하는 CSS 템플릿, SVG 표준, 레이아웃 패턴을 정의합니다.

---

## Marp CSS 템플릿

모든 `lecture.md` 파일의 프런트매터에 포함할 표준 CSS:

```markdown
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
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

section.lead {
  padding: 60px 80px;
  text-align: center;
  justify-content: center;
}

h1 {
  color: #2c3e50;
  font-size: 3.2em;
  margin-top: 0;
  font-weight: 700;
}

h2 {
  color: #3498db;
  font-size: 2.6em;
  margin-top: 0;
  font-weight: 700;
}

h3 {
  font-size: 1.6em;
  font-weight: 600;
}

p, li {
  font-size: 0.95em;
  line-height: 1.5;
  font-weight: 400;
}

code {
  background: #f4f4f4;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 1.1em;
}

table {
  font-size: 0.95em;
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
```

---

## SVG 이미지 표준

### viewBox & 크기

- 배경 이미지용: `viewBox="0 -80 600 960"` (세로로 긴 비율, 1:1.6)
- 인라인 이미지용: `viewBox="0 0 800 600"` (가로로 긴 비율, 4:3)

### 색상 팔레트

| 용도 | 색상 | 코드 |
|------|------|------|
| 주요 강조 (파랑) | Blue | `#3498db` |
| 성공/긍정 (초록) | Green | `#2ecc71` |
| 경고/주의 (노랑) | Yellow | `#f39c12` |
| 위험/강조 (빨강) | Red | `#e74c3c` |
| 보조 (보라) | Purple | `#9b59b6` |
| 텍스트 (진회색) | Dark | `#2c3e50` |
| 보조 텍스트 (회색) | Gray | `#7f8c8d` |
| 배경 그라데이션 시작 | Light Blue | `#e8f4fd` |
| 배경 그라데이션 끝 | Light Gray | `#dfe6e9` |

### SVG 레이아웃 원칙

1. **콘텐츠는 viewBox 중앙에 배치** (Marp 배경 이미지 지시어가 잘리지 않도록)
2. **내부 여백 확보**: 상하 80px, 좌우 100px 이상
3. **배경 그라데이션** 포함 (일관된 시각적 톤 유지)
4. **한글 텍스트**: `font-family="sans-serif"` 사용
5. **아이콘 크기**: 최소 30x30px, 최대 90x90px (인식 가능한 범위)

### SVG 기본 템플릿

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -80 600 960">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#e8f4fd;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#dfe6e9;stop-opacity:1" />
    </linearGradient>
  </defs>

  <rect x="0" y="-80" width="600" height="960" fill="url(#bgGrad)" rx="0"/>

  <!-- 메인 콘텐츠 영역 (중앙 배치) -->
  <!-- ... -->

  <!-- 제목 텍스트 -->
  <text x="300" y="500" text-anchor="middle" font-size="36" font-weight="bold"
        fill="#2c3e50" font-family="sans-serif">제목</text>
  <text x="300" y="545" text-anchor="middle" font-size="16"
        fill="#7f8c8d" font-family="sans-serif">부제</text>
</svg>
```

---

## 슬라이드 레이아웃 패턴

### 패턴 1: 배경 이미지 + 텍스트

```markdown
![bg left:35%](images/img_example.svg)

## 슬라이드 제목

### 부제

- 콘텐츠는 오른쪽 65% 영역에 표시
- 배경 이미지는 반드시 35% 사용 (40% 이상 금지)
```

### 패턴 2: 2단 그리드

```markdown
## 제목

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

<div>

### 왼쪽 제목

- 항목 1
- 항목 2

</div>

<div>

### 오른쪽 제목

- 항목 1
- 항목 2

</div>

</div>
```

### 패턴 3: 3단 그리드

```markdown
## 제목

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 30px;">

<div>

### 제목 1

내용

</div>

<div>

### 제목 2

내용

</div>

<div>

### 제목 3

내용

</div>

</div>
```

### 패턴 4: 하이라이트 박스

```markdown
<div class="highlight">
핵심 메시지: <strong>강조할 내용</strong>
</div>

<div class="success">
<strong>학습 포인트</strong>: 긍정적/완료 메시지
</div>

<div class="question">
질문이나 생각해볼 거리
</div>
```

### 패턴 5: 리드(타이틀) 슬라이드

```markdown
<!-- _class: lead -->

# Part N 제목

부제 또는 한 줄 메시지
```

### 패턴 6: 테이블 (공간 절약)

불릿 리스트 대신 테이블을 사용하면 세로 공간을 약 40-50% 절약:

```markdown
| 구분 | 항목 1 | 항목 2 | 항목 3 |
|------|--------|--------|--------|
| 행 1 | 내용 | 내용 | 내용 |
| 행 2 | 내용 | 내용 | 내용 |
```

---

## 파일 명명 규칙

### 디렉토리

- 소문자 케밥 케이스: `lecture-XX-주제명`
- XX는 두 자리 숫자: `01`, `02`, ..., `11`, `12`

### 마크다운 파일

- 메인 프레젠테이션: `lecture.md`
- 모듈화 파트: `part-01.md`, `part-02.md`, ...
- 개요: `outline.md`
- 요구사항: `requirements.md`

### 이미지 파일

- snake_case + 순번 조합: `img_파트_순번_설명.svg`
- 예시:
  - `img_title.svg` (타이틀 슬라이드용)
  - `img_1_1_concept.svg` (Part 1, 첫 번째 이미지)
  - `img_chatbot_vs_agent.svg` (설명적 이름)

### 중간 산출물 (.work/)

- `audience-analysis.md` - 수강생 분석
- `topic-research.md` - 주제 리서치
- `reference-analysis.md` - 기존 강의 분석
- `lab-sections.md` - 실습 섹션 초안
- `review-report.md` - 품질 리뷰 리포트

---

## 슬라이드 분량 가이드

### 시간-슬라이드 관계

- 평균 **1 슬라이드 = 2분** (이론 슬라이드 기준)
- 실습 슬라이드는 **1 슬라이드 = 3~5분** (실습 시간 포함)
- 60분 강의 = 약 25~30장, 120분 강의 = 약 45~55장

### 슬라이드 콘텐츠 밀도

- **텍스트**: 슬라이드당 불릿 최대 5~6개
- **테이블**: 최대 4행 × 5열
- **코드 블록**: 최대 8~10줄
- 초과 시 슬라이드를 분할

### Part 전환

- 각 Part 시작 전에 `<!-- _class: lead -->` 타이틀 슬라이드 삽입
- Part 종료 시 다음 Part 예고 슬라이드 삽입 (선택)

---

## 템플릿 진화

이 파일은 `/create-lecture-reflect` 실행 시 자동으로 갱신될 수 있습니다.
`learnings/create-lecture.md`에서 "반복 패턴"으로 승격된 항목 중 CSS/SVG/레이아웃 관련 교훈이 이 파일에 반영됩니다.

### 진화 규칙

1. learnings에서 "반복 패턴"으로 승격된 항목 중 CSS/SVG/레이아웃 관련 → 이 파일에 반영
2. 기존 패턴과 충돌하면 사용자에게 확인 후 반영
3. 변경 이력은 git commit으로 추적

### 변경 이력

| 날짜 | 항목 | 변경 내용 | 근거 |
|------|------|----------|------|
| (자동 기록) | | | |
