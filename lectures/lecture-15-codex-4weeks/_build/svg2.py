# -*- coding: utf-8 -*-
from svg1 import DEFS, AC, ACF, ACB, _box, _arrow

# (a) 지식과 맥락의 비대칭
ASYM = """
<svg viewBox="0 0 960 268" role="img" aria-label="조수는 분야 지식이 많고 내 맥락은 전혀 모르며, 나는 지식은 적지만 내 맥락을 전부 안다">
""" + DEFS + """
<text x="0" y="16" fill="currentColor" font-size="12" font-weight="600" opacity=".55" letter-spacing="2">조수</text>
<text x="150" y="52" text-anchor="end" fill="currentColor" font-size="13" opacity=".7">분야 지식</text>
<rect x="166" y="32" width="700" height="30" rx="4" """ + ACB + """ stroke-width="1.5"/>
<text x="878" y="52" font-size="12.5" font-weight="600" """ + ACF + """>거의 전부</text>
<text x="150" y="94" text-anchor="end" fill="currentColor" font-size="13" opacity=".7">내 맥락</text>
<rect x="166" y="74" width="700" height="30" rx="4" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".35" stroke-dasharray="5 4"/>
<text x="176" y="94" fill="currentColor" font-size="12" opacity=".55">내 회사 · 내 상사 · 내가 진짜 원하는 것 — 아무것도 모릅니다</text>

<line x1="0" y1="126" x2="960" y2="126" stroke="currentColor" opacity=".18"/>

<text x="0" y="158" fill="currentColor" font-size="12" font-weight="600" opacity=".55" letter-spacing="2">나</text>
<text x="150" y="194" text-anchor="end" fill="currentColor" font-size="13" opacity=".7">분야 지식</text>
<rect x="166" y="174" width="150" height="30" rx="4" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".6"/>
<text x="328" y="194" fill="currentColor" font-size="12" opacity=".6">그래서 배우러 왔습니다</text>
<text x="150" y="236" text-anchor="end" fill="currentColor" font-size="13" opacity=".7">내 맥락</text>
<rect x="166" y="216" width="700" height="30" rx="4" """ + ACB + """ stroke-width="1.5"/>
<text x="878" y="236" font-size="12.5" font-weight="600" """ + ACF + """>나만 압니다</text>
<text x="176" y="236" fill="currentColor" font-size="12" opacity=".65">왜 하는지 · 누가 읽는지 · 무엇이 성공인지</text>
<text x="0" y="266" fill="currentColor" font-size="12.5" font-weight="600" opacity=".75">그래서 관계가 이렇게 됩니다 — 지식은 저쪽이 많고, 판단은 이쪽이 합니다.</text>
</svg>"""

# (b) 질문 비용
COST = """
<svg viewBox="0 0 960 208" role="img" aria-label="사람에게 묻는 데는 미안함과 창피함과 대기 시간이 들지만 조수에게는 들지 않아, 혼자 헤매는 대신 바로 묻게 된다">
""" + DEFS + """
<text x="0" y="16" fill="currentColor" font-size="13" font-weight="600" opacity=".55" letter-spacing="2">사람에게 물을 때 드는 비용</text>
<rect x="0" y="32" width="196" height="52" rx="6" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".65"/>
<text x="98" y="64" text-anchor="middle" fill="currentColor" font-size="15" opacity=".82">미안함</text>
<rect x="206" y="32" width="196" height="52" rx="6" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".65"/>
<text x="304" y="64" text-anchor="middle" fill="currentColor" font-size="15" opacity=".82">창피함</text>
<rect x="412" y="32" width="196" height="52" rx="6" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".65"/>
<text x="510" y="64" text-anchor="middle" fill="currentColor" font-size="15" opacity=".82">기다리는 시간</text>
<text x="626" y="64" fill="currentColor" font-size="14" opacity=".62">→ 그래서 혼자 헤맵니다</text>

<text x="0" y="128" font-size="13" font-weight="600" letter-spacing="2" """ + ACF + """>조수에게 물을 때</text>
<rect x="0" y="144" width="608" height="52" rx="6" style="stroke:var(--acc);fill:var(--acc);fill-opacity:.22" stroke-width="1.5"/>
<text x="304" y="176" text-anchor="middle" font-size="15.5" font-weight="600" """ + ACF + """>0 에 가깝습니다</text>
<rect x="626" y="144" width="334" height="52" rx="6" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".3" stroke-dasharray="5 4"/>
<text x="793" y="170" text-anchor="middle" fill="currentColor" font-size="13" opacity=".62">단, 판단과 책임의 비용은</text>
<text x="793" y="188" text-anchor="middle" fill="currentColor" font-size="13" opacity=".62">그대로 남습니다</text>
</svg>"""

