# -*- coding: utf-8 -*-
"""w2.py 에서 실습 자료 두 개를 만듭니다.  python3 handouts.py 2

    ../worksheet.html   수강생용 실습지
    ../runsheet.html    강사용 진행표

프롬프트 문장, 표, 시각은 덱(w2.py)에서 읽어 옵니다. 덱을 고친 뒤 이 스크립트를 다시 실행하면
두 자료도 같은 문장으로 바뀝니다. 기록란과 '막혔을 때 보낼 문장'처럼 덱에 없는 안내만 여기에 적습니다.
보내는 문장 전체는 w2.SAY 에 있고, 화면의 줄과 같은 내용인지 여기서 검사합니다.
"""
import html as _h
import importlib
import pathlib
import re
import sys

import _shared                                      # noqa: F401
from deck import page                               # noqa: F401  (import 순서 고정)

n = (sys.argv[1:] or ['2'])[0]
m = importlib.import_module('w' + n)
out = pathlib.Path(__file__).resolve().parent.parent
SUBJECT = re.sub(r'^\d+주차\s*', '', m.TITLE)


# ───────────────────────── 덱에서 읽기 ─────────────────────────
def _text(h):
    return _h.unescape(re.sub(r'<[^>]+>', '', h.replace('<br>', ' '))).strip()


def _body(sec):
    """발표자 노트를 뺀 장표 HTML."""
    return re.sub(r'<div class="note">.*?</div>\s*(?=</section>)', '', sec, flags=re.S)


SLIDES = []                                         # (제목, 구간, 시각(분) 또는 None, 화면 문장, 원본 HTML)
for sec in m.S:
    title = re.search(r'data-title="([^"]*)"', sec).group(1)
    part = _h.unescape(re.search(r'data-part="([^"]*)"', sec).group(1))
    tm = re.search(r'(\d\d):(\d\d)', part)
    mins = int(tm.group(1)) * 60 + int(tm.group(2)) if tm else None
    seg = re.sub(r'\s*·?\s*\d\d:\d\d.*$', '', part).replace('BREAK', '쉬는 시간')
    body = _body(sec)
    line = re.search(r'<p class="(?:quipline|shotline)">(.*?)</p>|<h2 class="a">(.*?)</h2>|<h1>(.*?)</h1>',
                     body, flags=re.S)
    SLIDES.append((title, seg, mins, _text(next(g for g in line.groups() if g)) if line else '', sec))


def slide(title):
    hit = [s for s in SLIDES if s[0] == title]
    assert len(hit) == 1, '장표를 찾지 못했습니다: %s (%d개)' % (title, len(hit))
    return hit[0]


def prompt(title):
    """장표 화면에 따옴표로 적힌 프롬프트 한 개."""
    line = slide(title)[3]
    assert line.startswith('“') and line.endswith('”'), '프롬프트 장표가 아닙니다: ' + title
    return line[1:-1]


def clock(title):
    return '%02d:%02d' % divmod(slide(title)[2], 60)


def lines_of(title):
    """lines() 부품의 (라벨, 문장) 목록."""
    rows = re.findall(r'<div><b>(.*?)</b><span>(.*?)</span></div>', _body(slide(title)[4]))
    assert rows, 'lines 가 없습니다: ' + title
    return [(_text(a), _text(b).strip('“”')) for a, b in rows]


