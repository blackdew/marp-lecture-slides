---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-11-22 | 범위: 2026년 11월 (3주차) -->

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

갱신 2026-11-22 · 범위: 2026년 11월 누적 (3주차)

</div>

---

# 11월 한눈에

<div class="big">

AI 팀원이 상품이 되고, 최상위 모델은 더 싸지고, 안전장치가 필수가 된 달

</div>

- 11/7 Perplexity Teammates — 역할을 맡아 계속 일하는 AI 팀원
- 11/17~18 GPT-6.2·Gemini 4 Neon — 최상위급 모델이 이틀 사이 2종
- 11/19 Gemini for Mac — AI가 내 컴퓨터를 대신 조작
- 11/19 Anthropic 상장 — 약 810억 달러 조달
- 현실 — 'AI가 큰 가치를 줬다'는 CIO는 13% (가트너)

<div class="note">

11월 3주차 기준 — 매주 일요일 내용이 쌓입니다 (11/8~11/14 주간은 상세 반영하지 않음)

</div>

---

# 11월의 모델 — 싸진 최상위, 늘어난 전문 모델

| 무엇 | 날짜 | 핵심 한 줄 |
|---|---|---|
| GPT-6 Cyber (OpenAI) | 11/5 | 보안 전용, 리눅스 취약점 948개 발견 보도 |
| Inkling 2 Small·Hy4 등 | 11/3~5 | 작고 값싼 모델, 화면 보고 컴퓨터 조작 |
| Qwen4-Max (알리바바) | 11/16 | 입력 1.5달러대, 맥락 100만 토큰 |
| GPT-6.2 Astra·Sol (OpenAI) | 11/17 | Astra 값 20%↓, 실무 평가 +5~6점 |
| Gemini 4 Neon (Google) | 11/18 | 작업당 비용 32%↓, 코딩 에이전트 평가 1위 |

<div class="note">

흐름 — 월초엔 용도별 전문 모델, 월 중순엔 최상위 모델의 가격 인하 경쟁

</div>

<div class="src">

