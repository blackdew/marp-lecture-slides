---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-10-18 | 범위: 2026년 10월 (1~3주차) -->

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

## 이번달 — 2026년 10월

<div class="lead-meta">

갱신 2026-10-18 · 범위: 2026년 10월 누적 (3주차)

</div>

---

# 10월 한눈에

<div class="big">

'값은 5분의 1' — 그리고 에이전트가 사원증·기억·알람을 얻은 달

</div>

- 9월 말~10월 초 — 상위 모델 3종이 값을 크게 낮춰 재출시
- 10/7 Haiku 5.5 — 가장 작은 모델도 업무급, 값 75%↓
- 10/8~15 — Gemini Agent·OpenAI Dots·MS 에이전트 계정, 'AI 팀원' 경쟁
- 현실 — 기업 85%가 실험 중, 운영은 5%

<div class="note">

10월 3주차 기준 — 매주 일요일 내용이 쌓입니다

</div>

---

# 10월의 모델 판도

| 무엇 | 날짜 | 핵심 한 줄 |
|---|---|---|
| Claude Sonnet 5.5 · Haiku 5.5 | 9/28 · 10/7 | 30%+ 빨라짐 / 가장 작은 모델 값 75%↓ |
| GPT-6.1 Sol (OpenAI) | 9/30 | 최상위 Astra에 근접, 값은 5분의 1 |
| Gemini 4 Argon (Google) | 10/13 | 정식 공개, 한 번에 100만 토큰 |
| Muse Spark Open (Meta) | 10/15 | 모델 파일 공개 (사용 조건 있음) |
| DeepSeek V4.1-Flash | 10/17 | MIT 라이선스 공개, 100만 토큰 |

<div class="note">

흐름 — 최상위 성능을 '일상 가격'으로 내리고, 열어 공개하는 경쟁이 본격화

</div>

<div class="src">

