#.isdigit()
print("123".isdigit())        # True - 纯阿拉伯数字
print("①②③".isdigit())       # False - 圆圈数字不算
print("一二三".isdigit())     # False - 中文数字不算
print("12.3".isdigit())       # False - 包含小数点
print("".isdigit())           # False - 空字符串

#.isnumeric()
print("123".isnumeric())      # True - 阿拉伯数字
print("①②③".isnumeric())     # True - 圆圈数字
print("一二三".isnumeric())   # True - 中文数字
print("ⅣⅤⅥ".isnumeric())     # True - 罗马数字
print("12.3".isnumeric())     # False - 包含小数点

#.isalpha() 中英文都行 不能数字和符合
print("Hello".isalpha())      # True - 纯英文字母
print("你好".isalpha())       # True - 中文字符
print("Hello世界".isalpha())  # True - 混合字母和中文
print("Hello123".isalpha())   # False - 包含数字
print("Hello World".isalpha()) # False - 包含空格

#.isalnum()
print("Hello123".isalnum())   # True - 字母和数字
print("你好123".isalnum())    # True - 中文和数字
print("Hello世界123".isalnum()) # True - 混合
print("Hello 123".isalnum())  # False - 包含空格
print("Hello-123".isalnum())  # False - 包含连字符

#.islower()
print("hello".islower())      # True - 全部小写
print("Hello".islower())      # False - 有大写字母
print("hello123".islower())   # True - 数字不影响
print("hello world".islower()) # True - 空格不影响
print("".islower())           # False - 空字符串

#.isupper()
print("HELLO".isupper())      # True - 全部大写
print("Hello".isupper())      # False - 有小写字母
print("HELLO123".isupper())   # True - 数字不影响
print("HELLO WORLD".isupper()) # True - 空格不影响

#.istitle()
print("Hello World".istitle())    # True - 每个单词首字母大写
print("Hello world".istitle())    # False - 第二个单词不大写
print("This Is A Title".istitle()) # True
print("This is Not a Title".istitle()) # False
print("123 Title".istitle())      # True - 数字不影响

#.isspace()
print("   ".isspace())        # True - 空格
print("\t\n".isspace())       # True - 制表符和换行符
print("  hello  ".isspace())  # False - 包含非空白字符
print("".isspace())           # False - 空字符串