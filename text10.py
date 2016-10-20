#coding:utf-8
#判断101-200有多少个素数
import math
if __name__ == "__main__":
    pase = 0
    for i in range(101,201):
        s = int(math.sqrt(i))
        for j in range(2,s+1):
            if i % j == 0:
                pase = 0
                break
        if pase == 1:
            print i
        else:
            pase = 1
        
