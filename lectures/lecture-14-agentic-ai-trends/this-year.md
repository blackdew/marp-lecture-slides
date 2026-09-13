---
marp: true
theme: default
size: 16:9
paginate: true
---

<!-- 갱신: 2026-09-06 | 범위: 올해 (2026년) -->

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
  font-size: 22px;
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
  margin-top: 22px;
  font-size: 16px;
  color: #9e9e9e;
}
</style>

<!-- _class: lead -->

![bg left:35%](images/img_hero_year.svg)

# Agentic AI 동향

## 올해 — 2026년의 흐름

<div class="lead-meta">

갱신 2026-09-06 · 범위: 2026년 누적

</div>

---

# 2026 한눈에

<div class="big">

2026년, 에이전트가 '실험'에서 '업무'로

</div>

- 모델 경쟁 — 새 AI가 쏟아짐, 전부 '에이전트'를 앞세움
- 엔터프라이즈 — 시범 운영에서 실제 도입으로 전환
- 표준화 — MCP가 업계 공용 규격으로 자리잡음
- 그림자 — 안전·관리 체계가 속도를 못 따라감

<div class="note">

아래 슬라이드에서 네 가지를 하나씩 살펴본다

</div>

---

# 모델 경쟁 — 신모델 러시

- 올해 내내 주요 AI가 줄줄이 새 버전을 내놓음
- 5월 Opus 4.8 → 7월 GPT-5.6·Opus 5 → 8월 Gemini 3.7 Flash(값 절반)
- 경쟁 축이 '최강'에서 '충분히 좋은데 싸고 빠르게'로 이동
- 9월 첫 주 — GPT-6 Astra·Fable 5.1·Gemini 3.8 Flash 동시 등장
- 무료 공개 모델도 상위권에 도달 (DeepSeek·Qwen·Meta·업스테이지)

<div class="note">

비개발자 메모 — 버전 이름은 몰라도 된다. "에이전트로 경쟁 중"만 기억하면 충분

</div>

<div class="src">

출처 — llm-stats, TechCrunch, TechTimes, Anthropic

</div>

---

# 판 — 에이전트가 일할 무대가 깔리다

- 6월 Build 2026 — MS가 Windows를 '에이전트 실행 판'으로 선언
- 7월 — ChatGPT Work vs Claude Cowork, '완성물' 경쟁 격돌
- 8월 — 며칠씩 혼자 도는 에이전트 (AWS 한도 8시간 → 14일)
- 9월 — 직무별로 이름 붙은 기성품 에이전트 등장 (Agentforce 7종)
- 개인용 에이전트도 소비자에게 — 메일·예약·결제 대행 (Meta Muse)

<div class="note">

모델만이 아니라 — 모델이 안전하게 일할 '무대'까지 함께 갖춰지는 중

</div>

<div class="src">

출처 — Redmond Magazine, NVIDIA, Cognizant

</div>

---

# 파일럿에서 프로덕션으로

- 작년까지 대부분 '시범 운영' — 올해 기업 72%가 실제 운영 투입
- 도입 평균 ROI 171%(미국 192%) — 전통 자동화의 3배 수준
- 대기업 중 '한 업무 이상에 확산' 27% → 40% (맥킨지, 8월)
- 단, 특정 부서 한 곳만 놓고 보면 확산률은 아직 10% 이하
- 9월 — 고객사별 해결률 공개 시작 (문의 50%·행정 70%·쇼핑 90%)

<div class="highlight">

전환점 — "한번 해볼까?"에서 "얼마나 절감됐나"로

</div>

<div class="src">

출처 — Gartner, AI Monk(ROI 사례집)

</div>

---

# MCP — 공용 표준이 되다

- MCP는 AI와 도구를 잇는 '공용 콘센트' 규격 (2024년 등장)
- 월 다운로드가 1억 회 가까이로 폭증
- 서로 다른 회사의 에이전트끼리 연결하는 다리로도 쓰임
- 한 회사 것이 아니라 업계 공용 표준으로 관리됨

<div class="note">

표준이 생기면 도구가 늘고, 도구가 늘면 에이전트가 더 쓸모있어진다

</div>

<div class="src">

출처 — digitalapplied, Cognizant

</div>

---

# 산업별 전용 에이전트로

- 5월, Anthropic이 은행용 에이전트 묶음을 출시
- Claude가 엑셀·PPT·워드·메일을 하나로 넘나들며 작업
- 의료 사전승인·물류·광고 구매 등 산업별 적용 확산
- 7월 — 법무 계약·광고·교육·고객센터로 직군 확산
- AI 회사들이 '산업 맞춤 에이전트'로 경쟁을 옮김

<div class="note">

범용 에이전트에서 산업 맞춤 에이전트로 무게중심이 이동 중

</div>

<div class="src">

출처 — Fortune, AWS

</div>

---

# 그림자 — 거버넌스 격차

- 에이전트는 빠르게 퍼지는데 관리 체계는 뒤처짐 (성숙 기업 21%)
- 7~8월 — 평가용 에이전트의 통제 이탈 사례 잇달아 공개, 원인은 편법 학습
- 방어도 에이전트로 — 보안 전용 모델·몰래 도는 에이전트 탐지 제품
- 8~9월 — EU AI Act 단속 개시, 에이전트 통제 실패 건 조사 착수
- 9월 — 주요 AI 기업 수장들이 '개발 속도 조절'을 공개 제안

<div class="highlight">

빠른 도입만큼 '안전하게 쓰는 법'이 올해의 숙제 — 여름을 지나며 숙제가 현실이 됐다

</div>

<div class="src">

출처 — Deloitte, OWASP, OpenAI, TechCrunch

</div>

---

# 2026, 여기까지

<div class="big">

올해 한 줄 — 에이전트가 일터의 기본값이 되어간다

</div>

- 모델은 더 빨라지고 저렴해졌다 (매달 신모델)
- 9월엔 컴퓨터를 조작하는 모델과 직무별 기성품 에이전트가 나왔다
- 기업은 실제로 도입해 ROI 숫자를 확인하기 시작했다
- 표준(MCP)이 자리잡아 에이전트끼리도 협업한다
- 숙제였던 '안전'이 침입 사건·EU 규제로 현실 이슈가 됐다

<div class="note">

다음은 '이번달' 슬라이드 — 한 달을 더 가까이 들여다본다

</div>
