#有key和value对
#字典的key（键）是无序的、不重复的，可以是字符串、数字、bool值、元组，都是不可变的，列表不可以，字典和集合不可以
# value都行
#字典用{}
#字典是可变序列，但是key不能直接修改
''''''
'''
特点
无序（Python 3.7+ 保持插入顺序）
键值对存储
键必须是不可变类型
键唯一，值可以重复
可变
使用花括号 {} 表示

1.创建
# 直接创建
dict1 = {'name': 'Alice', 'age': 25, 'city': 'New York'}
dict2 = {1: 'one', 2: 'two', 3: 'three'}

# 使用dict()构造函数
dict3 = dict()  # 空字典
dict4 = dict(name='Bob', age=30)  # {'name': 'Bob', 'age': 30}
dict5 = dict([('a', 1), ('b', 2)])  # {'a': 1, 'b': 2}

# 字典推导式
dict6 = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

2.遍历
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# 方法1：遍历键
for key in person:
    print(f"Key: {key}")

# 方法2：遍历键
for key in person.keys():
    print(f"Key: {key}")

# 方法3：遍历值
for value in person.values():
    print(f"Value: {value}")

# 方法4：遍历键值对
for key, value in person.items():
    print(f"{key}: {value}")

3.函数
my_dict = {'a': 1, 'b': 2, 'c': 3}
# 访问元素
value = my_dict['a']  # 直接访问
value = my_dict.get('a')  # 安全访问，键不存在返回None
value = my_dict.get('d', 0)  # 键不存在返回默认值0

# 添加和修改元素
my_dict['d'] = 4  # 添加新键值对
my_dict['a'] = 10  # 修改现有键的值

# 删除元素
del my_dict['b']  # 删除指定键
popped = my_dict.pop('c')  # 删除并返回值
popped_item = my_dict.popitem()  # 删除并返回最后插入的键值对

# 其他方法
keys = my_dict.keys()  # 所有键
values = my_dict.values()  # 所有值
items = my_dict.items()  # 所有键值对

my_dict.update({'e': 5, 'f': 6})  # 批量更新
copied_dict = my_dict.copy()  # 浅拷贝
my_dict.clear()  # 清空字典

# 内置函数
length = len(my_dict)
'''


