# abs() - 绝对值
print(abs(-5))      # 5
print(abs(3.14))    # 3.14
print(abs(-2.5))    # 2.5

# round() - 四舍五入
print(round(3.14159))       # 3
print(round(3.14159, 2))    # 3.14
print(round(3.5))           # 4 (注意：银行家舍入法)
print(round(2.5))           # 2 (银行家舍入法：向最近的偶数舍入)

# pow() - 幂运算
print(pow(2, 3))        # 8
print(pow(2, 3, 5))     # 3 (2^3 mod 5)
print(2 ** 3)           # 8 (等价写法)

# divmod() - 返回商和余数
print(divmod(10, 3))    # (3, 1)
print(divmod(10.5, 3))  # (3.0, 1.5)

# max() 和 min() - 最大值和最小值
print(max(1, 5, 3, 9, 2))           # 9
print(min(1, 5, 3, 9, 2))           # 1
print(max([1, 5, 3, 9, 2]))         # 9
print(min([1, 5, 3, 9, 2]))         # 1

# sum() - 求和
print(sum([1, 2, 3, 4, 5]))         # 15
print(sum([1, 2, 3, 4, 5], 10))     # 25 (从10开始累加)