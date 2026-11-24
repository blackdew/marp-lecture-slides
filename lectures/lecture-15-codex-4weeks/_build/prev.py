# -*- coding: utf-8 -*-
import sys, pathlib
SK = ('<!doctype html><html><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
      '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);'
      'padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui}'
      'img{max-width:100%}[hidden]{display:none!important}</style>')
D = pathlib.Path('/private/tmp/claude-501/-Users-sookbunlee-Library-Application-Support-Claude-scratch-workspaces-7344fe49-955b-4076-b843-0d69138ca81b-5395bcd7-4eab-4f3b-b7e6-97d1b684760d-scratch-2026-11-08-61b3ec/3edc1d8b-6e85-4533-95b4-8320b986f957/scratchpad')
for n in sys.argv[1:]:
    src = pathlib.Path('../week%s.html' % n).read_text(encoding='utf-8')
    (D / ('prev%s.html' % n)).write_text(SK + '</head><body>' + src + '</body></html>', encoding='utf-8')
    print(D / ('prev%s.html' % n))
