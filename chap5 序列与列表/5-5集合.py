#python的集合和数学的集合概念一致，是无序的，不重复的，元素序列
# 只能存储不可变数据类型（不能存字典和列表
#{}
#是可变数据类型
''''''
'''
特点
无序
不重复元素
可变
只能包含不可变类型
使用花括号 {} 表示（空集合用set()）

1.集合
# 直接创建
set1 = {1, 2, 3, 4, 5}
set2 = {'a', 'b', 'c'}

# 使用set()构造函数
set3 = set()  # 空集合
set4 = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4} 自动去重
set5 = set("hello")  # {'h', 'e', 'l', 'o'}

# 集合推导式
set6 = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}

2.遍历
fruits = {'apple', 'banana', 'orange'}

# 直接遍历元素（顺序不确定）
for fruit in fruits:
    print(fruit)

# 转换为列表后遍历（如果需要顺序）
for fruit in sorted(fruits):
    print(fruit)

3.函数
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# 添加和删除元素
setA.add(6)  # 添加单个元素
setA.update([7, 8, 9])  # 添加多个元素
setA.remove(9)  # 删除元素，不存在则报错
setA.discard(10)  # 删除元素，不存在不报错
popped = setA.pop()  # 随机删除并返回一个元素

# 集合运算
union_set = setA | setB  # 并集 {1, 2, 3, 4, 5, 6, 7, 8}
intersection_set = setA & setB  # 交集 {4, 5}
difference_set = setA - setB  # 差集 {1, 2, 3}
symmetric_diff = setA ^ setB  # 对称差集 {1, 2, 3, 6, 7, 8}

# 集合关系
is_subset = {1, 2}.issubset(setA)  # True
is_superset = setA.issuperset({1, 2})  # True
is_disjoint = {1, 2}.isdisjoint({3, 4})  # True

# 其他方法
copied_set = setA.copy()  # 浅拷贝
setA.clear()  # 清空集合

# 内置函数
length = len(setA)
maximum = max(setA)
minimum = min(setA)
'''
