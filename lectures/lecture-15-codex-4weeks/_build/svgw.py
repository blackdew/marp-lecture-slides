# -*- coding: utf-8 -*-
"""장표용 픽토그램. 전부 currentColor 라서 다크·라이트에서 같이 보입니다."""

def _s(label, body, vb="0 0 120 120"):
    return ('<svg viewBox="%s" role="img" aria-label="%s" fill="none" stroke="currentColor" '
            'stroke-width="3" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % (vb, label, body))

def _ppl(n, on, y=60, x0=8, gap=11.5, r=3.4):
    o = []
    for i in range(n):
        x = x0 + i * gap
        op = '' if i < on else ' opacity=".25"'
        o.append('<circle cx="%.1f" cy="%.1f" r="%.1f"%s/>' % (x, y - 8, r, op))
        o.append('<path d="M%.1f %.1fv-6a%.1f %.1f 0 0 1 %.1f 0v6"%s/>' % (x - 4.6, y + 9, 4.6, 4.6, 9.2, op))
    return "".join(o)

# ---------------- 열기 / 마무리
CLOCKFAST = _s("빠르게 도는 시계", """
<circle cx="52" cy="60" r="34"/><path d="M52 40v20h15"/>
<path d="M94 42a38 38 0 0 1 0 36" opacity=".5"/><path d="M104 34a50 50 0 0 1 0 52" opacity=".3"/>""")

SUNLINE = _s("떠오르고 지는 해", """
<path d="M8 84h104"/><path d="M34 84a26 26 0 0 1 52 0"/>
<path d="M60 36v-10M30 46l-7-7M90 46l7-7M14 64H6M114 64h-8" opacity=".6"/>""")

# ---------------- 전환
BOX1 = _s("가득 찬 상자 하나", """
<rect x="26" y="26" width="68" height="68" rx="8"/>
<path d="M26 46h68M26 62h68M26 78h68" opacity=".45"/>""")

BOX3 = _s("상자 세 개", """
<rect x="6" y="40" width="32" height="40" rx="6"/>
<rect x="44" y="40" width="32" height="40" rx="6"/>
<rect x="82" y="40" width="32" height="40" rx="6"/>
<path d="M14 56h16M52 56h16M90 56h16" opacity=".45"/>""")

TRIO = _s("문서와 칠판과 실험용 플라스크", """
<rect x="6" y="36" width="28" height="48" rx="4"/><path d="M13 50h14M13 60h14M13 70h9" opacity=".5"/>
<rect x="46" y="34" width="34" height="28" rx="4"/><path d="M63 62v12M53 86l10-12M73 86l-10-12"/>
<path d="M96 34v16l-10 26a6 6 0 0 0 6 8h16a6 6 0 0 0 6-8l-10-26V34"/><path d="M92 34h16"/>""")

TWOUP = _s("나란히 올라가는 두 선", """
<path d="M10 96L44 62l18 16 38-44"/><path d="M84 34h16v16" opacity=".8"/>
<path d="M10 72L40 50l16 12 30-26" opacity=".4"/>""")

ACCEL = _s("점점 빨라지는 화살표", """
<path d="M16 60h74"/><path d="M76 44l16 16-16 16"/>
<path d="M14 42h40" opacity=".45"/><path d="M14 78h40" opacity=".45"/>
<path d="M100 36v48" opacity=".25"/>""")

NUM3 = _s("숫자가 들어갈 칸 세 개", """
<rect x="4" y="42" width="32" height="36" rx="5" stroke-dasharray="5 5"/>
<rect x="44" y="42" width="32" height="36" rx="5" stroke-dasharray="5 5"/>
<rect x="84" y="42" width="32" height="36" rx="5" stroke-dasharray="5 5"/>""")

CLOCK = _s("시계", """<circle cx="60" cy="60" r="38"/><path d="M60 36v24h18"/>""")

DOOR = _s("열린 문", """
<rect x="30" y="18" width="52" height="86" rx="4"/><path d="M30 18l24-8v92l-24 4" opacity=".5"/>
<circle cx="44" cy="62" r="2.6" fill="currentColor" stroke="none"/>
<path d="M90 44l16 16-16 16M106 60H74" opacity=".55"/>""")

# ---------------- 친구들
FOUR = _s("사람 네 명", _ppl(4, 4, y=62, x0=22, gap=26, r=7))

BOXDONE = _s("완성 표시가 된 상자", """
<rect x="20" y="30" width="80" height="64" rx="8"/><path d="M20 48h80"/>
<path d="M44 70l12 12 22-26"/>""")

BOOK = _s("펼친 책", """
<path d="M60 34v62"/><path d="M60 34c-12-8-28-8-44-6v60c16-2 32-2 44 6"/>
<path d="M60 34c12-8 28-8 44-6v60c-16-2-32-2-44 6"/>""")

BUILDING = _s("건물", """
<rect x="26" y="20" width="68" height="84" rx="4"/>
<path d="M40 38h12M68 38h12M40 58h12M68 58h12M40 78h12M68 78h12"/>
<path d="M52 104v-14h16v14"/>""")

BADGE = _s("배지", """
<path d="M60 14l34 14v28c0 24-16 40-34 50-18-10-34-26-34-50V28z"/>
<path d="M46 60l10 10 20-22"/>""")

CAL = _s("달력", """
<rect x="16" y="26" width="88" height="80" rx="7"/><path d="M16 48h88M40 16v18M80 16v18"/>
<circle cx="60" cy="74" r="12"/>""")

# ---------------- 어떻게 가능한가
STANDBY = _s("옆에 서서 기다리는 사람", """
<circle cx="34" cy="34" r="12"/><path d="M14 94v-22a20 20 0 0 1 40 0v22"/>
<circle cx="86" cy="34" r="12" opacity=".9"/><path d="M66 94v-22a20 20 0 0 1 40 0v22" opacity=".9"/>
<rect x="72" y="62" width="28" height="18" rx="3"/>""")

EXAM = _s("시험지", """
<rect x="24" y="14" width="72" height="92" rx="6"/>
<path d="M38 38h32M38 54h44M38 70h44M38 86h24" opacity=".6"/>
<circle cx="86" cy="34" r="14"/>""")

SCALE = _s("한쪽으로 크게 기운 저울", """
<path d="M60 18v84M34 102h52"/><path d="M14 38h92" transform="rotate(-16 60 38)"/>
<path d="M12 44l-8 20a14 14 0 0 0 28 0z"/><path d="M104 32l-8 20a14 14 0 0 0 28 0z"/>""")

BOARD = _s("수식이 적힌 칠판", """
<rect x="10" y="18" width="100" height="70" rx="6"/>
<path d="M26 40h20M36 30v20M58 38l16 14M74 38L58 52M86 44h14" opacity=".75"/>
<path d="M44 88v16M76 88v16" opacity=".5"/>""")

LOCK = _s("자물쇠", """
<rect x="26" y="52" width="68" height="52" rx="8"/>
<path d="M42 52V38a18 18 0 0 1 36 0v14"/>
<circle cx="60" cy="74" r="5"/><path d="M60 79v10"/>""")

RANK = _s("순위표 1위", """
<rect x="8" y="58" width="28" height="46" rx="3" opacity=".45"/>
<rect x="46" y="30" width="28" height="74" rx="3"/>
<rect x="84" y="70" width="28" height="34" rx="3" opacity=".45"/>
<path d="M56 46l4-4v18" /><path d="M22 14h32M38 14v10" opacity=".5"/>""")

GAMESCR = _s("설명 없는 게임 화면", """
<rect x="12" y="24" width="96" height="66" rx="6"/>
<rect x="28" y="40" width="16" height="16" rx="2"/><circle cx="78" cy="48" r="9"/>
<path d="M52 76l10-14 10 14z"/><path d="M44 104h32" opacity=".5"/>""")

EXCL = _s("느낌표", """<circle cx="60" cy="60" r="42"/><path d="M60 36v30"/>
<circle cx="60" cy="80" r="3.4" fill="currentColor" stroke="none"/>""")

MED = _s("의료 십자", """<rect x="16" y="22" width="88" height="76" rx="10"/>
<path d="M60 40v40M40 60h40"/>""")

CELL = _s("세포와 핵", """<circle cx="60" cy="60" r="40"/><circle cx="60" cy="60" r="14"/>
<circle cx="36" cy="42" r="3" fill="currentColor" stroke="none" opacity=".6"/>
<circle cx="86" cy="74" r="3" fill="currentColor" stroke="none" opacity=".6"/>
<circle cx="42" cy="86" r="3" fill="currentColor" stroke="none" opacity=".6"/>
<circle cx="84" cy="36" r="3" fill="currentColor" stroke="none" opacity=".6"/>""")

BUBBLEDOC = _s("말풍선과 서류", """
<path d="M6 26h46a6 6 0 0 1 6 6v26a6 6 0 0 1-6 6H28l-12 10V64H6a6 6 0 0 1-6-6V32a6 6 0 0 1 6-6z"
 transform="translate(6 8)"/>
<rect x="72" y="26" width="42" height="60" rx="5"/>
<path d="M82 44h22M82 56h22M82 68h14" opacity=".6"/>""")

ARROWBREAK = _s("끊긴 화살표와 이어진 화살표", """
<path d="M8 36h22M42 36h22M76 36h18" stroke-dasharray="0" opacity=".45"/>
<path d="M86 28l9 8-9 8" opacity=".45"/>
<path d="M8 82h86"/><path d="M86 74l9 8-9 8"/>""")

ARROW3 = _s("나란히 가는 화살표 셋", """
<path d="M10 34h78M80 26l9 8-9 8"/>
<path d="M10 60h78M80 52l9 8-9 8"/>
<path d="M10 86h78M80 78l9 8-9 8"/>""")

PPL65 = _s("열 명 중 일곱 명", _ppl(10, 7))
PPL20 = _s("열 명 중 두 명", _ppl(10, 2))

EMPTY = _s("비어 있는 칸", """
<rect x="14" y="34" width="92" height="52" rx="8" stroke-dasharray="6 7"/>
<path d="M50 60h20" opacity=".45"/>""")

BARS2 = _s("낮은 막대와 높은 막대", """
<path d="M8 104h104" opacity=".5"/>
<rect x="24" y="90" width="28" height="14" rx="2" opacity=".5"/>
<rect x="70" y="24" width="28" height="80" rx="2"/>""")

# ---------------- 실습
FINGER = _s("가리키는 손", """
<path d="M52 56V26a8 8 0 0 1 16 0v38"/><path d="M68 50a8 8 0 0 1 16 0v14"/>
<path d="M84 56a8 8 0 0 1 16 0v22a28 28 0 0 1-28 28H62a24 24 0 0 1-18-8L26 78a8 8 0 0 1 12-10l14 12"/>""")

SCREEN = _s("화면과 커서", """
<rect x="10" y="22" width="100" height="66" rx="6"/><path d="M44 104h32M60 88v16"/>
<path d="M30 44h24" opacity=".6"/><rect x="30" y="56" width="12" height="14" fill="currentColor" stroke="none"/>""")

REDO = _s("되돌아오는 화살표", """
<path d="M98 60a38 38 0 1 1-12-28"/><path d="M86 10v24H62"/>""")

STETH = _s("청진기", """
<path d="M34 18v24a22 22 0 0 0 44 0V18"/><path d="M26 18h16M70 18h16"/>
<path d="M56 64v10a22 22 0 0 0 30 20"/><circle cx="94" cy="88" r="12"/>""")

FOLDER = _s("폴더", """
<path d="M12 34a6 6 0 0 1 6-6h26l10 12h48a6 6 0 0 1 6 6v46a6 6 0 0 1-6 6H18a6 6 0 0 1-6-6z"/>
<path d="M12 56h96" opacity=".5"/>""")

GAMEPAD = _s("게임 패드", """
<rect x="8" y="40" width="104" height="46" rx="20"/>
<path d="M30 54v18M21 63h18"/><circle cx="86" cy="56" r="4.5" fill="currentColor" stroke="none"/>
<circle cx="96" cy="70" r="4.5" fill="currentColor" stroke="none"/>""")

CAL7 = _s("일곱 칸 달력", """
<rect x="4" y="44" width="112" height="34" rx="5"/>
<path d="M20 44v34M36 44v34M52 44v34M68 44v34M84 44v34M100 44v34"/>""")

# ---------------- 기존 위트용
KEYBOARD = _s("키보드 위에 한국어 말풍선", """
<path d="M32 12h56a10 10 0 0 1 10 10v20a10 10 0 0 1-10 10H56l-13 11V52h-11a10 10 0 0 1-10-10V22a10 10 0 0 1 10-10z"/>
<text x="60" y="39" text-anchor="middle" font-size="15" font-weight="600" fill="currentColor" stroke="none">한국어</text>
<rect x="8" y="76" width="104" height="36" rx="7"/>
<path d="M20 86h8M36 86h8M52 86h8M68 86h8M84 86h8M100 86h2M20 98h4M32 98h56M96 98h4"/>""")

TIMER = _s("타이머", """<circle cx="60" cy="70" r="38"/><path d="M46 14h28M60 14v14"/>
<path d="M60 48v22h16"/><path d="M94 38l8-8M26 38l-8-8"/>""")

POWER = _s("전원 버튼", """<circle cx="60" cy="62" r="40"/>
<path d="M44 42a22 22 0 1 0 32 0"/><path d="M60 32v26" stroke-width="5"/>""")

QUIET = _s("소리를 줄인 스피커", """<path d="M16 48h18l24-20v64L34 72H16z"/>
<path d="M74 52a18 18 0 0 1 0 28"/><path d="M92 40l20 20M112 40L92 60" opacity=".45"/>""")

YN = _s("y 키와 n 키", """<rect x="8" y="40" width="46" height="46" rx="9"/>
<text x="31" y="72" text-anchor="middle" font-size="27" font-weight="700" fill="currentColor" stroke="none">y</text>
<rect x="66" y="40" width="46" height="46" rx="9" opacity=".35"/>
<text x="89" y="72" text-anchor="middle" font-size="27" font-weight="700" fill="currentColor" stroke="none" opacity=".35">n</text>""")

TERM = _s("커서가 깜빡이는 터미널", """<rect x="10" y="30" width="100" height="64" rx="8"/><path d="M10 48h100"/>
<circle cx="23" cy="39" r="2.5" fill="currentColor" stroke="none"/>
<circle cx="33" cy="39" r="2.5" fill="currentColor" stroke="none"/>
<circle cx="43" cy="39" r="2.5" fill="currentColor" stroke="none"/>
<text x="24" y="76" font-size="17" font-weight="700" fill="currentColor" stroke="none">&gt;</text>
<rect x="40" y="62" width="13" height="18" rx="2" fill="currentColor" stroke="none"/>""")

# ---------------- 세상 변화 / 마무리
ROBOT = _s("휴머노이드 로봇", """
<rect x="34" y="30" width="52" height="40" rx="10"/>
<circle cx="50" cy="48" r="4" fill="currentColor" stroke="none"/>
<circle cx="70" cy="48" r="4" fill="currentColor" stroke="none"/>
<path d="M60 18v12"/><circle cx="60" cy="14" r="4"/>
<rect x="40" y="76" width="40" height="32" rx="6"/>
<path d="M34 82H20v20M86 82h14v20"/>""")

CAR = _s("자율주행 차", """
<path d="M14 72l10-26a8 8 0 0 1 7-5h58a8 8 0 0 1 7 5l10 26"/>
<rect x="10" y="72" width="100" height="26" rx="8"/>
<circle cx="34" cy="98" r="8"/><circle cx="86" cy="98" r="8"/>
<path d="M40 46h40" opacity=".5"/>
<circle cx="60" cy="60" r="5"/><path d="M60 50v-8" opacity=".6"/>""")

RETRY = _s("여러 번 반복해서 시도하는 화살표", """
<path d="M98 60a38 38 0 1 1-11-27"/><path d="M88 8v26H62"/>
<circle cx="60" cy="104" r="3" fill="currentColor" stroke="none" opacity=".5"/>
<circle cx="76" cy="104" r="3" fill="currentColor" stroke="none" opacity=".7"/>
<circle cx="92" cy="104" r="3" fill="currentColor" stroke="none"/>""")

GAUGE100 = _s("100까지 찬 눈금", """
<path d="M14 88a46 46 0 0 1 92 0" stroke-width="4" opacity=".25"/>
<path d="M14 88a46 46 0 0 1 92 0" stroke-width="4"/>
<path d="M60 88L92 54" stroke-width="4"/>
<circle cx="60" cy="88" r="6" fill="currentColor" stroke="none"/>
<text x="60" y="114" text-anchor="middle" font-size="19" font-weight="700" fill="currentColor" stroke="none">100%</text>""")

# ---------------- 장면 그림 (큰 삽화)
_AC = 'style="stroke:var(--acc)"'

NIGHT = ('<svg viewBox="0 0 320 250" role="img" '
 'aria-label="늦은 밤 모니터 두 대 앞에 앉은 사람과 쌓인 커피잔" '
 'fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">'
 # 창문과 밤
 '<rect x="214" y="8" width="96" height="72" rx="5" opacity=".55"/>'
 '<path d="M262 8v72M214 44h96" opacity=".3"/>'
 '<path d="M248 30a11 11 0 1 0 10 14 13 13 0 0 1-10-14z" opacity=".7"/>'
 '<path d="M228 60h.01M292 22h.01M296 62h.01" stroke-width="3.4" opacity=".6"/>'
 # 벽시계 — 11시 10분
 '<circle cx="40" cy="36" r="22" opacity=".55"/>'
 '<path d="M40 22v14l9 5" opacity=".55"/>'
 # 책상
 '<path d="M4 196h312"/>'
 '<path d="M30 196v34M290 196v34" opacity=".5"/>'
 # 모니터 1
 '<rect x="96" y="104" width="104" height="68" rx="5" ' + _AC + '/>'
 '<path d="M148 172v16M130 192h36" opacity=".6"/>'
 '<path d="M110 122h52M110 134h70M110 146h40" ' + _AC + ' opacity=".75"/>'
 '<path d="M110 158h26" stroke-width="3.2" ' + _AC + '/>'
 # 모니터 2
 '<rect x="210" y="116" width="78" height="56" rx="5" opacity=".6"/>'
 '<path d="M249 172v16M234 192h30" opacity=".45"/>'
 '<path d="M222 132h40M222 144h30" opacity=".45"/>'
 # 사람 뒷모습
 '<circle cx="48" cy="126" r="19"/>'
 '<path d="M14 196v-20a34 34 0 0 1 68 0v20"/>'
 '<path d="M8 196v-44a10 10 0 0 1 10-10" opacity=".45"/>'
 # 커피잔 셋
 '<path d="M236 196v-14h18v14M254 186h6a5 5 0 0 1 0 10h-6" opacity=".8"/>'
 '<path d="M266 196v-10h14v10" opacity=".55"/>'
 '<path d="M286 196v-8h12v8" opacity=".4"/>'
 '</svg>')
