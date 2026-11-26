# -*- coding: utf-8 -*-
"""w2.py 에서 실습 자료 두 개를 만듭니다.  python3 handouts.py 2

    ../worksheet.html   수강생용 실습지 (상황 카드 포함)
    ../runsheet.html    강사용 진행표

프롬프트 문장, 표, 시각은 덱(w2.py)에서 읽어 옵니다. 덱을 고친 뒤 이 스크립트를 다시 실행하면
두 자료도 같은 문장으로 바뀝니다. 기록란과 '막혔을 때 보낼 문장'처럼 덱에 없는 안내만 여기에 적습니다.
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


REQUEST = lines_of('실습 1')                          # (라벨, 문장) 요청 · 목적 · 읽는 사람 · 형식 · 확인
def joined(title):
    """lines() 로 나눠 적은 문장을 한 번에 보낼 형태로 이어 붙입니다."""
    return ' '.join(t for _, t in lines_of(title))


P2, P3, P3SAVE, P4 = (prompt(t) for t in ('질문 요청', '프롬프트 요청', '프롬프트 저장', '실습 4'))
P2FIX = prompt('문구 고치기')
ASKED = lines_of('에이전트의 질문')                 # 리허설에서 에이전트가 물어본 내용
ANSWER = lines_of('내 답')                         # 리허설에서 보낸 답
WRITTEN = lines_of('에이전트가 쓴 프롬프트')         # 리허설에서 에이전트가 쓴 프롬프트의 일부
P3RUN, P3AGAIN = joined('프롬프트대로 실행'), joined('프롬프트 다시 쓰기')
REDO = re.findall(r'“(.*?)”', cue('다시 요청하기', '예'))
FIT = table_of('잘 맞는 일')
METHODS = [slide(t)[3] for t in ('첫 번째 방식', '두 번째 방식', '세 번째 방식')]     # “첫 번째, 내가 다 적어서 요청”
NEXT = table_of('다음 단계')                         # [오늘 해본 방식, 다음 단계] 표. 첫 행은 머리글
NEXT_SAID = [lines_of(t)[0][1] for t in ('자료를 폴더에 두기', '계획부터 받기',
                                         '지침 파일로 남기기', '확인하게 하기')]   # 시연에서 보낸 요청, 표와 같은 순서


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
textarea.f{display:block;width:100%;min-height:36px;border:0;border-bottom:1.5px solid var(--line);border-radius:0;
  background:transparent;color:inherit;font:inherit;font-size:16px;line-height:1.5;padding:5px 2px;
  resize:none;overflow:hidden}
td.w textarea.f{border-bottom:0}
textarea.f::placeholder{color:var(--faint);opacity:.7}
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


def doc(title, kicker, lede, body, robots=False, top='', script=''):
    return ('<!DOCTYPE html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            + ('<meta name="robots" content="noindex">\n' if robots else '')
            + '<title>' + _h.escape(title) + '</title>\n<style>' + CSS + '</style>\n</head>\n<body>\n<main>\n'
            '<header><div class="kicker">' + kicker + '</div><h1>' + _h.escape(title) + '</h1>'
            '<p class="lede">' + lede + '</p>' + top + '</header>\n' + body +
            '\n<footer>이 문서는 <code>_build/handouts.py</code>가 덱에서 만든 생성물입니다.</footer>\n'
            '</main>\n' + (('<script>' + script + '</script>\n') if script else '') + '</body>\n</html>\n')


def q(text):
    return '<span class="q">“' + _h.escape(text) + '”</span>'


def say(text):
    return '<span class="say">“' + _h.escape(text) + '”</span>'


def sec(head, body, small=''):
    return '<section><h2>' + head + (('<small>' + small + '</small>') if small else '') + '</h2>' + body + '</section>'


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
def field(key, label, rows=1):
    return ('<textarea class="f" data-k="%s" rows="%d" aria-label="%s" placeholder="여기에 입력"></textarea>'
            % (key, rows, _h.escape(label, quote=True)))


def cell(key, label):
    return '<td class="w">' + field(key, label) + '</td>'


def blank(key, label):
    return '<div class="blank">' + field(key, label, 2) + '</div>'


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


def ease(n):
    return '<h3>이 방식이 편했던 정도</h3>' + choose('ease%d' % n, '실습 %d이 편했던 정도' % n, ['상', '중', '하'])


STORE_NOTE = ('<p class="store"><span>적은 내용은 이 기기의 브라우저에 저장됩니다. '
              '다른 기기나 다른 브라우저에서는 보이지 않습니다.</span>'
              '<button type="button" id="clear-all">적은 내용 모두 지우기</button>'
              '<span id="save-status" role="status" aria-live="polite"></span></p>')

# 저장소를 쓸 수 없는 브라우저(사생활 보호 모드 등)에서도 입력은 되도록 모든 접근을 try 로 감쌉니다.
STORE_JS = r"""
(function () {
  var KEY = 'lecture16-worksheet-v1';
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
def worksheet():
    b = []
    b.append(sec('시작하기 전에',
        '<ul>'
        '<li>바탕화면에 <b>2주차</b>라는 빈 폴더 만들기</li>'
        '<li>Codex의 새 채팅에서 <b>2주차</b> 폴더 고르기. ‘이 폴더를 신뢰할까요?’ 창이 뜨면 ‘폴더 신뢰’ 누르기</li>'
        '<li>전화번호와 주소는 적지 않기. 화면에 보여도 괜찮은 이야기만 적기</li>'
        '<li>엔터를 누르면 바로 전송. 여러 문장은 줄을 바꾸지 않고 이어서 적은 뒤 한 번에 전송</li>'
        '</ul>'))

    b.append(sec('인사 카드를 받을 세 사람',
        '<p>고마운 사람에게 보내는 인사 카드를 웹페이지로 만듭니다. '
        '세 가지 방식으로 세 장을 만들고, 받는 사람은 실습마다 바꿉니다.</p>'
        + tbl(['실습', '받는 사람', '함께한 일 한 가지'],
              [[td(t), cell('who%d' % i, t + ' 카드를 받는 사람'), cell('what%d' % i, t + ' 카드를 받는 사람과 함께한 일')]
               for i, t in enumerate(('첫 번째', '두 번째', '세 번째'), 1)])
        + '<h3>화면에 나오는 예시</h3>'
        '<p class="note">강의 화면의 세 사람입니다. 실습을 위해 지어낸 예시입니다.</p>'
        + tbl(['받는 사람', '함께한 일 한 가지'], [
            [td('여든둘 되신 어머니'), td('여름에 같이 김치를 담금')],
            [td('고등학교 때 담임이셨던 김 선생님'), td('졸업식 날 손편지를 받음')],
            [td('30년 친구 영희'), td('봄에 같이 지리산에 다녀옴')]])
        + '<p class="note">세 사람이 떠오르지 않으면 한 사람에게 세 장을 만들어도 됩니다. '
          '전화번호, 주소, 주민등록번호는 적지 않습니다.</p>'))

    rows = [[td('<b>' + _h.escape(a) + '</b>'), td('“' + _h.escape(s) + '”'), cell('req%d' % i, a + ' 줄에 적을 내 문장')]
            for i, (a, s) in enumerate(REQUEST, 1)]
    b.append(sec('첫 번째 카드의 요청 적기',
        '<p>화면의 예시를 보고, 첫 번째 카드에 맞는 문장을 오른쪽 칸에 적습니다. '
        '첫 줄과 마지막 줄은 예시를 그대로 적습니다.</p>'
        + tbl(['줄', '예시', '내 문장'], rows), clock('요청')))

    b.append(sec(METHODS[0],
        '<ol>'
        '<li>적어 둔 문장을 모두, 줄을 바꾸지 않고 이어서 입력</li>'
        '<li>한 번에 전송</li>'
        '<li>만들어진 카드 열어 보기</li>'
        '</ol>'
        '<h3>카드에서 확인할 것</h3>'
        + choose('check', '첫 번째 카드에서 확인할 것',
                 ['받는 사람의 이름이 있음', '내가 말하지 않은 이야기가 없음'], kind='checkbox') +
        '<h3>한 번 고쳐달라고 요청하기</h3>'
        '<p>예: ' + ', '.join(say(r) for r in REDO) + '</p>'
        + ease(1), clock('실습 1')))

    b.append(sec(METHODS[1],
        '<ol>'
        '<li>왼쪽 위 <b>새 채팅</b> 누르기</li>'
        '<li><b>2주차</b> 폴더 다시 고르기</li>'
        '<li>아래 문장을 그대로 전송' + q(P2) + '</li>'
        '<li>에이전트의 질문에 답하기. 아는 것은 답하고, 모르는 것은 ' + say('추천해줘') + '</li>'
        '<li>에이전트가 보여준 문구를 읽고, 내가 말하지 않은 내용이 있으면 빼달라고 요청' + q(P2FIX) + '</li>'
        '<li>문구가 마음에 들면 ' + say('좋아, 만들어줘') + '</li>'
        '</ol>'
        '<h3>화면의 예시: 에이전트가 물어본 내용</h3>'
        + tbl(['묻는 내용', '질문'], [[td(_h.escape(a)), td(_h.escape(t))] for a, t in ASKED])
        + '<h3>화면의 예시: 한 번에 보낸 답</h3>'
        + tbl(['답하는 내용', '문장'], [[td(_h.escape(a)), td('“' + _h.escape(t) + '”')] for a, t in ANSWER])
        + '<h3>카드에서 확인할 것</h3>'
        + choose('check2', '두 번째 카드에서 확인할 것',
                 ['받는 사람이 있음', '내가 말하지 않은 이야기가 없음'], kind='checkbox') +
        '<h3>진행이 막힐 때 보낼 문장</h3>'
        + tbl(['상황', '보낼 문장'], [
            [td('질문이 너무 많을 때'), td(say('세 가지만 질문해줘'))],
            [td('답을 다 했는데 시작하지 않을 때'), td(say('이제 만들어줘'))],
            [td('파일 종류를 묻지 않을 때'), td(say('웹페이지로 만들어줘'))]])
        + '<h3>에이전트가 물어본 내용 가운데 첫 번째 실습에서 적지 않았던 것</h3>'
        + blank('asked', '에이전트가 물어본 내용 가운데 첫 번째 실습에서 적지 않았던 것')
        + ease(2), clock('실습 2')))

    b.append(sec(METHODS[2],
        '<ol>'
        '<li>새 채팅을 누르고 <b>2주차</b> 폴더 고르기</li>'
        '<li>프롬프트를 써달라고 요청' + q(P3) + '</li>'
        '<li>에이전트가 쓴 프롬프트에 받는 사람이 적혀 있는지 찾아보기</li>'
        '<li>빠진 내용을 문장으로 알려주고 실행' + q(P3RUN) +
        '<span class="note">받는 사람과 추억은 예시입니다. 세 번째로 정한 사람의 내용으로 바꿉니다. '
        '프롬프트를 복사해서 고치지 않습니다.</span></li>'
        '<li>카드가 나온 뒤 프롬프트 저장' + q(P3SAVE) + '</li>'
        '<li>새 채팅에서 저장한 프롬프트로 한 장 더 만들기' + q(P3AGAIN) +
        '<span class="note">받는 사람만 바꾸면 앞 사람의 추억이 그대로 남습니다. 추억도 함께 바꿉니다.</span></li>'
        '</ol>'
        '<h3>화면의 예시: 에이전트가 쓴 프롬프트</h3>'
        + tbl(['항목', '내용'], [[td(_h.escape(a)), td(('“' + _h.escape(t) + '”') if a != '받는 사람' else _h.escape(t))]
                               for a, t in WRITTEN])
        + '<h3>카드에서 확인할 것</h3>'
        + choose('check3', '세 번째 카드에서 확인할 것',
                 ['받는 사람과 추억이 내 내용으로 바뀜', '‘카드 프롬프트’ 파일이 폴더에 생김'], kind='checkbox')
        + ease(3), clock('프롬프트 요청')))

    fit_rows = [[td(_h.escape(r[0])), td(_h.escape(r[1]))] for r in FIT[1:]]
    b.append(sec('가장 편했던 방식 고르기',
        choose('best', '가장 편했던 방식', ['첫 번째', '두 번째', '세 번째']) +
        '<p class="note">결과의 품질이 아니라 얼마나 편했는지를 기준으로 고릅니다.</p>'
        '<h3>' + _h.escape(slide('잘 맞는 일')[3]) + '</h3>'
        + tbl([_h.escape(c) for c in FIT[0]], fit_rows), clock('어느 방식')))

    assert len(NEXT) - 1 == len(NEXT_SAID), '다음 단계 표와 시연 장표의 수가 다릅니다'
    b.append(sec(slide('다음 단계')[3],
        '<p>수업에서는 강사가 보여주는 화면을 봅니다. 수업이 끝난 뒤에 한 가지씩 내 카드에 해봅니다.</p>'
        + ''.join('<h3>' + _h.escape(r[1]) + '</h3>' + q(t) for r, t in zip(NEXT[1:], NEXT_SAID))
        + '<p class="note">예로 적힌 이름과 추억은 내 카드에 맞게 바꿉니다.</p>', clock('다음 단계')))

    b.append(sec('네 번째 실습 · 다른 방법 묻기',
        '<p>세 번째 카드를 만든 채팅에 그대로 보냅니다. 에이전트가 알려준 방법은 읽기만 합니다.</p>'
        + q(P4) + '<h3>해보고 싶은 방법 한 가지</h3>' + blank('try', '해보고 싶은 방법 한 가지'), clock('실습 4')))

    b.append(sec(slide('이번 주')[3],
        '<p>오늘 고른 방식을 내 일에 세 번 써봅니다. 오늘 만든 카드 한 장은 실제로 보내 봅니다.</p>'
        + tbl(['회차', '요청한 일', '결과와 느낀 점'],
              [[td(str(i)), cell('hw%d-task' % i, '%d회차에 요청한 일' % i),
                cell('hw%d-result' % i, '%d회차의 결과와 느낀 점' % i)] for i in (1, 2, 3)])
        + '<h3>다음 주에 이야기할 잘 안 된 일 한 가지</h3>'
        + blank('next', '다음 주에 이야기할 잘 안 된 일 한 가지')))

    b.append(sec('진행이 멈췄을 때',
        tbl(['상황', '할 일'], [
            [td('진행이 멈춘 것처럼 보일 때'), td('승인 요청이 화면에 떠 있는지 확인')],
            [td('에이전트가 계획을 설명하고 확인을 구할 때'), td(say('좋아, 만들어줘'))],
            [td('폴더를 고를 수 없을 때'), td('옆의 ‘이 컴퓨터’가 눌려 있는지 확인')],
            [td('문장을 다 적기 전에 전송했을 때'), td('멈추지 않고 나머지 문장을 이어서 전송')],
            [td('앞에서 만든 카드 파일을 덮어쓰려고 할 때'), td(say('다른 이름으로 저장해줘'))],
            [td('프롬프트를 쓰지 않고 바로 만들기 시작할 때'), td(say('멈추고 프롬프트만 써줘'))]])))

    return doc('2주차 실습지', 'WEEK 2 / 4 · 수강생용', _h.escape(SUBJECT) + ' · 직접 적으면서 따라 하는 자료',
               '\n'.join(b), top=STORE_NOTE, script=STORE_JS)


# ───────────────────────── 강사용 진행표 ─────────────────────────
DO = {'실습 1', '다시 요청하기', '실습 2', '프롬프트 요청', '프롬프트대로 실행', '프롬프트 저장',
      '프롬프트 다시 쓰기', '실습 4'}
WRITE = {'요청', '목적', '읽는 사람', '형식', '확인 방법'}
ASK = {'체크인', '빈칸', '오늘 만들 것', '질문의 효과', '어느 방식', '확인 질문'}


def runsheet():
    b = []
    b.append(sec('강의 전에 준비할 것',
        '<ul>'
        '<li>ChatGPT 데스크탑 앱에서 Codex 화면이 열리는지 확인</li>'
        '<li>바탕화면의 <b>2주차</b> 폴더로 실습 1~3을 한 번 직접 실행</li>'
        '<li>수강생용 실습지(<code>worksheet.html</code>) 주소를 채팅창에 올릴 수 있게 준비</li>'
        '<li>아래의 ‘채팅창에 올릴 문장’을 복사해 둘 곳 준비</li>'
        '<li>‘같은 요청, 달라지는 답’ 장에서 보여줄 결과 두 개 준비 (선택)</li>'
        '<li>카드를 받을 사람이 떠오르지 않는 수강생에게 알려줄 예시 준비 (실습지에 세 가지 수록)</li>'
        '</ul>'))

    timed = [s for s in SLIDES if s[2] is not None]
    rows, cls = [], []
    for i, (title, seg, mins, line, _) in enumerate(timed):
        nxt = timed[i + 1][2] if i + 1 < len(timed) else 120
        tag = ('<span class="tag">실습</span>' if title in DO else
               '<span class="tag">적기</span>' if title in WRITE else
               '<span class="tag">질문</span>' if title in ASK else '')
        rows.append([td('%02d:%02d' % divmod(mins, 60), 't'), td('%d분' % (nxt - mins), 't'),
                     td(_h.escape(re.sub(r'^\d+주차 · ', '', seg))), td(_h.escape(title) + tag),
                     td(_h.escape(line))])
        cls.append('do' if title in DO else None)
    b.append(sec('시간표',
        '<p class="note">색이 칠해진 줄은 수강생이 Codex에 직접 입력하는 시간입니다. '
        '‘적기’는 종이에 자기 문장을 적는 시간, ‘질문’은 채팅창으로 답을 듣는 시간입니다.</p>'
        + tbl(['시각', '시간', '구간', '장표', '화면의 문장'], rows, cls)))

    request = ' '.join(s if s.endswith(('.', '?')) else s + '.' for _, s in REQUEST)
    b.append(sec('채팅창에 올릴 문장',
        tbl(['시각', '장표', '올릴 문장'], [
            [td(clock('오늘 만들 것'), 't'), td('오늘 만들 것'), td('수강생용 실습지 주소')],
            [td(clock('실습 1'), 't'), td('실습 1'), td(_h.escape(request))],
            [td(clock('다시 요청하기'), 't'), td('다시 요청하기'), td(_h.escape(prompt('다시 요청하기')))],
            [td(clock('실습 2'), 't'), td('실습 2'), td(_h.escape(P2))],
            [td(clock('프롬프트 요청'), 't'), td('프롬프트 요청'), td(_h.escape(P3))],
            [td(clock('프롬프트대로 실행'), 't'), td('프롬프트대로 실행'), td(_h.escape(P3RUN))],
            [td(clock('프롬프트 저장'), 't'), td('프롬프트 저장'), td(_h.escape(P3SAVE))],
            [td(clock('프롬프트 다시 쓰기'), 't'), td('프롬프트 다시 쓰기'), td(_h.escape(P3AGAIN))],
            [td(clock('실습 4'), 't'), td('실습 4'), td(_h.escape(P4))]])
        + '<p class="note">실습 1의 문장은 화면의 요청을 줄을 바꾸지 않고 이어 붙인 형태입니다. '
          '수강생은 자기가 적어 둔 문장으로 바꿔서 입력합니다.</p>'))

    b.append(sec('막힌 수강생에게 알려줄 문장',
        tbl(['상황', '알려줄 내용'], [
            [td('진행이 멈춘 것처럼 보임'), td('승인 요청이 화면에 떠 있는지 확인')],
            [td('‘이 폴더를 신뢰할까요?’ 창이 뜸'), td('‘폴더 신뢰’ 누르기. 폴더마다 한 번만 뜸')],
            [td('에이전트가 계획을 설명하고 확인을 구함'), td(say('좋아, 만들어줘'))],
            [td('폴더를 고를 수 없음'), td('옆의 ‘이 컴퓨터’가 눌려 있는지 확인')],
            [td('첫 문장만 전송함'), td('멈추지 않고 나머지 문장을 이어서 전송')],
            [td('에이전트의 질문이 너무 많음'), td(say('세 가지만 질문해줘'))],
            [td('답을 모르는 질문이 나옴'), td(say('추천해줘'))],
            [td('답을 다 했는데 시작하지 않음'), td(say('이제 만들어줘'))],
            [td('파일 종류를 묻지 않음'), td(say('웹페이지로 만들어줘'))],
            [td('앞 실습의 결과 파일을 덮어쓰려고 함'), td(say('다른 이름으로 저장해줘'))],
            [td('프롬프트를 쓰지 않고 바로 만들기 시작함'), td(say('멈추고 프롬프트만 써줘'))],
            [td('실습 4에서 바로 만들기 시작함'), td(say('만들지 말고 알려주기만 해줘'))]])))

    return doc('2주차 강사용 진행표', 'WEEK 2 / 4 · 강사용', _h.escape(SUBJECT) + ' · 시각별 진행과 채팅창에 올릴 문장',
               '\n'.join(b), robots=True)


for name, fn in (('worksheet.html', worksheet), ('runsheet.html', runsheet)):
    text = fn()
    (out / name).write_text(text, encoding='utf-8')
    print('%-15s %6d bytes' % (name, len(text.encode())))
