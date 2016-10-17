#coding:utf-8
#有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。

fels = [1,2,3,4]
for i in fels:
    for s in fels:
        for l in fels:
            if i !=s and s !=l and l != i:
                print "%d%d%d" %(i,s,l)
