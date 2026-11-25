# -*- coding: utf-8 -*-
"""2강에서 새로 쓰는 그림. 1강의 svg1 보조 함수를 그대로 씁니다."""
from svg1 import DEFS, AC, ACF, ACB, _box, _arrow     # noqa: F401

# ─────────────────────────────────────────── (a) 다음 단어 예측
PRED = """
<svg viewBox="0 0 960 296" role="img" aria-label="지금까지의 말 뒤에 올 단어의 확률을 계산해 하나를 고르고 뒤에 붙이는 과정을 반복한다">
""" + DEFS + """
<text x="0" y="14" fill="currentColor" font-size="12" font-weight="600" opacity=".55" letter-spacing="2">지금까지의 말</text>
<rect x="0" y="30" width="86" height="38" rx="5" stroke="currentColor" fill="none" stroke-width="1.4" opacity=".7"/>
<text x="43" y="55" text-anchor="middle" fill="currentColor" font-size="15">오늘</text>
<rect x="92" y="30" width="86" height="38" rx="5" stroke="currentColor" fill="none" stroke-width="1.4" opacity=".7"/>
<text x="135" y="55" text-anchor="middle" fill="currentColor" font-size="15">서울</text>
<rect x="184" y="30" width="86" height="38" rx="5" stroke="currentColor" fill="none" stroke-width="1.4" opacity=".7"/>
<text x="227" y="55" text-anchor="middle" fill="currentColor" font-size="15">날씨는</text>
<rect x="276" y="30" width="62" height="38" rx="5" """ + ACB + """ stroke-width="1.6" stroke-dasharray="5 4"/>
<text x="307" y="56" text-anchor="middle" font-size="17" font-weight="700" """ + ACF + """>?</text>

<path d="M307 68 L 307 100" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>

<rect x="90" y="106" width="434" height="142" rx="8" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".75"/>
<text x="110" y="130" fill="currentColor" font-size="12.5" font-weight="600" opacity=".7">다음에 올 말의 확률</text>
<text x="110" y="162" fill="currentColor" font-size="14">맑습니다</text>
<rect x="210" y="149" width="186" height="16" rx="3" """ + ACB + """ stroke-width="1.2"/>
<text x="410" y="162" font-size="13" font-weight="600" """ + ACF + """>62%</text>
<text x="110" y="196" fill="currentColor" font-size="14" opacity=".8">흐립니다</text>
<rect x="210" y="183" width="63" height="16" rx="3" stroke="currentColor" fill="none" stroke-width="1.2" opacity=".6"/>
<text x="410" y="196" fill="currentColor" font-size="13" opacity=".65">21%</text>
<text x="110" y="230" fill="currentColor" font-size="14" opacity=".8">춥습니다</text>
<rect x="210" y="217" width="27" height="16" rx="3" stroke="currentColor" fill="none" stroke-width="1.2" opacity=".6"/>
<text x="410" y="230" fill="currentColor" font-size="13" opacity=".65">9%</text>

<line x1="524" y1="177" x2="586" y2="177" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
<text x="555" y="167" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".7">하나를 고름</text>
<rect x="590" y="149" width="170" height="56" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="675" y="183" text-anchor="middle" font-size="15" font-weight="600" """ + ACF + """>맑습니다</text>
<path d="M760 160 C 860 110, 880 60, 360 49" fill="none" """ + AC + """ stroke-width="1.5" opacity=".75" stroke-dasharray="6 5" marker-end="url(#ara)"/>
<text x="810" y="108" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".7">뒤에 붙이고 다시</text>

<text x="0" y="286" fill="currentColor" font-size="12.5" opacity=".62">문장 전체를 미리 계획하고 쓰는 것이 아닙니다. 한 조각을 고르고, 그 조각까지 포함해 다음을 다시 고릅니다.</text>
</svg>"""

