# Codex로 진행한 앨범 제작 — 슬라이드 스크립트

## 슬라이드 1 — 제목

- Codex 기반 앨범 제작 자동화
- 사례: The Hunchback of Notre‑Dame — The Cathedral’s Shadow
- 흐름: 기획 → 가사/스타일 → 커버 → 곡별 파일

Notes

- 목표: 재현 가능한 파이프라인으로 대중성+예술성 동시 달성

## 슬라이드 2 — 목표와 성과

- 콰지모도 POV 영문 앨범 완성(영문 가사 + 한글 번역 동시 제공)
- Suno 포맷 통일: 섹션 괄호·줄바꿈 규칙·코러스 반복 고정
- 커버 자동 생성: 하단‑우측 담백한 회색 타이포(사진/시네마틱 톤)
- musician 폴더에 트랙별 .md(Style/Exclude/EN/KOR)

Notes

- 다음 앨범에도 동일하게 반복 가능한 규약 정립

## 슬라이드 3 — End‑to‑End 워크플로우

- Step 1: 앨범 제목/설명 → 시점/톤 확정
- Step 2: 트랙 개요(장면/대사/스타일 요약)
- Step 3: 가사/스타일(Suno EN + KOR), 훅/Exclude 정제
- Step 4: 커버 생성(bakedTitle / overlay)
- Step 5: musician/<artist>/<album>/에 트랙별 .md 생성

Notes

- 각 단계는 프롬프트 템플릿과 산출 파일로 연결

## 슬라이드 4 — 산출물/폴더 구조

- 앨범: `앨범기획/2025-09-28-The Hunchback of Notre‑Dame - The Cathedral’s Shadow`
- 문서: `앨범 기획.md`, `가사와 음악스타일.md`, `cover.png`
- 트랙: `musician/남해씨/…/[Track N] Title.md` (EN/KOR 포함)
- 도구: `tools/cover-gen/*` (gen, overlay, create-album-cover)

Notes

- 커버: 미니멀·필름룩 사진 스타일, 회색 타이포

## 슬라이드 5 — 가사/스타일 포맷(핵심)

- 섹션(괄호): `(Verse 1)`, `(Pre-Chorus)`, `(Chorus)`, `(Bridge)`, `(Final Chorus)` 등
- 줄바꿈: 섹션 전환마다 빈 줄 1줄 / 한 줄=한 문장 / 생략부호 금지 / “x2” 대신 코러스 본문 반복
- 이중 출력: `## Lyrics (Suno format)`(영문) + `## Lyrics (KOR)`(번역)
- Prompt: Style(≤200자, BPM/악기/믹스), Exclude(금지 요소) 엄격

Notes

- 곡 구조는 유연, 줄바꿈 규칙은 고정

## 슬라이드 6 — 앨범 내 구조 다양화

- 한 앨범에서 ≥3가지 구조 사용
- 변주: Intro/Outro/Instrumental/Post‑Chorus/Double‑Chorus/Bridge 생략 등
- 박자/템포 분포: 6/8 또는 3/4 포함, 업템포 2–3곡, 나머지 균형
- 인접 회피: 같은 구조/박자/템포 연속 금지

Notes

- 지루함 방지 + 이야기 흐름 유지

## 슬라이드 7 — Codex 활용 패턴

- 편집/자동화: apply_patch로 파일 생성/정렬/치환
- 실행/검증: shell로 스크립트 실행·결과 확인
- 문서화: 워크플로우/프롬프트 규칙을 repo 문서로 관리
- 리카빙: 브리지/콜백/아웃로 미세 편집, Exclude 강화

Notes

- 작은 단위 반복 → 안정적 품질 확보

## 슬라이드 8 — 커버 파이프라인

- bakedTitle: 모델이 타이틀 직접 렌더(사진/시네마틱, 미니멀 타이포)
- overlay: SVG/Sharp로 폰트/그라디언트/외곽선 정교 제어
- 스크립트: `create-album-cover.mjs`(title/subtitle/date/size/style/pos/colors/shadow)

Notes

- 산출: `cover.png`, 필요 시 3000×3000 업스케일

## 슬라이드 9 — 이슈 & 해결

- Git index.lock 충돌 → IDE Git 종료, 잠금 제거, 권한 정정
- 폴더/이름 드리프트 → 최종 폴더로 통합
- 포맷 편차 → [Track 1] 규격으로 일괄 정렬

Notes

- 표준 템플릿이 반복 작업 시간을 절감

## 슬라이드 10 — 대중성/예술성 밸런스

- 작사가: 짧고 반복 가능한 훅, 제목/키워드 전면 배치, 윤리/이미지 유지
- 프로듀서: 트랙별 시그니처 텍스처, Exclude 준수, 섬세한 다이내믹 리프트
- 싱어송라이터: 호흡/휴지 설계, 곡별 레인지 선택

Notes

- 앵커: “Sanctuary”, “Ceci tuera cela” 재귀 활용

## 슬라이드 11 — 재현 가능한 프롬프트

- 트랙(EN): Style/Exclude/가사(괄호 섹션·줄바꿈), KOR 번역 포함
- 커버: Photographic cinematic + Notre‑Dame silhouette + Portra‑like grading + minimal type
- 트랙 파일: Style/Exclude/EN/KOR → `musician/<artist>/<album>/`

Notes

- `ALBUM_WORKFLOW.md`, `곡제작.md`, `앨범제작.md` 참조

## 슬라이드 12 — 미리보기 링크

- 앨범 문서: `앨범기획/2025-09-28-…`
- 트랙 .md: `musician/남해씨/…/[Track N] … .md`
- 커버: `cover.png`

Notes

- 데모: 트랙 1–2곡과 커버 화면 공유

## 슬라이드 13 — 배움

- 리스크: 포맷 편차, 폴더 파편화, Git 잠금
- 해결: 표준 포맷, 단일 타깃 폴더, 작은 단위 커밋
- 결론: 줄바꿈 규칙 고정 + 구조 유연 전략이 현업 친화적

Notes

- 온보딩 속도/재현성 향상

## 슬라이드 14 — 다음 단계

- `## Prompt`에 Key/Tempo/Tags 추가
- Suno 제출용 per‑track .txt 번들
- 커버 3000×3000 업스케일/색 보정
- 앨범 템플릿 자동화 CLI

Notes

- 필요 시 스크립트/템플릿 추가 지원

## 슬라이드 15 — Q&A / 부록

- 부록: 프롬프트 샘플, 폴더 규칙, Exclude 체크리스트
- 레포 경로: `ALBUM_WORKFLOW.md`, `곡제작.md`, `앨범제작.md`

Notes

- 감사합니다 — 질문 환영합니다
