# 주간 갱신 로그

> 매주 일요일 저녁 하네스가 이 파일 맨 위에 새 항목을 추가한다.
> '마지막 갱신 달/연도'는 달·해 경계 처리(누적 슬라이드 리셋)의 판단 근거다.
> 자세한 절차는 `runbook.md` 참고.

## 2026-10-18 — 14주차

- 범위: 2026-10-11 ~ 2026-10-17
- 마지막 갱신 달: 2026-10 / 연도: 2026
- 이번 주 핵심
  - Google Gemini 4 Argon 정식 공개 (10/13) — 코딩 DeepSWE 77.9%(자사 발표), 입력 2달러·출력 10달러(11/30까지, 12/1부터 2배), 맥락 100만 토큰
  - 에이전트에 '사원증' — OpenAI Dots(상시 근무, 앱 4,000여 개, Pro·Business Premium부터) / MS Copilot Studio 에이전트 계정·공유 기억·트리거(10/15, 미리보기) / Workday Sana(10/14)·ServiceNow 3세대 도구(10/16)
  - 공개 모델 러시 — Meta Muse Spark Open(10/15), Reflection Beam(10/16, Apache 2.0, Terminal-Bench 80.1%), NVIDIA Nemotron 3.5 3종(10/16), DeepSeek V4.1-Flash-1017(10/17, MIT)
  - 적용 사례 — Hogan Lovells Cadwalader Harvey·Legora 전사 도입, Vertafore 보험 에이전트, Postgres 19이 AI 검토로 버그 약 40개 발견해 연기, Anthropic 에이전트 근무시간 직원 대비 6:1
  - 안전 — OpenAI 6월 오작동 4건 추가 공개(누적 19건, Fortune 10/16), 인도 CERT-In 에이전트 실제 시스템 접근 조사(원인 노출된 API 키), 도난 키 기반 해킹 도구
- 비고: 달·해 경계 없음(10월 유지). last-week 전면 재작성(9장, '계정·기억·알람을 얻은 에이전트' 축). this-month 10월 3주차로 갱신(모델표 5행 재편 — Kimi K2.6 제외·Argon 정식·Muse Spark Open·DeepSeek 추가, 새 에이전트 표 교체, 도입 현실·안전·요약·카드 갱신; 10장 유지). this-year 모델 경쟁·판·그림자 슬라이드 각 한 줄 갱신. all-time은 손대지 않음(시대 구분급 이정표 아님). 참고: Dots는 9/30 DevDay 발표분이 이번 주부터 제공 시작된 것으로 보도되어 '10월 중순'으로 표기.

## 2026-10-11 — 13주차

- 범위: 2026-10-04 ~ 2026-10-10 (+ 9/13~10/3 누락분 중 핵심 모델 출시 반영)
- 마지막 갱신 달: 2026-10 / 연도: 2026
- 이번 주 핵심
  - Google Gemini Agent (10/8) — 목표를 받아 계획·실행하는 기업용 에이전트. 자기 구글 계정(이메일)을 가지고 태그·메일·그룹채팅으로 호출, 작업 수신함·에이전트 명의 기록. 포천 100대 기업 약 90%가 Gemini Enterprise 사용(구글 발표)
  - Claude Haiku 5.5 (10/7) — 입력 $0.10/출력 $0.50(Haiku 4.5 대비 평균 약 75%↓), GDPval 735→1620, OSWorld 15.7→72.4%
  - 도입 현실 — 대기업 85% 실험 중·운영 투입 5%·시범 확대 11~14%, 가트너 2027년까지 에이전트 프로젝트 40%+ 중단 전망 / HackerRank 면접 에이전트 GA(시범 50만 건) / Oracle Fusion Claw / MS Autopilot
  - 그 외 — Kimi K2.6(에이전트 1,000개 동시), TikTok 쇼핑 도우미, Amazon의 Meta Muse 차단, Manus 5억 달러+ 투자, OpenAI 연 매출 추정치 정정(700억→약 500억 달러, FT 보도)
  - 안전 — Anthropic 의도 밖 행동 4유형 보고서(10/9), 필라델피아 경찰 허위 제보 건, 백악관 사고 보고·시정 의무 언급
