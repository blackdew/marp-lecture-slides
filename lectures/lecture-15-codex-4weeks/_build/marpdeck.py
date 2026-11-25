# -*- coding: utf-8 -*-
"""deck.py 와 같은 API 로 Marp 마크다운을 뽑는 출력기.

w1.py 는 손대지 않습니다. build_marp.py 가 sys.modules['deck'] 에 이 모듈을
끼워 넣으면, 같은 원본에서 커스텀 HTML 대신 Marp 가 나옵니다.
이미지(데이터 URI·인라인 SVG)는 images/ 아래 파일로 떨어집니다.
"""
import base64, hashlib, pathlib, re

IMG = pathlib.Path(__file__).resolve().parent.parent / 'images'
_seen = {}


# ────────────────────────────── 공통 ──────────────────────────────
def _t(s):
    """슬라이드용 HTML 조각을 마크다운으로."""
    if s is None:
        return ''
    s = str(s)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'</?(em|b|strong)>', '**', s)
    s = re.sub(r'</?(small|u|i|span)[^>]*>', '', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = s.replace('****', '')          # 빈 강조 제거
    return s.strip()


def _inline(s):
    return _t(s).replace('\n', ' ')


def _asset(payload, stem):
    """데이터 URI 또는 인라인 SVG 를 images/ 파일로 저장하고 경로를 돌려줍니다."""
    key = hashlib.md5(payload[:4000].encode()).hexdigest()[:8]
    if key in _seen:
        return _seen[key]
    IMG.mkdir(parents=True, exist_ok=True)
    if payload.startswith('data:'):
        head, b64 = payload.split(',', 1)
        ext = 'jpg' if 'jpeg' in head else ('png' if 'png' in head else 'bin')
        name = 'img_%s_%s.%s' % (stem, key, ext)
        (IMG / name).write_bytes(base64.b64decode(b64))
    else:                                            # 인라인 SVG
        name = 'img_%s_%s.svg' % (stem, key)
        svg = payload.replace('currentColor', '#13735F')
        if 'xmlns=' not in svg:
            svg = svg.replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" ', 1)
        (IMG / name).write_text(svg, encoding='utf-8')
    rel = 'images/' + name
    _seen[key] = rel
    return rel


def note(*paras):
    body = '\n'.join('%s: %s' % (_inline(c), _inline(t)) for c, t in paras)
    return '\n<!--\n' + body + '\n-->'


def _eyebrow(part, time):
    return '<!-- _footer: "%s · %s" -->' % (_inline(part), _inline(time))


# ───────────────────────── 본문 조각 ─────────────────────────
def bullets(items):
    return '\n'.join('- ' + _inline(x) for x in items)


def lines(items, tight=False, quote=False):
    return '\n'.join('- **%s**: %s' % (_inline(a), _inline(b)) for a, b in items)


def ag2(items):
    return '\n'.join('%d. %s%s' % (i, _inline(t), '  ←' if hl else '')
                     for i, (t, hl) in enumerate(items, 1))


def pic(img, alt=""):
    return '![%s](%s)' % (_inline(alt) or 'image', _asset(img, 'pic'))


def figbare(svg):
    return '![w:360](%s)' % _asset(svg, 'fig')


def split(a, b, kind=""):
    return (a or '') + '\n\n' + (b or '')


def table(headers, rows, cls=""):
    out = ['| ' + ' | '.join(_inline(h) for h in headers) + ' |',
           '|' + '---|' * len(headers)]
    for r in rows:
        out.append('| ' + ' | '.join(_inline(c) for c in r) + ' |')
    return '\n'.join(out)


def kpi(items):
    out = []
    for it in items:
        big_, small = _inline(it[0]), _inline(it[1])
        ref = _inline(it[2]) if len(it) > 2 else ''
        out.append('- **%s**: %s%s' % (big_, small, (' (%s)' % ref if ref else '')))
    return '\n'.join(out)


def bars(rows, full=24.0, scale="하루 24시간", line=None):
    out = []
    for label, hours, text, kind in rows:
        n = max(1, round(hours / full * 24))
        out.append('- %s **%s**  `%s`' % (_inline(label), _inline(text), '█' * n))
    out.append('')
    out.append('*%s 기준*' % _inline(scale))
    if line:
        out.append('')
        out.append('### ' + _inline(line))
    return '\n'.join(out)


def chat(turns):
    out = []
    for who, text, mine in turns:
        out.append('**%s** %s' % (_inline(who), '▸' if mine else '▪'))
        out.append('> ' + _inline(text).replace('\n', '\n> '))
        out.append('')
    return '\n'.join(out).rstrip()


def lnkrow(url, label):
    return '\n출처: [%s](%s)' % (_inline(label), url)


def cards(items, cols=3, tight=False):
    """deck.cards 와 같은 딕셔너리(lab·num·h·p·cl)를 받습니다."""
    out = []
    for it in items:
        lead = ' '.join(x for x in (_inline(it.get('num')), _inline(it.get('lab'))) if x)
        head, body = _inline(it.get('h')), _inline(it.get('p'))
        seg = []
        if lead and head:
            seg.append('%s **%s**' % (lead, head))
        elif head or lead:
            seg.append('**%s**' % (head or lead))
        if body:
            seg.append(body)
        if seg:
            out.append('- ' + ': '.join(seg))
    return '\n'.join(out)


def steps(items, ordered=True):
    """deck.steps 와 같은 (굵은 글씨, 설명) 2-튜플을 받습니다."""
    out = []
    for i, (b, s) in enumerate(items, 1):
        head, tail = _inline(b), _inline(s)
        mark = '%d.' % i if ordered else '-'
        out.append('%s **%s**: %s' % (mark, head, tail) if tail
                   else '%s %s' % (mark, head))
    return '\n'.join(out)


def term(label, code, copy=False, lead=None):
    return (('%s\n\n' % _inline(lead)) if lead else '') + '```text\n' + code + '\n```'


def fig(svg, caption):
    return figbare(svg) + '\n\n' + _inline(caption)


def fill(lab, p):
    return '- **%s** %s' % (_inline(lab), _inline(p))


def warn(t):
    return '> ⚠ ' + _inline(t)


def inote(t):
    return '> ' + _inline(t)


def agenda(rows):
    return '\n'.join('- `%s` **%s**: %s' % (_inline(t), _inline(p), _inline(d))
                     for t, p, d, hl in rows)


# ───────────────────────── 슬라이드 ─────────────────────────
def cover(title, kicker, h1, lede, chips, nt=None):
    o = ['<!-- _class: lead -->', '', '## ' + _inline(kicker), '', '# ' + _t(h1)]
    if lede:
        o += ['', _t(lede)]
    if chips:
        o += ['', ' · '.join(_inline(t) for t, _ in chips)]
    return '\n'.join(o) + (nt or '')


def section(title, kicker, h1, lede, nt=None):
    o = ['<!-- _class: lead -->', '', '## ' + _inline(kicker), '', '# ' + _t(h1)]
    if lede:
        o += ['', _t(lede)]
    return '\n'.join(o) + (nt or '')


def slide(title, part, time, head, body, foot=None, nt=None, sub=None):
    o = [_eyebrow(part, time), '', '## ' + _t(head)]
    if sub:
        o += ['', _t(sub)]
    o += ['', body or '']
    if foot:
        o += ['', _t(foot)]
    return '\n'.join(o) + (nt or '')


def stmt(title, part, body, tag, nt=None):
    return '<!-- _class: lead -->\n\n# ' + _t(body) + (nt or '')


def brk(h1, lede, part="쉬는 시간", nt=None):
    o = ['<!-- _class: lead -->', '', '## ' + _inline(part), '', '# ' + _t(h1)]
    if lede:
        o += ['', _t(lede)]
    return '\n'.join(o) + (nt or '')


def big(title, part, time, word, sub=None, nt=None, body=None):
    o = [_eyebrow(part, time), '<!-- _class: lead -->', '', '# ' + _t(word)]
    if sub:
        o += ['', _t(sub)]
    if body:
        o += ['', body]
    return '\n'.join(o) + (nt or '')


def quip(title, part, time, line, art=None, foot=None, nt=None, size=None):
    o = [_eyebrow(part, time), '<!-- _class: lead -->', '']
    if art:
        o += [figbare(art), '']
    o += ['# ' + _t(line)]
    if foot:
        o += ['', _t(foot)]
    return '\n'.join(o) + (nt or '')


def sym(title, part, time, art, line, foot=None, nt=None, size="lg"):
    return quip(title, part, time, line, art=art, foot=foot, nt=nt)


def shot(title, part, time, img, line, alt="", nt=None):
    o = [_eyebrow(part, time),
         '![bg right:46%](' + _asset(img, 'shot') + ')',
         '', '## ' + _t(line)]
    return '\n'.join(o) + (nt or '')


def person(title, part, time, head, left, right, img=None, alt="", svg=None,
           link=None, label=None, nt=None):
    o = [_eyebrow(part, time)]
    if img:
        o.append('![bg right:42%](' + _asset(img, 'person') + ')')
    elif svg:
        o.append('![bg right:42%](' + _asset(svg, 'person') + ')')
    o += ['', '## ' + _t(head), '', bullets(list(left) + list(right))]
    if link:
        o += ['', '출처: [%s](%s)' % (_inline(label or link), link)]
    return '\n'.join(o) + (nt or '')


# ───────────────────────── 문서 ─────────────────────────
FRONT = """---
marp: true
theme: default
size: 16:9
paginate: true
---

<style>
section { padding: 60px 80px; }
section.lead { text-align: center; justify-content: center; }
h1 { color: #16past; }
</style>
""".replace('#16past', '#1f2d28')


def page(title, slides):
    return FRONT + '\n' + '\n\n---\n\n'.join(slides) + '\n'
