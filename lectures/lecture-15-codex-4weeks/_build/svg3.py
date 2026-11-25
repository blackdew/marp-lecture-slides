# -*- coding: utf-8 -*-
from svg1 import DEFS, AC, ACF, ACB, _box, _arrow

# (a) 남은 선택지의 수
WILL = """
<svg viewBox="0 0 960 300" role="img" aria-label="80퍼센트인 사람은 안 될 때 포기라는 선택지가 남아 있어 멈추고, 100퍼센트인 사람은 그 선택지가 없어 방법을 계속 찾는다">
""" + DEFS + """
<text x="0" y="16" fill="currentColor" font-size="12" font-weight="600" opacity=".55" letter-spacing="2">하겠다는 마음 80%</text>
""" + _box(0, 40, 116, 48, "시켜본다") + """
<line x1="116" y1="64" x2="160" y2="64" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
""" + _box(164, 40, 100, 48, "안 된다") + """
<path d="M264 56 L 330 42" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
<path d="M264 76 L 330 96" stroke="currentColor" stroke-width="1.5" opacity=".35" stroke-dasharray="5 4" marker-end="url(#ar)"/>
<rect x="336" y="18" width="250" height="40" rx="8" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".7"/>
<text x="461" y="43" text-anchor="middle" fill="currentColor" font-size="13.5" font-weight="600">“역시 아직은 안 되네”</text>
<rect x="336" y="78" width="250" height="40" rx="8" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".3" stroke-dasharray="5 4"/>
<text x="461" y="103" text-anchor="middle" fill="currentColor" font-size="13" opacity=".5">다시 해본다: 잘 선택되지 않음</text>
<text x="606" y="43" fill="currentColor" font-size="12.5" opacity=".65">→ 판단이 틀렸는지 확인할 동기가 없습니다</text>
<text x="606" y="103" fill="currentColor" font-size="12.5" opacity=".5">→ 다음에도 시도하지 않습니다</text>

<line x1="0" y1="146" x2="960" y2="146" stroke="currentColor" opacity=".18"/>

<text x="0" y="178" font-size="12" font-weight="600" letter-spacing="2" """ + ACF + """>하겠다는 마음 100%</text>
""" + _box(0, 202, 116, 48, "시켜본다", acc=True) + """
<line x1="116" y1="226" x2="160" y2="226" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
""" + _box(164, 202, 100, 48, "안 된다", acc=True) + """
<line x1="264" y1="226" x2="330" y2="226" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
<rect x="336" y="202" width="250" height="48" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="461" y="222" text-anchor="middle" font-size="13.5" font-weight="600" """ + ACF + """>“왜 안 됐지?”</text>
<text x="461" y="241" text-anchor="middle" fill="currentColor" font-size="12" opacity=".7">쪼갠다 · 전제를 바꾼다 · 다른 각도로</text>
<line x1="586" y1="226" x2="648" y2="226" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
<rect x="652" y="202" width="120" height="48" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="712" y="232" text-anchor="middle" font-size="14" font-weight="600" """ + ACF + """>보통 세 번째</text>
<text x="790" y="232" fill="currentColor" font-size="12.5" opacity=".7">에 됩니다</text>
<path d="M712 250 C 712 286, 60 290, 56 256" fill="none" """ + AC + """ stroke-width="1.5" opacity=".45" stroke-dasharray="6 5" marker-end="url(#ara)"/>
<text x="0" y="296" fill="currentColor" font-size="12" opacity=".6">포기라는 선택지를 미리 뺐기 때문에 계속 방법을 찾습니다. 능력이 아니라 남은 선택지의 수가 다릅니다.</text>
</svg>"""

# (b) 맥락 설명 vs 협업
CTX = """
<svg viewBox="0 0 960 310" role="img" aria-label="맥락을 길게 적어주면 에이전트는 그 범위 안에서만 생각하지만, 짧게 주고 질문을 받으면 내가 정하지 않은 것이 드러난다">
""" + DEFS + """
<text x="0" y="16" fill="currentColor" font-size="12" font-weight="600" opacity=".55" letter-spacing="2">맥락을 다 적어주기</text>
<rect x="0" y="34" width="250" height="92" rx="8" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".7"/>
<text x="125" y="62" text-anchor="middle" fill="currentColor" font-size="13.5" font-weight="600">내가 아는 것 전부</text>
<text x="125" y="84" text-anchor="middle" fill="currentColor" font-size="12" opacity=".6">배경 · 형식 · 참고 · 금지</text>
<text x="125" y="106" text-anchor="middle" fill="currentColor" font-size="12" opacity=".6">적다가 지칩니다</text>
<line x1="250" y1="80" x2="312" y2="80" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
<rect x="316" y="34" width="250" height="92" rx="8" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".7" stroke-dasharray="5 4"/>
<text x="441" y="70" text-anchor="middle" fill="currentColor" font-size="13.5">적어준 범위 안에서만</text>
<text x="441" y="94" text-anchor="middle" fill="currentColor" font-size="13.5">생각합니다</text>
<text x="590" y="66" fill="currentColor" font-size="12.5" opacity=".65">더 좋은 방법을 제안하지 않습니다</text>
<text x="590" y="94" fill="currentColor" font-size="12.5" opacity=".65">안 적은 전제가 잘못된 결과를 만듭니다</text>

<line x1="0" y1="152" x2="960" y2="152" stroke="currentColor" opacity=".18"/>

<text x="0" y="184" font-size="12" font-weight="600" letter-spacing="2" """ + ACF + """>짧게 주고 질문 받기</text>
<rect x="0" y="202" width="180" height="56" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="90" y="236" text-anchor="middle" font-size="13.5" font-weight="600" """ + ACF + """>한 줄 + 질문 요청</text>
<path d="M180 218 L 300 218" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
<text x="240" y="210" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".7">무엇을 하려는지</text>
<path d="M300 244 L 180 244" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
<text x="240" y="262" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".7">질문 3개</text>
<rect x="304" y="202" width="180" height="56" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="394" y="236" text-anchor="middle" font-size="13.5" font-weight="600" """ + ACF + """>에이전트</text>
<text x="394" y="186" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".65">3~5회 주고받음</text>
<line x1="484" y1="230" x2="546" y2="230" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
<rect x="550" y="202" width="410" height="56" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="755" y="226" text-anchor="middle" font-size="13.5" font-weight="600" """ + ACF + """>“아, 나 이걸 안 정했네”</text>
<text x="755" y="247" text-anchor="middle" fill="currentColor" font-size="12" opacity=".7">에이전트가 하는 질문이 내가 안 정한 부분을 드러냅니다</text>
<text x="0" y="300" fill="currentColor" font-size="12.5" opacity=".6">맥락을 전부 적어주려 하지 말고, 에이전트가 먼저 묻게 만드세요.</text>
</svg>"""