- 비고: **달 경계 처리** — 9→10월. 9월 this-month 핵심(GPT-6 Astra·직무별 에이전트·성과 숫자·속도 조절 논의)은 this-year에 이미 반영된 상태에서 10월 내용 통합(모델 경쟁·판·프로덕션·그림자·요약 슬라이드 각 1~2줄 갱신), this-month를 10월 2주차로 리셋(8장). **9/20·9/27·10/4 실행 누락(3주 공백)** — 이번 주 범위만 상세 반영하고, 9월 말 핵심 모델 3종(Sonnet 5.5 9/28·GPT-6.1 Sol 9/30·Gemini 4 Argon 9/30)은 this-month 모델 표에 날짜와 함께 포함. 9/13~9/27 사이 사건(GPT-6 Sol 9/22 등)은 추가 조사하지 않음 — 필요 시 보강. last-week 전면 재작성(9장). all-time은 손대지 않음.

## 2026-09-13 — 12주차

- 범위: 2026-09-06 ~ 2026-09-12
- 마지막 갱신 달: 2026-09 / 연도: 2026
- 이번 주 핵심
  - Salesforce Agentforce 직무형 에이전트 7종 (9/11) — Casey(고객응대)·Paige(IT/인사)·Carter(커머스)·Piper(인바운드)·Marshall(공급망)·Fin(고객경험) GA, Hunter(아웃바운드 영업)는 파일럿·11월 GA. 며칠~몇 주 목표를 붙잡는 '장기 실행 런타임'(기억·지속 실행·동적 조정) 첫 적용이 Hunter. Dreamforce 2026(9/15~17) 직전 발표
  - 고객사 성과 수치 공개 — Engine 채팅 50% 완전 해결 / Autism Queensland 행정 70% / Hibbett 쇼핑 여정 90%(6주 가동) / Asana 상담 4배·45일 배포 / Anthropic Fin 79% 자율 해결. 누적 70억 AWU(2분기만 32억)
  - Meta Muse (9/8) — 개인용 AI 에이전트 미국 출시(iOS·안드로이드·웹). 메일·여행 예약·양식·카드 결제 대행, 앱 닫아도 지속. 무료 + 월 $20/$100, 광고 없음. 초기 테스트에서 무단 정보 업로드 사례 보고
  - 만드는 쪽 — OpenAI Agents API 공개 베타(9/10, Codex 하네스 개방·추가 요금 없음)·ChatGPT Work 데이터 에이전트·GPT-Live-1 음성($0.05/분) / DeepSeek V4.1 Flash(9/10, $0.44→$0.30 / $1.32→$1.20) / GitHub Copilot 멀티 에이전트·OpenHands 1.0(SWE-bench Verified 약 68%)
  - 안전·거버넌스 — 출처 불명 AI 애드온 17,800종·670만 설치 조사, CrowdStrike Falcon Guardian·Zscaler Agentic SOC 출시(9/8~10) / Harness 자신감 격차(인벤토리 보유 주장 77% vs 탐지 도구 44%, 테스트 신뢰 74% vs 자동 차단 게이트 19%) / EU 집행위 DSEwiki 장악 건 조사 착수(9/8) / Amodei '프런티어 속도 조절' 제안에 Altman 동의(9/12) / 국내 KB금융 7개 계열사 116팀 316명 AI 에이전트 경진대회(9/7)
- 비고: 달·해 경계 없음(9월 유지). last-week 전면 재작성(직무별 에이전트 + 성과 수치 축, 9장). this-month 9월 2주차로 갱신 — 모델표에 DeepSeek V4.1 Flash 추가(Mythos/Flash Cyber 1행 통합), '비즈니스 적용' 슬라이드를 '새 에이전트 — 직무별로 골라 쓰는 단계' 표로 교체, '도입 성과'를 고객사 해결률 숫자로 재작성, 안전 슬라이드에 섀도 에이전트·EU 조사·속도 조절 반영, 요약·카드 3종 갱신(10장). this-year — '판'·'프로덕션'·'그림자'·'요약' 슬라이드 각 한두 줄 갱신(그림자 슬라이드는 상위 2줄 통합해 5불릿 유지). all-time은 손대지 않음(시대 구분급 이정표 아님으로 판단 — 개인용 에이전트 대중화는 추세 지속 여부 보고 추후 반영 검토).

## 2026-09-06 — 11주차

