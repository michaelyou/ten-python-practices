#encoding=utf-8
from reportlab.graphics.shapes import Drawing, String, PolyLine
from reportlab.graphics import renderPDF

d = Drawing(100, 100)    #创建一个大小为100*100像素的图纸
s = String(50, 50, 'Hello, world!', textAnchor='middle')   #创建一个string图形元素

'''
data = [(0,0), (10,0), (10.10), (0,10)]
pred = [row[2] for row in data]
line = PolyLine(zip(times, pred))
d.add(line, strokeColor=colors.blue)
'''
d.add(s)
renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')