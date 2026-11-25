# -*- coding: utf-8 -*-
AC = 'style="stroke:var(--acc)"'
ACF = 'style="fill:var(--acc)"'
ACB = 'style="stroke:var(--acc);fill:var(--acc);fill-opacity:.1"'

DEFS = ('<defs>'
        '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        '<path d="M0 0 L10 5 L0 10 z" fill="currentColor"/></marker>'
        '<marker id="ara" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
        '<path d="M0 0 L10 5 L0 10 z" style="fill:var(--acc)"/></marker>'
        '</defs>')


def _box(x, y, w, h, label, sub=None, acc=False, dash=False):
    st = ' style="stroke:var(--acc);fill:var(--acc);fill-opacity:.1"' if acc else \
         ' stroke="currentColor" fill="none"'
    d = ' stroke-dasharray="5 4"' if dash else ''
    o = ['<rect x="%d" y="%d" width="%d" height="%d" rx="8"%s%s stroke-width="1.5" opacity="%s"/>'
         % (x, y, w, h, st, d, '1' if acc else '.75')]
    cy = y + h / 2 + (0 if not sub else -7)
    o.append('<text x="%d" y="%.0f" text-anchor="middle" fill="currentColor" font-size="15" '
             'font-weight="600">%s</text>' % (x + w / 2, cy + 5, label))
    if sub:
        o.append('<text x="%d" y="%.0f" text-anchor="middle" fill="currentColor" font-size="12" '
                 'opacity=".6">%s</text>' % (x + w / 2, cy + 23, sub))
    return "".join(o)


def _arrow(x1, y1, x2, y2, label=None, acc=False, dash=False, above=True, curve=None):
    m = 'url(#ara)' if acc else 'url(#ar)'
    st = ' style="stroke:var(--acc)"' if acc else ' stroke="currentColor"'
    d = ' stroke-dasharray="5 4"' if dash else ''
    if curve:
        p = 'M%d %d Q %d %d %d %d' % (x1, y1, curve[0], curve[1], x2, y2)
        o = ['<path d="%s" fill="none"%s%s stroke-width="1.5" opacity=".8" marker-end="%s"/>'
             % (p, st, d, m)]
        lx, ly = curve[0], curve[1]
    else:
        o = ['<line x1="%d" y1="%d" x2="%d" y2="%d"%s%s stroke-width="1.5" opacity=".8" '
             'marker-end="%s"/>' % (x1, y1, x2, y2, st, d, m)]
        lx, ly = (x1 + x2) / 2, (y1 + y2) / 2
    if label:
        o.append('<text x="%.0f" y="%.0f" text-anchor="middle" fill="currentColor" font-size="12" '
                 'opacity=".72">%s</text>' % (lx, ly - 9 if above else ly + 19, label))
    return "".join(o)


# 1. 처리 → 결정  (before / after day composition)
DAY = """
<svg viewBox="0 0 960 252" role="img" aria-label="전환 전에는 하루의 대부분이 처리였고, 전환 후에는 결정이 하루의 중심이 된다">
""" + DEFS + """
<text x="0" y="22" fill="currentColor" font-size="13" font-weight="600" opacity=".6" letter-spacing="2">전환 전</text>
<rect x="0" y="40" width="700" height="56" rx="6" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".7"/>
<text x="350" y="74" text-anchor="middle" fill="currentColor" font-size="15" font-weight="600">처리: 찾기 · 읽기 · 옮기기 · 양식 맞추기</text>
<rect x="708" y="40" width="130" height="56" rx="6" """ + AC + """ fill="none" stroke-width="1.5"/>
<text x="773" y="74" text-anchor="middle" font-size="14" font-weight="600" """ + ACF + """>결정</text>
<text x="852" y="74" fill="currentColor" font-size="12" opacity=".55">남는 게 없다</text>

<text x="0" y="150" fill="currentColor" font-size="13" font-weight="600" opacity=".6" letter-spacing="2">전환 후</text>
<rect x="0" y="166" width="240" height="56" rx="6" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".45" stroke-dasharray="5 4"/>
<text x="120" y="200" text-anchor="middle" fill="currentColor" font-size="14" opacity=".6">처리: 에이전트가 함</text>
<rect x="248" y="166" width="590" height="56" rx="6" """ + ACB + """ stroke-width="1.5"/>
<text x="543" y="200" text-anchor="middle" font-size="15" font-weight="600" """ + ACF + """>결정: 무엇을 할지 · 맡기기 · 결과 검증</text>
<text x="852" y="200" fill="currentColor" font-size="12" opacity=".55">쌓인다</text>
<line x1="0" y1="118" x2="960" y2="118" stroke="currentColor" opacity=".18"/>
</svg>"""