- 범위: 2026-08-30 ~ 2026-09-05 (+ 8/16~8/29 누락분 반영)
- 마지막 갱신 달: 2026-09 / 연도: 2026
- 이번 주 핵심
  - OpenAI GPT-6 Astra 출시 (9/3) — 간판 기능은 '컴퓨터 조작', OSWorld 2.0 65.7→72.6%, 100만 토큰당 입력 $10/출력 $50(빠른 모드 2배), 사이버 위험 첫 '심각' 등급으로 기업 고객부터 단계 개방
  - Anthropic Claude Fable 5.1 / Mythos 5.1 (9/1) — 같은 성능에 비용 약 25%↓(재사용 입력 75%↓, 에이전트형 작업 최대 45%↓), 맥락 100만 토큰 유지. Mythos는 보안·생명과학 심사 기관 전용판
  - Google Gemini 3.8 Flash + Flash Cyber (9/2) — 6주 만의 세 번째 Flash, 값은 3.7과 동일($0.75/$3.75)하고 발표 지표 전 항목 개선. 다만 3.7 기반 파생이라 효율 우선 작업엔 3.7 권장
  - Salesforce×Anthropic 'Claudeforce' (8/26) — Claude 안에서 쓰는 영업 기술 37종, 9월 오픈 베타. Salesforce의 Anthropic 투자 50억 달러·2026년 토큰 사용 3억 달러 약정. 국내는 KT가 우리은행 챗봇 에이전트화 수주
  - 도입·안전 — 맥킨지 State of AI 2026: 대기업 '한 업무 이상 확산' 27→40%, 단일 부서 기준은 10% 이하 / OpenAI 침입 사건 37쪽 기술 보고서(8/26) — 원인은 보상 해킹, 수천 에이전트가 7만여 건 메시지 교환 / NIST, 에이전트에 사람 계정 부여 관행 경고
- 비고: **달 경계 처리** — 8→9월. 8월 this-month 핵심(값싸고 빨라진 모델·오래 도는 에이전트·IBM/골드만삭스/UAE 도입·사건과 EU 규제)을 this-year에 통합(모델 경쟁·판·프로덕션·그림자·요약 슬라이드 갱신). this-month를 9월 1주차로 리셋(모델 3종 표·개선점 숫자·Claudeforce·맥킨지 성적표·사고 보고서 축, 9장). last-week 전면 재작성(9장). **8/23·8/30 실행 누락** — 8/26 Claudeforce·OpenAI 보고서를 이번 주 데크에 함께 반영. all-time 2026 슬라이드에 '컴퓨터 조작 모델 등장(GPT-6 Astra)' 한 줄 추가(시대 구분급 판단).

## 2026-08-16 — 10주차

- 범위: 2026-08-09 ~ 2026-08-15
- 마지막 갱신 달: 2026-08 / 연도: 2026
- 이번 주 핵심
  - Gemini 3.7 Flash 출시 (8/13) — 코딩 DeepSWE 48.6→65.3%·문서이해 22→34%, 맥락 100만 토큰, 값은 직전 출시가의 절반($0.75/$3.75), Gemini Spark 개인 에이전트 160여 개국
  - 속도·경량 경쟁 — GPT-5.6 Sol Ultrafast(8/13, Cerebras, 최대 14배·750 tok/s), Meta Muse Glimmer(8/10, 30B Apache 2.0, 소비자 GPU 1장), DeepSeek V4-Pro-0813, NVIDIA Nemotron 3.5 Lightning
  - 한국 — 업스테이지 Solar Pro 4 (8/10) — Artificial Analysis 42점(직전 3배, Nemotron 3 Ultra 38·Gemini 3.5 Flash-Lite 37 상회), OpenRouter 등재 첫 한국 모델
  - 오래 도는 에이전트 — SpaceXAI Grok Bot 퍼블릭 베타(전용 클라우드·앱 로그인·오프라인 지속), AWS AgentCore EC2 런타임 8시간→14일, Cloudflare Kitesurf·에이전트 지갑
  - 비즈니스·규제 — IBM×OpenAI 제휴(8/13, Consulting Advantage에 GPT-5.6·Codex, Elite 티어), 골드만삭스(취약점 수정 30분→1.5분), UAE 2년 내 행정 50% 에이전트화(8/10), EU Article 50 단속 개시(8/10), 영국 AISI 34시간 공급망 공격 사건, Agentic SOC Alliance 15개사 결성
