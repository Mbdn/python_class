#coding:utf-8
#一个有2000行文本文件每隔1000行写道一个新的文件中
r1 = open('all.txt','r')    #读取文件 
i = 0                       #计数器
f = open('001'+1,'w+')   #打开并查看是否有文件没有新建
f1 = open ('002.txt','w+')
for line in r1:             #把每一行给line
    i += 1
    #rr.write(line)          #写数据
    if i <= 1000:       #检查是否到1000行
        f.write(line)
    elif i <= 2000:
        f1.write(line)