# 2. 챗봇 vs 에이전트 — the actual difference
CHAT = """
<svg viewBox="0 0 960 330" role="img" aria-label="챗봇은 글로 된 답을 돌려주고 사람이 단계마다 직접 옮기지만, 에이전트는 내 컴퓨터의 파일을 직접 읽고 쓰며 끝까지 진행한다">
""" + DEFS + """
<text x="20" y="20" fill="currentColor" font-size="13" font-weight="600" opacity=".55" letter-spacing="2">채팅창 AI</text>
<line x1="470" y1="0" x2="470" y2="330" stroke="currentColor" opacity=".18" stroke-dasharray="4 5"/>
""" + _box(20, 110, 96, 56, "나") + _box(170, 110, 118, 56, "채팅창", "웹사이트 안") + \
_box(342, 110, 96, 56, "내 파일", dash=True) + \
_arrow(116, 128, 168, 128, "질문") + \
_arrow(168, 152, 118, 152, "답(글)", above=False) + \
_arrow(288, 138, 340, 138, "내가 직접") + """
<text x="229" y="226" text-anchor="middle" fill="currentColor" font-size="12.5" opacity=".72">복사 · 붙여넣기를 단계마다 내가 반복</text>
<text x="229" y="250" text-anchor="middle" fill="currentColor" font-size="12.5" opacity=".72">막히면 "할 수 없습니다"에서 멈춘다</text>
<text x="229" y="292" text-anchor="middle" fill="currentColor" font-size="13" font-weight="600" opacity=".55">결과 = 화면 위의 글</text>

<text x="500" y="20" font-size="13" font-weight="600" letter-spacing="2" """ + ACF + """>에이전트 (코덱스)</text>
""" + _box(500, 110, 96, 56, "나") + _box(650, 110, 128, 56, "에이전트", "내 컴퓨터 안", acc=True) + \
_box(832, 110, 108, 56, "내 폴더", "파일 · 설정", acc=True) + \
_arrow(596, 138, 648, 138, "목적", acc=True) + \
_arrow(778, 124, 830, 124, "읽기 · 쓰기", acc=True) + \
_arrow(830, 152, 780, 152, "결과 확인", acc=True, above=False) + """
<path d="M714 110 C 714 74, 790 74, 790 106" fill="none" """ + AC + """ stroke-width="1.5" opacity=".8" marker-end="url(#ara)"/>
<text x="752" y="66" text-anchor="middle" fill="currentColor" font-size="12" opacity=".72">막히면 다른 방법으로 다시</text>
<text x="720" y="226" text-anchor="middle" fill="currentColor" font-size="12.5" opacity=".72">여러 단계를 스스로 밟아 끝까지 간다</text>
<text x="720" y="250" text-anchor="middle" fill="currentColor" font-size="12.5" opacity=".72">내 파일을 바꿀 수 있다 → 안전장치가 필요하다</text>
<text x="720" y="292" text-anchor="middle" font-size="13" font-weight="600" """ + ACF + """>결과 = 저장된 파일</text>
</svg>"""

