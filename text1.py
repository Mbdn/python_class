#coding:utf-8
#一个有nM的文本文件，每隔1000行写道一个新的文件中
r1 = open('all.txt','r')    #读取文件 
i = -1   #计数器
ii = 0                     #文件名
for line in r1:             #把每一行给line
    i += 1
    if i % 10 == 0:
        ii += 1
    f = open(str(ii)+'.txt','a')    #打开要写入的文件
    f.write(line)                   #写入数据到文件
r1.close()                          

