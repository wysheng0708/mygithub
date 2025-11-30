'''
递归的核心：结束条件和自己调用自己
示例：斐波那契数列
'''
def shulie(n:int):
    if n==1 or n==2:
        return 1
    else:
        return shulie(n-1)+shulie(n-2)
print(shulie(9))