# 3. 안전장치 셋
SAFE = """
<svg viewBox="0 0 960 300" role="img" aria-label="요청은 승인을 거치고 샌드박스 범위 안에서만 파일을 바꿀 수 있으며, 되돌리기 기록이 남는다">
""" + DEFS + """
""" + _box(10, 108, 104, 60, "에이전트", "하려는 일") + """
<line x1="114" y1="138" x2="212" y2="138" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
<rect x="216" y="78" width="150" height="120" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="291" y="112" text-anchor="middle" font-size="12" font-weight="600" letter-spacing="1.5" """ + ACF + """>① 승인</text>
<text x="291" y="140" text-anchor="middle" fill="currentColor" font-size="15" font-weight="600">물어본다</text>
<text x="291" y="164" text-anchor="middle" fill="currentColor" font-size="12" opacity=".65">y / n 을 내가 누른다</text>
<text x="291" y="184" text-anchor="middle" fill="currentColor" font-size="12" opacity=".65">"언제 묻는가"</text>

<line x1="366" y1="138" x2="464" y2="138" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
<rect x="468" y="78" width="150" height="120" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="543" y="112" text-anchor="middle" font-size="12" font-weight="600" letter-spacing="1.5" """ + ACF + """>② 샌드박스</text>
<text x="543" y="140" text-anchor="middle" fill="currentColor" font-size="15" font-weight="600">아예 못 나간다</text>
<text x="543" y="164" text-anchor="middle" fill="currentColor" font-size="12" opacity=".65">허락한 폴더 밖 금지</text>
<text x="543" y="184" text-anchor="middle" fill="currentColor" font-size="12" opacity=".65">"어디까지 되는가"</text>

<line x1="618" y1="138" x2="716" y2="138" stroke="currentColor" stroke-width="1.5" opacity=".8" marker-end="url(#ar)"/>
""" + _box(720, 108, 110, 60, "내 파일") + """
<text x="775" y="196" text-anchor="middle" fill="currentColor" font-size="12" opacity=".55">여기까지 와야 바뀐다</text>
<path d="M830 138 C 900 138, 900 250, 500 250" fill="none" """ + AC + """ stroke-width="1.5" stroke-dasharray="6 5" opacity=".85" marker-end="url(#ara)"/>
<text x="700" y="272" text-anchor="middle" fill="currentColor" font-size="12.5" opacity=".75">③ 되돌리기: 옮긴 내역을 파일로 남겨 되돌릴 수 있게 한다</text>
<rect x="10" y="222" width="170" height="54" rx="8" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".45" stroke-dasharray="5 4"/>
<text x="95" y="246" text-anchor="middle" fill="currentColor" font-size="12.5" font-weight="600" opacity=".7">삭제 · 전송 · 결제</text>
<text x="95" y="265" text-anchor="middle" fill="currentColor" font-size="11.5" opacity=".6">끝까지 사람이 한다</text>
</svg>"""

# 4. 권한 모드 3단계 (what each step unlocks)
PERM = """
<svg viewBox="0 0 960 300" role="img" aria-label="읽기 전용은 보기만, 자동은 허락한 폴더 안에서 작업하고 밖으로 나갈 때 묻고, 전체 허용은 묻지 않는다">
""" + DEFS + """
<text x="0" y="18" fill="currentColor" font-size="12" font-weight="600" opacity=".55" letter-spacing="2">허락하는 범위</text>
<rect x="0" y="196" width="300" height="74" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="16" y="222" font-size="11.5" font-weight="600" letter-spacing="1.5" """ + ACF + """>1단계 · 오늘 시작</text>
<text x="16" y="246" fill="currentColor" font-size="16" font-weight="600">읽기 전용</text>
<text x="16" y="264" fill="currentColor" font-size="12" opacity=".65">읽기만. 아무것도 바뀌지 않는다</text>

<rect x="326" y="120" width="300" height="150" rx="8" """ + ACB + """ stroke-width="1.5"/>
<text x="342" y="146" font-size="11.5" font-weight="600" letter-spacing="1.5" """ + ACF + """>2단계 · 실습 1에서</text>
<text x="342" y="170" fill="currentColor" font-size="16" font-weight="600">자동 (물어봄)</text>
<text x="342" y="192" fill="currentColor" font-size="12" opacity=".65">정한 폴더 안: 알아서 한다</text>
<text x="342" y="212" fill="currentColor" font-size="12" opacity=".65">폴더 밖 · 위험한 일: 묻는다</text>
<text x="342" y="238" fill="currentColor" font-size="12" font-weight="600" opacity=".8">평소 쓰는 모드</text>
<text x="342" y="258" fill="currentColor" font-size="12" opacity=".65">읽기 전용이 하는 일 전부 포함</text>

<rect x="652" y="44" width="300" height="226" rx="8" stroke="currentColor" fill="none" stroke-width="1.5" opacity=".45" stroke-dasharray="6 5"/>
<text x="668" y="70" fill="currentColor" font-size="11.5" font-weight="600" letter-spacing="1.5" opacity=".6">3단계 · 오늘 안 씀</text>
<text x="668" y="94" fill="currentColor" font-size="16" font-weight="600" opacity=".75">전체 허용</text>
<text x="668" y="116" fill="currentColor" font-size="12" opacity=".6">묻지 않고 전부 실행한다</text>
<text x="668" y="136" fill="currentColor" font-size="12" opacity=".6">되돌릴 수 있는 상황에서만</text>
<text x="668" y="150" fill="currentColor" font-size="12" opacity=".6">수업에서는 쓰지 않습니다</text>
<line x1="0" y1="284" x2="960" y2="284" stroke="currentColor" opacity=".2"/>
<text x="0" y="300" fill="currentColor" font-size="11.5" opacity=".55">낮은 쪽에서 시작해서 필요할 때만 올린다 · /permissions 로 언제든 되돌린다</text>
</svg>"""
