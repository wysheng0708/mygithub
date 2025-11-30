''''''
'''
特点
有序：元素按插入顺序排列
可变：可以修改、添加、删除元素
允许重复元素
可包含不同类型的数据
使用方括号 [] 表示


1.创建
# 直接创建
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 'hello', 3.14, True]

# 使用list()构造函数
list4 = list()  # 空列表
list5 = list(range(5))  # [0, 1, 2, 3, 4]
list6 = list("hello")  # ['h', 'e', 'l', 'l', 'o']

# 列表推导式
list7 = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

2.遍历
fruits = ['apple', 'banana', 'orange']

# 方法1：直接遍历元素
for fruit in fruits:
    print(fruit)

# 方法2：遍历索引和元素
for i, fruit in enumerate(fruits):
    print(f"Index {i}: {fruit}")

# 方法3：通过索引遍历
for i in range(len(fruits)):
    print(fruits[i])

# 方法4：使用while循环
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
    
3.函数
# 基本操作
my_list = [1, 2, 3]

# 添加元素
my_list.append(4)  # [1, 2, 3, 4]
my_list.insert(1, 1.5)  # [1, 1.5, 2, 3, 4]
my_list.extend([5, 6])  # [1, 1.5, 2, 3, 4, 5, 6]

# 删除元素
my_list.remove(1.5)  # 删除第一个匹配的元素
popped = my_list.pop()  # 删除并返回最后一个元素
popped2 = my_list.pop(0)  # 删除并返回指定索引的元素

# 查找和统计
index = my_list.index(2)  # 返回元素的索引
count = my_list.count(2)  # 统计元素出现次数

# 排序和反转
my_list.sort()  # 升序排序
my_list.sort(reverse=True)  # 降序排序
my_list.reverse()  # 反转列表

# 其他操作
copied_list = my_list.copy()  # 浅拷贝
my_list.clear()  # 清空列表

# 内置函数
length = len(my_list)
maximum = max([1, 2, 3])
minimum = min([1, 2, 3])
total = sum([1, 2, 3])

'''