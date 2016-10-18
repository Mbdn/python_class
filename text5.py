#coding:utf-8
#一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？
#程序分析：在10万以内判断，先将该数加上100后再开方，再将该数加上268后再开方，如果开方后的结果满足如下条件，即是结果。请看具体分析：
if __name__== "__main__":
    import math
    for i in range(1,1000000):
        a =int (math.sqrt(i + 100))
        b = int(math.sqrt(i + 268))
        if (a*a == i + 100) and (b*b == i+ 268):
            print (i)
        
