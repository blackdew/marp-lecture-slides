---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-06-21 | 범위: 지난주 (2026-06-14 ~ 2026-06-20) -->

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

![bg left:35%](images/img_hero_week.svg)

# Agentic AI 동향

## 지난주 — 2026.06.14 ~ 06.20

<div class="lead-meta">

갱신 2026-06-21 · 범위: 지난 한 주

</div>

---

# 지난주 한눈에

<div class="big">

지난주의 중심 — 새 모델 3종 경쟁, 그리고 '에이전트끼리 협업'

</div>

- 새 모델 러시 — Gemini 3.5 Pro 출시 임박 (한 달 새 3종 경쟁)
- 서로 다른 회사의 에이전트가 한 흐름으로 협업 시작
- 기업 도입이 '실험'을 넘어 '실제 운영' 단계로
- NVIDIA·구글·메타 등 'AI 동료'를 만드는 판이 더 커짐

<div class="src">

영상: [한 달 새 신모델 3종 — 정리 영상 (YouTube)](https://www.youtube.com/watch?v=iYCRoY_x1HM)

</div>

---

# 새 모델 — Gemini 3.5 Pro, 출시 임박

- 6/19 기준 — 기업 고객 대상 제한 미리보기, 일반 출시 임박
- 한 번에 읽는 분량(맥락)이 200만 단어 수준으로 커짐
- 'Deep Think' — 어려운 문제를 더 오래 곱씹어 푸는 방식
- 같은 달에 GPT·Claude까지 — 신모델 3종이 동시 경쟁

<div class="highlight">

핵심 — 한 회사에 묶이지 않고 골라 쓰는 시대로

</div>

<div class="src">

출처: [TechTimes — Gemini 3.5 Pro](https://www.techtimes.com/articles/317919/20260606/google-gemini-35-pro-nears-june-launch-2-million-token-context-deep-think-reasoning.htm) · [신모델 3종 정리](https://www.essamamdani.com/blog/june-2026-ai-model-flood-gpt-gemini-claude)

</div>

---

# 새 에이전트 — 서로 다른 AI가 한 팀으로

- 6/18 Cognizant — ServiceNow의 AI 에이전트와 연동 발표
- 그동안 회사마다 따로 놀던 에이전트를 한 곳에서 지휘
- MCP(에이전트용 공용 콘센트 규격)로 연결돼 별도 작업 불필요
- 새 에이전트가 추가되면 자동 인식·배정

<div class="note">

MCP — AI와 도구·다른 AI를 같은 방식으로 꽂아 쓰게 해주는 표준

</div>

<div class="src">

출처: [Cognizant 공식 (6/18)](https://news.cognizant.com/2026-06-18-Cognizant-expands-cross-platform-agentic-AI-with-new-ServiceNow-AI-Agent-interoperability)

</div>

---

# 비즈니스 적용 — 숫자로 보는 도입 성과

| 지표 | 결과 |
|---|---|
| 에이전트 '실제 운영' 도입 | 기업 72% |
| 도입 평균 ROI | 171% (미국 192%) |
| 고객지원 통화 시간 | 약 25% 단축 |
| 상담 전환(돌려주기) | 최대 60% 감소 |

<div class="src">

출처: [기업 도입 ROI 사례집](https://aimonk.com/agentic-ai-examples-enterprise-roi-case-studies/) · [도입 통계 2026](https://paul-okhrem.com/enterprise-ai-agents-statistics-2026/)

</div>

---

# 그 외 주목할 소식

- NVIDIA — 기업용 '에이전트 개발 판' 공개 (17개 SW 기업 합류)
- 구글 검색 — 관심 주제를 알아서 챙겨주는 '정보 에이전트' 시작
- 구글 검색 — 식당·체험 예약까지 에이전트가 대신 처리
- 메타 — 기업용 AI 에이전트를 전 세계로 확대

<div class="note">

모델만이 아니라 — 모델을 '업무에 꽂는 판'이 빠르게 깔리는 중

</div>

<div class="src">

출처: [NVIDIA 에이전트 플랫폼](https://nvidianews.nvidia.com/news/ai-agents) · [Google 검색 I/O 2026](https://blog.google/products-and-platforms/products/search/search-io-2026/)

</div>

---

# 비개발자에게 무슨 의미인가

<div class="big">

지난주가 말해주는 것

</div>

- 새 모델은 매달 나온다 — 이름 외우기보다 '골라 쓰기'가 중요
- 서로 다른 회사의 AI가 한 팀처럼 협업하기 시작했다
- 기업은 '쓸까?'를 넘어 '얼마나 절감됐나'를 따지는 단계
- 식당 예약 같은 일상까지 검색이 대신 처리해준다

<div class="note">

다음 일요일, 이 슬라이드는 새로운 한 주의 소식으로 갱신됩니다

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

<a class="card" href="https://news.cognizant.com/2026-06-18-Cognizant-expands-cross-platform-agentic-AI-with-new-ServiceNow-AI-Agent-interoperability">
<span class="outlet">COGNIZANT</span>
<span class="head">서로 다른 에이전트를 한 곳에서 지휘 (6/18)</span>
<span class="link">news.cognizant.com</span>
</a>

<a class="card" href="https://nvidianews.nvidia.com/news/ai-agents">
<span class="outlet">NVIDIA</span>
<span class="head">기업용 '에이전트 개발 판' 공개</span>
<span class="link">nvidianews.nvidia.com</span>
</a>

<a class="card" href="https://blog.google/products-and-platforms/products/search/search-io-2026/">
<span class="outlet">GOOGLE 블로그</span>
<span class="head">검색의 '정보 에이전트'와 예약 자동화</span>
<span class="link">blog.google</span>
</a>

<a class="card" href="https://aimonk.com/agentic-ai-examples-enterprise-roi-case-studies/">
<span class="outlet">사례집</span>
<span class="head">기업 Agentic AI 도입 ROI 사례 모음</span>
<span class="link">aimonk.com</span>
</a>

</div>
