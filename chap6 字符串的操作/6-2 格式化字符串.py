name = "Alice"
age = 25

# format() 方法
print("My name is {} and I'm {} years old".format(name, age))
print("My name is {0} and I'm {1} years old".format(name, age))

# f-string (Python 3.6+)
print(f"My name is {name} and I'm {age} years old")

# % 格式化
print("My name is %s and I'm %d years old" % (name, age))

# 完整格式：{[变量名或索引]:[填充字符][对齐方式][宽度][.精度][类型]}
#            ↑               ↑     ↑       ↑    ↑     ↑     ↑
#           占位符           填充  对齐    宽度 小数点 精度  类型
# 只看{}里面的，外面的冒号没有作用
#  ：是引导符，意思是要按照：后面的格式
#填充字符是单个字符，第一个字符，不需要加什么空格
# <左对齐  >右对齐（默认） ^居中
#千位分隔符‘，’放在宽度那里
