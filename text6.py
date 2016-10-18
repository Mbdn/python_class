#coding:utf-8
#题目：输入某年某月某日，判断这一天是这一年的第几天？
if __name__ == "__main__":

    
    sput = raw_input("请输入年月日“格式为2015.15.14”:")
    print "输入的是：%s年%s月%s日" % (sput[0:4] ,sput[5:7] ,sput[8:10])
    sputs = sput[5:7]
    sputs1 = sput[8:10]