# ─────────────────────────────────────────── (b) 아직 모르는 잠재력
UNKNOWN = """
<svg viewBox="0 0 960 288" role="img" aria-label="모델 안에 있는 능력 가운데 지금까지 프롬프트로 찾아낸 부분은 일부이고, 나머지는 아직 꺼내는 말을 찾지 못한 상태다">
""" + DEFS + """
<text x="0" y="14" fill="currentColor" font-size="12" font-weight="600" opacity=".55" letter-spacing="2">학습으로 생긴 능력</text>
<rect x="0" y="28" width="560" height="208" rx="10" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".55" stroke-dasharray="6 5"/>

<rect x="28" y="120" width="196" height="92" rx="8" """ + ACB + """ stroke-width="1.6"/>
<text x="126" y="156" text-anchor="middle" font-size="14" font-weight="600" """ + ACF + """>찾아낸 사용법</text>
<text x="126" y="180" text-anchor="middle" fill="currentColor" font-size="12" opacity=".65">단계적으로 생각하게 하기</text>
<text x="126" y="198" text-anchor="middle" fill="currentColor" font-size="12" opacity=".65">예시 보여주기 · 역할 주기</text>

<rect x="252" y="54" width="84" height="56" rx="6" stroke="currentColor" fill="none" stroke-width="1.2" opacity=".32" stroke-dasharray="4 4"/>
<text x="294" y="89" text-anchor="middle" fill="currentColor" font-size="17" opacity=".3">?</text>
<rect x="352" y="54" width="84" height="56" rx="6" stroke="currentColor" fill="none" stroke-width="1.2" opacity=".32" stroke-dasharray="4 4"/>
<text x="394" y="89" text-anchor="middle" fill="currentColor" font-size="17" opacity=".3">?</text>
<rect x="452" y="54" width="84" height="56" rx="6" stroke="currentColor" fill="none" stroke-width="1.2" opacity=".32" stroke-dasharray="4 4"/>
<text x="494" y="89" text-anchor="middle" fill="currentColor" font-size="17" opacity=".3">?</text>
<rect x="252" y="126" width="84" height="56" rx="6" stroke="currentColor" fill="none" stroke-width="1.2" opacity=".32" stroke-dasharray="4 4"/>
<text x="294" y="161" text-anchor="middle" fill="currentColor" font-size="17" opacity=".3">?</text>
<rect x="352" y="126" width="184" height="56" rx="6" stroke="currentColor" fill="none" stroke-width="1.2" opacity=".32" stroke-dasharray="4 4"/>
<text x="444" y="161" text-anchor="middle" fill="currentColor" font-size="12.5" opacity=".42">아직 꺼내는 말을 못 찾은 것</text>

<line x1="560" y1="132" x2="622" y2="132" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
<text x="591" y="122" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".7">왜</text>

<text x="640" y="62" fill="currentColor" font-size="13.5" font-weight="600">가르친 게 아니라 생겼습니다</text>
<text x="640" y="84" fill="currentColor" font-size="12" opacity=".62">다음 단어를 맞히게 학습시켰더니 생긴 능력</text>
<text x="640" y="130" fill="currentColor" font-size="13.5" font-weight="600">꺼내는 말을 찾아야 나옵니다</text>
<text x="640" y="152" fill="currentColor" font-size="12" opacity=".62">같은 모델이 프롬프트에 따라 전혀 다른 결과</text>
<text x="640" y="198" fill="currentColor" font-size="13.5" font-weight="600">조합을 전수 조사할 수 없습니다</text>
<text x="640" y="220" fill="currentColor" font-size="12" opacity=".62">그래서 출시 뒤에도 계속 발견됩니다</text>

<text x="0" y="278" fill="currentColor" font-size="12.5" opacity=".62">만든 사람도 자기 모델이 무엇까지 할 수 있는지 다 모릅니다. 시켜봐야 알게 됩니다.</text>
</svg>"""

# ─────────────────────────────────────────── (c) 에이전트의 구조
LOOP = """
<svg viewBox="0 0 960 250" role="img" aria-label="컨텍스트를 받아 추론하고 도구로 실제 작업을 하고 결과를 확인해 안 됐으면 다시 반복하는 구조">
""" + DEFS + """
""" + _box(0, 54, 152, 62, "컨텍스트", "내가 준 말 + 읽은 파일") + """
""" + _arrow(152, 85, 206, 85) + """
""" + _box(210, 54, 142, 62, "추론", "다음 말을 고름", acc=True) + """
""" + _arrow(352, 85, 406, 85, acc=True) + """
""" + _box(410, 54, 168, 62, "도구", "파일 읽기·쓰기·실행", acc=True) + """
""" + _arrow(578, 85, 632, 85, acc=True) + """
""" + _box(636, 54, 152, 62, "결과 확인") + """
""" + _arrow(788, 85, 842, 85) + """
<rect x="846" y="54" width="114" height="62" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="903" y="92" text-anchor="middle" font-size="15" font-weight="600" """ + ACF + """>끝</text>
<path d="M712 116 C 712 186, 76 196, 76 122" fill="none" stroke="currentColor" stroke-width="1.5" opacity=".45" stroke-dasharray="6 5" marker-end="url(#ar)"/>
<text x="394" y="192" text-anchor="middle" fill="currentColor" font-size="12.5" opacity=".7">안 됐으면 스스로 다시 — 1강에서 화면으로 본 그 반복</text>
<text x="0" y="22" fill="currentColor" font-size="12" font-weight="600" opacity=".55" letter-spacing="2">에이전트 = 추론 + 도구 + 반복</text>
<text x="0" y="240" fill="currentColor" font-size="12.5" opacity=".62">챗봇은 가운데 칸까지입니다. 도구와 반복이 붙으면 말이 아니라 결과물이 남습니다.</text>
</svg>"""

