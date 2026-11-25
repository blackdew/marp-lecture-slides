# -*- coding: utf-8 -*-
from svg1 import DEFS, AC, ACF, ACB, _box

# (a) 프롬프트 → 메모 → 스킬
EVOLVE = """
<svg viewBox="0 0 960 272" role="img" aria-label="매번 새로 쓰던 프롬프트가 메모에 저장되고 다시 스킬이 되면서, 기억하는 주체가 나에게서 에이전트로 넘어간다">
""" + DEFS + """
<rect x="0" y="34" width="286" height="118" rx="10" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".6"/>
<text x="16" y="60" fill="currentColor" font-size="11.5" font-weight="600" letter-spacing="1.5" opacity=".6">1단계 · 1주차</text>
<text x="16" y="88" fill="currentColor" font-size="16" font-weight="600">매번 새로 씁니다</text>
<text x="16" y="112" fill="currentColor" font-size="12.5" opacity=".65">생각나는 대로 적습니다</text>
<text x="16" y="134" fill="currentColor" font-size="12.5" opacity=".65">결과도 매번 다릅니다</text>

<line x1="292" y1="93" x2="330" y2="93" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>

<rect x="336" y="34" width="286" height="118" rx="10" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".6"/>
<text x="352" y="60" fill="currentColor" font-size="11.5" font-weight="600" letter-spacing="1.5" opacity=".6">2단계 · 지금 여기</text>
<text x="352" y="88" fill="currentColor" font-size="16" font-weight="600">메모에 저장해 복사</text>
<text x="352" y="112" fill="currentColor" font-size="12.5" opacity=".65">훨씬 낫습니다</text>
<text x="352" y="134" fill="currentColor" font-size="12.5" opacity=".65">단, 내가 기억해서 꺼내야 합니다</text>

<line x1="628" y1="93" x2="666" y2="93" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>

<rect x="672" y="34" width="288" height="118" rx="10" """ + ACB + """ stroke-width="1.5"/>
<text x="688" y="60" font-size="11.5" font-weight="600" letter-spacing="1.5" """ + ACF + """>3단계 · 오늘</text>
<text x="688" y="88" fill="currentColor" font-size="16" font-weight="600">스킬</text>
<text x="688" y="112" fill="currentColor" font-size="12.5" opacity=".7">정해진 폴더에 파일로 넣어둡니다</text>
<text x="688" y="134" fill="currentColor" font-size="12.5" opacity=".7">이름만 부르면 알아서 꺼내 씁니다</text>

<line x1="0" y1="186" x2="960" y2="186" stroke="currentColor" opacity=".18"/>
<text x="0" y="212" fill="currentColor" font-size="12" font-weight="600" opacity=".55" letter-spacing="2">누가 기억하는가</text>
<text x="143" y="246" text-anchor="middle" fill="currentColor" font-size="14" opacity=".7">아무도</text>
<text x="479" y="246" text-anchor="middle" fill="currentColor" font-size="14" opacity=".7">내가</text>
<text x="816" y="246" text-anchor="middle" font-size="15" font-weight="600" """ + ACF + """>에이전트가</text>
<text x="479" y="270" text-anchor="middle" fill="currentColor" font-size="12" opacity=".55">2단계와 3단계의 차이는 이것 하나입니다</text>
</svg>"""