# (c) 세 가지 대화 방식
SHAPE = """
<svg viewBox="0 0 960 206" role="img" aria-label="지시형은 한 번 주고받고, 맥락 설명형은 한 번이지만 입력이 길고, 협업형은 짧은 주고받기를 여러 번 한다">
""" + DEFS + """
<text x="0" y="16" fill="currentColor" font-size="12" font-weight="600" opacity=".55" letter-spacing="2">① 지시형</text>
<line x1="0" y1="34" x2="0" y2="110" stroke="currentColor" opacity=".25"/>
<line x1="290" y1="34" x2="290" y2="110" stroke="currentColor" opacity=".25"/>
<rect x="6" y="44" width="80" height="16" rx="3" stroke="currentColor" fill="none" stroke-width="1.2" opacity=".75"/>
<line x1="88" y1="52" x2="284" y2="52" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
<line x1="284" y1="82" x2="90" y2="82" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
<rect x="6" y="74" width="80" height="16" rx="3" stroke="currentColor" fill="none" stroke-width="1.2" opacity=".4" stroke-dasharray="4 3"/>
<text x="320" y="58" fill="currentColor" font-size="12.5" opacity=".75">주고받기 1회 · 내가 쓴 시간 짧음</text>
<text x="320" y="82" fill="currentColor" font-size="12.5" opacity=".6">원한 것과 조금 다른 결과가 옵니다</text>

<text x="0" y="140" fill="currentColor" font-size="12" font-weight="600" opacity=".55" letter-spacing="2">② 맥락 설명형</text>
<line x1="0" y1="158" x2="0" y2="206" stroke="currentColor" opacity=".25"/>
<line x1="290" y1="158" x2="290" y2="206" stroke="currentColor" opacity=".25"/>
<rect x="6" y="166" width="80" height="44" rx="3" stroke="currentColor" fill="none" stroke-width="1.2" opacity=".75"/>
<line x1="88" y1="188" x2="284" y2="188" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
<line x1="284" y1="218" x2="90" y2="218" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
<text x="320" y="190" fill="currentColor" font-size="12.5" opacity=".75">주고받기 1회 · 준비에 시간이 가장 많이 듭니다</text>
<text x="320" y="214" fill="currentColor" font-size="12.5" opacity=".6">결과는 보통 ①보다 낫습니다. 저장해두면 재사용됩니다</text>

<text x="520" y="16" font-size="12" font-weight="600" letter-spacing="2" """ + ACF + """>③ 협업형</text>
<line x1="520" y1="34" x2="520" y2="110" """ + AC + """ opacity=".4"/>
<line x1="760" y1="34" x2="760" y2="110" """ + AC + """ opacity=".4"/>
<rect x="526" y="38" width="46" height="12" rx="3" """ + ACB + """ stroke-width="1.2"/>
<line x1="574" y1="44" x2="754" y2="44" """ + AC + """ stroke-width="1.4" marker-end="url(#ara)"/>
<line x1="754" y1="60" x2="576" y2="60" """ + AC + """ stroke-width="1.4" marker-end="url(#ara)"/>
<line x1="574" y1="76" x2="754" y2="76" """ + AC + """ stroke-width="1.4" marker-end="url(#ara)"/>
<line x1="754" y1="92" x2="576" y2="92" """ + AC + """ stroke-width="1.4" marker-end="url(#ara)"/>
<text x="790" y="48" fill="currentColor" font-size="12" opacity=".7">질문 3개</text>
<text x="790" y="80" fill="currentColor" font-size="12" opacity=".7">질문 3개</text>
<text x="520" y="134" fill="currentColor" font-size="12.5" opacity=".75">주고받기 3~5회 · 짧은 입력 여러 번</text>
<text x="520" y="158" font-size="12.5" font-weight="600" """ + ACF + """>내가 안 정했던 것이 질문으로 드러납니다</text>
<text x="520" y="184" fill="currentColor" font-size="12" opacity=".55">처음 하는 중요한 일에 씁니다. 익숙한 일에는 ①이 빠릅니다.</text>
</svg>"""
