#大小写
str='wdWJHhkji()9ef'
str=str.lower()
print(str)
str=str.upper()
print(str)
s = "apple,banana,orange"

#分割
# split() - 按分隔符分割
print(s.split(","))        # ['apple', 'banana', 'orange']
# splitlines() - 按行分割
text = "line1\nline2\nline3"
print(text.splitlines())   # ['line1', 'line2', 'line3']
# partition() - 分割为三部分
print("hello.world".partition("."))  # ('hello', '.', 'world')

#连接
# join() - 连接字符串列表
fruits = ['apple', 'banana', 'orange']
print(",".join(fruits))    # "apple,banana,orange"
print("-".join(["a", "b", "c"]))  # "a-b-c"

#替换
s = "I like apples, apples are tasty"
# replace() - 替换子串
print(s.replace("apples", "oranges"))
# 指定替换次数
print(s.replace("apples", "oranges", 1)) #第三个参数指定次数，默认全部替换

#对齐与填充
s = "hello"
print(s.ljust(10))         # "hello     " (左对齐)
print(s.rjust(10))         # "     hello" (右对齐)
print(s.center(10))        # "  hello   " (居中)
# 指定填充字符,居中对齐.center()
print(s.center(10, "*"))
print("123".zfill(5))      # "00123" (用0填充)


#strip（） 去除左右函数
#去掉左右空格
s=' 12c '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
#去掉指定字符，只能在字符两侧,对于abcd和dcba一样
s='12ce'
print(s.strip('c'))
print(s.strip('1'))


# 检查文件扩展名，后缀前缀
filename = "document.pdf"
if filename.lower().endswith(('.pdf', '.doc', '.docx')):
    print("这是文档文件")
print('demo.py'.endswith('.py'))#Ture
print('text.txt'.startswith('t'))#Ture





