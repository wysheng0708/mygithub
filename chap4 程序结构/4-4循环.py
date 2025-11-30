# 1. 遍历循环 for
# for 循环变量 in 遍历对象：
#     语句块
#else:
#     语句块（else可以没有

for i in '131dwfrtg':
   print(i)

for i in range(6):
    print(i)
#range(,,,)的使用和切片类似
for i in range(-4,-1,1):
    print(i)


#2. 无限循环结构
# 1.初始化条件变量
number = 0
# 2.循环条件
while number < 10:
    # 3.循环体 + 更新条件变量
    print(number, end=' ')
    number += 1  # 重要：必须更新条件变量，否则会无限循环