# ─────────────────────────────────────────── (d) 세 가지 사용법
WAYS = """
<svg viewBox="0 0 960 236" role="img" aria-label="프롬프트 엔지니어링은 내가 다 적고, 협력적 프롬프팅은 주고받으며 채우고, 메타프롬프트는 에이전트가 프롬프트를 써준다">
""" + DEFS + """
<text x="0" y="14" font-size="12" font-weight="600" letter-spacing="2" fill="currentColor" opacity=".55">① 프롬프트 엔지니어링</text>
<rect x="0" y="30" width="78" height="86" rx="6" stroke="currentColor" fill="none" stroke-width="1.4" opacity=".75"/>
<text x="39" y="78" text-anchor="middle" fill="currentColor" font-size="13.5" font-weight="600">나</text>
<line x1="78" y1="73" x2="206" y2="73" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
<text x="142" y="63" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".7">긴 프롬프트 1회</text>
<rect x="210" y="44" width="80" height="58" rx="6" stroke="currentColor" fill="none" stroke-width="1.4" opacity=".75"/>
<text x="250" y="78" text-anchor="middle" fill="currentColor" font-size="12.5">에이전트</text>
<text x="0" y="142" fill="currentColor" font-size="12.5" opacity=".72">목적 · 조건 · 형식 · 검증을 내가 적습니다</text>
<text x="0" y="164" fill="currentColor" font-size="12" opacity=".55">익숙한 일에 빠릅니다. 안 적은 전제는 반영되지 않습니다</text>

<line x1="320" y1="20" x2="320" y2="200" stroke="currentColor" opacity=".16"/>

<text x="348" y="14" font-size="12" font-weight="600" letter-spacing="2" fill="currentColor" opacity=".55">② 협력적 프롬프팅</text>
<rect x="348" y="30" width="78" height="86" rx="6" stroke="currentColor" fill="none" stroke-width="1.4" opacity=".75"/>
<text x="387" y="78" text-anchor="middle" fill="currentColor" font-size="13.5" font-weight="600">나</text>
<line x1="426" y1="52" x2="550" y2="52" stroke="currentColor" stroke-width="1.4" opacity=".8" marker-end="url(#ar)"/>
<line x1="550" y1="76" x2="428" y2="76" stroke="currentColor" stroke-width="1.4" opacity=".8" marker-end="url(#ar)"/>
<line x1="426" y1="100" x2="550" y2="100" stroke="currentColor" stroke-width="1.4" opacity=".8" marker-end="url(#ar)"/>
<text x="488" y="42" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".7">한두 줄</text>
<text x="488" y="94" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".7">질문 3개</text>
<rect x="554" y="44" width="80" height="58" rx="6" stroke="currentColor" fill="none" stroke-width="1.4" opacity=".75"/>
<text x="594" y="78" text-anchor="middle" fill="currentColor" font-size="12.5">에이전트</text>
<text x="348" y="142" fill="currentColor" font-size="12.5" opacity=".72">짧게 주고, 되묻게 만들어 답하면서 채웁니다</text>
<text x="348" y="164" fill="currentColor" font-size="12" opacity=".55">내가 안 정했던 것이 질문으로 드러납니다</text>

<line x1="664" y1="20" x2="664" y2="200" stroke="currentColor" opacity=".16"/>

<text x="692" y="14" font-size="12" font-weight="600" letter-spacing="2" """ + ACF + """>③ 메타프롬프트</text>
<rect x="692" y="30" width="78" height="86" rx="6" """ + ACB + """ stroke-width="1.5"/>
<text x="731" y="78" text-anchor="middle" font-size="13.5" font-weight="600" """ + ACF + """>나</text>
<line x1="770" y1="48" x2="876" y2="48" """ + AC + """ stroke-width="1.4" marker-end="url(#ara)"/>
<text x="823" y="38" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".7">무엇을 하려는지</text>
<line x1="876" y1="100" x2="772" y2="100" """ + AC + """ stroke-width="1.4" marker-end="url(#ara)"/>
<text x="823" y="118" text-anchor="middle" font-size="11.5" font-weight="600" """ + ACF + """>프롬프트</text>
<rect x="880" y="44" width="80" height="58" rx="6" """ + ACB + """ stroke-width="1.5"/>
<text x="920" y="78" text-anchor="middle" font-size="12.5" font-weight="600" """ + ACF + """>에이전트</text>
<text x="692" y="142" fill="currentColor" font-size="12.5" opacity=".72">프롬프트를 써달라고 먼저 시킵니다</text>
<text x="692" y="164" fill="currentColor" font-size="12" opacity=".55">받은 것을 읽어보고 고쳐서 실행합니다</text>

<text x="0" y="214" fill="currentColor" font-size="12.5" opacity=".62">우열이 아닙니다. 일의 성격과 사람에 따라 맞는 것이 다릅니다 — 오늘 세 번 다 해보고 고르세요.</text>
</svg>"""
