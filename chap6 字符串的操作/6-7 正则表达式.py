import re

text = "Hello, my phone number is 123-456-7890"

# 普通字符匹配
print(re.findall(r"Hello", text))  # ['Hello']

# 点号 . 匹配任意字符（除了换行符\n）
print(re.findall(r"m.", text))     # ['my']

# 字符集合 []
print(re.findall(r"[aeiou]", text))  # 匹配所有元音: ['e', 'o', 'e', 'o', 'e', 'u', 'e', 'i', 'o']

# 排除字符 [^]
print(re.findall(r"[^aeiou\s]", text))  # 匹配非元音非空白字符

'''
元字符： 
 . 匹配任意字符，除了\n
\w 数字，字母，下划线
\W 除了上面的
\s 任意空白字符
\S 任意非空白
\d 任意十进制

限定符： 用来限制匹配字数 
 ？：匹配前面的字符0次或一次（前面字符有没有都匹配
 +：前面的字符一次或者多次
 *：0次到多次
 {n}：n次
 {n,}：最少n次
 {n,m}：n到m次
 
 其他字符：
 []  []所指定的字符
 ^   不在[]的字符
 |  |左右的字符
 转义字符  本身
 [\u4e00-\u9fa5] 所有汉字
 分组（）
 
'''

import re

"""
正则表达式函数完整语法演示 - 学习笔记

每个函数都包含：
1. 完整语法
2. 参数说明
3. 返回值说明
4. 简单演示示例
"""


# ============================================================================
# 1. re.match() - 从字符串开头匹配
# ============================================================================
def demo_match():
    """
    re.match(pattern, string, flags=0)

    参数:
        pattern: 正则表达式模式
        string:  要匹配的字符串
        flags:   标志位，如 re.IGNORECASE

    返回值:
        匹配成功: 返回匹配对象
        匹配失败: 返回 None

    特点: 只匹配字符串的开头
    """
    text = "Hello World"

    # 示例1: 匹配开头
    result = re.match(r"Hello", text)
    if result:
        print(f"匹配成功: {result.group()}")
    else:
        print("匹配失败")

    # 示例2: 不匹配开头（返回None）
    result = re.match(r"World", text)
    print(f"匹配结果: {result}")  # None


# demo_match()

# ============================================================================
# 2. re.search() - 搜索整个字符串
# ============================================================================
def demo_search():
    """
    re.search(pattern, string, flags=0)

    参数:
        pattern: 正则表达式模式
        string:  要搜索的字符串
        flags:   标志位

    返回值:
        匹配成功: 返回第一个匹配对象
        匹配失败: 返回 None

    特点: 搜索整个字符串，返回第一个匹配
    """
    text = "Hello World, Hello Python"

    # 示例1: 搜索第一个匹配
    result = re.search(r"Hello", text)
    if result:
        print(f"找到匹配: '{result.group()}' 在位置 {result.start()}-{result.end()}")

    # 示例2: 使用分组
    result = re.search(r"(\w+) (\w+)", text)
    if result:
        print(f"完整匹配: '{result.group(0)}'")
        print(f"第一个单词: '{result.group(1)}'")
        print(f"第二个单词: '{result.group(2)}'")


# demo_search()

# ============================================================================
# 3. re.findall() - 查找所有匹配
# ============================================================================
def demo_findall():
    """
    re.findall(pattern, string, flags=0)

    参数:
        pattern: 正则表达式模式
        string:  要搜索的字符串
        flags:   标志位

    返回值:
        没有分组: 返回匹配字符串的列表
        有分组:   返回分组元组的列表

    特点: 返回所有非重叠匹配的列表
    """
    text = "苹果10元, 香蕉5元, 橙子8元"

    # 示例1: 无分组 - 返回字符串列表
    prices = re.findall(r"\d+元", text)
    print(f"所有价格: {prices}")  # ['10元', '5元', '8元']

    # 示例2: 有分组 - 返回元组列表
    items = re.findall(r"(\w+)(\d+)元", text)
    print(f"商品和价格: {items}")  # [('苹果', '10'), ('香蕉', '5'), ('橙子', '8')]


# demo_findall()

# ============================================================================
# 4. re.finditer() - 返回匹配对象的迭代器
# ============================================================================
def demo_finditer():
    """
    re.finditer(pattern, string, flags=0)

    参数:
        pattern: 正则表达式模式
        string:  要搜索的字符串
        flags:   标志位

    返回值:
        返回匹配对象的迭代器

    特点: 适合处理大量数据，节省内存
    """
    text = "John:25, Alice:30, Bob:28"

    # 示例: 遍历所有匹配
    print("人员信息:")
    for match in re.finditer(r"(\w+):(\d+)", text):
        name = match.group(1)
        age = match.group(2)
        position = match.span()
        print(f"  {name}: {age}岁 (位置: {position})")


# demo_finditer()

# ============================================================================
# 5. re.sub() - 替换匹配的文本
# ============================================================================
def demo_sub():
    """
    re.sub(pattern, repl, string, count=0, flags=0)

    参数:
        pattern: 正则表达式模式
        repl:    替换的字符串或函数
        string:  原始字符串
        count:   最大替换次数（0表示全部替换）
        flags:   标志位

    返回值:
        返回替换后的新字符串
    """
    text = "今天是2023-12-25，明天是2023-12-26"

    # 示例1: 简单替换
    new_text = re.sub(r"\d{4}-\d{2}-\d{2}", "XXXX-XX-XX", text)
    print(f"替换日期: {new_text}")

    # 示例2: 使用函数替换
    def increment_year(match):
        date = match.group(0)
        return date.replace("2023", "2024")

    new_text = re.sub(r"2023-\d{2}-\d{2}", increment_year, text)
    print(f"年份加1: {new_text}")

    # 示例3: 限制替换次数
    new_text = re.sub(r"\d", "X", text, count=4)
    print(f"替换前4个数字: {new_text}")


