#coding:utf-8
#输出国际象棋棋盘
if __name__ == "__main__":
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 ==  0:
                print "%c"%219,
            else:
                print "a",
        print 
