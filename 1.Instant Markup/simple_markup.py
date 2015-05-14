#encoding=utf-8
import sys, re
from util import *

print '<html><head><title>...</title><body>'

title = True  #默认第一行是title
for block in blocks('test_input.txt'):
#for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)  #将两个**之间的内容变为强调的html
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'

print '</body></html>'