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

<!-- _class: lead -->

# Part 2: 첫 체험

### 직접 해보면 달라집니다

---

## AI Agent CLI 도구 비교

### 어떤 Agent를 선택할까요?

| 도구 | 가격 | CLI 지원 | 특징 |
|------|------|----------|------|
| **Claude Code** | 유료 | O | Plan 모드로 실행 전 계획 검토 가능. 한국어에 강함 |
| **Gemini CLI** | 무료 | O | 완전 무료. 빠른 응답 속도. Google AI Studio 기반 |
| **Codex** | 유료/무료 | O | ChatGPT Plus 구독자 무료. 코드 생성에 특화 |

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">

<div>

**오늘 강의**: Claude Code CLI 중심으로 진행

</div>

<div>

**대안**: Gemini CLI (무료) / Codex (ChatGPT Plus 구독자)

</div>

</div>

<div class="highlight">
어떤 도구든 괜찮습니다! 핵심은 <strong>Agent를 직접 체험</strong>하는 것입니다.
</div>

---

## 설치 및 첫 실행

### 설치 가이드: [getclaudecode.com](https://getclaudecode.com/)

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 30px;">

<div>

**Claude Code**

```bash
npm install -g \
  @anthropic-ai/claude-code
```

```bash
claude
```

</div>

<div>

**Gemini CLI**

```bash
npm install -g \
  @google/gemini-cli
```

```bash
gemini
```

</div>

<div>

**Codex**

```bash
npm install -g \
  @openai/codex
```

```bash
codex
```

</div>

</div>

**첫 대화**: 프롬프트가 나타나면 입력해보세요

```
안녕? 자기소개 해줘.
```

**종료**: `Ctrl+C` 또는 `/exit`

---

## 실습 2-1: 자기소개 페이지 만들기

### 프롬프트 한 줄로 웹 페이지를!

**입력할 프롬프트**:

```
나를 소개하는 HTML 페이지를 만들어줘.
이름은 [본인 이름], 전공은 [본인 전공], 관심사는 [본인 관심사].
깔끔하고 예쁘게 디자인해줘.
```

**확인 방법**:

1. Agent가 파일을 생성하면 `Y` 를 눌러 승인
2. 생성된 HTML 파일을 브라우저에서 열기
3. 내 정보가 담긴 웹 페이지 확인!

<div class="highlight">
첫 프롬프트에서 결과물이 나오는 경험! <strong>이것이 Agent의 힘</strong>입니다.
</div>

---

## 실습 2-2: Plan 모드 체험

### Agent에게 "계획부터 보여줘"라고 요청하기

**Plan 모드 진입**: `Shift+Tab` 두 번 누르기

**입력할 프롬프트**:

```
자기소개 페이지에 다크모드 토글 버튼을 추가해줘.
버튼을 누르면 배경이 어두워지고 글자가 밝아지게 해줘.
```

**진행 순서**:

1. Agent가 **계획을 먼저 보여줌** (어떤 파일을, 어떻게 수정할지)
2. 계획 확인 후 `Y` 를 눌러 실행 승인
3. 수정된 페이지를 브라우저에서 새로고침

<div class="success">
<strong>학습 포인트</strong>: Plan 모드는 Agent의 안전장치입니다.<br/>
"실행 전에 계획을 검토한다" - 이것이 AI와 협업하는 핵심 습관!
</div>

---

## 중간 체크

<div class="question">
자기소개 페이지, 성공했나요?
</div>

### 잠깐, 생각해봅시다

- 방금 경험에서 **가장 놀라웠던 점**은?
- 이 기능을 **어디에 써먹을 수 있을까?**
  - 과제 발표 자료?
  - 팀프로젝트 페이지?
  - 포트폴리오?

<div class="highlight">
실패해도 괜찮아요. Agent도 실수합니다!<br/>
중요한 것은 <strong>"다시 시도하고, 더 구체적으로 요청하는 것"</strong>입니다.
</div>
