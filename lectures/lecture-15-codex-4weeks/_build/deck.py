# -*- coding: utf-8 -*-
"""Deck shell + slide components. One idea per slide, assertion headings."""
import html as _h
from style import CSS

JS = """
(function(){
  var FIT = null;
  var slides = Array.prototype.slice.call(document.querySelectorAll('.s'));
  var N = slides.length, i = 0;
  var fill = document.querySelector('.prog i');
  var cnt  = document.getElementById('cnt');
  var part = document.getElementById('part');
  var np   = document.getElementById('np');
  var npb  = document.getElementById('npBody');
  var ov   = document.getElementById('ov');
  var ovg  = document.getElementById('ovg');
  var bN   = document.getElementById('bN');
  var bO   = document.getElementById('bO');

  function phone(){ return window.matchMedia('(max-width:760px)').matches; }

  function fromHash(){
    var m = /^#s(\\d+)$/.exec(location.hash || '');
    if(!m) return 0;
    var n = parseInt(m[1],10) - 1;
    return (n >= 0 && n < N) ? n : 0;
  }

  function show(n){
    i = Math.max(0, Math.min(N-1, n));
    slides.forEach(function(s,k){ s.classList.toggle('on', k===i); });
    if(fill) fill.style.width = ((i+1)/N*100) + '%';
    if(cnt)  cnt.innerHTML = '<b>' + (i+1) + '</b> / ' + N;
    var s = slides[i];
    if(part) part.textContent = s.getAttribute('data-part') || '';
    var note = s.querySelector('.note');
    if(npb) npb.innerHTML = note ? note.innerHTML : '<p>이 슬라이드에는 노트가 없습니다.</p>';
    Array.prototype.forEach.call(ovg ? ovg.children : [], function(b,k){
      b.classList.toggle('cur', k===i);
    });
    if(history.replaceState) history.replaceState(null,'','#s'+(i+1));
    if(FIT) FIT();
  }

  // overview
  slides.forEach(function(s,k){
    var b = document.createElement('button');
    b.className = 'ovb' + (s.classList.contains('sect') ? ' sec' : '');
    b.innerHTML = '<u>' + (k+1) + '</u><span>' +
      (s.getAttribute('data-title') || '').replace(/&/g,'&amp;').replace(/</g,'&lt;') + '</span>';
    b.addEventListener('click', function(){ closeOv(); show(k); });
    if(ovg) ovg.appendChild(b);
  });

  function openOv(){ if(!ov) return; ov.hidden = false; if(bO) bO.classList.add('on'); }
  function closeOv(){ if(!ov) return; ov.hidden = true; if(bO) bO.classList.remove('on'); }
  function toggleOv(){ if(!ov) return; ov.hidden ? openOv() : closeOv(); }
  function toggleNp(){
    if(!np) return;
    np.hidden = !np.hidden;
    if(bN) bN.classList.toggle('on', !np.hidden);
  }

  document.addEventListener('keydown', function(e){
    if(e.metaKey || e.ctrlKey || e.altKey) return;
    var t = e.target;
    if(t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA')) return;
    var k = e.key;
    if(k === 'Escape'){ closeOv(); return; }
    if(phone()) return;
    if(k === 'ArrowRight' || k === 'PageDown' || k === ' '){ e.preventDefault(); show(i+1); }
    else if(k === 'ArrowLeft' || k === 'PageUp'){ e.preventDefault(); show(i-1); }
    else if(k === 'Home'){ e.preventDefault(); show(0); }
    else if(k === 'End'){ e.preventDefault(); show(N-1); }
    else if(k === 'n' || k === 'N'){ toggleNp(); }
    else if(k === 'o' || k === 'O'){ toggleOv(); }
    else if(k === 'f' || k === 'F'){ fs(); }
  });

  function fs(){
    var el = document.documentElement;
    if(document.fullscreenElement){ if(document.exitFullscreen) document.exitFullscreen(); }
    else if(el.requestFullscreen){ el.requestFullscreen().catch(function(){}); }
  }

  var pv = document.getElementById('pv'), nx = document.getElementById('nx');
  if(pv) pv.addEventListener('click', function(){ show(i-1); });
  if(nx) nx.addEventListener('click', function(){ show(i+1); });
  if(bN) bN.addEventListener('click', toggleNp);
  if(bO) bO.addEventListener('click', toggleOv);
  var bF = document.getElementById('bF'); if(bF) bF.addEventListener('click', fs);
  var ovc = document.getElementById('ovc'); if(ovc) ovc.addEventListener('click', closeOv);

  // theme toggle: flip away from whatever is currently rendered
  var bT = document.getElementById('bT');
  if(bT) bT.addEventListener('click', function(){
    var cur = document.documentElement.getAttribute('data-theme');
    if(!cur) cur = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    document.documentElement.setAttribute('data-theme', cur === 'dark' ? 'light' : 'dark');
  });

  // copy buttons
  function selectPre(pre){
    try{
      var r = document.createRange(); r.selectNodeContents(pre);
      var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(r);
    }catch(err){}
  }
  document.addEventListener('click', function(e){
    var b = e.target.closest ? e.target.closest('.copy') : null;
    if(!b) return;
    var pre = b.closest('.term').querySelector('pre');
    if(!pre) return;
    var txt = pre.innerText;
    function ok(){ b.classList.add('ok'); var o = b.textContent; b.textContent = '복사됨';
      setTimeout(function(){ b.classList.remove('ok'); b.textContent = o; }, 1400); }
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(txt).then(ok, function(){ selectPre(pre); b.textContent = '직접 복사'; });
    } else { selectPre(pre); b.textContent = '직접 복사'; }
  });

  window.addEventListener('hashchange', function(){ if(!phone()) show(fromHash()); });

  // 긴 프롬프트는 글자를 줄여 스크롤 없이 한 화면에 들어오게 합니다
  function fitPre(pre){
    pre.style.fontSize = '';
    var base = parseFloat(window.getComputedStyle(pre).fontSize);
    if(!base || !pre.clientHeight) return;
    var sz = base, min = base * 0.76, step = base * 0.02, g = 0;
    while(pre.scrollHeight > pre.clientHeight + 1 && sz > min && g++ < 40){
      sz -= step; pre.style.fontSize = sz + 'px';
    }
  }
  function fitAll(){
    var list;
    if(phone()){
      list = document.querySelectorAll('.term pre');
      Array.prototype.forEach.call(list, function(p){ p.style.fontSize = ''; });
      return;
    }
    var s = slides[i]; if(!s) return;
    Array.prototype.forEach.call(s.querySelectorAll('.term pre'), fitPre);
  }
  FIT = fitAll;
  var rt;
  window.addEventListener('resize', function(){ clearTimeout(rt); rt = setTimeout(fitAll, 120); });
  document.addEventListener('fullscreenchange', function(){ setTimeout(fitAll, 60); });

  show(fromHash());
})();
"""

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=IBM+Plex+Sans+KR:wght@300;400;500;600;700&'
         'family=IBM+Plex+Mono:wght@400;500&display=swap">')


