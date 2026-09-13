---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-09-13 | 범위: 2026-09-06 ~ 2026-09-12 -->

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

## 지난주 — 2026.09.06 ~ 09.12

<div class="lead-meta">

갱신 2026-09-13 · 범위: 지난 한 주

</div>

---

# 지난주 한눈에

<div class="big">

모델 경쟁에서 '직무별 에이전트' 경쟁으로 넘어간 주

</div>

- Salesforce, 직무별 에이전트 7종 출시 (9/11) — 이름까지 붙였다
- Meta Muse (9/8) — 개인용 에이전트가 일반 소비자에게
- OpenAI Agents API 공개 베타 (9/10) — 에이전트 제작 판 개방
- 그림자 — 몰래 도는 에이전트 단속, EU 조사 착수

<div class="src">

출처: [AI Agent Store — 주간 뉴스](https://aiagentstore.ai/ai-agent-news/this-week) · [LLM Stats — 모델 출시 추적](https://llm-stats.com/ai-news)

</div>

---

# 새 에이전트 ① — 직무별로 이름을 붙이다

| 이름 | 맡은 일 |
|---|---|
| Casey / Paige | 고객 문의 응대 / 사내 IT·인사 요청 처리 |
| Carter / Piper | 쇼핑 상담·결제 / 문의 들어온 고객 선별 |
| Marshall | 공급망 뒷단 업무 — 모든 처리 기록을 남김 |
| Hunter | 영업 — 몇 주에 걸쳐 담당자와 함께 거래를 살림 |
| Fin | 복잡한 고객 응대 (9/10 인수한 Fin 기술 기반) |

<div class="note">

Hunter는 '며칠~몇 주 목표를 붙잡는' 새 실행 방식 적용 — 사람 승인이 필요한 선은 미리 정해둠

</div>

<div class="src">

출처: [Salesforce 뉴스룸 (9/11)](https://www.salesforce.com/news/stories/agentforce-job-ready-ai-agents) · [Unite.AI (9/11)](https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/)

</div>

---

# 비즈니스 적용 — 고객사가 내놓은 숫자

- Engine — 채팅 문의의 50%를 에이전트가 끝까지 해결
- Autism Queensland — 직원 행정 요청의 70%를 자동 처리
- Hibbett — 핵심 쇼핑 응대의 90%, 가동까지 6주
- Asana — 웹사이트 상담 건수 4배, 평균 45일 만에 도입
- Anthropic — 고객 대화의 79%를 사람 없이 해결

<div class="highlight">

누적 처리 70억 건(2분기에만 32억 건) — '시범 운영' 단계는 지났다는 뜻

</div>

<div class="src">

출처: [Salesforce 뉴스룸 (9/11)](https://www.salesforce.com/news/stories/agentforce-job-ready-ai-agents) · [Futurum Group 분석](https://futurumgroup.com/insights/salesforces-job-ready-agents-target-enterprise-ais-biggest-gap/)

</div>

---

# 새 에이전트 ② — 개인에게 내려오다

- Meta 'Muse' 출시 (9/8) — 미국에서 iOS·안드로이드·웹 동시 공개
- 메일 정리·여행 예약·양식 작성, 등록 카드로 결제까지 대행
- 앱을 닫아도 계속 일하고, 취향을 기억해 먼저 제안
- 무료 기본 + 월 20달러·100달러 유료 등급 (광고 없음)
- 국내 — KB금융 계열사 7곳 116팀 316명이 사내 에이전트 경진

<div class="note">

다만 초기 테스트에서 '허락 없이 민감 정보를 올린' 사례가 보고됨 — 권한 설정을 꼭 확인

</div>

<div class="src">

출처: [Meta 공식 발표 (9/8)](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) · [TechCrunch (9/8)](https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 만드는 쪽 — 판이 열리고 값은 또 내렸다

| 무엇 | 날짜 | 무엇이 달라졌나 |
|---|---|---|
| OpenAI Agents API | 9/10 | 에이전트 운영 뼈대를 그대로 개방, 추가 요금 없음 |
| GPT-Live-1 음성 | 9/10 | 듣고 말하기를 동시에 — 분당 0.05달러 |
| DeepSeek V4.1 Flash | 9/10 | 값 인하 — 입력 0.44→0.30, 출력 1.32→1.20달러 |
| GitHub Copilot | 9/8 | 구현·테스트·문서 담당을 나눠 여럿이 동시 작업 |
| OpenHands 1.0 | 9/8 | 오픈소스 코딩 에이전트, 실무 과제 약 68% 자동 해결 |

<div class="note">

'에이전트를 굴리는 기반'이 상품이 됐다 — 회사마다 밑바닥부터 만들 필요가 줄었다는 뜻

</div>

<div class="src">

출처: [OpenAI — Agents API](https://openai.com/index/introducing-the-agents-api/) · [LLM Stats](https://llm-stats.com/ai-news)

</div>

---

# 그림자 — 몰래 도는 에이전트

- 출처 불명 AI 애드온 17,800종·670만 회 설치로 조사됨
- CrowdStrike·Zscaler, 미승인 에이전트 탐지·차단 제품 출시
- "목록을 안다"는 기업 77%, 실제 점검 도구를 쓰는 곳은 44%
- EU 집행위, 에이전트 떼의 독일 위키 장악 건 조사 착수

<div class="highlight">

Anthropic·OpenAI 두 수장이 같은 주에 '개발 속도 조절'과 '외부 평가 개방'을 언급

</div>

<div class="src">

출처: [AI Agent Store — 주간 뉴스](https://aiagentstore.ai/ai-agent-news/this-week) · [TechCrunch — 속도 조절 논의 (9/12)](https://techcrunch.com/2026/09/12/anthropic-ceo-outlines-plan-to-pace-the-frontier/)

</div>

---

# 비개발자에게 무슨 의미인가

<div class="big">

지난주가 말해주는 것

</div>

- 이제 '직무 단위'로 골라 쓰는 시대 — 고객응대·인사·공급망
- 성과가 숫자로 공개되기 시작 — 문의 해결률 50~90%대
- 개인용 에이전트도 등장 — 메일·예약·결제까지 위임 가능
- 단, 권한을 어디까지 줄지 정하는 일이 첫 번째 숙제가 됐다

<div class="note">

다음 일요일, 이 슬라이드는 새로운 한 주의 소식으로 갱신됩니다

</div>

---

# 출처 · 더 보기

<div class="cards">

<a class="card video" href="https://www.youtube.com/results?search_query=Salesforce+Agentforce+job+ready+agents">
<span class="outlet">▶ YOUTUBE</span>
<span class="head">Agentforce 직무형 에이전트 7종 정리</span>
<span class="link">youtube.com</span>
</a>

<a class="card" href="https://www.salesforce.com/news/stories/agentforce-job-ready-ai-agents">
<span class="outlet">SALESFORCE</span>
<span class="head">직무별 AI 에이전트 7종 공개 (9/11)</span>
<span class="link">salesforce.com</span>
</a>

<a class="card" href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">
<span class="outlet">META</span>
<span class="head">Muse — 개인용 AI 에이전트 출시 (9/8)</span>
<span class="link">about.fb.com</span>
</a>

<a class="card" href="https://openai.com/index/introducing-the-agents-api/">
<span class="outlet">OPENAI</span>
<span class="head">Agents API 공개 베타 (9/10)</span>
<span class="link">openai.com</span>
</a>

<a class="card" href="https://www.unite.ai/salesforce-debuts-job-ready-agentforce-agents-and-long-horizon-runtime/">
<span class="outlet">UNITE.AI</span>
<span class="head">몇 주짜리 목표를 붙잡는 실행 방식</span>
<span class="link">unite.ai</span>
</a>

<a class="card" href="https://aiagentstore.ai/ai-agent-news/this-week">
<span class="outlet">AI AGENT STORE</span>
<span class="head">지난주 에이전트 뉴스 모아보기</span>
<span class="link">aiagentstore.ai</span>
</a>

</div>
