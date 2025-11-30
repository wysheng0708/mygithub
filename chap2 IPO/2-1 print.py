
#完整语法： print(value,...,sep='',end='\n',file=None)
#print输出变量，直接写变量名，输出函数运算结果，也是直接写
#print输出字符串，数字也是，加‘’
#chr(x)是x这个数字对应的字符   ord(x)是x这个字符对应的数字
#print对文件操作，file=xxx
#sep=''时（默认） 前后两个变量之间有空格
#end='\n'（默认）输出完成有换行
'''
字符串格式化的方法：
1.f-string
 print(f"{a} * {b} = {a * b}")  对应f和{}
2.%占位
 print("学生: %s, 年龄: %d, 分数: %.1f" % (name, age, score)) 前面占位后面用%直接连接变量 多个用元组
3.str.format()
 print("{0} + {1} = {2}".format(3, 4, 7))  前面的数字是format里面的序号
'''