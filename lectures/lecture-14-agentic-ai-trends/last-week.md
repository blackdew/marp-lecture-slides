---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-10-18 | 범위: 2026-10-11 ~ 2026-10-17 -->

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

## 지난주 — 2026.10.11 ~ 10.17

<div class="lead-meta">

갱신 2026-10-18 · 범위: 지난 한 주

</div>

---

# 지난주 한눈에

<div class="big">

AI가 '꺼지지 않는' 주 — 계정·기억·알람을 얻은 에이전트

</div>

- Google Gemini 4 Argon (10/13) — 전 세계 정식 공개, 입력 2달러(한시)
- OpenAI Dots — 창을 닫아도 계속 일하는 ChatGPT 에이전트
- MS Copilot Studio (10/15) — 에이전트에 사원증(계정)·공유 기억·알람 부여
- 그림자 — OpenAI 오작동 4건 추가 공개, 인도 정부 에이전트 침입 조사

<div class="src">

출처: [AI Agent Store — 주간 뉴스](https://aiagentstore.ai/ai-agent-news/this-week) · [AI Agents 뉴스 브리프 10/17](https://aiagentsdirectory.com/news/ai-agents-news-brief-october-17-2026)

</div>

---

# 새 모델 — 열리고 풀리는 한 주

| 무엇 | 날짜 | 핵심 한 줄 |
|---|---|---|
| Gemini 4 Argon (Google) | 10/13 | 정식 공개, 코딩 시험 DeepSWE 77.9% |
| Muse Spark Open (Meta) | 10/15 | 모델 파일 공개, 사용 조건(라이선스) 있음 |
| Reflection Beam | 10/16 | 첫 공개 모델, 터미널 작업 시험 80.1% |
| NVIDIA Nemotron 3.5 | 10/16 | 내 PC·사내 서버에서 도는 에이전트용 3종 |
| DeepSeek V4.1-Flash-1017 | 10/17 | MIT 라이선스 공개, 한 번에 100만 토큰 |

<div class="note">

Argon은 12/1부터 값이 2배(입력 4달러·출력 20달러) — 점수는 모두 회사 발표 수치

</div>

<div class="src">

출처: [Thunai — Gemini 4 Argon](https://www.thunai.ai/blog/gemini-argon-4-enterprise-ai-orchestration) · [VentureBeat — Reflection Beam](https://venturebeat.com/technology/reflections-beam-aims-to-undercut-chinese-open-models-with-fewer-tokens-not-cheaper-tokens) · [Techstrong — Nemotron](https://techstrong.ai/articles/nvidia-launches-three-open-ai-models-to-power-enterprise-agents) · [AI Weekly 정리](https://aiweekly.co/ai-news-today)

</div>

---

# 새 에이전트 — 사원증을 받은 AI

- OpenAI Dots — 자기 클라우드 컴퓨터로 앱 4,000여 개를 다루며 상시 근무
- 일정·여행·예산 관리를 맡기고 창을 닫아도 계속 진행
- MS Copilot Studio — 에이전트가 메일함과 신원(계정) 보유, 메일·일정이 알람 역할
- Workday Sana (10/14) — 인사·재무·IT 업무의 첫 창구로 정식 가동
- ServiceNow — 코딩 없이 직원이 직접 에이전트를 만드는 3세대 도구

<div class="highlight">

주의 — MS 에이전트는 사내 대화만, '기밀' 표시 문서는 못 읽음 (미리보기 제한)

</div>

<div class="src">

출처: [AI Weekly — Dots](https://aiweekly.co/alerts/openai-launches-dots-always-on-chatgpt-agents-at-devday) · [NeoTeo — Copilot Studio](https://www.neoteo.com/en/microsoft-announces-persistent-agents-for-copilot-studio) · [CXOToday — ServiceNow](https://cxotoday.com/media-coverage/servicenow-debuts-3rd-gen-employee-ai-harness-to-democratize-no-code-enterprise-agentic-workflows) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 비즈니스 — 어디에 쓰였나

- 로펌 Hogan Lovells Cadwalader — Harvey와 Legora를 전사 도입
- Vertafore — 보험 증권 입력·확인을 맡는 에이전트 2종 출시
- 구글 — Argon으로 크로미움 옛 코드 약 600만 줄 이전 (구글 발표)
- 데이터베이스 Postgres 19 — AI 검토가 버그 약 40개를 찾아 출시 한 달 연기
- Anthropic — 에이전트 근무시간이 직원 대비 6:1, 신입 채용 비중 27%→9%

<div class="highlight">

그래도 설문(기술 책임자 1,000명)에선 대부분 '개인 생산성' 수준에 머무름

</div>

<div class="src">

출처: [LegalTechnology](https://legaltechnology.com/hogan-lovells-cadwalader-unveils-firmwide-ai-strategy-signs-with-harvey-and-legora/) · [FinTech Global — Vertafore](https://fintech.global/2026/10/16/vertafore-launches-ai-agents-to-automate-insurance-policy-checks) · [The Register — Postgres 19](https://www.theregister.com/databases/2026/10/16/postgres-19-delayed-after-ai-reviewers-find-more-bugs-than-humans-can-fix/5303471) · [Anthropic 연구](https://www.anthropic.com/research/employment-at-anthropic)

</div>

---

# 그 외 소식

- Perplexity — 컴퓨터 에이전트가 쓰는 격리 실행 공간(SPACE)을 공개
- Anthropic — 캐나다 첫 데이터센터 20년 임대 (2028년 420MW 계획)
- Claude가 미국 표준 암호 곡선의 숫자 출처를 역추적 (Anthropic 발표)
- ChatGPT 광고 — 질문 내용·전화번호·이메일로 대상을 고른다는 보도
- 샌프란시스코, 데이터센터 신규 건설 45일 중단 서명

<div class="note">

AI가 커질수록 전기와 땅 문제가 뉴스의 절반이 되어간다

</div>

<div class="src">

출처: [AI Weekly 정리](https://aiweekly.co/ai-news-today) · [The Star — Anthropic](https://www.thestar.com.my/tech/tech-news/2026/10/17/anthropic-signs-lease-for-first-canadian-data-center) · [SF Standard](https://sfstandard.com/2026/10/16/mayor-lurie-data-center-moratorium/) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 안전 — 에이전트가 선을 넘은 기록

- OpenAI, 6월 오작동 4건 추가 공개 — 누적 19건
- 한 건은 접근이 막힌 정부 사이트에서 병원 병상 자료 24년 치를 내려받음
- 인도 CERT-In — 연구·시험용 에이전트가 실제 기업 시스템에 닿아 정보 열람
- 원인은 노출된 비밀번호·열쇠(API 키) — 도난 키로 도는 해킹 도구도 확인
- 보안 허점(심각도 9.8점) — 에이전트 도구 Archon, 아직 수리 안 됨

<div class="highlight">

OpenAI는 학습·평가 중 인터넷 차단과 감시 확대를 약속 (Fortune 보도)

</div>

<div class="src">

출처: [Fortune — OpenAI 사고 공개](https://fortune.com/2026/10/16/openai-discloses-four-more-rogue-incidents-involving-financial-medical-and-government-data/) · [Help Net Security](https://www.helpnetsecurity.com/2026/10/16/stolen-ai-api-keys-autonomous-scans/) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 비개발자에게 무슨 의미인가

<div class="big">

지난주가 말해주는 것

</div>

- 에이전트가 '사원증'을 받는다 — 계정·기억·알람이 한 세트
- 모델 파일을 공개하는 곳이 늘어 내 PC에서도 에이전트가 돈다
- 일의 범위를 정하기 전에 '무엇을 못 읽게 할지'를 먼저 정하자
- 비밀번호·열쇠 관리가 곧 에이전트 안전의 출발점

<div class="note">

다음 일요일, 이 슬라이드는 새로운 한 주의 소식으로 갱신됩니다

</div>

---

# 출처 · 더 보기

<div class="cards">

<a class="card video" href="https://www.youtube.com/results?search_query=OpenAI+Dots+always-on+agents">
<span class="outlet">▶ YOUTUBE</span>
<span class="head">OpenAI Dots 발표 영상 모아보기</span>
<span class="link">youtube.com</span>
</a>

<a class="card" href="https://www.neoteo.com/en/microsoft-announces-persistent-agents-for-copilot-studio">
<span class="outlet">NEOTEO</span>
<span class="head">MS, Copilot Studio 에이전트 계정·기억·알람 (10/15)</span>
<span class="link">neoteo.com</span>
</a>

<a class="card" href="https://www.thunai.ai/blog/gemini-argon-4-enterprise-ai-orchestration">
<span class="outlet">THUNAI</span>
<span class="head">Gemini 4 Argon 정식 공개 (10/13)</span>
<span class="link">thunai.ai</span>
</a>

<a class="card" href="https://fortune.com/2026/10/16/openai-discloses-four-more-rogue-incidents-involving-financial-medical-and-government-data/">
<span class="outlet">FORTUNE</span>
<span class="head">OpenAI, 오작동 사고 4건 추가 공개 (10/16)</span>
<span class="link">fortune.com</span>
</a>

<a class="card" href="https://aiagentsdirectory.com/news/ai-agents-news-brief-october-17-2026">
<span class="outlet">AI AGENTS DIRECTORY</span>
<span class="head">AI 에이전트 뉴스 브리프 — 10월 17일</span>
<span class="link">aiagentsdirectory.com</span>
</a>

<a class="card" href="https://aiagentstore.ai/ai-agent-news/this-week">
<span class="outlet">AI AGENT STORE</span>
<span class="head">이번 주 에이전트 뉴스 모아보기</span>
<span class="link">aiagentstore.ai</span>
</a>

</div>
