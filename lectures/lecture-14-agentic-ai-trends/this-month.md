---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-10-11 | 범위: 2026년 10월 (1~2주차) -->

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

갱신 2026-10-11 · 범위: 2026년 10월 누적 (2주차)

</div>

---

# 10월 한눈에

<div class="big">

'성능은 그대로, 값은 5분의 1' — 그리고 에이전트가 팀원이 된 달

</div>

- 9월 말~10월 초 — 상위 모델 3종이 값을 크게 낮춰 재출시
- 10/7 — 가장 작은 모델 Claude Haiku 5.5, 값 75%↓
- 10/8 — Google Gemini Agent, 이메일 주소를 가진 AI 팀원
- 현실 — 기업 85%가 실험 중, 운영은 5%

<div class="note">

10월 2주차 기준 — 매주 일요일 내용이 쌓입니다

</div>

---

# 10월의 모델 판도

| 무엇 | 날짜 | 핵심 한 줄 |
|---|---|---|
| Claude Sonnet 5.5 | 9/28 | 30%+ 빨라짐, 값은 그대로 (입력 2달러) |
| GPT-6.1 Sol (OpenAI) | 9/30 | 최상위 Astra에 근접, 값은 5분의 1 |
| Gemini 4 Argon (Google) | 9/30 | 제한 공개, 한 번에 최대 100만 토큰 출력 |
| Claude Haiku 5.5 | 10/7 | 가장 작은 모델 — 값 75%↓ |
| Kimi K2.6 (Moonshot) | 10/5 | 무료 공개, 에이전트 1,000개 동시 운용 |

<div class="note">

흐름 — 최상위 성능을 '일상 가격'으로 내려보내는 경쟁이 본격화

</div>

<div class="src">