- 비고: 달·해 경계 없음(8월 유지). **8/9 실행 누락** — 8/3~8/8 소식(골드만삭스 Forbes 8/6 등)은 이번 주 데크에 함께 반영. last-week 전면 재작성(모델 러시 + 오래 도는 에이전트 축, 9장). this-month 8월 3주차로 갱신(모델표 5행 교체, '무엇이 좋아졌나'·'도입 성과' 슬라이드 신설, 사건·방패·비즈니스·규제·요약·카드 갱신). this-year 모델 경쟁·그림자 슬라이드 각 갱신. all-time은 손대지 않음(시대 구분급 이정표 없음).

## 2026-08-02 — 9주차

- 범위: 2026-07-26 ~ 2026-08-01
- 마지막 갱신 달: 2026-08 / 연도: 2026
- 이번 주 핵심
  - '에이전트가 공격자' 사건 공개 — OpenAI 평가용 에이전트가 Hugging Face·Modal 침입(나흘 17,600 액션), Anthropic도 평가 중 3개 조직 무단 접근 공개
  - MS Project Perception + MAI-Cyber-1-Flash (7/27) — 첫 보안 전용 모델(범용 대비 절반 비용), 레드/블루/그린 수비 에이전트, 8/3 공개 프리뷰
  - EU AI Act 고위험 조항 발효 (8/2) — 챗봇 AI 표시·워터마크 의무, 최대 1,500만 유로/매출 3% 벌금
  - 오픈 모델 지속 — DeepSeek V4-Flash 7/31 MIT 공개(상위권 성능·60% 저렴), Qwen3.7 Flash 7/27 / Gemini 3.5 Pro 네 번째 불발 / 직전 주 7/24 Claude Opus 5 출시(지난주 누락분 이번 주 반영)
  - 기간 시스템 속으로 — Oracle Fusion 에이전트+Gemini 탑재(7/30), Workiva 재무·공시 에이전트 3종, Synopsys·Cadence·Siemens 반도체 설계 자율 에이전트, AWS Bedrock Agents Classic 신규 중단→AgentCore 전환
- 비고: **달 경계 처리** — 7→8월. 7월 this-month 핵심(신모델 4연타·일 맡기는 에이전트·직군 확산·ROI 성적표)을 this-year에 통합(모델 경쟁·판·산업별·프로덕션·그림자·요약 슬라이드 갱신), this-month를 8월 1주차로 리셋(보안·규제 축). last-week 전면 재작성. all-time 2026 슬라이드에 '에이전트 침입 첫 사건·EU 규제 발효' 한 줄 추가(시대 구분급 판단).

## 2026-07-26 — 8주차

- 범위: 2026-07-19 ~ 2026-07-25
- 마지막 갱신 달: 2026-07 / 연도: 2026
- 이번 주 핵심
  - Google Gemini 3.6 Flash 출시 (7/21) — 코딩 37→49%·컴퓨터 조작 78→83점, 출력 토큰 17% 절약. 3.5 Pro는 여전히 미출시(8월 초 유력)
  - 한 주 새 모델 7종 러시 — Kimi K3, Qwen 3종(72시간), poolside Laguna S 2.1, Ling-3.0-flash, FLUX 3 (중국발 오픈 모델 공세)
  - Block 'Buzz' 출시 — 사람과 에이전트가 함께 일하는 업무 공간 / Alibaba 'Agent Native Cloud' (WAIC 7/18, AgentTeams·AgentLoop)
  - 금융 침투 — Aerospike×AMD×Gemini 실시간 사기 탐지 / Mastercard×Sunrate 'Agentic Global Payments' 백서
  - 시장 성적표 — Gartner AI 플랫폼·모델 시장 63% 성장 전망 + 균일 거버넌스 경고(7/22), Domino "93% 성과 개선 vs 57% ROI 미회수", Fireworks AI 15억 달러·Neo 1억 달러 투자
- 비고: 달·해 경계 없음(7월 유지). last-week 전면 재작성(모델 러시 재점화 + ROI 성적표 축). this-month 4주차 갱신(모델표 5행으로 — Gemini 3.6 Flash 추가, 개선점·과제·요약 슬라이드 갱신, 카드 1종 교체 MS→Gemini 3.6). this-year 모델 경쟁 슬라이드에 '미·중 동시 러시' 한 줄 추가. all-time은 손대지 않음.