출처: [The Hacker News](https://thehackernews.com/2026/11/openai-launches-gpt-6-cyber-after-ai.html) · [BenchLM — 11월 신모델](https://benchlm.ai/model-updates/releases/november-2026) · [llm-stats — Qwen4-Max](https://llm-stats.com/blog/research/qwen4-max-launch) · [OpenAI](https://openai.com/id-ID/index/introducing-gpt-6-2-astra-sol/) · [Google 블로그](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

</div>

---

# 모델 — 무엇이 좋아졌나

- GPT-6.2 Astra — 전작보다 값 20%↓, 출력은 22% 줄이고 실무 평가 +6점
- GPT-6.2 Sol — 값은 그대로, 실무 평가 +5점
- Gemini 4 Neon — 같은 일을 전작(Carbon)보다 32% 싸게, 4단계로 '생각 깊이' 조절
- 단, 사용자 반응은 엇갈림 — "긴 작업 중 자꾸 멈추고 되묻는다"
- 12월 1일부터 일부 Gemini 4 모델 값 2배 인상 예정

<div class="highlight">

점수는 회사 발표 기준 — 내 업무에 맞는지는 직접 시험해 봐야 한다

</div>

<div class="src">

출처: [OpenAI](https://openai.com/id-ID/index/introducing-gpt-6-2-astra-sol/) · [Wccftech](https://wccftech.com/openais-gpt-6-2-astra-becomes-the-first-model-to-achieve-a-100-score-on-arc-agi-3-while-being-8x-cheaper-than-anthropics-fable-5-2-but-actual-users-are-not-impressed/?type=AI) · [ITdaily](https://itdaily.com/news/software/google-gemini-4-neon/)

</div>

---

# 새 에이전트 — 맡기고, 내 컴퓨터까지 맡긴다

| 무엇 | 날짜 | 무엇을 대신 해주나 |
|---|---|---|
| Perplexity Teammates | 11/7 | 역할별 에이전트 동시 가동, 슬랙 호출 |
| AWS Kiro 봇 | 11/5 | 기억하며 정기 개발 작업 반복 |
| DigitalOcean Cuttlefish | 11/5 | 아이폰으로 도구 사용 승인·중단 |
| Gemini for Mac | 11/19 | 파일 정리·양식 입력·앱 조작 (미국) |
| MS Copilot Autopilot | 11/18 | 자기 회사 계정을 가진 자율 에이전트 (보도) |

<div class="note">

'맡기는 기능'과 '미리보고 승인·중단하는 기능'이 한 세트로 나온다

</div>

<div class="src">

출처: [PCMag](https://au.pcmag.com/ai/120788/perplexity-teammates-ai-agent-help-you-work) · [VentureBeat — Kiro](https://venturebeat.com/technology/aws-launches-agentic-ai-kiro-bots-with-memory-and-support-for-recurring-development-jobs) · [AIthority — Cuttlefish](https://aithority.com/it-and-devops/cloud/digitalocean-launches-cuttlefish-to-supervise-ai-agents-from-anywhere-with-box-as-launch-partner) · [TechCrunch — Gemini for Mac](https://techcrunch.com/2026/11/19/google-gives-gemini-the-ability-to-use-your-mac-for-you/) · [Emergent](https://emergent.sh/news/microsoft-copilot-autopilot-launches-agent)

</div>

---

# 도입 현실 — 돈은 몰리고, 성과는 증명 중

- Anthropic 상장 (11/19) — 주당 83달러, 기업가치 약 1.5조 달러
- 인수 — Five9의 Level AI(약 3.25억 달러), Sierra의 Anon, Meta의 Conductor
- 금융사 59%가 멀티 에이전트 시범·도입, 전사 운영은 10% (Capgemini)
- 가트너 CIO 설문 — 큰 가치를 얻었다는 응답 13%
- 성과 사례 — OpenAI 코딩 에이전트, 3개월간 속도 저하 600여 건 원인 규명 (정확도 70%)

<div class="highlight">

투자는 활발한데 '성과 측정'이 병목 — 'AI가 찾고 사람이 확인'하는 곳이 먼저 성과를 낸다

</div>

<div class="src">

출처: [ABC7](https://abc7.com/story/what-know-before-anthropic-goes-public/20054746/) · [CXO Digital Pulse](https://www.cxodigitalpulse.com/five9-agrees-to-acquire-level-ai-for-approximately-325-million) · [Capgemini 보도자료](https://www.globenewswire.com/news-release/2026/11/05/3396012/0/en/financial-institutions-accelerate-transition-to-multi-agent-ai-in-drive-for-bottom-line-value.html) · [Gartner 설문 보도](https://globenewswire.com/news-release/2026/11/06/3397758/0/en/ai-deployment-only-13-of-cios-say-ai-has-delivered-significant-value.html) · [OpenAI](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/)

</div>

---

# 안전 — 감시·차단 제품과 실제 사고

- 월초 — CrowdStrike 'AI 킬 스위치', Sysdig·Cloudflare 에이전트별 권한 관리
- Meta Muse — 다른 사용자 정보가 보였다는 직원 제보 (보도, Meta는 시험판 문제라 설명)
- EU 집행위 — AI 해킹 도구가 쓰인 것으로 보이는 공격에 급여 시스템 중단 (보도)
- OpenAI 의료 에이전트 — 접속 앱 제한·관리자 승인 단계 도입
- 미 상원 — 상장사 AI 공시 강화 법안 발의

<div class="highlight">

에이전트 수가 늘수록 '기록하고 멈출 수 있는가'가 도입 조건이 된다

</div>

<div class="src">

출처: [SecurityWeek](https://www.securityweek.com/sysdig-adds-runtime-security-and-governance-for-ai-agents) · [TechCrunch — Muse](https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/) · [The Register](https://www.theregister.com/cyber-crime/2026/11/19/european-commission-scrambles-to-contain-ai-assisted-cyberattack/5311103) · [BERI](https://www.beri.net/article/chatgpt-for-healthcare-computer-use-agents-20-plugins-availity-oracle-hdi-healthadminbench-baa-admin-approvals-ehr)

</div>

---

# 11월, 여기까지 (3주차)

<div class="big">

11월 요약 — 더 싸진 AI가 내 컴퓨터까지 맡고, 안전장치는 필수품이 된다

</div>

- 최상위 모델이 한 주에 2종, 값은 더 내려갔다
- 역할을 맡는 AI 팀원, 컴퓨터를 대신 쓰는 에이전트가 구독 상품이 됐다
- AI 회사 상장 등 돈은 몰리지만 큰 가치를 얻은 기업은 13%
- 정보 노출·AI 해킹 사고가 실제로 보도되기 시작했다

<div class="note">

다음은 '지난주' — 가장 최근 일주일을 본다

</div>

---

# 출처 · 영상으로 더 보기

<div class="cards">

<a class="card video" href="https://www.youtube.com/results?search_query=GPT-6.2+Astra">
<span class="outlet">▶ YOUTUBE</span>
<span class="head">GPT-6.2 Astra 영상 모아보기</span>
<span class="link">youtube.com</span>
</a>

<a class="card" href="https://openai.com/id-ID/index/introducing-gpt-6-2-astra-sol/">
<span class="outlet">OPENAI</span>
<span class="head">GPT-6.2 Astra·Sol 공개 (11/17)</span>
<span class="link">openai.com</span>
</a>

<a class="card" href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/">
<span class="outlet">GOOGLE</span>
<span class="head">Gemini 4 Neon 공개 (11/18)</span>
<span class="link">blog.google</span>
</a>

<a class="card" href="https://au.pcmag.com/ai/120788/perplexity-teammates-ai-agent-help-you-work">
<span class="outlet">PCMAG</span>
<span class="head">Perplexity Teammates 출시 (11/7)</span>
<span class="link">pcmag.com</span>
</a>

<a class="card" href="https://globenewswire.com/news-release/2026/11/06/3397758/0/en/ai-deployment-only-13-of-cios-say-ai-has-delivered-significant-value.html">
<span class="outlet">GLOBENEWSWIRE</span>
<span class="head">가트너 — CIO 13%만 '큰 가치' (11/6)</span>
<span class="link">globenewswire.com</span>
</a>

<a class="card" href="https://abc7.com/story/what-know-before-anthropic-goes-public/20054746/">
<span class="outlet">ABC7</span>
<span class="head">Anthropic 상장, 알아둘 것 (11/19)</span>
<span class="link">abc7.com</span>
</a>

</div>