def table_of(title):
    rows = re.findall(r'<tr>(.*?)</tr>', _body(slide(title)[4]), flags=re.S)
    return [[_text(c) for c in re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', r, flags=re.S)] for r in rows]


def cue(title, name):
    """발표자 노트에서 머리말이 name 인 문단."""
    hit = re.search(r'<span class="cue">' + re.escape(name) + r'</span> (.*?)</p>', slide(title)[4], flags=re.S)
    assert hit, '노트 머리말이 없습니다: %s / %s' % (title, name)
    return _text(hit.group(1))


def quotes_of(title):
    """lines() 부품에서 따옴표로 적힌 줄만. 화면에 나눠 적은 요청 문장입니다."""
    rows = re.findall(r'<div><b>(.*?)</b><span>(.*?)</span></div>', _body(slide(title)[4]))
    return [_text(b)[1:-1] for _, b in rows if _text(b).startswith('“') and _text(b).endswith('”')]


def _norm(s):
    return re.sub(r'[\s.,]', '', s)


SAY = {}                                            # 장표 제목 → 보내는 문장 목록
for _t, _v in m.SAY.items():
    SAY[_t] = [_v] if isinstance(_v, str) else list(_v)
    assert _norm(''.join(SAY[_t])) == _norm(''.join(quotes_of(_t))), '화면의 줄과 보내는 문장이 다릅니다: ' + _t


def one(title):
    assert len(SAY[title]) == 1, title
    return SAY[title][0]


def tool(title):
    """요청 장표의 '쓰는 도구' 줄."""
    return '<p class="note">에이전트가 쓰는 도구: <b>' + _h.escape(dict(lines_of(title))['쓰는 도구']) + '</b></p>'


def warn(text):
    return '<p class="warn">' + text + '</p>'


def learned(title):
    """'익힌 방법' 장표의 방법과 내 일에 쓰는 예."""
    d = dict(lines_of(title))
    return ('<p class="got">익힌 방법: <b>' + _h.escape(d['방법']) + '</b><br>내 일에 쓰기: '
            + _h.escape(d['내 일에 쓰기']) + '</p>')


RESERVE, UNRESERVE = SAY['매일 예약']
CARD_FIX = m.CARD_FIX
REUSE = m.REUSE
METHODS = lines_of('오늘 익힌 방법')                  # [(실습, 익힌 방법)]
LEFT = lines_of('수업 뒤에 남는 것')                  # [(남는 곳, 남는 것)]
REDO = re.findall(r'“(.*?)”', cue('보고서 고치기', '예'))
PLAN_MORE = m.PLAN_MORE                              # [(주제, 문장)] 공부 계획, 사업 계획
MADE = lines_of('오늘 만든 것')                      # [(만든 것, 에이전트가 쓴 도구)]


# ───────────────────────── 공통 틀 ─────────────────────────
CSS = """
:root{--bg:#F6F5F2;--panel:#fff;--line:#DEDAD1;--fg:#1A1D22;--dim:#525B66;--faint:#88919C;
  --acc:#13735F;--accs:rgba(19,115,95,.09)}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);line-height:1.6;font-size:16px;word-break:keep-all;
  font-family:"IBM Plex Sans KR","Noto Sans KR",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
main{max-width:820px;margin:0 auto;padding:28px 16px 56px}
header{margin-bottom:20px}
.kicker{font-size:12px;letter-spacing:.16em;color:var(--acc);font-weight:600}
h1{font-size:28px;line-height:1.3;margin:6px 0 4px}
.lede{color:var(--dim);margin:0}
section{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin:14px 0;
  break-inside:avoid}
h2{font-size:19px;margin:0 0 10px;line-height:1.4}
h2 small{font-size:13px;font-weight:500;color:var(--faint);margin-left:8px}
h3{font-size:15px;margin:16px 0 6px;color:var(--dim)}
p{margin:6px 0}
ul,ol{margin:6px 0;padding-left:22px}
li{margin:3px 0}
.q{display:block;background:var(--accs);border-left:3px solid var(--acc);border-radius:6px;
  padding:9px 12px;margin:8px 0;font-weight:600}
.say{font-weight:600;color:var(--acc)}
td .say{white-space:nowrap}
.tw{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:15px}
th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
th{background:#F1EEE8;font-weight:600;white-space:nowrap}
td.w{min-width:180px;padding:4px 6px}
textarea.f{display:block;width:100%;min-height:36px;border:1.5px solid var(--line);border-radius:6px;
  background:#fff;color:inherit;font:inherit;font-size:16px;line-height:1.5;padding:5px 2px;
  resize:none;overflow:hidden}
td.w textarea.f{border:0}
textarea.f::placeholder{color:var(--dim);opacity:.8}
textarea.f:focus-visible{outline:2px solid var(--acc);outline-offset:1px}
.blank{margin:4px 0 10px}
.pick{display:flex;flex-wrap:wrap;gap:8px 18px;margin:8px 0;padding:0;list-style:none}
.pick li{margin:0}
.pick label{display:inline-flex;align-items:center;gap:7px;cursor:pointer}
.pick input{width:17px;height:17px;margin:0;accent-color:var(--acc)}
.store{display:flex;flex-wrap:wrap;align-items:center;gap:6px 12px;margin:12px 0 0;font-size:14px;color:var(--dim)}
.store button{font:inherit;font-size:13px;color:var(--dim);background:var(--panel);border:1px solid var(--line);
  border-radius:8px;padding:5px 11px;cursor:pointer}
.store button:focus-visible{outline:2px solid var(--acc);outline-offset:1px}
.store button.arm{color:#fff;background:#B3261E;border-color:#B3261E}
#save-status{color:var(--acc);font-weight:600}
.tag{display:inline-block;font-size:12px;font-weight:600;color:var(--acc);background:var(--accs);
  border-radius:99px;padding:1px 9px;margin-left:6px;white-space:nowrap}
.note{font-size:14px;color:var(--dim)}
.warn{background:#FBEDEC;border-left:3px solid #B3261E;border-radius:6px;padding:9px 12px;margin:8px 0;font-weight:600}
.got{background:var(--accs);border-radius:6px;padding:8px 12px;margin:12px 0 0}
tr.do td{background:var(--accs)}
td.t{white-space:nowrap;font-variant-numeric:tabular-nums}
footer{font-size:13px;color:var(--faint);margin-top:18px}
@media (max-width:560px){h1{font-size:23px}section{padding:15px 14px}table{font-size:14px}}
@media print{
  @page{size:A4;margin:14mm}
  body{background:#fff;font-size:11.5pt}
  main{max-width:none;padding:0}
  section{border-color:#bbb;margin:9px 0;padding:12px 14px}
  .q,tr.do td,th,.tag{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  a{color:inherit;text-decoration:none}
  .store{display:none}
  textarea.f{border-bottom-color:#999}
  textarea.f::placeholder{color:transparent}
}
"""


def doc(title, kicker, lede, body, robots=False, top='', script='', foot=True):
    return ('<!DOCTYPE html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            + ('<meta name="robots" content="noindex">\n' if robots else '')
            + '<title>' + _h.escape(title) + '</title>\n<style>' + CSS + '</style>\n</head>\n<body>\n<main>\n'
            '<header><div class="kicker">' + kicker + '</div><h1>' + _h.escape(title) + '</h1>'
            '<p class="lede">' + lede + '</p>' + top + '</header>\n' + body +
            ('\n<footer>이 문서는 <code>_build/handouts.py</code>가 덱에서 만든 생성물입니다.</footer>\n' if foot else '\n') +
            '</main>\n' + (('<script>' + script + '</script>\n') if script else '') + '</body>\n</html>\n')


def q(text):
    return '<span class="q">“' + _h.escape(text) + '”</span>'


def say(text):
    return '<span class="say">“' + _h.escape(text) + '”</span>'


def sec(head, body, small='', id=''):
    """절 하나. id 를 주면 덱의 링크가 이 절로 바로 옵니다 (w2.py 의 ws)."""
    return ('<section' + ((' id="' + id + '"') if id else '') + '><h2>' + head
            + (('<small>' + small + '</small>') if small else '') + '</h2>' + body + '</section>')


def tbl(headers, rows, cls=None):
    o = ['<div class="tw"><table><thead><tr>' + ''.join('<th>' + h + '</th>' for h in headers) + '</tr></thead><tbody>']
    for i, r in enumerate(rows):
        o.append('<tr' + ((' class="' + cls[i] + '"') if cls and cls[i] else '') + '>' + ''.join(r) + '</tr>')
    o.append('</tbody></table></div>')
    return ''.join(o)


def td(text, c=None):
    return '<td' + ((' class="' + c + '"') if c else '') + '>' + text + '</td>'


# 입력 칸마다 고정된 이름(key)을 붙입니다. 저장한 값은 이 이름으로 되찾으므로,
# 칸을 추가하거나 순서를 바꿔도 이미 적어 둔 값이 다른 칸으로 밀리지 않습니다.
def field(key, label, rows=1, ph='여기에 입력'):
    return ('<textarea class="f" data-k="%s" rows="%d" aria-label="%s" placeholder="%s"></textarea>'
            % (key, rows, _h.escape(label, quote=True), _h.escape(ph, quote=True)))


def cell(key, label, ph='여기에 입력'):
    return '<td class="w">' + field(key, label, ph=ph) + '</td>'


def blank(key, label, ph='여기에 입력'):
    return '<div class="blank">' + field(key, label, 2, ph) + '</div>'


def choose(key, label, items, kind='radio'):
    """선택 칸. radio 는 하나만 고르고, checkbox 는 항목마다 따로 저장합니다."""
    o = ['<ul class="pick"' + (' role="radiogroup"' if kind == 'radio' else '')
         + ' aria-label="' + _h.escape(label, quote=True) + '">']
    for i, text in enumerate(items):
        attrs = ('type="radio" name="%s" data-k="%s" value="%s"' % (key, key, _h.escape(text, quote=True))
                 if kind == 'radio' else 'type="checkbox" data-k="%s-%d"' % (key, i + 1))
        o.append('<li><label><input ' + attrs + '>' + _h.escape(text) + '</label></li>')
    o.append('</ul>')
    return ''.join(o)


STORE_NOTE = ('<p class="store"><span>적은 내용은 이 기기의 브라우저에 저장됩니다. '
              '다른 기기나 다른 브라우저에서는 보이지 않습니다.</span>'
              '<button type="button" id="clear-all">적은 내용 모두 지우기</button>'
              '<span id="save-status" role="status" aria-live="polite"></span></p>')

# 저장소를 쓸 수 없는 브라우저(사생활 보호 모드 등)에서도 입력은 되도록 모든 접근을 try 로 감쌉니다.
STORE_JS = r"""
(function () {
  var KEY = 'lecture16-worksheet-v3';
  var data = {};
  var status = document.getElementById('save-status');
  var timer = null;
  function tell(text) {
    status.textContent = text;
    clearTimeout(timer);
    timer = setTimeout(function () { status.textContent = ''; }, 2500);
  }
  try { data = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; }
  catch (e) { data = {}; }
  function save() {
    try { localStorage.setItem(KEY, JSON.stringify(data)); tell('저장했습니다'); }
    catch (e) { tell('이 브라우저에서는 저장할 수 없습니다. 창을 닫으면 내용이 사라집니다.'); }
  }
  function grow(el) { el.style.height = 'auto'; el.style.height = el.scrollHeight + 'px'; }
  var texts = document.querySelectorAll('textarea[data-k]');
  var picks = document.querySelectorAll('input[data-k]');
  function fill() {
    texts.forEach(function (el) {
      el.value = typeof data[el.dataset.k] === 'string' ? data[el.dataset.k] : '';
      grow(el);
    });
    picks.forEach(function (el) {
      el.checked = el.type === 'radio' ? data[el.dataset.k] === el.value : data[el.dataset.k] === true;
    });
  }
  texts.forEach(function (el) {
    el.addEventListener('input', function () { data[el.dataset.k] = el.value; grow(el); save(); });
  });
  picks.forEach(function (el) {
    el.addEventListener('change', function () {
      data[el.dataset.k] = el.type === 'radio' ? el.value : el.checked;
      save();
    });
  });
  fill();
  window.addEventListener('resize', function () { texts.forEach(grow); });
  window.addEventListener('beforeprint', function () { texts.forEach(grow); });

  // 지우기는 두 번 눌러야 실행됩니다. 실수로 한 번 누른 경우에는 4초 뒤에 원래대로 돌아갑니다.
  var clear = document.getElementById('clear-all');
  var label = clear.textContent;
  var armed = null;
  clear.addEventListener('click', function () {
    if (!armed) {
      clear.classList.add('arm');
      clear.textContent = '한 번 더 누르면 모두 지워집니다';
      armed = setTimeout(function () { armed = null; clear.classList.remove('arm'); clear.textContent = label; }, 4000);
      return;
    }
    clearTimeout(armed); armed = null;
    clear.classList.remove('arm'); clear.textContent = label;
    data = {};
    try { localStorage.removeItem(KEY); } catch (e) {}
    fill();
    tell('모두 지웠습니다');
  });
})();
"""


# ───────────────────────── 수강생용 실습지 ─────────────────────────
NEWCHAT = '<p>새 채팅을 열고 <b>2주차</b> 폴더를 다시 고른 뒤 시작합니다.</p>'
CONFIRM = ('<p class="note">에이전트가 어떻게 만들지 먼저 보여 주고 만들어도 되는지 물으면, 읽어 보고 '
           + say('응, 만들어줘') + '라고 답합니다.</p>')


def worksheet():
    b = []
    b.append(sec('시작하기 전에',
        '<ul>'
        '<li>바탕화면에 <b>2주차</b>라는 빈 폴더 만들기</li>'
        '<li>Codex의 새 채팅에서 <b>2주차</b> 폴더 고르기. ‘이 폴더를 신뢰할까요?’ 창이 뜨면 '
        '폴더 이름이 2주차인지 보고 ‘폴더 신뢰’ 누르기</li>'
        '<li>새 채팅을 열 때마다 <b>2주차</b> 폴더를 다시 고르기</li>'
        '<li>전화번호, 집 주소, 실제 이름은 적지 않기. 다른 사람이 봐도 괜찮은 이야기만 적기</li>'
        '<li>엔터를 누르면 바로 보내짐. 여러 문장은 줄을 바꾸지 않고 이어서 적은 뒤 한 번에 보내기</li>'
        '<li>아래의 문장은 예시. 받는 사람, 주제, 경험은 내 것으로 바꿔 적기</li>'
        '<li>허용이나 설치를 묻는 창이 뜨면 내용을 읽고 누르기. 뜻을 모르는 창은 누르지 말고 강사에게 묻기</li>'
        '</ul>'))

    b.append(sec('첫 번째 실습 · 연하장',
        '<p>Codex 채팅 하나에서 모든 단계를 이어서 합니다. 뒤 단계의 요청이 앞 단계에서 만든 그림을 쓰기 때문입니다.</p>'
        '<h3>연하장을 받는 사람</h3>' + blank('card-who', '연하장을 받는 사람', '예: 40년 된 친구, 큰언니 (이름 대신 호칭으로)')
        + '<h3>그림판으로 그리기</h3>' + q(one('그림판으로 그리기')) + tool('그림판으로 그리기')
        + '<ul><li>허용을 묻는 창이 뜨면 ‘이 대화 허용’ 누르기. ‘항상 허용’은 누르지 않기</li>'
          '<li>에이전트가 그리는 동안에는 마우스와 키보드에 손을 대지 않기</li>'
          '<li>그림판 조작이 되지 않으면 이 단계를 건너뛰고 다음 단계부터 진행</li></ul>'
        '<h3>말로 설명해서 그림 받기</h3>' + q(one('그림 생성')) + tool('그림 생성')
        + tbl(['바꿀 부분', '내가 적을 내용'], [
            [td('<b>모습</b>'), cell('img-look', '그림의 모습', '예: 소나무와 학이 있는 모습')],
            [td('<b>느낌</b>'), cell('img-feel', '그림의 느낌', '예: 색연필로 그린 느낌')]])
        + '<h3>그림으로 연하장 만들기</h3>' + q(one('연하장 만들기')) + tool('연하장 만들기') + CONFIRM
        + '<h3>연하장에서 고칠 곳 말하기</h3><p>예: ' + say(CARD_FIX) + '</p>'
        '<h3>연하장을 인터넷에 올리기</h3>'
        + warn('이 요청을 보내면 연하장이 인터넷에 올라갑니다. 인터넷 주소를 아는 사람은 누구나 볼 수 있습니다. '
               '전화번호, 집 주소, 실제 이름이 없는지 먼저 읽어 봅니다.')
        + q(one('인터넷 주소')) + tool('인터넷 주소')
        + '<h3>내 연하장의 인터넷 주소</h3>'
        + blank('card-url', '내 연하장의 인터넷 주소', '복사한 인터넷 주소를 여기에 붙여 넣기')
        + '<h3>서로 보내기</h3>'
        '<ol><li>내 연하장의 인터넷 주소를 복사해서 수업 채팅창에 올리기</li>'
        '<li>다른 사람이 올린 주소를 하나 골라 열어 보기</li></ol>'
        '<h3>확인할 것</h3>'
        + choose('check-card', '연하장에서 확인할 것',
                 ['연하장에 받는 사람의 호칭이 적혀 있음', '연하장에 전화번호, 집 주소, 실제 이름이 없음',
                  '인터넷 주소를 수업 채팅창에 올림', '다른 사람의 연하장을 열어 봄'], kind='checkbox')
        + learned('연하장에서 익힌 방법'), id='card'))

    b.append(sec('내 프롬프트 만들기',
        '<p>연하장을 만든 Codex 채팅으로 돌아갑니다. 왼쪽 목록에서 그 채팅을 누릅니다.</p>'
        '<h3>연하장을 만들면서 내가 고쳐 달라고 한 것</h3>'
        + blank('my-standard', '연하장을 만들면서 내가 고쳐 달라고 한 것', '예: 맨 아래에 ‘두쫀쿠 동지가’ 넣기')
        + '<h3>고친 내용을 프롬프트로 정리하기</h3>' + q(one('프롬프트로 정리')) + tool('프롬프트로 정리')
        + '<p class="note">프롬프트는 다음에 다시 쓰려고 정리해 둔 요청입니다. '
          '에이전트가 쓴 프롬프트에서 내가 고쳐 달라고 한 것을 찾아봅니다.</p>'
        '<h3>저장하기 전에: 매번 하지 않을 일 빼기</h3>'
        + warn('프롬프트에 인터넷에 올리는 내용이 들어 있으면, 그 프롬프트를 쓸 때마다 연하장이 인터넷에 올라갑니다. '
               '저장하기 전에 끝까지 읽어 봅니다.')
        + q(SAY['프롬프트 다듬기'][0])
        + '<h3>프롬프트를 파일로 저장하기</h3>' + q(one('프롬프트 저장')) + tool('프롬프트 저장')
        + '<h3>새 채팅에서 다시 쓰기</h3>'
        '<p>수업에서는 강사의 화면으로 봅니다. 새 채팅을 열고 <b>2주차</b> 폴더를 고른 뒤 보냅니다.</p>'
        + q(REUSE)
        + '<p class="note">‘대학 친구’ 자리에 다른 받는 사람을 넣습니다.</p>'
        '<h3>다음에 쓸 때: 고친 내용을 프롬프트에 반영하기</h3>'
        '<p>프롬프트로 만든 결과를 더 고쳤다면, 고친 뒤에 보냅니다. 다음에는 같은 조정을 다시 하지 않아도 됩니다.</p>'
        + q(SAY['프롬프트 다듬기'][1])
        + '<h3>확인할 것</h3>'
        + choose('check-prompt', '내 프롬프트에서 확인할 것',
                 ['프롬프트에 내가 고쳐 달라고 한 것이 들어 있음', '인터넷에 올리는 내용을 뺐음',
                  '2주차 폴더에 ‘연하장 프롬프트’ 파일이 생김'], kind='checkbox')
        + '<p class="got">익힌 방법: <b>고친 내용을 프롬프트로 남기기</b><br>'
          '내 일에 쓰기: 자주 만드는 문서, 자주 쓰는 안내문, 매달 하는 정리</p>', id='prompt'))

    b.append(sec('두 번째 실습 · 계획 보고서',
        NEWCHAT + '<p>여행, 공부, 사업 가운데 하나를 고릅니다.</p>'
        + choose('plan-kind', '계획 보고서의 주제', ['여행 계획', '공부 계획', '사업 계획'])
        + tool('계획 보고서') + '<h3>여행 계획</h3>' + q(one('계획 보고서'))
        + ''.join('<h3>' + _h.escape(k) + '</h3>' + q(v) for k, v in PLAN_MORE)
        + '<h3>내 상황</h3>'
        '<p class="note">무엇을 하려는지, 언제 얼마 동안 하는지, 꼭 고려해야 할 점이 무엇인지를 적습니다. '
        '내 상황을 적지 않으면 에이전트가 그 내용을 반영할 수 없습니다.</p>'
        + blank('plan-me', '계획 보고서에 적을 내 상황') + CONFIRM
        + warn('보고서는 인터넷에 올리지 않습니다. 문장 끝의 “인터넷에 올리지는 마”를 빼지 않습니다.')
        + '<h3>보고서에서 고칠 곳 말하기</h3>'
        '<p>예: ' + ', '.join(say(r) for r in REDO) + '</p>'
        + warn('보고서에 적힌 가격, 영업시간, 일정은 틀릴 수 있습니다. '
               '보고서의 내용대로 예약하거나 결제하기 전에 출처를 눌러 확인합니다.')
        + '<h3>확인할 것</h3>'
        + choose('check-plan', '계획 보고서에서 확인할 것', ['보고서에 내가 적은 조건이 반영돼 있음'], kind='checkbox')
        + learned('계획 보고서에서 익힌 방법'), id='plan'))

    b.append(sec('세 번째 실습 · 관심 주제 보고서',
        NEWCHAT + '<p>‘보이스피싱 수법’ 자리에 내 관심 주제를 넣습니다.</p>'
        '<h3>내 관심 주제</h3>' + blank('topic', '내 관심 주제', '예: 겨울철 난방비 줄이는 방법')
        + q(one('관심 주제 보고서')) + tool('관심 주제 보고서') + CONFIRM
        + warn('건강과 돈에 관한 내용은 그대로 따르지 않습니다. 출처를 눌러서 그 내용이 실제로 있는지 확인합니다.')
        + '<h3>같은 일을 매일 하게 하기</h3>'
        '<p>수업에서는 강사의 화면으로 봅니다. 직접 해볼 때는 아래의 순서로 합니다.</p>'
        '<ol><li>예약하기' + q(RESERVE) + '</li>'
        '<li>생긴 예약 항목을 눌러 내용 읽어 보기</li>'
        '<li>예약 지우기' + q(UNRESERVE) + '</li></ol>' + tool('매일 예약')
        + warn('지우지 않은 예약은 수업이 끝난 뒤에도 매일 실행됩니다. 수업이 끝나기 전에 지웁니다.')
        + '<h3>확인할 것</h3>'
        + choose('check-topic', '관심 주제 보고서에서 확인할 것',
                 ['출처 하나를 눌러서 내용을 확인함', '예약을 만들었다면 지웠음'], kind='checkbox')
        + learned('주제 보고서에서 익힌 방법'), id='topic'))

    b.append(sec('네 번째 실습 · 블로그 글',
        NEWCHAT + '<p>‘가족과 김장한 이야기’ 자리에 내 경험을 넣습니다.</p>'
        '<h3>글로 쓸 내 경험</h3>' + blank('blog', '글로 쓸 내 경험', '예: 지난달에 다녀온 여행')
        + q(one('블로그 글 쓰기')) + tool('블로그 글 쓰기')
        + '<h3>내가 겪은 장면 덧붙이기</h3>'
        + blank('blog-scene', '덧붙일 장면', '예: 배추는 마흔 포기였고, 손주가 양념을 버무렸어')
        + q(one('장면 덧붙이기'))
        + '<p class="note">에이전트가 쓴 글에 내가 겪지 않은 일이 들어가지 않았는지 읽어 봅니다. '
          '글은 Codex 채팅에만 나옵니다. 쓸 때는 글을 복사해서 붙여 넣습니다.</p>'
        + learned('블로그 글에서 익힌 방법'), id='blog'))

    b.append(sec('다섯 번째 실습 · 쇼츠',
        '<p>연하장을 만든 Codex 채팅으로 돌아갑니다. 왼쪽 목록에서 그 채팅을 누릅니다.</p>'
        '<h3>인사말 음성</h3>' + q(one('음성 만들기')) + tool('음성 만들기')
        + '<p class="note">받는 사람을 바꿨으면 ‘친구’ 자리도 바꿉니다. 만들어지는 음성은 컴퓨터가 읽어 주는 목소리입니다.</p>'
        '<h3>그림과 음성으로 영상 만들기</h3><p>수업에서는 강사의 화면으로 봅니다. 시간이 남으면 직접 해봅니다.</p>'
        + q(one('쇼츠 영상')) + tool('쇼츠 영상')
        + '<p class="note">에이전트가 어느 그림을 쓸지 물으면 ' + say('말로 설명해서 받은 그림으로 해줘') + '라고 답합니다.</p>'
        + warn('에이전트가 프로그램을 설치하겠다고 물으면 허용하지 않고 강사에게 알립니다.')
        + learned('쇼츠에서 익힌 방법'), id='shorts'))

    b.append(sec(slide('오늘 익힌 방법')[3],
        tbl(['어디에서', '익힌 방법'], [[td(_h.escape(a)), td(_h.escape(t))] for a, t in METHODS])))

    b.append(sec(slide('오늘 만든 것')[3],
        tbl(['만든 것', '에이전트가 쓴 도구', '만들었으면 표시'],
            [[td(_h.escape(a)), td(_h.escape(t)),
              td(choose('made%d' % i, a + '을(를) 만들었는지', ['만듦'], kind='checkbox'))]
             for i, (a, t) in enumerate(MADE, 1)])))

    b.append(sec(slide('수업 뒤에 남는 것')[3],
        tbl(['어디에', '남는 것'], [[td(_h.escape(a)), td(_h.escape(t))] for a, t in LEFT])
        + warn('예약을 만들었다면 수업이 끝나기 전에 지웁니다.')
        + '<p class="note">2주차 폴더의 파일은 지워도 됩니다. 공개한 연하장을 내리는 방법은 수업에서 안내합니다.</p>'))

    b.append(sec(slide('이번 주')[3],
        '<p>오늘 만든 것 가운데 하나를 골라 프롬프트로 남기고, 새 채팅에서 그 프롬프트로 다시 만들어 봅니다. '
        '오늘 만든 연하장은 가족 한 사람에게 실제로 보내 봅니다.</p>'
        '<h3>프롬프트로 남길 것</h3>' + blank('hw', '이번 주에 프롬프트로 남길 것', '예: 연하장, 여행 계획 보고서')
        + '<h3>피클에 한 가지 맡겨 보기</h3>'
        + '<p>피클은 휴대폰에 설치하는 AI 에이전트입니다. 전화와 웹 작업으로 일을 대신 처리합니다. '
          '아이폰과 안드로이드에서 쓰고, PC용은 없습니다.</p>'
        + '<ul><li><a href="' + m.PICKLE_IOS + '" target="_blank" rel="noopener">아이폰: 앱스토어에서 설치</a></li>'
          '<li><a href="' + m.PICKLE_ANDROID + '" target="_blank" rel="noopener">안드로이드: 구글 플레이에서 설치</a></li>'
          '<li><a href="' + m.PICKLE_SITE + '" target="_blank" rel="noopener">공식 사이트: pickle.com/ko</a></li></ul>'
        + '<ul><li>애플, 구글, 카카오 계정이나 휴대폰 번호로 가입</li>'
          '<li>초대 링크가 없으면 대기 명단에 등록될 수 있음</li>'
          '<li>앱의 이름은 ‘피클: 나만의 AI 에이전트’. ‘피클플러스’와 다른 앱</li></ul>'
        + warn('전화는 걸기 전에 허락받게 하고, 결제와 예약은 내가 승인한 뒤에 하게 합니다. '
               '메일과 쇼핑 계정은 며칠 써 본 뒤에 연결합니다.')
        + blank('pickle', '피클에 맡겨 본 일과 결과', '예: 동네 빵집의 영업시간을 전화로 물어보기')
        + '<h3>잘 안 된 일</h3><p class="note">다음 주 수업에서 이야기합니다.</p>'
        + blank('next', '잘 안 된 일')))

    b.append(sec('막혔을 때',
        tbl(['상황', '할 일'], [
            [td('진행이 멈춘 것처럼 보일 때'), td('Codex 채팅을 아래로 내려 허용을 묻는 창이 떠 있는지 확인')],
            [td('에이전트가 만들어도 되는지 물을 때'), td(say('응, 만들어줘'))],
            [td('연하장을 공개해도 되는지 물을 때'), td('연하장을 읽어 본 뒤 공개해 달라고 답하기')],
            [td('보고서를 공개해도 되는지 물을 때'), td('공개하지 말라고 답하기')],
            [td('프로그램을 설치하겠다고 물을 때'), td('허용하지 않고 강사에게 알리기')],
            [td('폴더를 고를 수 없을 때'), td('폴더를 고르는 자리 옆의 ‘이 컴퓨터’가 선택돼 있는지 확인')],
            [td('문장을 다 적기 전에 보냈을 때'), td('에이전트를 멈추지 말고 나머지 문장을 이어서 보내기')],
            [td('결과가 마음에 들지 않을 때'), td('처음부터 다시 요청하지 않고, 고칠 곳을 한 가지씩 말하기')],
            [td('그림판 조작이 되지 않을 때'), td('그 단계를 건너뛰고 그림 받기부터 진행')]])))

    return doc('2주차 실습지', 'WEEK 2 / 4 · 수강생용', _h.escape(SUBJECT) + ' · 직접 적으면서 따라 하는 자료',
               '\n'.join(b), top=STORE_NOTE, script=STORE_JS, foot=False)


# ───────────────────────── 강사용 진행표 ─────────────────────────
DO = {'그림판으로 그리기', '그림 생성', '연하장 만들기', '연하장 고치기', '인터넷 주소', '서로 보내기',
      '프롬프트로 정리', '프롬프트 다듬기', '프롬프트 저장',
      '계획 보고서', '보고서 고치기', '관심 주제 보고서', '출처 확인', '블로그 글 쓰기', '장면 덧붙이기',
      '음성 만들기'}
SHOW = {'다시 쓰기', '매일 예약', '쇼츠 영상'}             # 강사의 화면으로 보여 주는 장표
ASK = {'지난 한 주', '빈칸', '받은 연하장', '품질 기준', '연하장에서 익힌 방법', '계획 보고서에서 익힌 방법',
       '주제 보고서에서 익힌 방법', '블로그 글에서 익힌 방법', '쇼츠에서 익힌 방법', '오늘 익힌 방법'}


def runsheet():
    b = []
    b.append(sec('강의 전에 준비할 것',
        '<ul>'
        '<li>ChatGPT 데스크탑 앱에서 Codex 화면이 열리는지 확인</li>'
        '<li>바탕화면의 <b>2주차</b> 폴더로 모든 실습을 한 번씩 직접 실행</li>'
        '<li>수강생용 실습지(<code>worksheet.html</code>) 주소를 수업 채팅창에 올릴 수 있게 준비</li>'
        '<li>아래의 ‘수업 채팅창에 올릴 문장’을 복사해 둘 곳 준비</li>'
        '<li>쇼츠 실습이 안 될 때 보여줄 영상 한 편 준비</li>'
        '</ul>'))

    b.append(sec('강의 전에 Windows에서 확인할 것',
        '<p class="note">리허설은 Mac에서 했습니다. 아래 항목은 수강생과 같은 Windows와 같은 요금제의 계정으로 '
        '한 번씩 실행해서, 되는지와 걸리는 시간을 확인합니다.</p>'
        + tbl(['항목', '확인할 내용', '안 될 때'], [
            [td('그림판으로 그리기'), td('허용 창이 뜨는지, 그림이 폴더에 저장되는지'), td('이 단계를 건너뛰고 그림 받기부터 진행')],
            [td('연하장 만들기'), td('‘지금까지 만든 그림’이 그림판 그림과 생성한 그림을 모두 가리키는지'), td('그림을 이름으로 다시 말하게 하기')],
            [td('연하장의 인터넷 주소'), td('주소가 발급되는지, 주소를 복사하는 위치, 공개한 연하장을 내리는 방법'), td('웹페이지 파일을 열어서 확인')],
            [td('매일 예약'), td('예약 항목이 생기는지, 지워지는지'), td('강사의 화면으로 보여 주기')],
            [td('음성 만들기'), td('음성 파일이 생기는지, 채팅에서 들리는지'), td('강사의 화면으로 보여 주기')],
            [td('쇼츠 영상'), td('영상이 만들어지는지, 도구 설치를 묻는지'), td('준비해 둔 영상 보여 주기')],
            [td('계획 보고서, 관심 주제 보고서, 블로그 글'),
             td('앱에서 실행해 보지 않음. 결과가 어디에 열리는지, 에이전트가 보고서를 공개하려고 하는지'),
             td('공개를 물으면 공개하지 말라고 답하게 하기')],
            [td('승인을 묻는 창'), td('연하장 공개와 음성 만들기에서 승인을 묻는 창이 뜨는지, 그 문구'),
             td('창의 문구를 미리 보여 주고 읽은 뒤 누르게 하기')]])))

    timed = [s for s in SLIDES if s[2] is not None]
    rows, cls = [], []
    for i, (title, seg, mins, line, _) in enumerate(timed):
        nxt = timed[i + 1][2] if i + 1 < len(timed) else 120
        tag = ('<span class="tag">실습</span>' if title in DO else
               '<span class="tag">시연</span>' if title in SHOW else
               '<span class="tag">질문</span>' if title in ASK else '')
        rows.append([td('%02d:%02d' % divmod(mins, 60), 't'), td('%d분' % (nxt - mins), 't'),
                     td(_h.escape(re.sub(r'^\d+주차 · ', '', seg))), td(_h.escape(title) + tag),
                     td(_h.escape(line))])
        cls.append('do' if title in DO else None)
    b.append(sec('시간표',
        '<p class="note">색이 칠해진 줄은 수강생이 직접 해보는 시간입니다. '
        '‘시연’은 강사의 화면으로 보여 주는 시간, ‘질문’은 수업 채팅창으로 답을 듣는 시간입니다.</p>'
        + tbl(['시각', '시간', '구간', '장표', '화면의 글'], rows, cls)))

    b.append(sec('수업 채팅창에 올릴 문장',
        tbl(['시각', '장표', '올릴 문장'],
            [[td(clock('오늘 만들 것'), 't'), td('오늘 만들 것'), td('수강생용 실습지 주소')]]
            + [[td(clock(t), 't'), td(_h.escape(t)), td(_h.escape(s))] for t in m.SAY for s in SAY[t]]
            + [[td(clock('다시 쓰기'), 't'), td('다시 쓰기'), td(_h.escape(REUSE))]])
        + '<p class="note">문장은 예시입니다. 수강생은 받는 사람, 주제, 경험을 자기 것으로 바꿔서 입력합니다.</p>'))

    b.append(sec('막힌 수강생에게 알려줄 문장',
        tbl(['상황', '알려줄 내용'], [
            [td('진행이 멈춘 것처럼 보임'), td('채팅을 아래로 내려 허용이나 승인을 묻는 창이 떠 있는지 확인')],
            [td('‘이 폴더를 신뢰할까요?’ 창이 뜸'), td('‘폴더 신뢰’ 누르기. 폴더마다 한 번만 뜸')],
            [td('‘(앱 이름)을(를) 사용하도록 허용할까요?’ 창이 뜸'), td('‘이 대화 허용’ 누르기')],
            [td('에이전트가 구성을 설명하고 확인을 구함'), td(say('응, 만들어줘'))],
            [td('연하장을 공개해도 되는지 물음'), td('연하장을 읽어 본 뒤 공개해 달라고 답하게 하기')],
            [td('보고서를 공개해도 되는지 물음'), td('공개하지 말라고 답하게 하기')],
            [td('폴더를 고를 수 없음'), td('옆의 ‘이 컴퓨터’가 눌려 있는지 확인')],
            [td('첫 문장만 전송함'), td('멈추지 않고 나머지 문장을 이어서 전송')],
            [td('결과가 마음에 들지 않음'), td('고칠 곳을 한 가지씩 말하기')],
            [td('쇼츠에서 어느 그림을 쓸지 물음'), td(say('말로 설명해서 받은 그림으로 해줘'))],
            [td('프로그램을 설치하겠다고 물음'), td('허용하지 않게 하고, 강사의 영상 보여 주기')],
            [td('예약을 지우지 않고 나가려 함'), td(say(UNRESERVE.rstrip('.')))]])))

    return doc('2주차 강사용 진행표', 'WEEK 2 / 4 · 강사용', _h.escape(SUBJECT) + ' · 시각별 진행과 수업 채팅창에 올릴 문장',
               '\n'.join(b), robots=True)


for name, fn in (('worksheet.html', worksheet), ('runsheet.html', runsheet)):
    text = fn()
    (out / name).write_text(text, encoding='utf-8')
    print('%-15s %6d bytes' % (name, len(text.encode())))
