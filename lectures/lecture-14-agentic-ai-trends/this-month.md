---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-11-08 | 범위: 2026년 11월 (1주차) -->

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

## 이번달 — 2026년 11월

<div class="lead-meta">

갱신 2026-11-08 · 범위: 2026년 11월 누적 (1주차)

</div>

---

# 11월 한눈에

<div class="big">

'AI 팀원'이 상품이 되고, '끄는 버튼'도 함께 팔리는 달

</div>

- 11/7 Perplexity Teammates — 역할을 맡아 계속 일하는 AI 팀원 (월 200달러대)
- 11/5 GPT-6 Cyber — 보안 점검 전용 모델
- 11/3~5 CrowdStrike 등 — 에이전트 감시·킬 스위치 제품 잇따라
- 현실 — 가트너 설문에서 'AI가 큰 가치를 줬다'는 CIO 13%

<div class="note">

11월 1주차 기준 — 매주 일요일 내용이 쌓입니다 (10월 내용은 올해 슬라이드로 통합)

</div>

---

# 11월의 모델 — 전문화·소형화

| 무엇 | 날짜 | 핵심 한 줄 |
|---|---|---|
| GPT-6 Cyber (OpenAI) | 11/5 | 보안 전용, 리눅스 취약점 948개 발견 보도 |
| Inkling 2 Small | 11/5 | 전체 594B 중 17B만 사용, 이미지 입력 |
| Hy4 (텐센트) | 11/3~4 | 화면을 보고 컴퓨터 조작 |
| SWE-2 Flash (Cognition) | 11/4 | 코딩 에이전트용 빠른 모델 |
| Gemini Omni 1.2 Flash | 11/6 | 영상 15초, 값 약 30%↓ |

<div class="note">

흐름 — 범용 '최강'보다 용도별 전문 모델과 값싼 모델이 늘어난다

</div>

<div class="src">