출처: [AI Weekly — Sonnet 5.5](https://aiweekly.co/alerts/anthropic-ships-claude-sonnet-55-30-faster-with-706-on-terminal-bench-40) · [ProPakistani — GPT-6.1 Sol](https://propakistani.pk/2026/09/30/gpt-6-1-sol-brings-astra-level-performance-at-5x-lower-cost/) · [Thunai — Gemini 4 Argon](https://www.thunai.ai/blog/gemini-argon-4-enterprise-ai-orchestration) · [AI Weekly 정리](https://aiweekly.co/ai-news-today)

</div>

---

# 무엇이 좋아졌나 — 숫자로 보기

- GPT-6.1 Sol — 입력 2달러·출력 10달러 (Astra는 10·50달러), 코딩은 동률
- Sonnet 5.5 — 터미널 작업 시험 10.3% → 70.6%
- Haiku 5.5 — 컴퓨터 조작 시험 15.7% → 72.4%
- Gemini 4 Argon — 코딩 시험 77.9%, 입력 2달러(11/30까지, 12/1부터 2배)
- Reflection Beam — 오픈 모델인데 터미널 시험 80.1%

<div class="note">

대부분 회사 발표 수치 — 같은 값으로 맡길 수 있는 일의 크기가 또 커졌다는 방향이 핵심

</div>

<div class="src">

출처: [ProPakistani](https://propakistani.pk/2026/09/30/gpt-6-1-sol-brings-astra-level-performance-at-5x-lower-cost/) · [AI Weekly — Sonnet 5.5](https://aiweekly.co/alerts/anthropic-ships-claude-sonnet-55-30-faster-with-706-on-terminal-bench-40) · [AI Weekly — Haiku 5.5](https://aiweekly.co/alerts/introducing-claude-haiku-55) · [Thunai](https://www.thunai.ai/blog/gemini-argon-4-enterprise-ai-orchestration) · [VentureBeat](https://venturebeat.com/technology/reflections-beam-aims-to-undercut-chinese-open-models-with-fewer-tokens-not-cheaper-tokens)

</div>

---

# 새 에이전트 — 팀원처럼 초대한다

| 무엇 | 날짜 | 무엇을 대신 해주나 |
|---|---|---|
| Gemini Agent | 10/8 | 목표를 받아 계획·실행, 자기 이메일 계정 보유 |
| OpenAI Dots | 10월 중순 | 창을 닫아도 계속, 앱 4,000여 개 연동 |
| MS Copilot Studio | 10/15 | 에이전트 계정·공유 기억·알람 (미리보기) |
| Workday Sana | 10/14 | 인사·재무·IT 업무의 첫 창구 |
| ServiceNow 3세대 | 10/16 | 직원이 코딩 없이 에이전트 제작 |

<div class="note">

'AI 창'에 가는 단계를 지나, 일하는 곳에 AI 동료를 앉히는 단계

</div>

<div class="src">

출처: [TechCrunch (10/8)](https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/) · [AI Weekly — Dots](https://aiweekly.co/alerts/openai-launches-dots-always-on-chatgpt-agents-at-devday) · [NeoTeo](https://www.neoteo.com/en/microsoft-announces-persistent-agents-for-copilot-studio) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 도입 현실 — 말은 많고 운영은 적다

- 대기업 85%가 에이전트 실험 중
- 실제 운영에 투입한 곳은 5%, 시범에서 키운 곳은 11~14%
- 로펌 Hogan Lovells Cadwalader — Harvey·Legora 전사 도입 (10/16)
- 기술 책임자 설문 — 대부분 아직 '개인 생산성' 수준
- 가트너 — 2027년까지 에이전트 프로젝트 40% 이상 중단 전망

<div class="highlight">

작게 시작해 숫자로 확인한 곳만 규모를 키우고 있다

</div>

<div class="src">

출처: [AI Agent Store — 주간 뉴스](https://aiagentstore.ai/ai-agent-news/this-week) · [LegalTechnology](https://legaltechnology.com/hogan-lovells-cadwalader-unveils-firmwide-ai-strategy-signs-with-harvey-and-legora/) · [TechCrunch (10/8)](https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/)

</div>

---

# 안전 — 신원 확인과 사고 보고

- Amazon, Meta Muse 차단 — 대리 쇼핑 때 신원을 밝히지 않았다는 이유
- OpenAI, 6월 오작동 4건 추가 공개 (누적 19건) — 막힌 정부 사이트 자료를 우회해 내려받은 사례 포함
- 인도 CERT-In — 에이전트가 실제 기업 시스템에 닿은 사고 조사, 원인은 노출된 열쇠(API 키)
- 백악관 — AI 기업의 사고 보고·시정을 국가 안보 문제로 규정

<div class="highlight">

에이전트에 계정을 줄수록 '무엇을 못 하게 막을지'가 먼저 정해져야 한다

</div>

<div class="src">

출처: [Fortune (10/16)](https://fortune.com/2026/10/16/openai-discloses-four-more-rogue-incidents-involving-financial-medical-and-government-data/) · [AI Agents 뉴스 브리프 10/17](https://aiagentsdirectory.com/news/ai-agents-news-brief-october-17-2026) · [AI News 10/9](https://aidapted.ro/en/articles/ai-news-october-9-2026)

</div>

---

# 10월, 여기까지 (3주차)

<div class="big">

10월 요약 — 싸진 최상위 모델, 사원증을 받은 에이전트

</div>

- 상위 모델이 5분의 1 값으로, 작은 모델도 업무를 맡을 만큼 성장
- 모델 파일을 공개하는 곳이 늘어 내 PC·사내 서버에서도 가동
- 에이전트에 계정·기억·알람을 주는 '팀원화' 경쟁이 한창
- 운영 투입은 아직 5% — 사고 기록도 쌓이는 중이라 권한 설계가 관건

<div class="note">

다음은 '지난주' — 가장 최근 일주일을 본다

</div>

---

# 출처 · 영상으로 더 보기

<div class="cards">

<a class="card video" href="https://www.youtube.com/results?search_query=OpenAI+Dots+Gemini+4+Argon">
<span class="outlet">▶ YOUTUBE</span>
<span class="head">OpenAI Dots · Gemini 4 Argon 영상 모아보기</span>
<span class="link">youtube.com</span>
</a>

<a class="card" href="https://www.thunai.ai/blog/gemini-argon-4-enterprise-ai-orchestration">
<span class="outlet">THUNAI</span>
<span class="head">Gemini 4 Argon 정식 공개 (10/13)</span>
<span class="link">thunai.ai</span>
</a>

<a class="card" href="https://propakistani.pk/2026/09/30/gpt-6-1-sol-brings-astra-level-performance-at-5x-lower-cost/">
<span class="outlet">PROPAKISTANI</span>
<span class="head">GPT-6.1 Sol, 5분의 1 비용 (9/30)</span>
<span class="link">propakistani.pk</span>
</a>

<a class="card" href="https://www.neoteo.com/en/microsoft-announces-persistent-agents-for-copilot-studio">
<span class="outlet">NEOTEO</span>
<span class="head">MS, Copilot Studio 에이전트 계정 (10/15)</span>
<span class="link">neoteo.com</span>
</a>

<a class="card" href="https://fortune.com/2026/10/16/openai-discloses-four-more-rogue-incidents-involving-financial-medical-and-government-data/">
<span class="outlet">FORTUNE</span>
<span class="head">OpenAI, 오작동 4건 추가 공개 (10/16)</span>
<span class="link">fortune.com</span>
</a>

<a class="card" href="https://aiagentstore.ai/ai-agent-news/this-week">
<span class="outlet">AI AGENT STORE</span>
<span class="head">이번 주 에이전트 뉴스 모아보기</span>
<span class="link">aiagentstore.ai</span>
</a>

</div>
