---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-11-08 | 범위: 2026-11-01 ~ 2026-11-07 -->

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

## 지난주 — 2026.11.1 ~ 11.7

<div class="lead-meta">

갱신 2026-11-08 · 범위: 지난 한 주

</div>

---

# 지난주 한눈에

<div class="big">

AI가 '팀원'이 되고, 곧바로 '감시 장치'도 따라붙은 주

</div>

- Perplexity Teammates (11/7) — 역할을 맡고 계속 일하는 AI 팀원
- Meta Muse — 목소리·아바타 대화와 프로젝트 공간 추가
- OpenAI GPT-6 Cyber (11/5) — 보안 취약점을 찾는 전용 모델
- CrowdStrike — 폭주하는 에이전트를 끄는 'AI 킬 스위치'

<div class="src">

출처: [AI Agents 브리프 11/7](https://aiagentsdirectory.com/news/ai-agents-directory-daily-brief-november-7-2026) · [AI Agents 브리프 11/6](https://aiagentsdirectory.com/news/ai-agents-news-brief-november-6-2026) · [AI Agent Store — 주간 뉴스](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 새 모델 — 작고 전문화된 모델의 주

| 무엇 | 날짜 | 핵심 한 줄 |
|---|---|---|
| GPT-6 Cyber (OpenAI) | 11/5 | 보안 점검 전용, 리눅스 취약점 948개 발견 보도 |
| Inkling 2 Small (Thinking Machines) | 11/5 | 필요한 부분만 쓰는 방식(전체 594B 중 17B), 이미지 입력 |
| Hy4 (텐센트) | 11/3~4 | 화면을 보고 컴퓨터를 조작하는 능력 추가 |
| SWE-2 Flash (Cognition) | 11/4 | 코딩 에이전트용 빠른 모델 |
| Gemini Omni 1.2 Flash | 11/6 | 영상 최대 15초, 이전 버전보다 값 약 30%↓ |

<div class="note">

Inkling 2 Small은 공개 모델 파일이 '다음 주' 예정이라는 2차 보도 — 사양은 회사 발표·제3자 집계 기준

</div>

<div class="src">

출처: [The Hacker News — GPT-6 Cyber](https://thehackernews.com/2026/11/openai-launches-gpt-6-cyber-after-ai.html) · [BenchLM — 11월 신모델](https://benchlm.ai/model-updates/releases/november-2026) · [Opper — 모델 출시 추적](https://opper.ai/model-releases) · [DEV — AI 일일 요약 11/7](https://dev.to/hiroki-ii-ai/ai-daily-digest-november-7-2026-ai-cracks-legacy-rsa-gemini-omni-gets-longer-clips-first-3f6p)

</div>

---

# 새 에이전트 — 일을 맡기고 자리를 비운다

- Perplexity Teammates — 역할을 정해 여러 개를 동시에 돌리고 슬랙으로 호출 (월 200달러 Max 요금제)
- Meta Muse — 목소리로 대화하는 아바타, 진행 중 프로젝트를 모아 보는 '스페이스'
- AWS Kiro 봇 — 기억을 갖고 정해진 주기로 개발 작업을 반복 수행
- DigitalOcean Cuttlefish — 에이전트의 도구 사용을 아이폰으로 승인·중단
- Anthropic — Claude에서 소비 내역을 분석하는 개인 재무 기능 (미국, 시범)

<div class="highlight">

핵심 — '맡기는 것'만큼 '멀리서 승인하고 멈추는 것'이 기능이 됐다

</div>

<div class="src">

출처: [PCMag — Perplexity Teammates](https://au.pcmag.com/ai/120788/perplexity-teammates-ai-agent-help-you-work) · [Datastudios — Muse 음성](https://www.datastudios.org/post/meta-muse-voice-conversations-expressive-avatars-us) · [VentureBeat — Kiro 봇](https://venturebeat.com/technology/aws-launches-agentic-ai-kiro-bots-with-memory-and-support-for-recurring-development-jobs) · [AIthority — Cuttlefish](https://aithority.com/it-and-devops/cloud/digitalocean-launches-cuttlefish-to-supervise-ai-agents-from-anywhere-with-box-as-launch-partner) · [TechCrunch — Claude 개인 재무](https://techcrunch.com/2026/11/05/claude-can-now-analyze-your-spending-with-its-new-personal-finance-tool/)

</div>

---

# 비즈니스 — 사고, 사들이고, 숫자로 확인

- Five9 — AI 고객응대 업체 Level AI를 약 3억 2,500만 달러에 인수 합의
- Sierra — 웹사이트 로그인·양식 입력을 대신하는 Anon 인수
- Meta — 코딩 에이전트 여러 개를 병렬로 돌리는 Conductor 인수
- 금융사 설문(Capgemini, 1,100명) — 59%가 여러 에이전트 시범·도입, 전사 운영 10%
- 약 절반은 에이전트의 성과(ROI)를 꾸준히 보여주지 못함

<div class="highlight">

가트너 CIO 설문(2,002명)에서도 'AI가 큰 가치를 줬다'는 응답은 13%

</div>

<div class="src">

출처: [CXO Digital Pulse — Five9](https://www.cxodigitalpulse.com/five9-agrees-to-acquire-level-ai-for-approximately-325-million) · [Unite.AI — Sierra](https://www.unite.ai/sierra-acquires-anon-to-help-ai-agents-complete-web-workflows) · [The Next Web — Meta](https://thenextweb.com/news/meta-acquires-conductor-ai-coding-agents-superintelligence-labs) · [Capgemini 보도자료](https://www.globenewswire.com/news-release/2026/11/05/3396012/0/en/financial-institutions-accelerate-transition-to-multi-agent-ai-in-drive-for-bottom-line-value.html) · [Gartner 설문 보도자료](https://globenewswire.com/news-release/2026/11/06/3397758/0/en/ai-deployment-only-13-of-cios-say-ai-has-delivered-significant-value.html)

</div>

---

# 그 외 소식

- GitHub Copilot — 웹·모바일·터미널·슬랙을 오가며 같은 작업을 이어가는 클라우드 세션
- Adobe — 마케팅·고객경험 에이전트를 Anthropic·구글·MS·OpenAI 플랫폼 안에서 제공 (11/4)
- Smartsheet — 상태 보고·후속 연락을 자동화하는 에이전트 추가
- 구글 딥마인드 — AI가 옛 1024비트 RSA 암호의 약점 2개 발견 (2048비트는 영향 없음)
- 아마존 — 일부 미국 고객은 문자로 알렉사에게 쇼핑을 맡김

<div class="note">

RSA 암호는 온라인 결제·로그인에 쓰이는 잠금 방식 — 지금 쓰는 키(2048비트 이상)는 안전하다는 설명

</div>

<div class="src">

출처: [Adobe 보도자료](https://news.adobe.com/news/2026/11/adobe-integrates-agentic-cx-enterprise-coworker-into-ai-platforms.html) · [City AM — Smartsheet](https://www.cityam.com/smartsheet-adds-new-ai-agents-integrations-and-security-advancements-at-engage-2026) · [Crypto Briefing — RSA](https://cryptobriefing.com/google-deepmind-ai-rsa-1024-bit-weaknesses) · [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 안전 — 끄는 버튼이 제품이 되다

- CrowdStrike 'AI 킬 스위치' — 실행 중인 에이전트를 끄고 네트워크를 끊고 재실행을 막음
- 같은 회사 — 규칙을 어기지 않아도 '평소와 다른 행동'을 잡아내는 탐지 기능
- Sysdig·Cloudflare — 에이전트별 접근 권한·활동 분석 출시
- 보안 연구 — 악성 브라우저 확장이 Claude 원격 지시 기능을 악용할 수 있음 (연구 보고)
- 팔로알토, 에이전트 열쇠 관리 업체 인수 협상 보도 (미확정)

<div class="highlight">

에이전트가 늘수록 '누가 무엇을 했는지 기록하고 멈출 수 있는가'가 선택 기준

</div>

<div class="src">

출처: [AI Agent Store](https://aiagentstore.ai/ai-agent-news/this-week) · [SecurityWeek — Sysdig](https://www.securityweek.com/sysdig-adds-runtime-security-and-governance-for-ai-agents) · [Unite.AI — Cloudflare](https://www.unite.ai/cloudflare-adds-personal-agent-analytics-and-per-agent-access-controls) · [The Hacker News — 악성 확장](https://thehackernews.com/2026/11/malicious-browser-extensions-could-use.html)

</div>

---

# 비개발자에게 무슨 의미인가

<div class="big">

지난주가 말해주는 것

</div>

- AI 팀원이 월 200달러대 상품으로 나오기 시작했다
- 도입은 늘지만 '큰 가치'를 얻은 곳은 아직 소수 — 성과 측정이 먼저
- 맡기기 전에 '언제 어떻게 멈출지'를 정해 두자
- 보안 전용 AI는 공격과 방어 양쪽에서 쓰인다

<div class="note">

다음 일요일, 이 슬라이드는 새로운 한 주의 소식으로 갱신됩니다

</div>

---

# 출처 · 더 보기

<div class="cards">

<a class="card video" href="https://www.youtube.com/results?search_query=Perplexity+Teammates">
<span class="outlet">▶ YOUTUBE</span>
<span class="head">Perplexity Teammates 소개 영상 모아보기</span>
<span class="link">youtube.com</span>
</a>

<a class="card" href="https://au.pcmag.com/ai/120788/perplexity-teammates-ai-agent-help-you-work">
<span class="outlet">PCMAG</span>
<span class="head">Perplexity Teammates 출시 (11/7)</span>
<span class="link">pcmag.com</span>
</a>

<a class="card" href="https://thehackernews.com/2026/11/openai-launches-gpt-6-cyber-after-ai.html">
<span class="outlet">THE HACKER NEWS</span>
<span class="head">OpenAI GPT-6 Cyber 출시 (11/5)</span>
<span class="link">thehackernews.com</span>
</a>

<a class="card" href="https://www.globenewswire.com/news-release/2026/11/05/3396012/0/en/financial-institutions-accelerate-transition-to-multi-agent-ai-in-drive-for-bottom-line-value.html">
<span class="outlet">GLOBENEWSWIRE</span>
<span class="head">금융사 멀티 에이전트 도입 설문 (11/5)</span>
<span class="link">globenewswire.com</span>
</a>

<a class="card" href="https://aiagentsdirectory.com/news/ai-agents-directory-daily-brief-november-7-2026">
<span class="outlet">AI AGENTS DIRECTORY</span>
<span class="head">AI 에이전트 뉴스 브리프 — 11월 7일</span>
<span class="link">aiagentsdirectory.com</span>
</a>

<a class="card" href="https://aiagentstore.ai/ai-agent-news/this-week">
<span class="outlet">AI AGENT STORE</span>
<span class="head">이번 주 에이전트 뉴스 모아보기</span>
<span class="link">aiagentstore.ai</span>
</a>

</div>
