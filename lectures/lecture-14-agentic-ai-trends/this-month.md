---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-06-21 | 범위: 이번달 (2026년 6월) -->

<style>
section {
  padding: 60px 80px;
  font-size: 26px;
}

section.lead {
  padding: 60px 80px;
}

section.lead h1 {
  font-size: 56px;
  margin-bottom: 8px;
  color: #0d47a1;
}

section.lead h2 {
  font-size: 32px;
  color: #555;
  font-weight: 400;
  margin-top: 0;
}

section h1 {
  font-size: 44px;
  color: #0d47a1;
}

ul {
  line-height: 1.6;
}

table {
  font-size: 21px;
}

table th {
  background: #e3f2fd;
}

.lead-meta {
  font-size: 21px;
  color: #1976d2;
  font-weight: 600;
  margin-top: 26px;
}

.big {
  font-size: 30px;
  font-weight: 700;
  line-height: 1.5;
  color: #0d47a1;
  margin: 14px 0 22px 0;
}

.note {
  margin-top: 24px;
  padding: 16px 22px;
  background: #f5f5f5;
  border-left: 5px solid #1976d2;
  font-size: 22px;
}

.highlight {
  margin-top: 24px;
  padding: 16px 22px;
  background: #fff3e0;
  border-left: 5px solid #ef6c00;
  font-size: 23px;
}

.src {
  margin-top: 20px;
  font-size: 17px;
  color: #9e9e9e;
}

.src a {
  color: #1976d2;
  text-decoration: none;
}

.cards {
  display: flex;
  flex-wrap: wrap;
  gap: 16px 18px;
  margin-top: 26px;
}

.card {
  display: block;
  width: 508px;
  box-sizing: border-box;
  border: 1px solid #d6dde2;
  border-left: 5px solid #1976d2;
  border-radius: 10px;
  padding: 12px 18px;
  background: #ffffff;
  text-decoration: none;
}

.card .outlet {
  display: block;
  font-size: 14px;
  font-weight: 700;
  color: #1976d2;
}

.card .head {
  display: block;
  font-size: 18px;
  font-weight: 600;
  color: #1f2937;
  margin: 3px 0;
  line-height: 1.3;
}

.card .link {
  display: block;
  font-size: 14px;
  color: #94a3b8;
}

.card.video {
  border-left-color: #d32f2f;
}

.card.video .outlet {
  color: #d32f2f;
}
</style>

<!-- _class: lead -->

![bg left:35%](images/img_hero_month.svg)

# Agentic AI 동향

## 이번달 — 2026년 6월

<div class="lead-meta">

갱신 2026-06-21 · 범위: 2026년 6월 누적

</div>

---

# 6월 한눈에

<div class="big">

2026년 6월 — 신모델 3종 경쟁, 그리고 PC가 '에이전트 판'으로

</div>

- 한 달 새 신모델 3종(Claude·Gemini·GPT) 동시 경쟁
- Windows가 에이전트를 직접 실행하는 판으로 진화
- 서로 다른 회사의 에이전트끼리 협업하기 시작
- 도입 성과가 ROI 숫자로 계속 확인됨

<div class="note">

아래에서 새 모델 → 실행 판 → 협업 → 성과 순으로 본다

</div>

---

# 6월에 나온·임박한 모델

| 무엇 | 등장·상태 | 핵심 한 줄 |
|---|---|---|
| Claude Fable 5 | 6/9 출시 | 어려운 추론에서 최상위급 |
| Gemini 3.5 Pro | 6월 임박 | 맥락 200만·'Deep Think' |
| GPT 신형 | 6월 예고 | 맥락 150만으로 확대 |
| Windows 에이전트 | Build 2026 | PC가 에이전트 실행 판으로 |

<div class="note">

공통점 — 자랑하는 건 '에이전트로 얼마나 일을 잘하나'

</div>

<div class="src">

