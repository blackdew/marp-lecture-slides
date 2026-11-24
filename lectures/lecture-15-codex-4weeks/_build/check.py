# -*- coding: utf-8 -*-
import sys, re, pathlib
from html.parser import HTMLParser
VOID = {'area','base','br','col','embed','hr','img','input','link','meta','source','track','wbr'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.stack=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t in VOID: return
        names=[k for k,_ in a]
        dup=[k for k in set(names) if names.count(k)>1]
        if dup: s.err.append('line %d: <%s> duplicate attr %s'%(s.getpos()[0],t,dup))
        s.stack.append((t,s.getpos()[0]))
    def handle_endtag(s,t):
        if t in VOID: return
        if not s.stack: s.err.append('line %d: stray </%s>'%(s.getpos()[0],t)); return
        if s.stack[-1][0]!=t:
            s.err.append('line %d: </%s> but open <%s> from line %d'%(s.getpos()[0],t,s.stack[-1][0],s.stack[-1][1]))
            for k in range(len(s.stack)-1,-1,-1):
                if s.stack[k][0]==t: del s.stack[k:]; return
            return
        s.stack.pop()
for f in sys.argv[1:]:
    txt=pathlib.Path(f).read_text(encoding='utf-8')
    body=txt.split('</style>',1)[1].split('<script>',1)[0]
    p=P(); p.feed(body)
    left=[x for x in p.stack]
    print('--',f)
    for e in p.err[:20]: print('  ERR',e)
    if left: print('  UNCLOSED',left[:10])
    secs=len(re.findall(r'<section',body))
    notes=len(re.findall(r'class="note"',body))
    print('  sections=%d notes=%d  errors=%d unclosed=%d'%(secs,notes,len(p.err),len(left)))
