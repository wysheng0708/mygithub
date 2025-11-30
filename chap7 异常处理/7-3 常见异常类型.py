''''''
"""
Python 异常类型完整列表（名称和说明）

BaseException - 所有异常的基类
    SystemExit - Python解释器退出
    KeyboardInterrupt - 用户中断执行（通常为Ctrl+C）
    GeneratorExit - 生成器或协程被关闭时引发

Exception - 常规异常的基类
    StopIteration - 迭代器没有更多值
    StopAsyncIteration - 异步迭代器没有更多值
    ArithmeticError - 算术错误的基类
        FloatingPointError - 浮点计算错误
        OverflowError - 算术运算结果太大无法表示
        ZeroDivisionError - 除以零
    AssertionError - assert语句失败
    AttributeError - 属性引用或赋值失败
    BufferError - 缓冲区操作相关错误
    EOFError - input()函数遇到文件结束条件
    ImportError - 导入模块/对象失败
        ModuleNotFoundError - 找不到模块
    LookupError - 查找操作的基类
        IndexError - 序列下标超出范围
        KeyError - 在字典中找不到键
    MemoryError - 内存不足
    NameError - 找不到局部或全局名称
        UnboundLocalError - 访问未初始化的本地变量
    OSError - 操作系统错误
        BlockingIOError - 操作将阻塞对象设置为非阻塞操作
        ChildProcessError - 子进程操作失败
        ConnectionError - 连接相关错误的基类
            BrokenPipeError - 管道破裂
            ConnectionAbortedError - 连接尝试被对等方中止
            ConnectionRefusedError - 连接尝试被对等方拒绝
            ConnectionResetError - 连接被对等方重置
        FileExistsError - 创建已存在的文件或目录
        FileNotFoundError - 请求的文件或目录不存在
        InterruptedError - 系统调用被输入信号中断
        IsADirectoryError - 在目录上请求文件操作
        NotADirectoryError - 在非目录上请求目录操作
        PermissionError - 没有足够权限执行操作
        ProcessLookupError - 进程不存在
        TimeoutError - 系统函数超时
    ReferenceError - 弱引用尝试访问已垃圾回收的对象
    RuntimeError - 其他类别未涵盖的一般错误
        NotImplementedError - 抽象方法需要派生类重写
        RecursionError - 超过最大递归深度
    SyntaxError - Python语法错误
        IndentationError - 缩进错误
            TabError - 制表符和空格混用
    SystemError - Python解释器内部错误
    TypeError - 操作或函数应用于不适当类型的对象
    ValueError - 操作或函数接收到类型正确但值不合适的参数
        UnicodeError - Unicode相关错误的基类
            UnicodeDecodeError - Unicode解码错误
            UnicodeEncodeError - Unicode编码错误
            UnicodeTranslateError - Unicode转译错误
    Warning - 警告的基类
        DeprecationWarning - 关于已弃用功能的警告
        PendingDeprecationWarning - 关于将来弃用功能的警告
        RuntimeWarning - 关于可疑运行时行为的警告
        SyntaxWarning - 关于可疑语法特征的警告
        UserWarning - 用户代码生成的警告
        FutureWarning - 关于将来语义更改的警告
        ImportWarning - 导入模块时可能的错误警告
        UnicodeWarning - Unicode相关警告
        BytesWarning - 字节相关警告

其他常见异常：
    NotImplementedError - 抽象方法需要派生类重写
    EnvironmentError - 已合并到OSError中（Python 3.3+）
    IOError - 已合并到OSError中（Python 3.3+）
    WindowsError - Windows系统调用失败（OSError的子类）
    vmError - 虚拟机错误
"""

# 实际使用示例：
try:
    # 可能引发异常的代码
    result = 10 / 0
except ZeroDivisionError:
    # 处理特定异常
    print("发生了除以零错误")
except Exception as e:
    # 处理其他所有异常
    print(f"发生了其他异常: {e}")
finally:
    # 无论是否发生异常都会执行
    print("清理操作")