def page(title, slides):
    return (
        '<!DOCTYPE html>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, '
        'viewport-fit=cover">\n'
        '<title>' + title + '</title>\n'
        '<meta name="claude:viewport-fit-sides" content="cover">\n'
        + FONTS + '\n<style>' + CSS + '</style>\n'
        '<div class="app">\n'
        '  <div class="wrap"><div class="stage">\n' + "\n".join(slides) + '\n  </div></div>\n'
        '  <div class="bar">\n'
        '    <div class="btns"><button class="btn" id="pv">←</button>'
        '<button class="btn" id="nx">→</button></div>\n'
        '    <span class="meta" id="cnt"></span>\n'
        '    <span class="meta" id="part"></span>\n'
        '    <div class="prog"><i></i></div>\n'
        '    <div class="btns">'
        '<button class="btn" id="bN">노트 N</button>'
        '<button class="btn" id="bO">목차 O</button>'
        '<button class="btn" id="bF">전체화면 F</button>'
        '<button class="btn" id="bT">테마</button></div>\n'
        '  </div>\n'
        '  <div class="np" id="np" hidden><h4>발표자 노트</h4><div id="npBody"></div></div>\n'
        '  <p class="hint"><kbd>→</kbd> <kbd>Space</kbd> 다음 · <kbd>←</kbd> 이전 · '
        '<kbd>N</kbd> 발표자 노트 · <kbd>O</kbd> 목차 · <kbd>F</kbd> 전체화면 · '
        '폰에서는 전체가 세로로 펼쳐져 복습용 문서가 됩니다.</p>\n'
        '</div>\n'
        '<div class="ov" id="ov" hidden><h4>목차: 클릭하면 이동합니다 '
        '<button class="btn" id="ovc" style="margin-left:10px">닫기 Esc</button></h4>'
        '<div class="ovg" id="ovg"></div></div>\n'
        '<script>' + JS + '</script>\n'
    )


