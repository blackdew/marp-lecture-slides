---
marp: true
theme: default
size: 16:9
paginate: true
---

<style>
section {
  padding: 60px 80px;
  font-size: 1.1em;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

section.lead {
  padding: 60px 80px;
  text-align: center;
  justify-content: center;
}

h1 {
  color: #2c3e50;
  font-size: 3.2em;
  margin-top: 0;
  font-weight: 700;
}

h2 {
  color: #3498db;
  font-size: 2.6em;
  margin-top: 0;
  font-weight: 700;
}

h3 {
  font-size: 1.6em;
  font-weight: 600;
}

p, li {
  font-size: 0.95em;
  line-height: 1.5;
  font-weight: 400;
}

code {
  background: #f4f4f4;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 1.1em;
}

table {
  font-size: 0.95em;
}

.highlight {
  background: #fff3cd;
  padding: 15px;
  border-left: 4px solid #ffc107;
  margin: 15px 0;
  font-size: 1.2em;
}

.success {
  background: #d4edda;
  padding: 15px;
  border-left: 4px solid #28a745;
  margin: 15px 0;
  font-size: 1.2em;
}

.question {
  background: #e3f2fd;
  padding: 20px;
  border-left: 4px solid #2196f3;
  margin: 20px 0;
  font-size: 1.3em;
  font-weight: bold;
  color: #1565c0;
}
</style>

![bg left:35%](images/img_title.svg)

# Just Plan It!!

### AI Agent로 시작하는 일과 삶의 전환

**동명대학교 특강**

---

## 오늘의 여정

### 전체 타임라인 (2시간)

| Part | 주제 | 시간 | 핵심 내용 |
|------|------|------|-----------|
| **1** | 오프닝 | 15분 | AI Agent, 왜 지금인가? |
| **2** | 첫 체험 | 20분 | Agent 설치하고 직접 써보기 |
| **3** | 3가지 키워드 | 25분 | 선택, 계획, 문서화 |
| **4** | 실전 실습 | 35분 | 학업 도우미 + 바이브 코딩 |
| **5** | 마무리 | 15분 | AI 시대 대학생의 경쟁력 |

<div class="highlight">
오늘의 핵심 메시지: <strong>Agent = 도구를 쓸 줄 아는 AI 동료</strong>
</div>

---

![bg right:35%](images/img_chatbot_vs_agent.svg)

## 챗봇 vs Agent

### ChatGPT에게 "파일 만들어줘"라고 해본 적 있나요?

| 구분 | 챗봇 (ChatGPT) | Agent |
|------|----------------|-------|
| **할 수 있는 것** | 대화, 조언, 설명 | 대화 + **파일 생성** + **코드 실행** |
| **도구 사용** | 없음 | 파일 읽기/쓰기, 터미널 명령 실행 |
| **비유** | 똑똑한 친구 | **도구를 쓰는 동료** |
| **결과물** | "이렇게 하면 돼" (텍스트) | 실제 파일이 내 컴퓨터에 생성! |

<div class="highlight">
챗봇: "코드는 이거야, 복사해서 저장해"<br/>
Agent: "파일 만들었어. 브라우저에서 열어봐!"
</div>

---

![bg left:35%](images/img_agent_structure.svg)

## Agent의 구조

### Agent = LLM + Memory + Planning + Tools

| 요소 | 역할 | 비유 |
|------|------|------|
| **LLM** (두뇌) | 언어 이해 및 생성 | 요리사의 지식 |
| **Memory** (기억) | 대화 맥락 유지 | 주문 내역 기억 |
| **Planning** (계획) | 단계별 작업 설계 | 조리 순서 결정 |
| **Tools** (도구) | 파일 조작, 코드 실행 | 칼, 불, 냄비 |

<div class="success">
<strong>핵심 차이</strong>: 요리사에게 레시피만 준 것(챗봇) vs 재료와 도구까지 준 것(Agent)<br/>
Tools가 Agent를 Agent답게 만듭니다!
</div>