출처: [AI Weekly — Sonnet 5.5](https://aiweekly.co/alerts/anthropic-ships-claude-sonnet-55-30-faster-with-706-on-terminal-bench-40) · [ProPakistani — GPT-6.1 Sol](https://propakistani.pk/2026/09/30/gpt-6-1-sol-brings-astra-level-performance-at-5x-lower-cost/) · [DEV — Gemini 4 Argon](https://dev.to/hassann/what-is-gemini-4-argon-18b5)

</div>

---

# 무엇이 좋아졌나 — 숫자로 보기

- GPT-6.1 Sol — 입력 2달러·출력 10달러 (Astra는 10·50달러)
- 코딩 시험은 Astra와 동률, 비용은 약 5분의 1
- 규칙을 우회하려던 비율 64.4% → 23.5%로 감소
- Sonnet 5.5 — 터미널 작업 시험 10.3% → 70.6%
- Haiku 5.5 — 컴퓨터 조작 시험 15.7% → 72.4%

<div class="note">

대부분 회사 발표 수치 — 같은 값으로 맡길 수 있는 일의 크기가 또 커졌다는 방향이 핵심

</div>

<div class="src">

출처: [ProPakistani](https://propakistani.pk/2026/09/30/gpt-6-1-sol-brings-astra-level-performance-at-5x-lower-cost/) · [AI Weekly — Sonnet 5.5](https://aiweekly.co/alerts/anthropic-ships-claude-sonnet-55-30-faster-with-706-on-terminal-bench-40) · [AI Weekly — Haiku 5.5](https://aiweekly.co/alerts/introducing-claude-haiku-55)

</div>

---

# 새 에이전트 — 팀원처럼 초대한다

| 무엇 | 날짜 | 무엇을 대신 해주나 |
|---|---|---|
| Gemini Agent | 10/8 | 목표를 받아 계획·실행, 자기 이메일 계정 보유 |
| Oracle Fusion Claw | 10/5 | 회계·구매(ERP) 프로그램 안에서 에이전트 조율 |
| Microsoft Autopilot | 10/5 | 며칠씩 혼자 도는 에이전트, 직원 1인 1개 구상 |
| TikTok 쇼핑 도우미 | 10/5 | 앱 안에서 추천부터 원클릭 결제까지 |
| Ironclad Agent | 10/9 | 계약 이력을 학습해 계약 업무 보조 |

<div class="note">

'AI 창'에 가는 단계를 지나, 일하는 곳에 AI 동료를 앉히는 단계

</div>

<div class="src">

출처: [TechCrunch (10/8)](https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 도입 현실 — 말은 많고 운영은 적다

- 대기업 85%가 에이전트 실험 중
- 실제 운영에 투입한 곳은 5%, 시범에서 키운 곳은 11~14%
- HackerRank 면접 에이전트 — 시범 중 약 50만 건 진행
- Gemini Enterprise — 포천 100대 기업의 약 90%가 사용 (구글)
- 가트너 — 2027년까지 에이전트 프로젝트 40% 이상 중단 전망

<div class="highlight">

작게 시작해 숫자로 확인한 곳만 규모를 키우고 있다

</div>

<div class="src">

출처: [AI Agent Store — 주간 뉴스](https://aiagentstore.ai/ai-agent-news/this-week) · [TechCrunch (10/8)](https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/)

</div>

---

# 안전 — 신원 확인과 사고 보고

- Amazon, Meta Muse 차단 — 대리 쇼핑 때 신원을 밝히지 않았다는 이유
- Anthropic, 모델의 의도 밖 행동 4유형 보고서 공개 (10/9)
- 필라델피아 경찰, 허위 살인 제보가 AI 모델발로 확인
- 백악관 — AI 기업의 사고 보고·시정을 국가 안보 문제로 규정

<div class="highlight">

에이전트도 '누가, 누구를 대신해' 일하는지 밝히는 규칙이 필요해졌다

</div>

<div class="src">

출처: [AI News 10/9](https://aidapted.ro/en/articles/ai-news-october-9-2026) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 10월, 여기까지 (2주차)

<div class="big">

10월 요약 — 싸진 최상위 모델, 팀원이 된 에이전트

</div>

- 상위 모델이 5분의 1 값으로, 작은 모델도 업무를 맡을 만큼 성장
- 새 경쟁 축은 '조직 안에 에이전트를 앉히는 방식'
- 쇼핑·결제 대행이 늘며 신원 확인 규칙 충돌이 시작
- 운영 투입은 아직 5% — 지금 시작하는 쪽이 앞선다

<div class="note">

다음은 '지난주' — 가장 최근 일주일을 본다

</div>

---

# 출처 · 영상으로 더 보기

<div class="cards">

<a class="card video" href="https://www.youtube.com/results?search_query=GPT-6.1+Sol">
<span class="outlet">▶ YOUTUBE</span>
<span class="head">GPT-6.1 Sol 정리 — 값은 5분의 1</span>
<span class="link">youtube.com</span>
</a>

<a class="card" href="https://propakistani.pk/2026/09/30/gpt-6-1-sol-brings-astra-level-performance-at-5x-lower-cost/">
<span class="outlet">PROPAKISTANI</span>
<span class="head">GPT-6.1 Sol, 5분의 1 비용 (9/30)</span>
<span class="link">propakistani.pk</span>
</a>

<a class="card" href="https://aiweekly.co/alerts/anthropic-ships-claude-sonnet-55-30-faster-with-706-on-terminal-bench-40">
<span class="outlet">AI WEEKLY</span>
<span class="head">Claude Sonnet 5.5 — 30% 빨라짐 (9/28)</span>
<span class="link">aiweekly.co</span>
</a>

<a class="card" href="https://aiweekly.co/alerts/introducing-claude-haiku-55">
<span class="outlet">AI WEEKLY</span>
<span class="head">Claude Haiku 5.5 — 값 75% 인하 (10/7)</span>
<span class="link">aiweekly.co</span>
</a>

<a class="card" href="https://techcrunch.com/2026/10/08/google-brings-agentic-ai-to-gemini-starting-with-businesses/">
<span class="outlet">TECHCRUNCH</span>
<span class="head">구글, 기업용 Gemini 에이전트 (10/8)</span>
<span class="link">techcrunch.com</span>
</a>

<a class="card" href="https://aiagentstore.ai/ai-agent-news/this-week">
<span class="outlet">AI AGENT STORE</span>
<span class="head">이번 주 에이전트 뉴스 모아보기</span>
<span class="link">aiagentstore.ai</span>
</a>

</div>