# ---------------------------------------------------------------- components

def note(*paras):
    out = ['<div class="note">']
    for cue, text in paras:
        out.append('<p><span class="cue">' + cue + '</span> ' + text + '</p>')
    out.append('</div>')
    return "".join(out)


def slide(title, part, time, head, body, foot=None, nt=None, sub=None):
    o = ['<section class="s" data-title="' + _h.escape(title, quote=True) +
         '" data-part="' + _h.escape(part + ' · ' + time, quote=True) + '">']
    o.append('<div class="eyebrow"><b>' + part + '</b><span>' + time + '</span><i>' + title + '</i></div>')
    o.append('<h2 class="a">' + head + '</h2>')
    if sub:
        o.append('<p class="sub">' + sub + '</p>')
    o.append('<div class="body">' + body + '</div>')
    if foot:
        o.append('<p class="foot">' + foot + '</p>')
    if nt:
        o.append(nt)
    o.append('</section>')
    return "\n".join(o)


def cover(title, kicker, h1, lede, chips, nt=None):
    c = "".join('<span class="chip' + (' on' if k else '') + '">' + t + '</span>' for t, k in chips)
    return ('<section class="s cover" data-title="' + title + '" data-part="표지">'
            '<div class="kicker">' + kicker + '</div><h1>' + h1 + '</h1>'
            + ('<p class="lede">' + lede + '</p>' if lede else '')
            + '<div class="chips">' + c + '</div>' + (nt or '') + '</section>')


def section(title, kicker, h1, lede, nt=None):
    return ('<section class="s sect" data-title="[섹션] ' + title + '" data-part="' + kicker + '">'
            '<div class="kicker">' + kicker + '</div><h1>' + h1 + '</h1>'
            + ('<p class="lede">' + lede + '</p>' if lede else '') + (nt or '') + '</section>')


def stmt(title, part, body, tag, nt=None):
    return ('<section class="s stmt" data-title="' + title + '" data-part="' + part + '">'
            '<p>' + body + '</p><div class="tag">' + tag + '</div>' + (nt or '') + '</section>')


def brk(h1, lede, part="쉬는 시간", nt=None):
    return ('<section class="s brk" data-title="쉬는 시간" data-part="' + part + '">'
            '<div class="kicker">BREAK</div><h1>' + h1 + '</h1>'
            '<p class="lede">' + lede + '</p>' + (nt or '') + '</section>')


def big(title, part, time, word, sub=None, nt=None, body=None):
    """키워드 한 장 — 단어나 숫자 하나가 화면을 채웁니다."""
    o = ['<section class="s big" data-title="' + _h.escape(title, quote=True) +
         '" data-part="' + _h.escape(part + ' · ' + time, quote=True) + '">']
    o.append('<div class="eyebrow"><b>' + part + '</b><span>' + time + '</span><i>' + title + '</i></div>')
    import re as _re
    _plain = [_re.sub(r'<[^>]+>', '', x) for x in _re.split(r'<br\s*/?>', word)]
    _n = max((len(x.strip()) for x in _plain), default=0)
    _cl = '' if _n <= 4 else (' b2' if _n <= 7 else (' b3' if _n <= 11 else ' b4'))
    o.append('<div class="bigwrap' + (' row' if body else '') + '">')
    o.append('<div class="bigcol"><div class="bigword' + _cl + '">' + word + '</div>')
    if sub:
        o.append('<p class="bigsub">' + sub + '</p>')
    o.append('</div>')
    if body:
        o.append('<div class="bigbody">' + body + '</div>')
    o.append('</div>')
    if nt:
        o.append(nt)
    o.append('</section>')
    return "\n".join(o)


def sym(title, part, time, art, line, foot=None, nt=None, size="lg"):
    """그림 하나 + 문장 하나. 이 덱의 기본 장표입니다."""
    return quip(title, part, time, line, art=art, foot=foot, nt=nt, size=size)


