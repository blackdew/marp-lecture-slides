# -*- coding: utf-8 -*-
"""2주차 픽토그램. 1주차 svgw.py 와 같은 방식(120x120, currentColor 선)으로 그립니다.

글자는 물음표처럼 기호 하나만 넣습니다. 설명은 장표의 문장과 발표자 노트에 둡니다.
"""
from svgw import _s

_Q = ('<text x="%d" y="%d" text-anchor="middle" font-size="%d" font-weight="700" '
      'fill="currentColor" stroke="none"%s>?</text>')


def _doc(n):
    """줄이 n개 적힌 문서. 마지막 줄만 굵게 그려 새로 덧붙인 줄임을 나타냅니다."""
    o = ['<rect x="26" y="12" width="68" height="96" rx="7"/>']
    for i in range(n):
        y = 34 + i * 18
        last = (i == n - 1)
        o.append('<path d="M40 %dh%d"%s/>' % (y, 40 if last else 34,
                 ' stroke-width="5"' if last else ' opacity=".4"'))
    return "".join(o)


DOC1 = _s("한 줄이 적힌 문서", _doc(1))
DOC2 = _s("두 줄이 적힌 문서", _doc(2))
DOC3 = _s("세 줄이 적힌 문서", _doc(3))
DOC4 = _s("네 줄이 적힌 문서", _doc(4))
DOC5 = _s("다섯 줄이 적힌 문서", _doc(5))

QBUBBLE = _s("물음표가 든 말풍선", """
<path d="M24 18h72a10 10 0 0 1 10 10v42a10 10 0 0 1-10 10H62l-20 18V80H24a10 10 0 0 1-10-10V28a10 10 0 0 1 10-10z"/>
""" + _Q % (60, 63, 38, ''))

BLANK = _s("낱말 두 개와 비어 있는 다음 칸", """
<rect x="4" y="42" width="32" height="36" rx="5"/><path d="M12 60h16" opacity=".5"/>
<rect x="44" y="42" width="32" height="36" rx="5"/><path d="M52 60h16" opacity=".5"/>
<rect x="84" y="42" width="32" height="36" rx="5" stroke-dasharray="5 5"/>
""" + _Q % (100, 68, 22, ''))

NEXT = _s("예측한 낱말을 붙이고 다시 예측하는 과정", """
<rect x="4" y="30" width="30" height="34" rx="5" opacity=".5"/>
<rect x="42" y="30" width="30" height="34" rx="5" opacity=".5"/>
<rect x="84" y="30" width="30" height="34" rx="5" fill="currentColor"/>
<path d="M99 72v10a10 10 0 0 1-10 10H26"/><path d="M36 82l-10 10 10 10"/>""")

TWODOC = _s("같은 요청에서 나온 서로 다른 문서 두 개", """
<path d="M12 46h26a6 6 0 0 1 6 6v14a6 6 0 0 1-6 6H24l-8 8v-8h-4a6 6 0 0 1-6-6V52a6 6 0 0 1 6-6z"/>
<path d="M50 52l16-16M50 68l16 16" opacity=".6"/>
<rect x="72" y="8" width="40" height="46" rx="5"/>
<path d="M80 22h24M80 31h24M80 40h14" opacity=".55"/>
<rect x="72" y="66" width="40" height="46" rx="5"/>
<path d="M88 80h16M88 89h16M88 98h16" opacity=".55"/>
<path d="M81 80h.01M81 89h.01M81 98h.01" stroke-width="4"/>""")

UNKNOWN = _s("확인한 능력의 작은 칸과 아직 확인하지 못한 넓은 범위", """
<rect x="8" y="12" width="104" height="96" rx="10" stroke-dasharray="6 7" opacity=".7"/>
<rect x="20" y="60" width="40" height="36" rx="6"/><path d="M31 78l7 7 12-14"/>
""" + _Q % (86, 56, 30, ' opacity=".7"'))

NOTME = _s("내용이 적힌 문서와 점선으로 그린 사람", """
<rect x="6" y="28" width="46" height="64" rx="6"/>
<path d="M16 44h26M16 56h26M16 68h26M16 80h16" opacity=".5"/>
<circle cx="88" cy="42" r="13" stroke-dasharray="5 5"/>
<path d="M66 94V80a22 22 0 0 1 44 0v14" stroke-dasharray="5 5"/>""")

ASK = _s("짧은 요청 말풍선과 물음표로 답하는 말풍선", """
<path d="M16 12h34a9 9 0 0 1 9 9v16a9 9 0 0 1-9 9H32l-10 9v-9h-6a9 9 0 0 1-9-9V21a9 9 0 0 1 9-9z" opacity=".5"/>
<path d="M19 29h28" opacity=".5"/>
<path d="M60 56h44a9 9 0 0 1 9 9v22a9 9 0 0 1-9 9h-6v10l-11-10H60a9 9 0 0 1-9-9V65a9 9 0 0 1 9-9z"/>
""" + _Q % (82, 86, 26, ''))

PENDOC = _s("문서와 연필", """
<rect x="14" y="12" width="62" height="96" rx="7"/>
<path d="M28 34h34M28 50h34M28 66h20" opacity=".45"/>
<path d="M62 92l38-38 12 12-38 38-15 3z"/><path d="M92 62l12 12" opacity=".6"/>""")

FIXDOC = _s("한 줄을 고치고 확인 표시를 한 문서", """
<rect x="12" y="12" width="66" height="96" rx="7"/>
<path d="M26 34h38M26 70h38M26 88h22" opacity=".4"/>
<path d="M26 52h38" stroke-width="5"/>
<path d="M88 78l9 9 17-21" stroke-width="4"/>""")

