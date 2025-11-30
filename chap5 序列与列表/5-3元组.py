''''''
'''
特点:
有序：元素按插入顺序排列
不可变：创建后不能修改
允许重复元素
可包含不同类型的数据
使用圆括号 () 表示
性能比列表好

1.创建
# 直接创建
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'hello', 3.14, True)

# 单个元素的元组（注意逗号）
tuple4 = (1,)  # 这是元组
not_tuple = (1)  # 这不是元组，是整数

# 使用tuple()构造函数
tuple5 = tuple()  # 空元组
tuple6 = tuple([1, 2, 3])  # 从列表转换 (1, 2, 3)
tuple7 = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')

2.遍历
colors = ('red', 'green', 'blue')

# 方法1：直接遍历元素
for color in colors:
    print(color)

# 方法2：遍历索引和元素
for i, color in enumerate(colors):
    print(f"Index {i}: {color}")

# 方法3：通过索引遍历
for i in range(len(colors)):
    print(colors[i])
    
3.函数
my_tuple = (1, 2, 2, 3, 4)

# 元组方法有限（因为不可变）
index = my_tuple.index(2)  # 返回元素的第一个索引
count = my_tuple.count(2)  # 统计元素出现次数

# 内置函数
length = len(my_tuple)
maximum = max(my_tuple)
minimum = min(my_tuple)
total = sum(my_tuple)

# 元组解包
a, b, c, d, e = my_tuple
a, b, *rest = my_tuple  # a=1, b=2, rest=[2, 3, 4]

# 元组拼接（创建新元组）
new_tuple = my_tuple + (5, 6)  # (1, 2, 2, 3, 4, 5, 6)
'''