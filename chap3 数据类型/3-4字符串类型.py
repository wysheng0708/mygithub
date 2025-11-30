
#str:多行字符串用三引号
print('''wer
ddcc
dccc''')


# 转义字符：
# \n换行 \t水平制表位 \'单引号 \"双引号 \\一个反斜杠 r使转义字符失效
# 字符串索引：0到xxx\-yyy到-1
# 字符串切片：x[:::]最右边是步长 可以为负 左闭右开注意
x='wfqjnwijekw'
print(x[0],x[-5])
print(x[1:4])
print(x[-6:])

#字符串操作 可以直接加就是连接 可以复制
s1='ewd'
s2='12'
print(s1+s2,s1*4,s2*3)
#x in y 如果x是y的子串 就是true 不然就是false
print(s1 in s2,'1' in s2)

