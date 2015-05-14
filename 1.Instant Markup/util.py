#encoding=utf-8
def lines(file):
    f = open(file)
    for line in f:
        #print line
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():  #不是空行
            block.append(line)
        elif block:
            yield ''.join(block).strip()   #产生一个块
            block = []

'''
for block in blocks('test_input.txt'):
    pass
'''