출처: [The Hacker News](https://thehackernews.com/2026/11/openai-launches-gpt-6-cyber-after-ai.html) · [BenchLM — 11월 신모델](https://benchlm.ai/model-updates/releases/november-2026) · [Opper](https://opper.ai/model-releases) · [DEV — 11/7 요약](https://dev.to/hiroki-ii-ai/ai-daily-digest-november-7-2026-ai-cracks-legacy-rsa-gemini-omni-gets-longer-clips-first-3f6p)

</div>

---

# 새 에이전트 — 맡기고 자리를 비운다

| 무엇 | 날짜 | 무엇을 대신 해주나 |
|---|---|---|
| Perplexity Teammates | 11/7 | 역할별 에이전트 동시 가동, 슬랙 호출 |
| Meta Muse | 11/6~7 | 음성 대화 아바타, 프로젝트 공간 |
| AWS Kiro 봇 | 11/5 | 기억하며 정기 개발 작업 반복 |
| DigitalOcean Cuttlefish | 11/5 | 아이폰으로 도구 사용 승인·중단 |
| Claude 개인 재무 | 11/5 | 소비 내역 분석 (미국·시범) |

<div class="note">

'맡기는 기능'과 '멀리서 승인·중단하는 기능'이 한 세트로 나온다

</div>

<div class="src">

출처: [PCMag](https://au.pcmag.com/ai/120788/perplexity-teammates-ai-agent-help-you-work) · [VentureBeat — Kiro](https://venturebeat.com/technology/aws-launches-agentic-ai-kiro-bots-with-memory-and-support-for-recurring-development-jobs) · [AIthority — Cuttlefish](https://aithority.com/it-and-devops/cloud/digitalocean-launches-cuttlefish-to-supervise-ai-agents-from-anywhere-with-box-as-launch-partner) · [TechCrunch](https://techcrunch.com/2026/11/05/claude-can-now-analyze-your-spending-with-its-new-personal-finance-tool/)

</div>

---

# 도입 현실 — 사고팔고, 그러나 성과는 아직

- Five9 — Level AI 약 3억 2,500만 달러 인수 합의 (11/5)
- Sierra — 웹 조작 기술 Anon 인수, Meta — 코딩 에이전트 업체 Conductor 인수
- 금융사 59%가 멀티 에이전트 시범·도입, 전사 운영은 10%
- 가트너 CIO 설문 — 큰 가치를 얻었다는 응답 13%
- 약 절반이 에이전트의 ROI를 꾸준히 증명하지 못함

<div class="highlight">

인수·투자는 활발한데 '성과 측정'이 병목이다

</div>

<div class="src">

출처: [CXO Digital Pulse](https://www.cxodigitalpulse.com/five9-agrees-to-acquire-level-ai-for-approximately-325-million) · [Unite.AI — Sierra](https://www.unite.ai/sierra-acquires-anon-to-help-ai-agents-complete-web-workflows) · [Capgemini 보도자료](https://www.globenewswire.com/news-release/2026/11/05/3396012/0/en/financial-institutions-accelerate-transition-to-multi-agent-ai-in-drive-for-bottom-line-value.html) · [Gartner 설문 보도](https://globenewswire.com/news-release/2026/11/06/3397758/0/en/ai-deployment-only-13-of-cios-say-ai-has-delivered-significant-value.html)

</div>

---

# 안전 — 감시와 킬 스위치

- CrowdStrike — AI 킬 스위치(끄기·네트워크 차단·재실행 방지)와 이상 행동 탐지
- Sysdig·Cloudflare — 에이전트별 접근 권한과 활동 분석
- 연구 보고 — 악성 브라우저 확장이 Claude 원격 지시 기능을 악용 가능
- 딥마인드 — AI가 옛 1024비트 RSA 약점 발견 (2048비트는 영향 없음)

<div class="highlight">

에이전트 수가 늘수록 '기록하고 멈출 수 있는가'가 도입 조건이 된다

</div>

<div class="src">

출처: [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) · [SecurityWeek](https://www.securityweek.com/sysdig-adds-runtime-security-and-governance-for-ai-agents) · [The Hacker News](https://thehackernews.com/2026/11/malicious-browser-extensions-could-use.html) · [Crypto Briefing](https://cryptobriefing.com/google-deepmind-ai-rsa-1024-bit-weaknesses)

</div>

---

# 11월, 여기까지 (1주차)

<div class="big">

11월 요약 — AI 팀원은 상품이 되고, 안전장치는 필수품이 된다

</div>

- 보안·영상 등 용도별 전문 모델이 늘었다
- 역할을 맡아 계속 일하는 에이전트가 월 구독 상품이 됐다
- 인수합병은 활발하나 큰 가치를 얻은 기업은 13%
- 킬 스위치·권한 관리 제품이 쏟아진다

<div class="note">

다음은 '지난주' — 가장 최근 일주일을 본다

</div>

---

# 출처 · 영상으로 더 보기

<div class="cards">

<a class="card video" href="https://www.youtube.com/results?search_query=Perplexity+Teammates">
<span class="outlet">▶ YOUTUBE</span>
<span class="head">Perplexity Teammates 영상 모아보기</span>
<span class="link">youtube.com</span>
</a>

<a class="card" href="https://au.pcmag.com/ai/120788/perplexity-teammates-ai-agent-help-you-work">
<span class="outlet">PCMAG</span>
<span class="head">Perplexity Teammates 출시 (11/7)</span>
<span class="link">pcmag.com</span>
</a>

<a class="card" href="https://thehackernews.com/2026/11/openai-launches-gpt-6-cyber-after-ai.html">
<span class="outlet">THE HACKER NEWS</span>
<span class="head">OpenAI GPT-6 Cyber (11/5)</span>
<span class="link">thehackernews.com</span>
</a>

<a class="card" href="https://venturebeat.com/technology/aws-launches-agentic-ai-kiro-bots-with-memory-and-support-for-recurring-development-jobs">
<span class="outlet">VENTUREBEAT</span>
<span class="head">AWS Kiro 봇 — 기억과 반복 작업 (11/5)</span>
<span class="link">venturebeat.com</span>
</a>

<a class="card" href="https://www.globenewswire.com/news-release/2026/11/05/3396012/0/en/financial-institutions-accelerate-transition-to-multi-agent-ai-in-drive-for-bottom-line-value.html">
<span class="outlet">GLOBENEWSWIRE</span>
<span class="head">금융사 멀티 에이전트 설문 (11/5)</span>
<span class="link">globenewswire.com</span>
</a>

<a class="card" href="https://aiagentstore.ai/ai-agent-news/this-week">
<span class="outlet">AI AGENT STORE</span>
<span class="head">이번 주 에이전트 뉴스 모아보기</span>
<span class="link">aiagentstore.ai</span>
</a>

</div>