def quip(title, part, time, line, art=None, foot=None, nt=None, size=None):
    """위트 한 장 — 짧은 문장과 작은 그림. 구간이 바뀔 때 숨을 돌리는 자리입니다."""
    o = ['<section class="s quip' + ((' ' + size) if size else '') + '" data-title="' + _h.escape(title, quote=True) +
         '" data-part="' + _h.escape(part + ' · ' + time, quote=True) + '">']
    if art:
        o.append('<div class="quipart">' + art + '</div>')
    o.append('<p class="quipline">' + line + '</p>')
    if foot:
        o.append('<p class="quipfoot">' + foot + '</p>')
    if nt:
        o.append(nt)
    o.append('</section>')
    return "\n".join(o)


def shot(title, part, time, img, line, alt="", nt=None):
    """캡처 한 장 + 문장 하나."""
    o = ['<section class="s shot" data-title="' + _h.escape(title, quote=True) +
         '" data-part="' + _h.escape(part + ' · ' + time, quote=True) + '">']
    o.append('<div class="eyebrow"><b>' + part + '</b><span>' + time + '</span><i>' + title + '</i></div>')
    o.append('<div class="shotimg"><img src="' + img + '" alt="' + _h.escape(alt or title, quote=True) + '"></div>')
    o.append('<p class="shotline">' + line + '</p>')
    if nt:
        o.append(nt)
    o.append('</section>')
    return "\n".join(o)


def person(title, part, time, head, left, right, img=None, alt="", svg=None,
           link=None, label=None, nt=None):
    """사람 한 명 — 가운데 화면, 좌우에 설명. link 가 있으면 화면 아래에 붙입니다."""
    o = ['<section class="s ppl" data-title="' + _h.escape(title, quote=True) +
         '" data-part="' + _h.escape(part + ' \u00b7 ' + time, quote=True) + '">']
    o.append('<div class="eyebrow"><b>' + part + '</b><span>' + time + '</span><i>' + title + '</i></div>')
    o.append('<h2 class="a">' + head + '</h2>')
    mid = ('<div class="shotimg"><img src="' + img + '" alt="' +
           _h.escape(alt or title, quote=True) + '"></div>') if img else \
          ('<div class="figfull">' + svg + '</div>' if svg else '')
    if link:
        mid += ('<a class="lnk" href="' + _h.escape(link, quote=True) +
                '" target="_blank" rel="noopener">' + (label or link) + '</a>')
    o.append('<div class="body"><div class="trio">'
             + bullets(left)
             + '<div class="pshot">' + mid + '</div>'
             + bullets(right) + '</div></div>')
    if nt:
        o.append(nt)
    o.append('</section>')
    return "\n".join(o)


def lines(items, tight=False, quote=False):
    """키워드 줄 — 큰 글씨 한 덩어리와 설명 한 줄. quote=True 면 뒷줄을 키웁니다."""
    o = ['<div class="lines' + (' t' if tight else '') + (' q' if quote else '') + '">']
    for b, s in items:
        o.append('<div><b>' + b + '</b>' + ('<span>' + s + '</span>' if s else '') + '</div>')
    o.append('</div>')
    return "".join(o)


def pic(img, alt=""):
    """이미지 한 칸. split 안에 넣어 씁니다."""
    return '<div class="shotimg"><img src="' + img + '" alt="' + _h.escape(alt, quote=True) + '"></div>'


def bullets(items):
    """설명 목록 — 짧은 명사구 두세 줄."""
    return '<ul class="bl">' + "".join('<li>' + x + '</li>' for x in items) + '</ul>'


def ag2(items):
    """번호 달린 목차. items = [(제목, 강조여부), ...]"""
    o = ['<ol class="ag2">']
    for i, (txt, on) in enumerate(items, 1):
        o.append('<li' + (' class="on"' if on else '') + '><u>%02d</u><b>%s</b></li>' % (i, txt))
    o.append('</ol>')
    return "".join(o)


def figbare(svg):
    """설명 없이 그림만. 설명은 발표자 노트에 둡니다."""
    return '<div class="figfull">' + svg + '</div>'


def cards(items, cols=3, tight=False):
    out = ['<div class="cards c' + str(cols) + (' tight' if tight else '') + '">']
    for it in items:
        cl = 'card' + (' ' + it['cl'] if it.get('cl') else '')
        o = ['<div class="' + cl + '">']
        if it.get('lab'):
            o.append('<div class="lab">' + it['lab'] + '</div>')
        if it.get('num'):
            o.append('<div class="num">' + it['num'] + '</div>')
        if it.get('h'):
            o.append('<h3>' + it['h'] + '</h3>')
        if it.get('p'):
            o.append('<p>' + it['p'] + '</p>')
        o.append('</div>')
        out.append("".join(o))
    out.append('</div>')
    return "".join(out)


