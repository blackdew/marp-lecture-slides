# -*- coding: utf-8 -*-
CSS = """
*{box-sizing:border-box}
:root{
  --bg:#101318; --panel:#171B22; --panel2:#1E242D; --line:#2A313C; --line2:#374151;
  --fg:#E9EBEF; --dim:#A6AEBA; --faint:#6E7784;
  --acc:#5ECFAE; --accs:rgba(94,207,174,.13); --accl:rgba(94,207,174,.40);
  --warn:#E3A75A; --warns:rgba(227,167,90,.12); --warnl:rgba(227,167,90,.38);
  color-scheme:dark;
}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]){
  --bg:#F6F5F2; --panel:#FFFFFF; --panel2:#F1EEE8; --line:#DEDAD1; --line2:#C8C3B8;
  --fg:#1A1D22; --dim:#525B66; --faint:#88919C;
  --acc:#13735F; --accs:rgba(19,115,95,.09); --accl:rgba(19,115,95,.32);
  --warn:#8A5A14; --warns:rgba(138,90,20,.09); --warnl:rgba(138,90,20,.30);
  color-scheme:light;
}}
:root[data-theme="light"]{
  --bg:#F6F5F2; --panel:#FFFFFF; --panel2:#F1EEE8; --line:#DEDAD1; --line2:#C8C3B8;
  --fg:#1A1D22; --dim:#525B66; --faint:#88919C;
  --acc:#13735F; --accs:rgba(19,115,95,.09); --accl:rgba(19,115,95,.32);
  --warn:#8A5A14; --warns:rgba(138,90,20,.09); --warnl:rgba(138,90,20,.30);
  color-scheme:light;
}
body{
  margin:0; background:var(--bg); color:var(--fg);
  font-family:"IBM Plex Sans KR","Noto Sans KR",-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-weight:400; -webkit-font-smoothing:antialiased; word-break:keep-all; overflow-wrap:break-word;
  padding-left:max(16px,env(safe-area-inset-left,0px));
  padding-right:max(16px,env(safe-area-inset-right,0px));
}
.app{max-width:1500px;margin:0 auto;padding-block:14px 10px}
.wrap{position:relative}
.stage{
  position:relative; container-type:inline-size; aspect-ratio:16/9;
  background:var(--panel); border:1px solid var(--line); border-radius:16px; overflow:hidden;
}

/* ---------- slide frame ---------- */
.s{position:absolute;inset:0;display:none;flex-direction:column;padding:4.2cqi 5cqi 3.4cqi;min-width:0}
.s.on{display:flex}
.eyebrow{display:flex;align-items:baseline;gap:1.4cqi;flex:0 0 auto;margin-bottom:2.2cqi}
.eyebrow b{font-size:1.28cqi;font-weight:600;letter-spacing:.16em;color:var(--acc)}
.eyebrow span{font-size:1.22cqi;letter-spacing:.14em;color:var(--faint)}
.eyebrow i{margin-left:auto;font-style:normal;font-size:1.22cqi;letter-spacing:.08em;color:var(--faint);font-family:"IBM Plex Mono",monospace}
h2.a{
  font-size:3.45cqi; line-height:1.2; font-weight:600; letter-spacing:-.022em;
  margin:0 0 2.4cqi; max-width:30ch; text-wrap:balance;
}
h2.a em{font-style:normal;color:var(--acc)}
.sub{font-size:1.58cqi;line-height:1.5;color:var(--dim);margin:-1.2cqi 0 2.2cqi;max-width:62ch}
.body{flex:1 1 auto;display:flex;flex-direction:column;gap:1.6cqi;min-height:0;min-width:0}
.foot{flex:0 0 auto;margin-top:2cqi;font-size:1.36cqi;line-height:1.52;color:var(--dim);max-width:76ch}
.foot b{color:var(--fg);font-weight:600}

/* ---------- cover / section / statement / break ---------- */
.s.cover,.s.sect,.s.stmt,.s.brk{justify-content:center;padding:6cqi 7cqi}
.s.cover{background:
  radial-gradient(120% 90% at 86% 8%, var(--accs), transparent 60%),
  var(--panel);}
.kicker{font-size:1.3cqi;font-weight:600;letter-spacing:.3em;color:var(--acc);margin-bottom:2.6cqi}
h1{font-size:6.2cqi;line-height:1.2;font-weight:700;letter-spacing:-.015em;margin:0 0 3.2cqi;max-width:21ch;text-wrap:balance;word-break:keep-all}
h1 em{font-style:normal;color:var(--acc)}
.lede{font-size:1.86cqi;line-height:1.56;color:var(--dim);max-width:52ch;margin:0 0 3.4cqi}
.chips{display:flex;flex-wrap:wrap;gap:.9cqi}
.chip{font-size:1.24cqi;letter-spacing:.04em;color:var(--dim);border:1px solid var(--line2);border-radius:99px;padding:.7cqi 1.5cqi}
.chip.on{border-color:var(--accl);color:var(--acc);background:var(--accs)}
.s.sect{background:var(--panel2)}
.s.sect .kicker{color:var(--faint)}
.s.sect h1{font-size:5.6cqi;max-width:22ch}
.s.stmt{align-items:flex-start;background:var(--panel2)}
.s.stmt p{font-size:5cqi;line-height:1.24;font-weight:600;letter-spacing:-.03em;margin:0;max-width:26ch;text-wrap:balance}
.s.stmt p em{font-style:normal;color:var(--acc)}
.s.stmt .tag{margin-top:3.2cqi;font-size:1.3cqi;letter-spacing:.2em;color:var(--faint)}
.s.brk{align-items:center;text-align:center}
.s.brk h1{font-size:4.6cqi;max-width:24ch}
.s.brk .lede{margin:0 auto;max-width:44ch}

/* ---------- cards ---------- */
.cards{display:grid;gap:1.0cqi;flex:1 1 auto;min-height:0}
.cards.c2{grid-template-columns:1fr 1fr}
.cards.c3{grid-template-columns:repeat(3,1fr)}
.cards.c4{grid-template-columns:repeat(4,1fr)}
.cards.tight{flex:0 0 auto}
.body > .cards.tight:only-child{margin:auto 0}
.card{
  display:flex;flex-direction:column;gap:.7cqi;min-width:0;
  background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:1.62cqi 1.7cqi;
}
.card.hi{border-color:var(--accl);background:var(--accs)}
.card.wa{border-color:var(--warnl);background:var(--warns)}
.card .lab{font-size:1.1cqi;font-weight:600;letter-spacing:.14em;color:var(--faint)}
.card.hi .lab{color:var(--acc)}
.card.wa .lab{color:var(--warn)}
.card h3{font-size:1.86cqi;line-height:1.3;font-weight:600;letter-spacing:-.01em;margin:0}
.card p{font-size:1.34cqi;line-height:1.47;color:var(--dim);margin:0}
.card p b{color:var(--fg);font-weight:600}
.card .num{font-size:3.6cqi;font-weight:700;letter-spacing:-.03em;color:var(--acc);line-height:1}

/* ---------- steps ---------- */
ol.steps,ul.steps{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:1.15cqi;counter-reset:st}
ol.steps li{counter-increment:st;display:grid;grid-template-columns:auto 1fr;gap:1.4cqi;align-items:start}
ol.steps li::before{
  content:counter(st);font-family:"IBM Plex Mono",monospace;font-size:1.3cqi;font-weight:500;
  width:2.5cqi;height:2.5cqi;display:grid;place-items:center;border-radius:99px;
  border:1px solid var(--accl);color:var(--acc);background:var(--accs);margin-top:.15cqi;
}
ul.steps li{display:grid;grid-template-columns:auto 1fr;gap:1.4cqi;align-items:start}
ul.steps li::before{content:"";width:.7cqi;height:.7cqi;border-radius:99px;background:var(--acc);margin-top:1.05cqi}
.steps li b{display:block;font-size:1.74cqi;line-height:1.34;font-weight:600;margin-bottom:.3cqi}
.steps li span{display:block;font-size:1.38cqi;line-height:1.5;color:var(--dim)}

/* ---------- table ---------- */
.tw{flex:1 1 auto;min-height:0;min-width:0;overflow:auto}
table{width:100%;border-collapse:collapse;font-size:1.33cqi}
th,td{text-align:left;padding:1.0cqi 1.2cqi;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.46}
thead th{font-size:1.18cqi;font-weight:600;letter-spacing:.1em;color:var(--faint);border-bottom:1px solid var(--line2);white-space:nowrap}
tbody tr:last-child td{border-bottom:0}
td:first-child{font-weight:600;color:var(--fg);white-space:nowrap}
td.g{color:var(--dim)}
td em{font-style:normal;color:var(--acc);font-weight:600}
table.cmp{font-size:1.92cqi}
table.cmp th,table.cmp td{padding:1.6cqi 1.4cqi;width:50%;word-break:keep-all}
table.cmp thead th{font-size:1.3cqi}
table.cmp thead th:last-child{color:var(--acc)}
table.cmp td:first-child{color:var(--dim);font-weight:400;white-space:normal}
table.cmp td:last-child{color:var(--fg);font-weight:600}
table.sum4{font-size:1.95cqi}
table.sum4 th,table.sum4 td{padding:1.3cqi 1.2cqi}
table.sum4 thead th{font-size:1.28cqi}
table.sum4 td:last-child{color:var(--acc);font-weight:600;white-space:nowrap}
table.vs td:first-child{color:var(--dim);font-weight:400}
table.vs th:nth-child(2),table.vs td:nth-child(2){color:var(--dim)}
table.vs th:nth-child(3),table.vs td:nth-child(3){background:var(--accs)}
table.vs td:nth-child(3){color:var(--fg);font-weight:500}

/* ---------- terminal / prompt ---------- */
.term{
  background:#0C0F14;border:1px solid var(--line2);border-radius:10px;overflow:hidden;
  display:flex;flex-direction:column;min-width:0;min-height:0;
}
:root[data-theme="light"] .term{background:#15181D}
@media (prefers-color-scheme: light){:root:not([data-theme="dark"]) .term{background:#15181D}}
.term .th{
  display:flex;align-items:center;gap:1cqi;padding:.85cqi 1.3cqi;
  border-bottom:1px solid rgba(255,255,255,.09);background:rgba(255,255,255,.035);
}
.term .th span{font-size:1.1cqi;letter-spacing:.1em;color:#8A93A0;font-weight:600}
.term .th .dot{width:.75cqi;height:.75cqi;border-radius:99px;background:#5ECFAE;opacity:.8;flex:0 0 auto}
.copy{
  margin-left:auto;font:inherit;font-size:1.08cqi;font-weight:600;letter-spacing:.06em;cursor:pointer;
  color:#9BE8D1;background:rgba(94,207,174,.14);border:1px solid rgba(94,207,174,.34);
  border-radius:6px;padding:.4cqi 1cqi;
}
.copy:hover{background:rgba(94,207,174,.24)}
.copy.ok{color:#0C0F14;background:#5ECFAE;border-color:#5ECFAE}
.term pre{
  margin:0;padding:1.5cqi 1.6cqi;overflow:auto;flex:1 1 auto;word-break:break-word;
  font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:1.3cqi;line-height:1.56;
  color:#D7DCE4;white-space:pre-wrap;word-break:break-word;
}
.term pre .c{color:#7A8494}
.term pre .p{color:#5ECFAE}
.term pre .o{color:#E3A75A}
/* 긴 프롬프트는 글자를 줄여서 스크롤 없이 한 화면에 들어오게 합니다 */
.term.t2 pre{font-size:1.15cqi;line-height:1.52;padding:1.3cqi 1.4cqi}
.term.t3 pre{font-size:1.0cqi;line-height:1.48;padding:1.1cqi 1.2cqi}

/* ---------- 키워드 한 장 ---------- */
.s.big .bigwrap{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;min-height:0;min-width:0}
.s.big .bigwrap.row{flex-direction:row;align-items:center;gap:5cqi}
.s.big .bigwrap.row .bigbody{border-left:1px solid var(--line);padding-left:5cqi}
/* 번호 달린 목차 */
.ag2{display:flex;flex-direction:column;list-style:none;margin:0;padding:0}
.ag2 li{display:flex;align-items:baseline;gap:2.4cqi;padding:1.45cqi 0;border-bottom:1px solid var(--line)}
.ag2 li:last-child{border-bottom:0}
.ag2 u{text-decoration:none;font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:1.25cqi;letter-spacing:.12em;color:var(--faint);flex:0 0 auto}
.ag2 b{font-size:2.5cqi;font-weight:600;letter-spacing:-.015em;word-break:keep-all}
.ag2 li.on b{color:var(--acc)}
.ag2 li.on u{color:var(--acc);opacity:.75}
.s.big .bigwrap.row .bigcol{flex:0 0 auto}
.s.big .bigwrap.row .bigbody{flex:1 1 auto;min-width:0}
.bigword{font-weight:700;color:var(--fg);word-break:keep-all;
  font-size:11cqi;line-height:1.0;letter-spacing:-.03em}
.bigword.b2{font-size:8.7cqi;line-height:1.1;letter-spacing:-.022em}
.bigword.b3{font-size:6.9cqi;line-height:1.16;letter-spacing:-.015em}
.bigword.b4{font-size:5.7cqi;line-height:1.22;letter-spacing:-.01em}
.bigword em{font-style:normal;color:var(--acc)}
.bigword small{font-size:.3em;font-weight:600;letter-spacing:-.02em;margin-left:.08em}
.bigsub{font-size:1.85cqi;line-height:1.5;color:var(--dim);margin:2.6cqi 0 0;max-width:48ch}
.bigsub b{color:var(--fg);font-weight:600}

/* ---------- 위트 한 장 ---------- */
.s.quip{align-items:center;justify-content:center;text-align:center;gap:3.2cqi}
.quipart{width:19cqi;color:var(--acc);flex:0 0 auto}
.s.quip.lg .quipart{width:26cqi}
.s.quip.sm .quipart{width:13cqi}
.quipart svg{display:block;width:100%;height:auto}
.quipline{font-size:3.9cqi;line-height:1.42;font-weight:600;letter-spacing:-.008em;margin:0;max-width:26ch;text-wrap:balance;word-break:keep-all}
.s.quip.lg .quipline{font-size:4.4cqi;max-width:21ch}
.s.quip.sm .quipline{font-size:3.2cqi;max-width:34ch}
.quipline em{font-style:normal;color:var(--acc)}
.quipfoot{font-size:1.4cqi;color:var(--faint);margin:0}

/* ---------- 캡처 한 장 ---------- */
.s.shot{align-items:center;gap:2.4cqi}
.shotimg{flex:1 1 auto;min-height:0;min-width:0;display:flex;align-items:center;justify-content:center;width:100%}
.shotimg img{max-width:100%;max-height:100%;width:auto;height:auto;display:block;
  border-radius:12px;border:1px solid var(--line2);box-shadow:0 6px 28px rgba(0,0,0,.28)}
.shotline{flex:0 0 auto;font-size:2.9cqi;line-height:1.38;font-weight:600;letter-spacing:-.008em;word-break:keep-all;
  margin:0;text-align:center;max-width:36ch;text-wrap:balance}
.shotline em{font-style:normal;color:var(--acc)}

/* ---------- 설명 목록 ---------- */
.bl{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;justify-content:center;gap:1.5cqi;flex:1 1 auto;min-width:0}
.bl li{font-size:1.95cqi;line-height:1.5;color:var(--dim);padding-left:2cqi;position:relative;word-break:keep-all}
.bl li::before{content:"";position:absolute;left:0;top:.66em;width:.62cqi;height:.62cqi;border-radius:99px;background:var(--acc);opacity:.7}
.bl b{color:var(--fg);font-weight:600}

/* ---------- 키워드 줄 ---------- */
.lines{display:flex;flex-direction:column;justify-content:center;gap:1.9cqi;flex:1 1 auto;min-height:0}
.lines.t{justify-content:flex-start;flex:0 0 auto}
.lines > div{display:flex;flex-wrap:wrap;align-items:baseline;gap:.4cqi 1.8cqi;min-width:0}
.lines b{font-size:2.9cqi;font-weight:600;letter-spacing:-.02em}
.lines b em{font-style:normal;color:var(--acc)}
.lines span{font-size:1.75cqi;line-height:1.5;color:var(--dim)}
/* 따옴표가 내용인 줄: 라벨과 비슷한 무게로 */
.lines.q{gap:2.4cqi}
.lines.q span{font-size:2.3cqi;line-height:1.4;color:var(--dim)}

/* ---------- 도해 전면 ---------- */
.figfull{flex:1 1 auto;display:flex;align-items:center;min-height:0;min-width:0}
.figfull svg{display:block;width:100%;height:auto;max-width:100%;color:var(--fg)}
.figfull svg text{word-break:normal}

/* ---------- figure ---------- */
figure{margin:0;flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:1.4cqi;min-height:0;min-width:0}
figure svg{display:block;width:100%;height:auto;flex:0 1 auto;min-height:0;max-width:100%;color:var(--fg)}
figure svg text{word-break:normal}
figcaption{font-size:1.3cqi;line-height:1.5;color:var(--dim);flex:0 0 auto}
figcaption b{color:var(--fg);font-weight:600}

/* ---------- fill (instructor slot) ---------- */
.fill{
  border:1.5px dashed var(--warnl);border-radius:10px;background:var(--warns);
  padding:1.8cqi;display:flex;flex-direction:column;gap:.7cqi;min-width:0;
}
.fill .lab{font-size:1.1cqi;font-weight:600;letter-spacing:.14em;color:var(--warn)}
/* 강사 입력 칸이 혼자 있을 때는 장표를 채웁니다 */
.body > .fill:only-child{flex:1 1 auto;display:flex;flex-direction:column;justify-content:center;gap:1cqi}
.fill p{margin:0;font-size:1.4cqi;line-height:1.52;color:var(--dim)}
.warn{
  border-left:2px solid var(--warn);background:var(--warns);border-radius:0 8px 8px 0;
  padding:1.2cqi 1.6cqi;font-size:1.32cqi;line-height:1.5;color:var(--dim);
}
.warn b{color:var(--warn);font-weight:600}
.note-i{
  border-left:2px solid var(--accl);background:var(--accs);border-radius:0 8px 8px 0;
  padding:1.2cqi 1.6cqi;font-size:1.34cqi;line-height:1.52;color:var(--dim);
}
.note-i b{color:var(--fg);font-weight:600}

/* ---------- misc layout ---------- */
.split{display:grid;grid-template-columns:1fr 1fr;gap:1.6cqi;flex:1 1 auto;min-height:0;min-width:0}
.split.w{grid-template-columns:1.15fr .85fr}
.split.n{grid-template-columns:.85fr 1.15fr}
.trio{display:grid;grid-template-columns:1fr 1.62fr 1fr;gap:2.6cqi;flex:1 1 auto;
  min-height:0;min-width:0;align-items:stretch}
.trio > *{min-width:0;min-height:0}
.trio .bl{align-self:center;flex:0 0 auto;justify-content:center;gap:1.35cqi}
.trio .bl li{font-size:1.72cqi;line-height:1.52}
.pshot{display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:1.2cqi;height:100%;min-width:0;min-height:0}
.pshot .shotimg,.pshot .figfull{flex:1 1 auto;min-height:0}
.pshot .figfull svg{max-height:100%}
.lnk{display:inline-block;flex:0 0 auto;font-family:"IBM Plex Mono",ui-monospace,monospace;
  font-size:1.18cqi;letter-spacing:.03em;color:var(--faint);text-decoration:none;
  border-bottom:1px solid var(--line2);padding-bottom:.3cqi;word-break:break-all}
.lnk:hover{color:var(--acc);border-color:var(--acc)}
.lnkrow{margin:1.7cqi 0 0;flex:0 0 auto}
.chat{display:flex;flex-direction:column;gap:1.7cqi;flex:1 1 auto;
  justify-content:center;min-width:0;min-height:0}
.chat .row{display:flex;flex-direction:column;gap:.6cqi;max-width:74%}
.chat .row.me{align-self:flex-end;align-items:flex-end}
.chat .who{font-size:1.18cqi;letter-spacing:.08em;color:var(--faint)}
.chat .bub{background:var(--panel2);border:1px solid var(--line);border-radius:14px;
  padding:1.5cqi 1.9cqi;font-size:1.9cqi;line-height:1.52;word-break:keep-all;color:var(--fg)}
.chat .row.me .bub{background:var(--accs);border-color:var(--accl)}
.chat .bub b{color:var(--acc);font-weight:600}
.chat .bub ol{margin:.9cqi 0 0;padding-left:1.5em}
.chat .bub li{margin-top:.4cqi}
.ppl h2.a{max-width:none;margin:0 0 2.1cqi}
.col{display:flex;flex-direction:column;gap:1.2cqi;min-width:0;min-height:0}
.agenda{display:flex;flex-direction:column;gap:.44cqi;flex:1 1 auto;min-height:0}
.agenda div{display:grid;grid-template-columns:7cqi 1fr auto;gap:1.4cqi;align-items:baseline;padding:.74cqi 0;border-bottom:1px solid var(--line)}
.agenda div:last-child{border-bottom:0}
.agenda time{font-family:"IBM Plex Mono",monospace;font-size:1.3cqi;color:var(--acc);font-weight:500}
.agenda p{margin:0;font-size:1.5cqi;line-height:1.36}
.agenda i{font-style:normal;font-size:1.2cqi;color:var(--faint);font-family:"IBM Plex Mono",monospace}
.agenda div.hl p{font-weight:600}
.agenda div.hl{background:var(--accs);margin:0 -1.2cqi;padding:.74cqi 1.2cqi;border-radius:6px;border-bottom:0}
.quad{flex:1 1 auto;display:grid;grid-template-columns:auto 1fr 1fr;grid-template-rows:auto 1fr 1fr;gap:1cqi;min-height:0}
.quad .ax{font-size:1.18cqi;font-weight:600;letter-spacing:.1em;color:var(--faint);display:grid;place-items:center;text-align:center}
.quad .ax.v{writing-mode:vertical-rl;rotate:180deg}
.quad .q{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:1.5cqi;display:flex;flex-direction:column;gap:.55cqi;min-width:0}
.quad .q.f{border-color:var(--accl);background:var(--accs)}
.quad .q h4{margin:0;font-size:1.6cqi;font-weight:600;line-height:1.26}
.quad .q.f h4{color:var(--acc)}
.quad .q p{margin:0;font-size:1.22cqi;line-height:1.45;color:var(--dim)}
.quad .q p.do{margin-top:auto;color:var(--fg);font-weight:600;font-size:1.22cqi}
.kpi{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4cqi;flex:1 1 auto;min-height:0}
.kpi div{background:var(--panel2);border:1px solid var(--line);border-radius:10px;padding:1.9cqi;display:flex;flex-direction:column;gap:.8cqi;justify-content:center}
.kpi b{font-size:4.6cqi;font-weight:700;letter-spacing:-.04em;color:var(--acc);line-height:1}
.kpi span{font-size:1.32cqi;line-height:1.48;color:var(--dim)}
.kpi u{text-decoration:none;display:block;margin-top:.5cqi;padding-top:.9cqi;
  border-top:1px solid var(--line);font-size:1.18cqi;line-height:1.42;color:var(--faint)}
.tbars{display:flex;flex-direction:column;gap:4cqi;flex:1 1 auto;justify-content:center;min-height:0}
.tbar{display:flex;flex-direction:column;gap:1.2cqi;min-width:0}
.tbh{display:flex;align-items:baseline;justify-content:space-between;gap:2cqi}
.tbn{font-size:2.15cqi;font-weight:600;letter-spacing:-.012em;word-break:keep-all;color:var(--fg)}
.tbv{font-size:2.15cqi;font-weight:700;letter-spacing:-.02em;white-space:nowrap}
.tbt{height:3.6cqi;background:var(--panel2);border:1px solid var(--line);border-radius:7px;overflow:hidden}
.tbt i{display:block;height:100%;border-radius:6px 0 0 6px}
.tbar.agent .tbv{color:var(--dim)}
.tbar.agent .tbt i{background:var(--dim);opacity:.38}
.tbar.mine .tbv{color:var(--acc)}
.tbar.mine .tbt i{background:var(--acc)}
.tbscale{display:flex;justify-content:space-between;margin-top:-1.6cqi;
  font-family:"IBM Plex Mono",ui-monospace,monospace;font-size:1.16cqi;
  letter-spacing:.1em;color:var(--faint)}
.tbline{margin:2.4cqi 0 0;font-size:2.75cqi;line-height:1.34;font-weight:600;
  letter-spacing:-.016em;word-break:keep-all;text-align:center;color:var(--fg);
  text-wrap:balance}
.tbline b{color:var(--acc);font-weight:700}
.rule{height:1px;background:var(--line);flex:0 0 auto}

/* ---------- chrome ---------- */
.bar{display:flex;align-items:center;gap:12px;padding:12px 4px 0;flex-wrap:wrap}
.prog{flex:1 1 180px;height:3px;background:var(--line);border-radius:99px;overflow:hidden;min-width:120px}
.prog i{display:block;height:100%;width:0;background:var(--acc);transition:width .22s ease}
.meta{font-size:12px;letter-spacing:.1em;color:var(--faint);font-family:"IBM Plex Mono",monospace;white-space:nowrap}
.meta b{color:var(--fg);font-weight:600}
.btns{display:flex;gap:6px;flex-wrap:wrap}
.btn{
  font:inherit;font-size:12px;font-weight:500;letter-spacing:.04em;cursor:pointer;color:var(--dim);
  background:transparent;border:1px solid var(--line2);border-radius:7px;padding:6px 11px;
}
.btn:hover{color:var(--fg);border-color:var(--fg)}
.btn.on{color:var(--acc);border-color:var(--accl);background:var(--accs)}
.hint{font-size:12px;color:var(--faint);line-height:1.5;padding:8px 4px 0}
.hint kbd{
  font-family:"IBM Plex Mono",monospace;font-size:11px;border:1px solid var(--line2);
  border-radius:4px;padding:1px 5px;color:var(--dim);
}

/* notes panel */
.np{
  margin-top:12px;background:var(--panel);border:1px solid var(--line);border-radius:12px;
  padding:16px 18px;font-size:14px;line-height:1.66;color:var(--dim);
}
.np h4{margin:0 0 10px;font-size:12px;letter-spacing:.16em;color:var(--acc);font-weight:600}
.np b{color:var(--fg);font-weight:600}
.np .cue{color:var(--acc);font-weight:600;font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.06em}
.np p{margin:0 0 9px}
.np p:last-child{margin:0}
.note{display:none}

/* overview */
.ov{
  position:fixed;inset:0;z-index:50;background:var(--bg);overflow:auto;
  padding:max(20px,env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-right,0px)) 28px max(16px,env(safe-area-inset-left,0px));
}
.ov h4{margin:4px 0 16px;font-size:12px;letter-spacing:.18em;color:var(--faint);font-weight:600}
.ovg{display:grid;grid-template-columns:repeat(auto-fill,minmax(188px,1fr));gap:8px;max-width:1300px;margin:0 auto}
.ovb{
  font:inherit;text-align:left;cursor:pointer;background:var(--panel);color:var(--dim);
  border:1px solid var(--line);border-radius:9px;padding:10px 12px;display:flex;gap:9px;align-items:baseline;
}
.ovb:hover{border-color:var(--acc);color:var(--fg)}
.ovb u{text-decoration:none;font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--faint);flex:0 0 auto}
.ovb span{font-size:13px;line-height:1.35}
.ovb.cur{border-color:var(--acc);background:var(--accs);color:var(--fg)}
.ovb.sec{background:var(--panel2);border-style:dashed}

/* ---------- phone: reading document ---------- */
@media (max-width:760px){
  .app{padding-block:8px 24px}
  .stage{aspect-ratio:auto;container-type:normal;background:transparent;border:0;border-radius:0;display:flex;flex-direction:column;gap:14px;overflow:visible}
  .s{position:static;display:flex!important;padding:20px 18px;background:var(--panel);border:1px solid var(--line);border-radius:12px}
  .s.cover,.s.sect,.s.stmt,.s.brk{padding:26px 18px}
  .bar,.np,.hint{display:none}
  .eyebrow{margin-bottom:12px;gap:10px}
  .eyebrow b,.eyebrow span,.eyebrow i{font-size:10.5px;letter-spacing:.12em}
  h1{font-size:30px;margin-bottom:16px}
  .s.sect h1,.s.brk h1{font-size:25px}
  .s.stmt p{font-size:24px}
  .s.stmt .tag{margin-top:16px;font-size:11px}
  .kicker{font-size:10.5px;margin-bottom:12px}
  .lede{font-size:15px;margin-bottom:16px}
  .chip{font-size:11px;padding:5px 11px}
  h2.a{font-size:21px;margin-bottom:14px;max-width:none}
  .sub{font-size:14.5px;margin:-6px 0 14px}
  .body{gap:12px}
  .foot{font-size:13.5px;margin-top:14px}
  .cards,.cards.c2,.cards.c3,.cards.c4,.kpi,.split,.split.w,.split.n,.trio{grid-template-columns:1fr;display:grid;gap:10px}
  .trio .bl li{font-size:15px}
  .pshot{height:auto;gap:8px}
  .lnk{font-size:12px}
  .lnkrow{margin-top:10px}
  .chat{gap:12px}
  .chat .row{max-width:88%}
  .chat .bub{font-size:15px;padding:11px 13px;border-radius:11px}
  .chat .who{font-size:11px}
  .card{padding:14px}
  .card .lab{font-size:10px}
  .card h3{font-size:16px}
  .card p{font-size:13.5px}
  .card .num{font-size:30px}
  .kpi b{font-size:36px}
  .kpi span{font-size:13px}
  .steps li b{font-size:15.5px}
  .steps li span{font-size:13.5px}
  ol.steps li::before{width:21px;height:21px;font-size:11px}
  ul.steps li::before{width:6px;height:6px;margin-top:8px}
  .steps,ol.steps,ul.steps{gap:11px}
  ol.steps li,ul.steps li{gap:11px}
  table{font-size:13px}
  th,td{padding:9px 10px}
  thead th{font-size:10.5px}
  td:first-child{white-space:normal}
  .tw{overflow-x:auto}
  table.cmp{font-size:15px}
  table.cmp th,table.cmp td{padding:10px 8px}
  table.sum4{font-size:15px}
  table.sum4 th,table.sum4 td{padding:10px 8px}
  .term pre,.term.t2 pre,.term.t3 pre{font-size:12px;line-height:1.62;padding:13px 14px}
  .bigword{font-size:48px;line-height:1.06}
  .bigword.b2{font-size:38px;line-height:1.12}
  .bigword.b3{font-size:31px;line-height:1.2}
  .bigword.b4{font-size:26px;line-height:1.26}
  .s.big .bigwrap.row{flex-direction:column;align-items:flex-start;gap:18px}
  .s.big .bigwrap.row .bigbody{border-left:0;padding-left:0}
  .ag2 li{padding:11px 0;gap:14px}
  .ag2 u{font-size:11px}
  .ag2 b{font-size:17px}
  .bigword small{font-size:22px}
  .bigsub{font-size:15px;margin-top:14px;max-width:none}
  .s.quip{text-align:left;align-items:flex-start;gap:16px}
  .quipart,.s.quip.lg .quipart,.s.quip.sm .quipart{width:74px}
  .quipline,.s.quip.lg .quipline,.s.quip.sm .quipline{font-size:23px;max-width:none}
  .quipfoot{font-size:13px}
  .lines{gap:15px}
  .lines b{font-size:19px}
  .lines span{font-size:15px}
  .lines.q{gap:18px}
  .lines.q span{font-size:16px}
  .bl{gap:11px}
  .bl li{font-size:15px;padding-left:16px}
  .bl li::before{width:5px;height:5px}
  .s.shot{gap:14px}
  .shotimg img{max-height:none;width:100%}
  .shotline{font-size:20px;max-width:none;text-align:left}
  .term .th{padding:8px 11px}
  .term .th span{font-size:10px}
  .copy{font-size:10.5px;padding:4px 9px}
  figcaption{font-size:13px}
  .fill{padding:14px}
  .fill .lab{font-size:10px}
  .fill p{font-size:13.5px}
  .warn,.note-i{font-size:13px;padding:11px 13px}
  .kpi u{font-size:12px;padding-top:8px}
  .tbars{gap:20px}
  .tbn,.tbv{font-size:16px}
  .tbt{height:22px}
  .tbscale{font-size:11px;margin-top:-10px}
  .tbline{font-size:19px;margin-top:16px;text-align:left}
  .agenda div{grid-template-columns:52px 1fr;gap:10px;padding:8px 0}
  .agenda div i{display:none}
  .agenda time{font-size:12px}
  .agenda p{font-size:14px}
  .agenda div.hl{margin:0;padding:8px 10px}
  .quad{grid-template-columns:1fr;grid-template-rows:none}
  .quad .ax{display:none}
  .quad .q{padding:14px}
  .quad .q h4{font-size:15.5px}
  .quad .q p,.quad .q p.do{font-size:13px}
}
/* 강사 노트는 화면에서 N 키로만 봅니다: 공유 링크(폰 문서 모드)에는 노출하지 않습니다 */
"""
