---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-05-24 | 범위: 지난주 (2026-05-17 ~ 2026-05-23) -->

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

## 지난주 — 2026.05.17 ~ 05.23

<div class="lead-meta">

갱신 2026-05-24 · 범위: 지난 한 주

</div>

---

# 지난주 한눈에

<div class="big">

지난주의 중심 — Google I/O 2026 (5/19)

</div>

- 새 모델 Gemini 3.5 Flash — 작고 빠른데 작년 최상위급 성능
- 새 에이전트 Gemini Spark — 24시간 일하는 개인 비서
- 기업용 에이전트 — Dell·Camunda·Salesforce가 줄줄이 발표
- 공통점 — '대화하는' AI가 아니라 '대신 일하는' AI

<div class="src">

영상: [Google I/O '26 키노트 풀영상 (YouTube)](https://www.youtube.com/live/wYSncx9zLIU)

</div>

---

# 새 모델 — Gemini 3.5 Flash, 무엇이 좋아졌나

- 5/19 공개 — '작고 빠르고 싼' 등급의 새 모델
- 작년 최상위 모델(3.1 Pro)을 시험 15개 중 11개에서 앞섬
- 틀린 답(환각)을 내는 비율이 이전 세대보다 크게 줄어듦
- 출력 속도 약 4배 — 에이전트를 더 많이·싸게 굴릴 수 있음

<div class="highlight">

핵심 — 비싼 최상위 모델 없이도 에이전트를 일상에서 굴릴 수 있게 됐다

</div>

<div class="src">

출처: [TechCrunch](https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/) · [Google DeepMind](https://deepmind.google/models/gemini/flash/)

</div>

---

# 새 에이전트 — Gemini Spark가 대신 하는 일

- 24시간 켜진 개인 에이전트 — 폰·노트북이 꺼져 있어도 동작
- Gmail·캘린더·문서와 연결해 일을 알아서 처리
- 사례 ① 매달 신용카드 청구서에서 숨은 수수료를 찾아 알림
- 사례 ② 아이 학교 메일에서 마감일만 뽑아 매일 요약

<div class="note">

돈 쓰기·메일 보내기 같은 중요한 일은 실행 전에 사용자에게 먼저 묻는다

</div>

<div class="src">

출처: [TechCrunch](https://techcrunch.com/2026/05/19/google-introduces-gemini-spark-a-24-7-agentic-assistant-with-gmail-integration/) · [Google 블로그](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/)

</div>

---

# 비즈니스에 들어간 에이전트

| 회사 | 에이전트가 하는 일 | 푸는 문제 |
|---|---|---|
| Dell | PC에서 직접 도는 에이전트 | 민감 데이터를 밖으로 안 보냄 |
| Salesforce | 영업 화면 속 'AI 동료' | 고객 정보 찾고 처리하는 수고 |
| Camunda | 업무 절차를 자동 개선 | 비효율을 사람이 못 찾아냄 |
| Blue Yonder | 물류를 단계별로 자동 처리 | 매일 수천 건 배송 최적화 |

<div class="src">

출처: [Dell 뉴스룸](https://www.dell.com/en-us/dt/corporate/newsroom/announcements/detailpage.press-releases~usa~2026~05~dell-technologies-delivers-production-ready-agentic-ai-from-deskside-to-data-center.htm) · [주간 AI 뉴스 정리](https://www.buildfastwithai.com/blogs/ai-news-today-may-18-2026)

</div>

---

# 그 외 주목할 소식

- 검색 속 '정보 에이전트' — 관심 주제를 24시간 대신 지켜봄
- Android Halo — 백그라운드 에이전트 상태를 보여주는 새 화면
- Anthropic — 에이전트용 격리 실행 환경·도구 연결 기능 강화

<div class="note">

작게 보여도, '에이전트를 늘 켜두는' 시대를 준비하는 조각들

</div>

<div class="src">

출처: [Google I/O 개발자 키노트 정리](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/)

</div>

---

# 비개발자에게 무슨 의미인가

<div class="big">

지난주가 말해주는 것

</div>

- 모델이 싸지고 빨라져 — 에이전트를 '늘 켜두는' 게 현실이 됐다
- 개인 비서(Spark)가 자잘한 집안일·돈 관리까지 챙긴다
- 기업은 영업·물류·업무절차에 에이전트를 실제로 투입한다

<div class="note">

다음 일요일, 이 슬라이드는 새로운 한 주의 소식으로 갱신됩니다

</div>

---

# 출처 · 영상으로 더 보기

<div class="cards">

<a class="card video" href="https://www.youtube.com/live/wYSncx9zLIU">
<span class="outlet">▶ YOUTUBE</span>
<span class="head">Google I/O '26 키노트 풀영상</span>
<span class="link">youtube.com/live/wYSncx9zLIU</span>
</a>

<a class="card" href="https://blog.google/innovation-and-ai/sundar-pichai-io-2026/">
<span class="outlet">GOOGLE 블로그</span>
<span class="head">Sundar Pichai 오프닝 키노트 정리</span>
<span class="link">blog.google</span>
</a>

<a class="card" href="https://techcrunch.com/2026/05/19/with-gemini-3-5-flash-google-bets-its-next-ai-wave-on-agents-not-chatbots/">
<span class="outlet">TECHCRUNCH</span>
<span class="head">Gemini 3.5 Flash — 구글의 에이전트 승부수</span>
<span class="link">techcrunch.com</span>
</a>

<a class="card" href="https://techcrunch.com/2026/05/19/google-introduces-gemini-spark-a-24-7-agentic-assistant-with-gmail-integration/">
<span class="outlet">TECHCRUNCH</span>
<span class="head">24시간 개인 에이전트 'Gemini Spark' 공개</span>
<span class="link">techcrunch.com</span>
</a>

<a class="card" href="https://deepmind.google/models/gemini/flash/">
<span class="outlet">GOOGLE DEEPMIND</span>
<span class="head">Gemini 3.5 Flash 공식 모델 페이지</span>
<span class="link">deepmind.google</span>
</a>

<a class="card" href="https://www.dell.com/en-us/dt/corporate/newsroom/announcements/detailpage.press-releases~usa~2026~05~dell-technologies-delivers-production-ready-agentic-ai-from-deskside-to-data-center.htm">
<span class="outlet">DELL 뉴스룸</span>
<span class="head">PC에서 도는 'Deskside Agentic AI'</span>
<span class="link">dell.com</span>
</a>

</div>
