# cases/ — 강의용 원자료 (raw cases)

이 디렉토리는 `lecture-14-agentic-ai-trends` 슬라이드(last-week / this-month / this-year / all-time)를 갱신할 때 입력 데이터로 사용하는 **개별 AI 사례 파일** 모음입니다.

## 출처

`blackdew/gyeol-memory` 리포의 `memory/semantics/source/ai-cases/`에서 가져온 사본. 원본은 매주 월요일 09:00 KST에 Anthropic Cloud routine(`trig_01JbjQ7nYhVvABfCqLKB1584`)이 WebSearch로 자율 큐레이션하여 갱신.

## 갱신 방식

이 cases/ 디렉토리는 **수동 동기화**가 기본:
- 슬라이드 갱신 작업(런북 절차) 시작 시 gyeol 리포의 ai-cases/를 pull → cases/로 덮어쓰기
- 또는 슬라이드 갱신 routine 자체에 sync 단계를 추가

각 사례 파일에는 frontmatter로 `category`, `relevance`, `tags`, `url` 등이 포함되어 있어 슬라이드 갱신 시 필터링하기 좋습니다.

## 파일 명명

`YYYY-MM-DD-{slug}.md` — 날짜는 *발견일* (배포일 아님)

## 카테고리

- `agentic-experiment` — AI가 실제 비즈니스 자율 운영 (Project Vend, Andon Cafe류)
- `dev-tool` — Claude Code/Cursor/Devin 등 개발 도구 도입 사례
- `enterprise-adoption` — 기업 AI 자동화 도입
- `failure-case` — 실패·한계 사례 (강의용으로 가장 가치 큼)

## 활용 가이드

런북(`../runbook.md`)의 "콘텐츠 방향"에 부합하는 사례만 선별해 슬라이드에 반영:
- 구체적 수치가 있는 사례 우선 (Rakuten 79% 단축 등)
- 한 줄로 청중에게 설명 가능한 사례 우선
- "왜 의미가 있는가"가 명확한 사례 우선

## 현재 수록 (2026-05-24 기준)

| 파일 | 카테고리 | relevance |
|---|---|---|
| 2026-05-24-andon-cafe-mona.md | agentic-experiment | high |
| 2026-05-24-pocketos-db-deletion.md | failure-case | high |
| 2026-05-24-rakuten-claude-code.md | dev-tool | high |
| 2026-05-24-anthropic-agentic-coding-report.md | dev-tool | medium |
| 2026-05-26-mexico-gov-ai-cyberattack.md | failure-case | (확인) |
| 2026-05-26-nx-console-supply-chain-attack.md | failure-case | (확인) |