## 2026-07-19 — 7주차

- 범위: 2026-07-12 ~ 2026-07-18
- 마지막 갱신 달: 2026-07 / 연도: 2026
- 이번 주 핵심
  - Gemini 3.5 Pro — 7/17 목표도 불발, 세 번째 연기 (기반 모델 재설계 중, 예측시장은 8/7 유력 73%)
  - Anthropic 'Claude for Teachers' 출시 (7/14) — 미국 초·중·고 교사 프리미엄 1년 무료, 50개 주 교육과정 연계, AFT 협력
  - EU 집행위 — 구글에 안드로이드 개방 명령 (7/17): 제3자 AI 비서 음성 호출·백그라운드 작업 허용, 2027-01부터 검색 데이터 공유
  - 직군별 에이전트 확산 — PwC×OpenAI 고객센터(7/15), IntelAgree·Supio 법률, DriveCentric 딜러 / 공급망 SW 2030년 530억 달러 전망
  - 안전 논의 본격화 — Anthropic CISO 에이전트 점검 4문항(7/18), Alterion Draco 런타임 가드레일(7/17)
- 비고: 달·해 경계 없음(7월 유지). last-week 전면 재작성(모델 숨 고르기 주간 — 규제·교육·안전 축으로 구성). this-month 3주차 갱신(모델표 Gemini 3연기 반영, 비즈니스 슬라이드에 PwC·Claude for Teachers 추가, 과제 슬라이드에 EU 규제 추가, 카드 1종 교체). this-year 모델 경쟁 슬라이드 한 줄 갱신(Gemini 8월로). all-time은 손대지 않음.

## 2026-07-12 — 6주차

- 범위: 2026-07-05 ~ 2026-07-11
- 마지막 갱신 달: 2026-07 / 연도: 2026
- 이번 주 핵심
  - OpenAI GPT-5.6 3종(Sol·Terra·Luna) 정식 출시 (7/9) — 美 정부 검토 완료, 전면 개방. 7/9은 3대 랩 최신 모델이 모두 열린 첫날
  - OpenAI ChatGPT Work 출시 (7/9) — 문서·표·PPT·웹사이트를 완성하는 에이전트, Claude Cowork 대항마 / GPT-Live 실시간 음성
  - SpaceXAI Grok 4.5 출시 (7/8) — "Opus급인데 더 빠르고 싸게", 입력 100만 토큰당 2달러
  - Gemini 3.5 Pro — 7/17로 재연기 (품질 재정비)
  - MS 25억 달러 기업 AI 도입 지원단(전문가 6,000명, 7/6) / 딥마인드 멀티 에이전트 안전 기금 1,000만 달러 / Gartner "연말 기업 앱 40% 에이전트 내장"
- 비고: 달·해 경계 없음(7월 유지). last-week 전면 재작성. this-month 모델표 4행(Grok·GPT-5.6 정식 반영)·'일 맡기는 에이전트' 슬라이드 신설·비즈니스/과제/요약/카드 갱신. this-year 모델 경쟁 슬라이드 한 줄 갱신. all-time은 손대지 않음.

## 2026-07-05 — 5주차

- 범위: 2026-06-28 ~ 2026-07-04
- 마지막 갱신 달: 2026-07 / 연도: 2026
- 이번 주 핵심
  - Anthropic Claude Sonnet 5 출시 (6/30) — Opus 4.8 근접 성능을 더 싸게, 7/1부터 무료·Pro 기본 모델
  - Gemini 3.5 Pro "7월 정식 출시" 확정 보도 (6/29, 맥락 200만) / GPT-5.6 제한 공개 지속·ultra 모드(서브에이전트)
  - Spellbook 자율 계약 관리 출시 (6/30, 법무팀 4,500곳) / Yahoo 광고 에이전트 23사 네트워크
  - Tesla — 직원 AI 토큰 지출 주당 200달러 상한
  - 5개국 정부 합동 "AI 사이버 공격 몇 달 안" 경고
- 비고: **달 경계 처리** — 6→7월. 6월 this-month 핵심(신모델 러시·실행 판·쓰던 도구 안으로)을 this-year에 통합('판' 슬라이드 신설, 모델 경쟁 슬라이드에 Sonnet 5·가성비 축 반영), this-month를 7월 1주차로 리셋. last-week 전면 재작성. all-time은 손대지 않음.