# demo_sub()

# ============================================================================
# 6. re.split() - 根据模式分割字符串
# ============================================================================
def demo_split():
    """
    re.split(pattern, string, maxsplit=0, flags=0)

    参数:
        pattern:  正则表达式模式（作为分隔符）
        string:   要分割的字符串
        maxsplit: 最大分割次数
        flags:    标志位

    返回值:
        返回分割后的字符串列表
    """
    text = "apple,banana;orange:grape"

    # 示例1: 按多种分隔符分割
    fruits = re.split(r"[,;:]", text)
    print(f"分割水果: {fruits}")  # ['apple', 'banana', 'orange', 'grape']

    # 示例2: 包含分隔符
    fruits_with_delim = re.split(r"([,;:])", text)
    print(f"包含分隔符: {fruits_with_delim}")

    # 示例3: 限制分割次数
    limited_split = re.split(r"[,;:]", text, maxsplit=2)
    print(f"最多分割2次: {limited_split}")  # ['apple', 'banana', 'orange:grape']


# demo_split()

# ============================================================================
# 7. re.compile() - 编译正则表达式
# ============================================================================
def demo_compile():
    """
    re.compile(pattern, flags=0)

    参数:
        pattern: 正则表达式模式
        flags:   标志位

    返回值:
        返回编译后的正则表达式对象

    特点: 提高重复使用时的性能
    """
    # 编译正则表达式
    email_pattern = re.compile(r"\w+@\w+\.\w+")
    phone_pattern = re.compile(r"\d{3}-\d{3}-\d{4}")

    text = "联系: test@email.com 或打电话 123-456-7890"

    # 使用编译后的模式
    email = email_pattern.search(text)
    phone = phone_pattern.search(text)

    print(f"邮箱: {email.group() if email else '未找到'}")
    print(f"电话: {phone.group() if phone else '未找到'}")


# demo_compile()

# ============================================================================
# 8. 常用标志（Flags）演示
# ============================================================================
def demo_flags():
    """
    常用标志:
        re.IGNORECASE (re.I) - 忽略大小写
        re.MULTILINE (re.M)  - 多行模式
        re.DOTALL (re.S)     - 点号匹配所有字符（包括换行符）
        re.VERBOSE (re.X)    - 忽略空白和注释
    """
    text = "Hello\nWorld\nHELLO\nWORLD"

    # re.IGNORECASE - 忽略大小写
    matches = re.findall(r"hello", text, re.IGNORECASE)
    print(f"忽略大小写: {matches}")  # ['Hello', 'HELLO']

    # re.MULTILINE - 多行模式
    matches = re.findall(r"^\w+", text, re.MULTILINE)
    print(f"多行模式: {matches}")  # ['Hello', 'World', 'HELLO', 'WORLD']

    # re.DOTALL - 点号匹配所有
    match = re.search(r"H.*W", text, re.DOTALL)
    if match:
        print(f"点号匹配所有: '{match.group()}'")


# demo_flags()

# ============================================================================
# 9. 分组功能演示
# ============================================================================
def demo_groups():
    """
    分组类型:
        (pattern)        - 普通分组
        (?P<name>pattern) - 命名分组
        (?:pattern)      - 非捕获分组
    """
    text = "张三:30, 李四:25"

    # 普通分组
    matches = re.findall(r"(\w+):(\d+)", text)
    print(f"普通分组: {matches}")  # [('张三', '30'), ('李四', '25')]

    # 命名分组
    for match in re.finditer(r"(?P<name>\w+):(?P<age>\d+)", text):
        print(f"命名分组 - 姓名: {match.group('name')}, 年龄: {match.group('age')}")

    # 非捕获分组
    matches = re.findall(r"(?:\w+):(\d+)", text)
    print(f"非捕获分组（只捕获年龄）: {matches}")  # ['30', '25']


# demo_groups()

# ============================================================================
# 10. 实际应用示例
# ============================================================================
def practical_examples():
    """
    实际应用场景演示
    """

    # 1. 邮箱验证
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    print("邮箱验证:")
    test_emails = ["test@example.com", "invalid.email", "user@domain.co.uk"]
    for email in test_emails:
        print(f"  {email}: {'有效' if validate_email(email) else '无效'}")

    # 2. 提取手机号
    def extract_phones(text):
        pattern = r'1[3-9]\d{9}'  # 中国手机号格式
        return re.findall(pattern, text)

    text_with_phones = "联系13812345678或18887654321"
    phones = extract_phones(text_with_phones)
    print(f"提取的手机号: {phones}")

    # 3. 清理HTML标签
    def remove_html_tags(html):
        return re.sub(r'<[^>]+>', '', html)

    html_text = "<div>Hello <b>World</b></div>"
    clean_text = remove_html_tags(html_text)
    print(f"清理HTML: {clean_text}")


# practical_examples()

# ============================================================================
# 运行所有演示
# ============================================================================
if __name__ == "__main__":
    print("开始正则表达式函数演示...\n")

    demo_match()
    print()

    demo_search()
    print()

    demo_findall()
    print()

    demo_finditer()
    print()

    demo_sub()
    print()

    demo_split()
    print()

    demo_compile()
    print()

    demo_flags()
    print()

    demo_groups()
    print()

    practical_examples()

    print("\n所有演示完成！")