# (b) description 매칭
MATCH = """
<svg viewBox="0 0 960 290" role="img" aria-label="내가 쓰는 말이 description에 들어 있으면 스킬이 불리고, description이 막연하면 불리지 않아 에이전트가 자기 방식대로 한다">
""" + DEFS + """
<text x="0" y="16" font-size="12" font-weight="600" letter-spacing="2" """ + ACF + """>불리는 경우</text>
<rect x="0" y="32" width="208" height="54" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="104" y="55" text-anchor="middle" fill="currentColor" font-size="12" opacity=".65">내가 한 말</text>
<text x="104" y="76" text-anchor="middle" font-size="14" font-weight="600" """ + ACF + """>“주보 써줘”</text>
<line x1="208" y1="59" x2="262" y2="59" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
<rect x="266" y="32" width="400" height="54" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="282" y="52" fill="currentColor" font-size="11.5" opacity=".6">description</text>
<text x="282" y="74" fill="currentColor" font-size="13">“…‘주간보고’, <tspan font-weight="600">‘주보’</tspan>, ‘이번 주 보고’ 같은 말이 나오면 쓴다.”</text>
<line x1="666" y1="59" x2="720" y2="59" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
<rect x="724" y="32" width="236" height="54" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="842" y="64" text-anchor="middle" font-size="14" font-weight="600" """ + ACF + """>스킬이 실행됩니다</text>

<line x1="0" y1="122" x2="960" y2="122" stroke="currentColor" opacity=".18"/>

<text x="0" y="152" fill="currentColor" font-size="12" font-weight="600" opacity=".55" letter-spacing="2">안 불리는 경우</text>
<rect x="0" y="168" width="208" height="54" rx="8" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".6"/>
<text x="104" y="191" text-anchor="middle" fill="currentColor" font-size="12" opacity=".6">내가 한 말</text>
<text x="104" y="212" text-anchor="middle" fill="currentColor" font-size="14" font-weight="600" opacity=".8">“주보 써줘”</text>
<line x1="208" y1="195" x2="262" y2="195" stroke="currentColor" stroke-width="1.5" opacity=".6" marker-end="url(#ar)"/>
<rect x="266" y="168" width="400" height="54" rx="8" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".45" stroke-dasharray="5 4"/>
<text x="282" y="188" fill="currentColor" font-size="11.5" opacity=".5">description</text>
<text x="282" y="210" fill="currentColor" font-size="13" opacity=".6">“보고서 작성”: 언제 꺼내야 하는지 알 수 없습니다</text>
<line x1="666" y1="195" x2="720" y2="195" stroke="currentColor" stroke-width="1.5" opacity=".45" stroke-dasharray="5 4" marker-end="url(#ar)"/>
<rect x="724" y="168" width="236" height="54" rx="8" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".45" stroke-dasharray="5 4"/>
<text x="842" y="200" text-anchor="middle" fill="currentColor" font-size="13.5" opacity=".6">그냥 자기 방식대로 씁니다</text>
<text x="0" y="266" fill="currentColor" font-size="12.5" opacity=".7">에이전트는 본문을 읽고 판단하지 않습니다. <tspan font-weight="600">description만 보고</tspan> 꺼낼지 말지 정합니다.</text>
<text x="0" y="288" fill="currentColor" font-size="12.5" opacity=".6">그래서 내가 실제로 쓰는 말이 거기 그대로 들어 있어야 합니다.</text>
</svg>"""

# (c) 금요일 반복
LOOP = """
<svg viewBox="0 0 960 250" role="img" aria-label="한 주 일하고 반복을 찾아 스킬로 만들면 다음 주가 더 빨라지고, 그 자리에 새 반복이 보이면서 스킬이 매주 하나씩 늘어난다">
""" + DEFS + """
""" + _box(30, 40, 170, 56, "한 주 일한다") + """
<line x1="200" y1="68" x2="256" y2="68" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
""" + _box(260, 40, 230, 56, "세 번 이상 한 일을 찾는다", acc=True) + """
<text x="375" y="118" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".65">“이번 주에 비슷한 걸 세 번 이상 시킨 게 있어?”</text>
<line x1="490" y1="68" x2="546" y2="68" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
""" + _box(550, 40, 170, 56, "스킬로 만든다", acc=True) + """
<line x1="720" y1="68" x2="776" y2="68" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
<rect x="780" y="40" width="150" height="56" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="855" y="66" text-anchor="middle" font-size="13.5" font-weight="600" """ + ACF + """>다음 주가</text>
<text x="855" y="86" text-anchor="middle" font-size="13.5" font-weight="600" """ + ACF + """>더 빨라진다</text>
<path d="M855 96 C 855 170, 115 180, 115 104" fill="none" """ + AC + """ stroke-width="1.5" opacity=".5" stroke-dasharray="6 5" marker-end="url(#ara)"/>
<text x="485" y="186" text-anchor="middle" fill="currentColor" font-size="12.5" opacity=".7">빨라진 자리에 새로운 반복이 보입니다. 그게 다음 주의 스킬입니다</text>
<line x1="0" y1="208" x2="960" y2="208" stroke="currentColor" opacity=".18"/>
<text x="0" y="234" fill="currentColor" font-size="12.5" opacity=".7">매주 금요일 30분이면 충분합니다. <tspan font-weight="600">반년이면 스킬 20개.</tspan> 이 강의가 끝나도 혼자 이어갈 수 있습니다.</text>
</svg>"""