# (c) 내 능력 경계
EDGE = """
<svg viewBox="0 0 960 300" role="img" aria-label="내 능력 안쪽 일을 맡기면 시간만 절약되고, 바깥쪽 일을 맡기면 혼자서는 못 만들 결과가 나온다">
""" + DEFS + """
<rect x="40" y="40" width="430" height="222" rx="12" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".45" stroke-dasharray="6 5"/>
<text x="56" y="66" fill="currentColor" font-size="12" font-weight="600" opacity=".6" letter-spacing="2">내 능력 안</text>
<text x="56" y="100" fill="currentColor" font-size="14.5" opacity=".85">메일 다듬기 · 문장 고치기 · 요약하기</text>
<text x="56" y="128" fill="currentColor" font-size="12.5" opacity=".6">내가 해도 되는 일이라 결과도 ‘내 수준’입니다</text>
<line x1="56" y1="152" x2="454" y2="152" stroke="currentColor" opacity=".2"/>
<text x="56" y="182" fill="currentColor" font-size="13" opacity=".7">절약되는 것</text>
<text x="56" y="212" fill="currentColor" font-size="20" font-weight="600" opacity=".85">30분 → 10분</text>
<text x="56" y="240" fill="currentColor" font-size="12.5" opacity=".6">고맙지만 삶이 바뀌지는 않습니다</text>

<rect x="500" y="40" width="430" height="222" rx="12" """ + ACB + """ stroke-width="1.5"/>
<text x="516" y="66" font-size="12" font-weight="600" letter-spacing="2" """ + ACF + """>내 능력 밖</text>
<text x="516" y="100" fill="currentColor" font-size="14.5">PC 점검 보고서 · 계약서 조항 비교 · 1만 줄 이상값 찾기</text>
<text x="516" y="128" fill="currentColor" font-size="12.5" opacity=".65">방법을 모르는 일이라 결과가 ‘내 수준’이 아닙니다</text>
<line x1="516" y1="152" x2="914" y2="152" stroke="currentColor" opacity=".2"/>
<text x="516" y="182" fill="currentColor" font-size="13" opacity=".7">얻는 것</text>
<text x="516" y="212" font-size="20" font-weight="600" """ + ACF + """>못 하던 일 → 되는 일</text>
<text x="516" y="240" fill="currentColor" font-size="12.5" opacity=".65">지난주 PC 점검 보고서가 이쪽이었습니다</text>
<path d="M470 150 L 496 150" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
<text x="484" y="290" text-anchor="middle" fill="currentColor" font-size="12.5" opacity=".7">“써봤는데 별거 없더라”는 왼쪽만 시켜본 사람의 말입니다</text>
</svg>"""

# (d) 숙련 경로
PATH = """
<svg viewBox="0 0 960 250" role="img" aria-label="시켜보고 안 될 때 대부분은 여기서 멈추지만, 왜 안 됐는지 묻고 빠진 것을 채워 다시 시키면 되는 일로 옮겨간다">
""" + DEFS + """
""" + _box(0, 86, 140, 56, "시켜본다") + """
<line x1="140" y1="114" x2="196" y2="114" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
""" + _box(200, 86, 140, 56, "안 된다") + """
<path d="M270 142 L 270 196" stroke="currentColor" stroke-width="1.5" opacity=".5" stroke-dasharray="5 4" marker-end="url(#ar)"/>
<rect x="160" y="200" width="220" height="42" rx="8" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".4" stroke-dasharray="5 4"/>
<text x="270" y="226" text-anchor="middle" fill="currentColor" font-size="12.5" opacity=".6">“역시 안 되네” — 대부분 여기서 멈춤</text>
<line x1="340" y1="114" x2="396" y2="114" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
<text x="368" y="104" text-anchor="middle" font-size="11.5" font-weight="600" """ + ACF + """>여기서 갈린다</text>
""" + _box(400, 86, 190, 56, "왜 안 됐는지 묻는다", acc=True) + """
<text x="495" y="166" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".65">“내가 뭘 더 알려줬어야 했어?”</text>
<line x1="590" y1="114" x2="646" y2="114" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
""" + _box(650, 86, 150, 56, "채워서 다시", acc=True) + """
<text x="725" y="166" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".65">경로 · 전제 · 형식 · 범위</text>
<line x1="800" y1="114" x2="856" y2="114" """ + AC + """ stroke-width="1.5" marker-end="url(#ara)"/>
<rect x="860" y="86" width="100" height="56" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="910" y="112" text-anchor="middle" font-size="13.5" font-weight="600" """ + ACF + """>되는 일</text>
<text x="910" y="132" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".65">1번 칸으로</text>
<path d="M910 142 C 910 220, 70 230, 70 148" fill="none" stroke="currentColor" stroke-width="1.5" opacity=".35" stroke-dasharray="6 5" marker-end="url(#ar)"/>
<text x="490" y="20" text-anchor="middle" fill="currentColor" font-size="12.5" opacity=".7">조수가 똑똑해진 게 아니라, 당신이 잘 시키게 된 것입니다</text>
</svg>"""
