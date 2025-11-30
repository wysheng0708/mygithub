#不可变序列 定义之后不可以添加、删除、修改元素；可以切片访问；可以作为字典的键，列表不可以
#用（）定义；列表是【】
#元组只有一个元素的时候，逗号也不能省略,因为是括号组成的，省略就是其他类型了

#创建
# 1. 直接()
t=('hello',[10,20,30],'python')
print(t)
# 2. tuple()
t=tuple('helloword')
print(t)
t=tuple([10,20,30])
print(t)
t=tuple(range(4))
print(t)

#一些函数
print(10 in t)
print(3 in t)
print(max(t))
print(min(t))
print(sum(t))
print(len(t))
print(t.count(0))
print(t.index(0))

#遍历--与列表相同 切片和索引等也一致
t=('python','hello','world')
print(t[0])
print(t[0:3:2])
for item in t:
    print(item)
for i in range(len(t)):
    print(t[i])
for index,item in enumerate(t):
    print(index,item)
for index,item in enumerate(t,start=11):#遍历的序号可以修改
    print(index,item)

#元组的生成式是一个生成器对象 要改格式才行
t=(i for i in range(1,4))
print(t)
t=tuple(t)
print(t)