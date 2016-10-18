#coding:utf-8
#题目：输入某年某月某日，判断这一天是这一年的第几天？
#先用字典设好有多少天，在用if判断是否是瑞年还是平年，在根据年份的月天数加上如期
if __name__ == "__main__":
    days = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
    year,month,day = input("请输入年:"),input("月:"),input("日:")
    if not days.has_key(month):                                         #判断字典里面是否有这个键
        print "输入有误"
    sum = days[month] + day                                             #月的天数加输入的日期
    if month >= 2:
        if year %400 == 0 or (year % 4 == 0 and year % 100 != 0):       #判断是否为瑞年
            sum += 1
    print "是第%s天." % sum
