#coding:utf-8
#九九口诀
import math
if __name__ == "__main__":
    i = range(1,10)
    for a in i:
        for b  in range(1,a + 1):
            print "%s * %s = %s" % (a,b,a*b),
        print 
