#比如说做一个整数除法计算器，但是用户不小心输入除数0或者字符等，程序就会报错

#python的异常处理机制：
#try...except：
#try：
#   可能会出异常的代码
#except 异常类型：
#   异常处理代码
#else:(可以没有）
#    没有异常需要执行的代码
#finally：（可以没有）
#     有没有异常都要执行的代码

try:
    num1=int(input('请输入被除数：'))
    num2=int(input('请输入除数：'))
    result=num1/num2
    print('结果为',result)
except ZeroDivisionError:   #这些异常不是自己命名的，是固定的很多函数
    print('除数不能为0')
except ValueError:
    print('请输入数字')
except BaseException:
    print('未知异常')