출처: [LLM 업데이트 — llm-stats](https://llm-stats.com/llm-updates) · [신모델 3종 정리](https://www.essamamdani.com/blog/june-2026-ai-model-flood-gpt-gemini-claude)

</div>

---

# 모델이 어떻게 강해졌나

- Claude Fable 5 — 길고 복잡한 작업일수록 격차가 더 벌어짐
- Gemini 3.5 Pro — 한 번에 읽는 분량(맥락)이 200만 단어급
- 'Deep Think' — 어려운 문제를 더 오래 곱씹어 정확도를 높임
- 공통 — '오래 일하기'와 'PC 직접 사용'이 핵심 경쟁력

<div class="highlight">

새 버전의 자랑거리가 '대화 솜씨'에서 '일 처리력'으로 옮겨갔다

</div>

<div class="src">

출처: [TechTimes — Gemini 3.5 Pro](https://www.techtimes.com/articles/317919/20260606/google-gemini-35-pro-nears-june-launch-2-million-token-context-deep-think-reasoning.htm) · [LLM 업데이트](https://llm-stats.com/llm-updates)

</div>

---

# 새 판 — PC가 에이전트를 직접 돌린다

- Microsoft Build 2026 — Windows를 'AI 에이전트 실행 판'으로 선언
- Windows 365 for Agents·실행 컨테이너 등 도구 공개
- NVIDIA — 기업용 '에이전트 개발 판' 공개 (17개 SW 기업 합류)
- 안전 장치(OpenShell)로 사내 데이터 보호하며 에이전트 실행

<div class="note">

모델만이 아니라 — 모델을 안전하게 돌릴 '판'까지 빠르게 짜이는 중

</div>

<div class="src">

출처: [Microsoft Build 2026](https://redmondmag.com/articles/2026/06/02/microsoft-uses-build-2026-to-put-ai-agents-at-the-center-of-windows.aspx) · [NVIDIA 플랫폼](https://nvidianews.nvidia.com/news/ai-agents)

</div>

---

# 에이전트끼리 협업이 시작되다

- 6/18 Cognizant — ServiceNow의 AI 에이전트와 연동 발표
- 그동안 회사마다 따로 놀던 에이전트를 한 곳에서 지휘
- MCP(공용 콘센트 규격)로 연결돼 별도 작업 없이 자동 연동
- 구글 검색 — '정보 에이전트'와 식당·체험 예약 자동화 시작

<div class="note">

MCP — AI와 도구·다른 AI를 같은 방식으로 꽂아 쓰게 해주는 표준

</div>

<div class="src">

출처: [Cognizant (6/18)](https://news.cognizant.com/2026-06-18-Cognizant-expands-cross-platform-agentic-AI-with-new-ServiceNow-AI-Agent-interoperability) · [Google 검색 I/O 2026](https://blog.google/products-and-platforms/products/search/search-io-2026/)

</div>

---

# 숫자로 보는 도입 성과

| 지표 | 결과 |
|---|---|
| 에이전트 '실제 운영' 도입 | 기업 72% |
| 도입 평균 ROI | 171% (미국 192%) |
| 1년 내 ROI 달성 | 임원 74% |
| 고객지원 통화 시간 | 약 25% 단축 |

<div class="highlight">

'AI가 일을 한다'가 구호가 아니라 숫자로 확인되는 단계

</div>

<div class="src">

출처: [도입 ROI 사례집](https://aimonk.com/agentic-ai-examples-enterprise-roi-case-studies/) · [도입 통계 2026](https://paul-okhrem.com/enterprise-ai-agents-statistics-2026/)

</div>

---

# 6월, 여기까지

<div class="big">

6월 요약 — 모델은 골라 쓰고, 에이전트는 협업한다

</div>

- 신모델 3종이 동시 경쟁 — 한 회사 묶임에서 벗어나는 흐름
- Windows·NVIDIA 등 에이전트 '실행 판'이 빠르게 깔림
- 서로 다른 회사의 에이전트끼리 협업하기 시작
- 도입 성과가 ROI 숫자로 계속 확인됨

<div class="note">

다음은 '지난주' — 가장 최근 일주일을 본다

</div>

---

# 출처 · 영상으로 더 보기

<div class="cards">

<a class="card video" href="https://www.youtube.com/watch?v=iYCRoY_x1HM">
<span class="outlet">▶ YOUTUBE</span>
<span class="head">신모델 3종(Claude·GPT·Gemini) 정리 영상</span>
<span class="link">youtube.com</span>
</a>

<a class="card" href="https://www.techtimes.com/articles/317919/20260606/google-gemini-35-pro-nears-june-launch-2-million-token-context-deep-think-reasoning.htm">
<span class="outlet">TECHTIMES</span>
<span class="head">Gemini 3.5 Pro — 6월 출시 임박, 맥락 200만</span>
<span class="link">techtimes.com</span>
</a>

<a class="card" href="https://redmondmag.com/articles/2026/06/02/microsoft-uses-build-2026-to-put-ai-agents-at-the-center-of-windows.aspx">
<span class="outlet">REDMOND</span>
<span class="head">Build 2026 — Windows가 에이전트 실행 판으로</span>
<span class="link">redmondmag.com</span>
</a>

<a class="card" href="https://nvidianews.nvidia.com/news/ai-agents">
<span class="outlet">NVIDIA</span>
<span class="head">기업용 '에이전트 개발 판' 공개</span>
<span class="link">nvidianews.nvidia.com</span>
</a>

<a class="card" href="https://news.cognizant.com/2026-06-18-Cognizant-expands-cross-platform-agentic-AI-with-new-ServiceNow-AI-Agent-interoperability">
<span class="outlet">COGNIZANT</span>
<span class="head">서로 다른 에이전트를 한 곳에서 지휘 (6/18)</span>
<span class="link">news.cognizant.com</span>
</a>

<a class="card" href="https://aimonk.com/agentic-ai-examples-enterprise-roi-case-studies/">
<span class="outlet">사례집</span>
<span class="head">기업 Agentic AI 도입 ROI 사례 모음</span>
<span class="link">aimonk.com</span>
</a>

</div>