PICK = _s("세 칸 가운데 고른 한 칸", """
<rect x="4" y="40" width="32" height="40" rx="6" opacity=".4"/>
<rect x="44" y="36" width="32" height="48" rx="6" stroke-width="4"/>
<path d="M52 60l6 7 11-14" stroke-width="4"/>
<rect x="84" y="40" width="32" height="40" rx="6" opacity=".4"/>""")

SEARCH = _s("돋보기 안의 사람", """
<circle cx="50" cy="50" r="34"/><path d="M75 75l31 31" stroke-width="5"/>
<circle cx="50" cy="42" r="9"/><path d="M33 68a17 17 0 0 1 34 0"/>""")

ONE = _s("조절 막대 셋 가운데 하나만 옮긴 모습", """
<path d="M12 32h96M12 60h96M12 88h96" opacity=".4"/>
<circle cx="42" cy="32" r="7" opacity=".45"/>
<circle cx="80" cy="60" r="9" fill="currentColor"/>
<circle cx="42" cy="88" r="7" opacity=".45"/>""")

DOCGAP = _s("한 줄이 비어 있는 문서", """
<rect x="26" y="12" width="68" height="96" rx="7"/>
<path d="M40 34h40M40 52h40M40 88h26" opacity=".4"/>
<path d="M40 70h40" stroke-width="5" stroke-dasharray="6 7"/>""")

MORE = _s("점점 늘어나는 칸", """
<rect x="6" y="46" width="24" height="28" rx="5"/>
<rect x="38" y="46" width="24" height="28" rx="5"/>
<rect x="70" y="46" width="24" height="28" rx="5" opacity=".55"/>
<rect x="102" y="46" width="14" height="28" rx="5" stroke-dasharray="4 5" opacity=".4"/>
<path d="M82 18v16M74 26h16"/>""")

LINK3 = _s("서로 이어진 세 칸", """
<rect x="42" y="8" width="36" height="30" rx="6"/>
<rect x="6" y="80" width="36" height="30" rx="6"/>
<rect x="78" y="80" width="36" height="30" rx="6"/>
<path d="M50 44L32 74M70 44l18 30M48 95h24"/>
<path d="M30 62l2 12 11-5M79 69l9 5 3-11M64 89l8 6-8 6" opacity=".7"/>""")

SAVEDOC = _s("보관함에 넣는 문서", """
<rect x="40" y="6" width="40" height="50" rx="5"/>
<path d="M49 20h22M49 30h22M49 40h12" opacity=".5"/>
<path d="M60 62v22M50 76l10 10 10-10"/>
<path d="M12 74v26a8 8 0 0 0 8 8h80a8 8 0 0 0 8-8V74"/>""")

ENVELOPE = _s("카드가 든 봉투", """
<rect x="12" y="30" width="96" height="66" rx="7"/>
<path d="M12 38l48 34 48-34"/>
<path d="M60 20c-5-9-18-5-14 5 3 7 14 13 14 13s11-6 14-13c4-10-9-14-14-5z" opacity=".55"/>""")

# ── 실습에서 에이전트가 조작하는 것
POINTER = _s("앱 창 안에서 움직이는 마우스 화살표", """
<rect x="10" y="18" width="100" height="76" rx="7"/><path d="M10 34h100" opacity=".5"/>
<circle cx="36" cy="64" r="13" opacity=".5"/>
<path d="M62 46v36l9-9 7 16 7-3-7-16h13z" fill="currentColor" stroke="none"/>""")

UPLOAD = _s("지구로 올라가는 화살표", """
<circle cx="60" cy="38" r="26"/>
<path d="M34 38h52M60 12c-13 11-13 41 0 52M60 12c13 11 13 41 0 52" opacity=".5"/>
<path d="M60 110V76M47 89l13-13 13 13" stroke-width="4"/>""")

WEBSEARCH = _s("돋보기 안의 지구", """
<circle cx="50" cy="50" r="34"/><path d="M75 75l31 31" stroke-width="5"/>
<path d="M17 50h66M50 16c-15 13-15 55 0 68M50 16c15 13 15 55 0 68" opacity=".5"/>""")

CODE = _s("꺾쇠 기호가 적힌 문서", """
<rect x="22" y="12" width="76" height="96" rx="7"/>
<path d="M50 44L37 60l13 16M70 44l13 16-13 16" stroke-width="4"/>""")

TOOLS = _s("가운데 원과 이어진 도구 세 개", """
<circle cx="60" cy="60" r="15"/>
<rect x="8" y="10" width="30" height="30" rx="6"/><rect x="82" y="10" width="30" height="30" rx="6"/>
<rect x="45" y="84" width="30" height="30" rx="6"/>
<path d="M38 36l11 12M82 36L71 48M60 75v9" opacity=".6"/>""")

NEWS = _s("제목과 본문이 있는 소식지", """
<rect x="14" y="22" width="92" height="78" rx="6"/>
<path d="M28 40h38" stroke-width="5"/><rect x="78" y="34" width="16" height="13" opacity=".6"/>
<path d="M28 58h66M28 72h66M28 86h40" opacity=".45"/>""")

PHONE = _s("확인 표시가 뜬 휴대폰", """
<rect x="34" y="8" width="52" height="104" rx="10"/><path d="M52 21h16M52 99h16" opacity=".45"/>
<path d="M46 60l10 10 18-21" stroke-width="5"/>""")
