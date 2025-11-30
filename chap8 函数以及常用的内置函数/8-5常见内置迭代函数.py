# iter() - 创建迭代器
numbers = [1, 2, 3, 4, 5]
num_iter = iter(numbers)

# next() - 获取下一个元素
print(next(num_iter))  # 1
print(next(num_iter))  # 2
print(next(num_iter))  # 3

# 提供默认值避免 StopIteration
print(next(num_iter, 'No more items'))  # 4
print(next(num_iter, 'No more items'))  # 5
print(next(num_iter, 'No more items'))  # 'No more items'

# 从可调用对象创建迭代器（直到遇到哨兵值）
def read_until_stop():
    return input("Enter value (or 'stop' to end): ")

stop_iter = iter(read_until_stop, 'stop')
for value in stop_iter:
    print(f"Received: {value}")

fruits = ['apple', 'banana', 'orange', 'grape']


#enumerate() - 带索引的迭代
# 基本用法
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 输出:
# 0: apple
# 1: banana
# 2: orange
# 3: grape

# 指定起始索引
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# 输出:
# 1: apple
# 2: banana
# 3: orange
# 4: grape

# 实际应用：处理文件行号
lines = ["First line", "Second line", "Third line"]
for line_num, line in enumerate(lines, 1):
    print(f"Line {line_num}: {line}")

#zip()并行迭代
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['New York', 'London', 'Tokyo']

# 基本用法
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 多个序列
for name, age, city in zip(names, ages, cities):
    print(f"{name} from {city} is {age} years old")

# 转换为字典
name_age_dict = dict(zip(names, ages))
print(name_age_dict)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# 不等长序列 - 以最短的为准
short_list = [1, 2]
long_list = ['a', 'b', 'c', 'd']
for num, letter in zip(short_list, long_list):
    print(f"{num} -> {letter}")  # 只输出前两个

# 使用 itertools.zip_longest 处理不等长序列
from itertools import zip_longest
for num, letter in zip_longest(short_list, long_list, fillvalue='N/A'):
    print(f"{num} -> {letter}")

#reverse（）翻转迭代
# 列表反向迭代
numbers = [1, 2, 3, 4, 5]
for num in reversed(numbers):
    print(num)  # 5, 4, 3, 2, 1

# 字符串反向
text = "hello"
for char in reversed(text):
    print(char)  # o, l, l, e, h

# range反向
for i in reversed(range(5)):
    print(i)  # 4, 3, 2, 1, 0


# 自定义对象的反向迭代（需要实现 __reversed__ 方法）
class CountUp:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(1, self.n + 1):
            yield i

    def __reversed__(self):
        for i in range(self.n, 0, -1):
            yield i


for num in CountUp(3):
    print(num)  # 1, 2, 3

for num in reversed(CountUp(3)):
    print(num)  # 3, 2, 1


#map()映射函数迭代
# 基本用法：对每个元素应用函数
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# 多个序列
a = [1, 2, 3]
b = [10, 20, 30]
result = map(lambda x, y: x + y, a, b)
print(list(result))  # [11, 22, 33]

# 使用内置函数
words = ['hello', 'world', 'python']
lengths = map(len, words)
print(list(lengths))  # [5, 5, 6]


# 与方法一起使用
class Person:
    def __init__(self, name):
        self.name = name

    def get_name_upper(self):
        return self.name.upper()


people = [Person('alice'), Person('bob'), Person('charlie')]
names_upper = map(Person.get_name_upper, people)
print(list(names_upper))  # ['ALICE', 'BOB', 'CHARLIE']


#filter（）过滤元素
# 基本用法：过滤满足条件的元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # [2, 4, 6, 8, 10]

# 使用 None 过滤假值
mixed = [0, 1, False, True, '', 'hello', [], [1, 2]]
truthy = filter(None, mixed)
print(list(truthy))  # [1, True, 'hello', [1, 2]]

# 过滤复杂对象
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

products = [
    Product('Laptop', 1000),
    Product('Mouse', 25),
    Product('Keyboard', 75),
    Product('Monitor', 300)
]

affordable = filter(lambda p: p.price < 100, products)
for product in affordable:
    print(f"{product.name}: ${product.price}")

#sorted（）排序迭代
# 基本排序
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(numbers))  # [1, 1, 2, 3, 4, 5, 6, 9]

# 降序排序
print(sorted(numbers, reverse=True))  # [9, 6, 5, 4, 3, 2, 1, 1]

# 自定义排序键
words = ['apple', 'banana', 'cherry', 'date']
print(sorted(words, key=len))  # ['date', 'apple', 'banana', 'cherry']

# 复杂对象排序
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# 按成绩排序
by_grade = sorted(students, key=lambda s: s['grade'])
print(by_grade)
# [{'name': 'Charlie', 'grade': 78}, {'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 92}]

# 多重排序
data = [(1, 'b'), (2, 'a'), (1, 'a'), (2, 'b')]
# 先按元组第一个元素，再按第二个元素排序
print(sorted(data))  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]


#生成器
# 生成器表达式（惰性求值）
numbers = [1, 2, 3, 4, 5]

# 列表推导式（立即求值）
squares_list = [x ** 2 for x in numbers]
print(squares_list)  # [1, 4, 9, 16, 25]

# 生成器表达式（惰性求值）
squares_gen = (x ** 2 for x in numbers)
print(squares_gen)  # <generator object <genexpr> at 0x...>
print(list(squares_gen))  # [1, 4, 9, 16, 25]


# 生成器表达式节省内存
# 处理大文件时特别有用
def process_large_file(filename):
    # 一次性读取所有行到内存
    with open(filename) as f:
        lines = f.readlines()

    # 使用生成器表达式逐行处理
    with open(filename) as f:
        long_lines = (line.strip() for line in f if len(line) > 50)
        for line in long_lines:
            process_line(line)


# 链式生成器表达式
numbers = range(10)
result = (x ** 2 for x in numbers if x % 2 == 0)
filtered = (x for x in result if x > 10)
print(list(filtered))  # [16, 36, 64]



#