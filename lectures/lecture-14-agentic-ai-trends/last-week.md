---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-10-11 | 범위: 2026-10-04 ~ 2026-10-10 -->

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

## 지난주 — 2026.10.04 ~ 10.10

<div class="lead-meta">

갱신 2026-10-11 · 범위: 지난 한 주

</div>

---

# 지난주 한눈에

<div class="big">

AI가 '내 팀원'이 되는 주 — 이메일 주소를 가진 에이전트

</div>

- Google Gemini Agent (10/8) — 목표를 주면 계획·실행하는 업무용 에이전트
- Claude Haiku 5.5 (10/7) — 가장 작은 모델이 값 75%↓, 성능은 대폭 상승
- 기업 현실 — 85%가 실험 중, 실제 운영은 5%
- 그림자 — Anthropic 오작동 보고서, 백악관 사고 보고 의무 언급

<div class="src">

출처: [AI Agent Store — 주간 뉴스](https://aiagentstore.ai/ai-agent-news/this-week) · [AI News 10/9](https://aidapted.ro/en/articles/ai-news-october-9-2026)

</div>

---

# 새 모델 — Claude Haiku 5.5 (10/7)

| 비교 | 이전 Haiku 4.5 | Haiku 5.5 |
|---|---|---|
| 값(입력/출력, 100만 토큰) | 평균 약 4배 비쌈 | 0.10달러 / 0.50달러 |
| 지식노동 평가(GDPval) | 735점 | 1620점 |
| 컴퓨터 조작 평가(OSWorld) | 15.7% | 72.4% |
| 어려운 종합시험(도구 사용) | 18.7% | 57.4% |

<div class="note">

'가장 작고 싼 모델'이 한 세대 전 최상위급 일을 한다 — 단, 위 점수는 회사 발표 수치 (Asana는 지연시간 30%↓ 보고)

</div>

<div class="src">

출처: [AI Weekly — Haiku 5.5](https://aiweekly.co/alerts/introducing-claude-haiku-55) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 새 에이전트 — Gemini Agent (10/8)

- 목표만 주면 계획을 세우고, 부하 에이전트에게 일을 나눔
- 자기만의 구글 계정(이메일 주소)을 가진 팀원처럼 동작
- 메일에 태그하거나 그룹 채팅에 초대해서 일을 맡김
- 처리 내역을 '작업 수신함'에 남기고, 기록은 에이전트 이름으로 저장
- MS 365·Slack·Jira 등 외부 도구와 MCP로 연결

<div class="highlight">

기업 고객부터 — 포천 100대 기업의 약 90%가 이미 Gemini Enterprise 사용 중 (구글 발표)

</div>

<div class="src">

출처: [TechCrunch (10/8)](https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/) · [AI News 10/9](https://aidapted.ro/en/articles/ai-news-october-9-2026)

</div>

---

# 비즈니스 — 도입 현실과 새 제품

- 대기업 85%가 에이전트 실험 중, 운영 투입은 5%
- 시범 운영 중 규모를 키우는 곳은 11~14%
- HackerRank — 면접 에이전트 정식 출시, 시범 중 약 50만 건 진행
- Oracle — ERP 안에 에이전트 조율 기능(Fusion Claw) 탑재
- Microsoft — 며칠씩 도는 'Autopilot' 에이전트를 직원 1인 1개로 구상

<div class="highlight">

가트너 전망 — 2027년까지 에이전트 프로젝트의 40% 이상이 중단될 수 있음

</div>

<div class="src">

출처: [AI Agent Store — 주간 뉴스](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 그 외 소식

- Kimi K2.6 (Moonshot, 오픈소스) — 에이전트 최대 1,000개를 동시에 굴림
- TikTok — 앱 안 쇼핑 도우미·원클릭 결제 (Shopify·Stripe 협력)
- Amazon이 Meta Muse를 차단 — 대리 쇼핑 시 신원 미표시 문제
- Manus, 5억 달러 이상 투자 유치 (Meta 인수는 중국 당국이 불허)
- OpenAI 연 매출 추정치 700억→약 500억 달러로 정정 보도

<div class="note">

에이전트가 '대신 사는 시대'가 되자, 쇼핑몰은 "너 누구냐"를 묻기 시작했다

</div>

<div class="src">

출처: [AI News 10/9](https://aidapted.ro/en/articles/ai-news-october-9-2026) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 안전 — 오작동 기록과 사고 대응

- Anthropic, 평가·내부 사용 중 나온 '의도 밖 행동' 4유형 보고서 공개 (10/9)
- 필라델피아 경찰 — 허위 살인 제보가 AI 모델에서 나온 것으로 확인 (자동 걸러져 출동은 없었음)
- 백악관 — AI 기업은 사고를 보고하고 바로잡아야 한다는 입장
- AI 연구소들, 대형 사고를 가정한 모의 훈련 진행

<div class="highlight">

핵심 — 에이전트가 늘수록 "사고가 나면 누가 알리고 누가 고치나"가 먼저 정해져야 한다

</div>

<div class="src">

출처: [AI Agent Store — 주간 뉴스](https://aiagentstore.ai/ai-agent-news/this-week) · [AI News 10/9](https://aidapted.ro/en/articles/ai-news-october-9-2026)

</div>

---

# 비개발자에게 무슨 의미인가

<div class="big">

지난주가 말해주는 것

</div>

- AI 에이전트를 '직원처럼' 팀에 초대하는 방식이 나왔다
- 가장 작은 모델도 업무 대부분을 맡을 만큼 싸고 똑똑해졌다
- 도입은 말만 많고 운영은 5% — 먼저 시작하면 앞서간다
- 쇼핑·결제를 맡길 땐 '누가 대신 사는지' 밝히는 규칙이 필수

<div class="note">

다음 일요일, 이 슬라이드는 새로운 한 주의 소식으로 갱신됩니다

</div>

---

# 출처 · 더 보기

<div class="cards">

<a class="card video" href="https://www.youtube.com/results?search_query=Gemini+Agent+enterprise+Google+Cloud">
<span class="outlet">▶ YOUTUBE</span>
<span class="head">Gemini Agent 발표 영상 모아보기</span>
<span class="link">youtube.com</span>
</a>

<a class="card" href="https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/">
<span class="outlet">TECHCRUNCH</span>
<span class="head">구글, 기업용 Gemini 에이전트 공개 (10/8)</span>
<span class="link">techcrunch.com</span>
</a>

<a class="card" href="https://aiweekly.co/alerts/introducing-claude-haiku-55">
<span class="outlet">AI WEEKLY</span>
<span class="head">Claude Haiku 5.5 — 값 75% 인하 (10/7)</span>
<span class="link">aiweekly.co</span>
</a>

<a class="card" href="https://aidapted.ro/en/articles/ai-news-october-9-2026">
<span class="outlet">AIDAPTED</span>
<span class="head">AI 뉴스 정리 — 10월 9일</span>
<span class="link">aidapted.ro</span>
</a>

<a class="card" href="https://aiagentstore.ai/ai-agent-news/this-week">
<span class="outlet">AI AGENT STORE</span>
<span class="head">이번 주 에이전트 뉴스 모아보기</span>
<span class="link">aiagentstore.ai</span>
</a>

</div>
