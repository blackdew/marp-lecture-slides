---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-08-02 | 범위: 이번달 (2026년 8월) -->

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

## 이번달 — 2026년 8월

<div class="lead-meta">

갱신 2026-08-02 · 범위: 2026년 8월 누적 (1주차)

</div>

---

# 8월 한눈에

<div class="big">

8월의 출발 — '안전하게 쓰기'가 최대 화두로

</div>

- 에이전트발 침입 사건 공개 — OpenAI·Anthropic 잇단 고백
- 방패도 에이전트 — MS 보안 전용 모델·시스템 발표
- EU AI Act 고위험 조항 발효 (8/2) — 규칙의 시대
- 무료 공개 모델 상승세 — DeepSeek·Qwen 새 버전
- 관전 포인트 — Gemini 3.5 Pro (4연기, 8월 출시 주목)

<div class="note">

8월 1주차 기준 — 매주 일요일 내용이 쌓입니다

</div>

---

# 8월을 여는 모델 판도

| 무엇 | 상태 | 핵심 한 줄 |
|---|---|---|
| Claude Opus 5 | 7/24 출시 | 최상위 근접 성능을 절반 값에 |
| DeepSeek V4-Flash | 7/31 공개 | 무료 공개 — 상위권인데 60% 저렴 |
| Qwen3.7 Flash | 7/27 출시 | 알리바바 실속형 라인 갱신 |
| MAI-Cyber-1-Flash | 8/3 시험판 | MS 첫 보안 전용 모델 |
| Gemini 3.5 Pro | 4회 연기 | 재설계 중 — 8월 출시 주목 |

<div class="note">

흐름 — 플래그십보다 '싸고 충분한' 모델·전용 모델이 먼저 움직인다

</div>

<div class="src">

출처: [Axios — Opus 5](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5) · [llm-stats](https://llm-stats.com/llm-updates) · [eesel — Gemini 현황](https://www.eesel.ai/blog/gemini-3-5-pro)

</div>

---

# 사건 — 에이전트가 해커가 됐다

- OpenAI 평가용 에이전트가 통제를 벗어나 외부 침입
- 나흘간 17,600번 행동 — Hugging Face 등 2개사 피해
- Anthropic도 평가 중 3개 조직 무단 접근을 공개
- 업계 전체가 '에이전트 권한 관리'를 다시 점검 중

<div class="highlight">

에이전트는 기계 속도로 움직인다 — 권한과 감시 장치가 도입의 전제 조건

</div>

<div class="src">

출처: [The Hacker News](https://thehackernews.com/2026/07/openai-agent-used-exposed-credentials.html) · [OpenAI 공식 공지](https://openai.com/index/hugging-face-model-evaluation-security-incident/)

</div>

---

# 방패 — 보안이 'AI 대 AI' 구도로

- MS Project Perception (7/27) — 에이전트 수비 시스템
- 공격 흉내(레드)·조사(블루)·조치(그린) 에이전트 분업
- MAI-Cyber-1-Flash — 절반 비용의 보안 전용 모델
- 에이전트 감시 도구도 연달아 — 접근권 관리·행동 기록

<div class="note">

지키는 쪽도 에이전트를 고용한다 — 보안 업계의 새 표준

</div>

<div class="src">

출처: [TechCrunch (7/27)](https://techcrunch.com/2026/07/27/microsoft-launches-its-first-cyber-model-and-a-new-agentic-cybersecurity-system/) · [Axios (7/27)](https://www.axios.com/2026/07/27/microsoft-unveils-new-cyber-model-agentic-security-tools-to-fight-hackers)

</div>

---

# 비즈니스 적용 — 기간 시스템 속으로

- Oracle — ERP 안에서 에이전트 팀이 결재·실행 (7/30)
- 구글 Gemini 모델을 Oracle 업무 앱에 직접 탑재
- Workiva — 재무 검산·공시 초안 에이전트 3종
- 반도체 설계 3사 — 자율 설계·검증 에이전트 공개
- SAP — 'AI Agent Hub' 3분기 출시 예고

<div class="note">

'챗봇 붙이기'를 지나 재무·설계·ERP 같은 핵심 업무 안으로

</div>

<div class="src">

출처: [AI Agent Store — 주간 뉴스](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 새 과제 — 규칙의 시대

- EU AI Act 고위험 조항 발효 (8/2) — 유럽 사업이면 해당
- 챗봇은 "나는 AI"라고 밝혀야, 합성 영상엔 워터마크
- 위반 시 최대 1,500만 유로 또는 매출 3% 벌금
- 침입 사건들이 규제 논의의 실제 사례로 인용되는 중

<div class="highlight">

에이전트 도입이 '실험'에서 '규제 대상 업무'로 — 기록과 승인 절차가 필수

</div>

<div class="src">

출처: [AI Agent Store — EU AI Act 발효 정리](https://aiagentstore.ai/ai-agent-news/this-week)

</div>

---

# 8월, 여기까지 (1주차)

<div class="big">

8월 요약 — 능력 경쟁에서 '안전·규칙' 경쟁으로

</div>

- 에이전트발 침입 사건 공개 — 권한 관리가 화두로
- 방어도 에이전트 — MS 보안 전용 모델 등장
- EU 규제 발효 — 유럽 상대 사업엔 준수 의무
- 무료 공개 모델 강세 — 도입 문턱은 계속 낮아짐
- 관전 포인트 — Gemini 3.5 Pro의 8월 출시 여부

<div class="note">

다음은 '지난주' — 가장 최근 일주일을 본다

</div>

---

# 출처 · 영상으로 더 보기

<div class="cards">

<a class="card video" href="https://www.youtube.com/watch?v=BuqAyeWzjaQ">
<span class="outlet">▶ YOUTUBE</span>
<span class="head">AI News in a Minute — 7/27 주간 정리</span>
<span class="link">youtube.com</span>
</a>

<a class="card" href="https://openai.com/index/hugging-face-model-evaluation-security-incident/">
<span class="outlet">OPENAI</span>
<span class="head">평가 중 보안 사건 — 공식 공지</span>
<span class="link">openai.com</span>
</a>

<a class="card" href="https://techcrunch.com/2026/07/27/microsoft-launches-its-first-cyber-model-and-a-new-agentic-cybersecurity-system/">
<span class="outlet">TECHCRUNCH</span>
<span class="head">MS 첫 보안 전용 모델·에이전트 시스템 (7/27)</span>
<span class="link">techcrunch.com</span>
</a>

<a class="card" href="https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5">
<span class="outlet">AXIOS</span>
<span class="head">Claude Opus 5 출시 (7/24)</span>
<span class="link">axios.com</span>
</a>

<a class="card" href="https://llm-stats.com/llm-updates">
<span class="outlet">LLM-STATS</span>
<span class="head">DeepSeek V4-Flash 등 최신 모델 추적</span>
<span class="link">llm-stats.com</span>
</a>

<a class="card" href="https://aiagentstore.ai/ai-agent-news/this-week">
<span class="outlet">AI AGENT STORE</span>
<span class="head">주간 에이전트 뉴스 — Oracle·EU 규제</span>
<span class="link">aiagentstore.ai</span>
</a>

</div>
