#coding:utf-8
#一个有2000行文本文件每隔1000行写道一个新的文件中
r1 = open('all.txt','r')    #读取文件 
i = 0   #计数器
ii = -1                     #

for line in r1:             #把每一行给line
    i += 1
    #rr.write(line)          #写数据
    if i % 10000 == 0:
        ii += 1
    f = open(str(ii)+'.txt','a')
    f.write(line)


r1.close()