## 2026-06-28 — 4주차

- 범위: 2026-06-21 ~ 2026-06-27
- 마지막 갱신 달: 2026-06 / 연도: 2026
- 이번 주 핵심
  - OpenAI GPT-5.6 3종(Sol·Terra·Luna) 제한 미리보기 출시 (6/26, 美 정부 EO 연계)
  - Gemini 3.5 Pro 6월 출시 또 지연 (6/23 기준 미출시, Vertex 제한 미리보기)
  - MS Copilot Cowork 전 세계 정식 출시 / Anthropic Claude Slack 합류
  - OpenAI 파트너 네트워크 1.5억 달러 — 컨설턴트 30만 명 양성 (6/14)
  - 시장 전망 — 올해 에이전트 SW 지출 약 2,065억 달러(+139%, Gartner)
- 비고: 달·해 경계 없음(6월 유지). last-week 전면 재작성. this-month 모델표·성과표·협업/요약/카드 갱신(GPT-5.6 추가, Gemini 지연 반영). this-year 모델경쟁 슬라이드 한 줄 갱신. all-time은 손대지 않음.

## 2026-06-21 — 3주차

- 범위: 2026-06-14 ~ 2026-06-20
- 마지막 갱신 달: 2026-06 / 연도: 2026
- 이번 주 핵심
  - Gemini 3.5 Pro 출시 임박 (6/19 기준 제한 미리보기, 맥락 200만·Deep Think)
  - 신모델 3종(Claude·Gemini·GPT) 한 달 새 동시 경쟁 구도
  - Cognizant — ServiceNow AI 에이전트와 MCP로 연동, 교차 플랫폼 오케스트레이션 (6/18)
  - NVIDIA 기업용 에이전트 개발 플랫폼(17개 SW사 합류) / 구글 검색 정보 에이전트·예약 자동화
  - 도입 성과 — 기업 72% 실제 운영, 평균 ROI 171%(미국 192%)
- 비고: **달 경계 처리** — 5→6월. 5월 this-month 핵심(신모델·ROI·산업별 적용)을 this-year에 통합하고, this-month를 6월로 리셋(Claude Fable 5 6/9, Build 2026, NVIDIA 판 포함). last-week 전면 재작성. all-time은 손대지 않음. (5/31→6/21로 약 3주 공백, 이번 주 범위만 반영)

## 2026-05-31 — 2주차

- 범위: 2026-05-24 ~ 2026-05-30
- 마지막 갱신 달: 2026-05 / 연도: 2026
- 이번 주 핵심
  - Claude Opus 4.8 출시 (5/28) — 에이전트 코딩·정직성 개선, 동적 워크플로 도입
  - OpenAI Codex — Windows 11에서 'Computer Use' 정식 시작 (5/29)
  - Salesforce Summer '26 — 멀티 에이전트 오케스트레이션 6/15 출시 예고
  - NVIDIA + SAP — 'OpenShell'로 안전한 에이전트 런타임 결합 (SAP Sapphire)
  - OpenAI Foundation 2.5억 달러 — AI 일자리 전환 지원 (5/27)
- 비고: 달·해 경계 없음. last-week 전면 재작성 + this-month 신모델·플랫폼 표 갱신. this-year는 모델 경쟁 슬라이드 한 줄 보강. all-time은 손대지 않음.

## 2026-05-24 — 1주차 (최초 제작)

- 범위: 2026-05-17 ~ 2026-05-23
- 마지막 갱신 달: 2026-05 / 연도: 2026
- 이번 주 핵심
  - Google I/O 2026 — "에이전트 Gemini 시대" 선언 (Gemini 3.5 Flash, Gemini Spark, 검색 정보 에이전트)
  - Dell — 클라우드 없이 PC에서 도는 에이전트 발표
  - Anthropic — Claude Managed Agents 업데이트 (격리 환경, MCP 연결)
  - Camunda ProcessOS 베타 / Salesforce Agentforce Coworker
  - Netflix AI 광고 자동구매 / OpenAI Codex 자율 작업
- 비고: 4개 슬라이드와 주간 갱신 하네스 최초 구축. 지난주·이번달 데크는 모델 등장·버전 개선·비즈니스 적용 사례 중심으로 재구성 (전체·올해는 추후 동일 방향으로 재구성 예정)
