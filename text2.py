#coding:utf-8
#请问一个日志文本文件有2000行，我要提取其中的100行到200行，怎么做？
line_count = sum(1 for i in open('all.txt','r'))        #求出总行数
i = 0
with open('all.txt','r') as Read:
    for line in Read:
        i += 1
        if i > 100 and i < 201:
            f = open('001.txt','a')
            f.write(line)


