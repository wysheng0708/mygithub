#注意：input返回的类型是字符串 想要其他的需要转换
#比如name=int（input（xxx）） figure=float（input（））
#或者用eval()处理
#多值输入：可以用spliter分割 提前说好分隔符
data = input("请输入多个数字，用空格分隔: ")
numbers = data.split()  # 分割字符串
numbers = [float(x) for x in numbers]  # 转换为数字

print(f"您输入了 {len(numbers)} 个数字")
print(f"数字列表: {numbers}")
print(f"总和: {sum(numbers)}")
print(f"平均值: {sum(numbers) / len(numbers)}")