def steps(items, ordered=True):
    tag = 'ol' if ordered else 'ul'
    out = ['<' + tag + ' class="steps">']
    for b, s in items:
        out.append('<li><div><b>' + b + '</b>' + ('<span>' + s + '</span>' if s else '') + '</div></li>')
    out.append('</' + tag + '>')
    return "".join(out)


def table(headers, rows, cls=""):
    out = ['<div class="tw"><table' + (' class="' + cls + '"' if cls else '') + '>']
    if headers:
        out.append('<thead><tr>' + "".join('<th>' + h + '</th>' for h in headers) + '</tr></thead>')
    out.append('<tbody>')
    for r in rows:
        out.append('<tr>' + "".join(
            '<td' + (' class="g"' if k and not str(c).startswith('<') else '') + '>' + c + '</td>'
            for k, c in enumerate(r)) + '</tr>')
    out.append('</tbody></table></div>')
    return "".join(out)


def term(label, code, copy=False, lead=None):
    n = code.count('\n') + 1          # 줄 수에 따라 글자 크기를 한 단 내립니다
    cl = ' t3' if n >= 15 else (' t2' if n >= 12 else '')
    h = ['<div class="term' + cl + '"><div class="th"><span class="dot"></span><span>' + label + '</span>']
    if copy:
        h.append('<button class="copy">복사</button>')
    h.append('</div><pre>' + code + '</pre></div>')
    return (('<p class="sub" style="margin:0 0 .6cqi">' + lead + '</p>') if lead else '') + "".join(h)


def fig(svg, caption):
    return '<figure>' + svg + '<figcaption>' + caption + '</figcaption></figure>'


def fill(lab, p):
    return '<div class="fill"><div class="lab">' + lab + '</div><p>' + p + '</p></div>'


def warn(t):
    return '<div class="warn">' + t + '</div>'


def inote(t):
    return '<div class="note-i">' + t + '</div>'


def split(a, b, kind=""):
    return ('<div class="split' + ((' ' + kind) if kind else '') + '">'
            '<div class="col">' + a + '</div><div class="col">' + b + '</div></div>')


def agenda(rows):
    out = ['<div class="agenda">']
    for t, p, d, hl in rows:
        out.append('<div' + (' class="hl"' if hl else '') + '><time>' + t + '</time><p>' + p +
                   '</p><i>' + d + '</i></div>')
    out.append('</div>')
    return "".join(out)


def chat(turns):
    """대화 말풍선. turns = [(말한이, 내용, 내말인가), ...]"""
    out = ['<div class="chat">']
    for who, text, mine in turns:
        out.append('<div class="row' + (' me' if mine else '') + '">'
                   '<span class="who">' + who + '</span>'
                   '<div class="bub">' + text + '</div></div>')
    out.append('</div>')
    return "".join(out)


def lnkrow(url, label):
    """출처 링크 한 줄."""
    return ('<p class="lnkrow"><a class="lnk" href="' + _h.escape(url, quote=True) +
            '" target="_blank" rel="noopener">' + label + '</a></p>')


def bars(rows, full=24.0, scale="하루 24시간", line=None):
    """가로 띠 비교. rows = [(이름, 시간, 표기, 종류), ...]"""
    out = ['<div class="tbars">']
    for label, hours, text, kind in rows:
        pct = max(0.0, min(100.0, hours / full * 100.0))
        out.append('<div class="tbar ' + kind + '">'
                   '<div class="tbh"><span class="tbn">' + label + '</span>'
                   '<span class="tbv">' + text + '</span></div>'
                   '<div class="tbt"><i style="width:%.1f%%"></i></div></div>' % pct)
    out.append('<div class="tbscale"><span>0</span><span>' + scale + '</span></div>')
    if line:
        out.append('<p class="tbline">' + line + '</p>')
    out.append('</div>')
    return "".join(out)


def kpi(items):
    """숫자 칸. (큰숫자, 설명) 또는 (큰숫자, 설명, 비교기준)."""
    out = ['<div class="kpi">']
    for it in items:
        b, s = it[0], it[1]
        ref = it[2] if len(it) > 2 else None
        out.append('<div><b>' + b + '</b><span>' + s + '</span>'
                   + ('<u>' + ref + '</u>' if ref else '') + '</div>')
    out.append('</div>')
    return "".join(out)
