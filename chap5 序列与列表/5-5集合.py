#python的集合和数学的集合概念一致，是无序的，不重复的，元素序列
# 只能存储不可变数据类型（不能存字典和列表
#{}
#是可变数据类型

#创建:
s={10,'ss',20}
print(s)
#s={[1,2,3],[4,5,6],[7,8,9]} TypeError: unhashable type: 'list'
s=set()
print(s,type(s))
s={}
print(s,type(s))#直接用{}生成的是字典
#set（）
s=set('helloworld')
print(s)
s=set([1,2,3])
print(s)
s=set(range(9))
print(s)

#函数：len(),min,max,in,notin都有

#集合的特性：交集&（AB） 并| 差-（A-B） 补集^（A|B-AB）

#函数：
s.add(10)
s.remove(10)
s.clear()

#遍历
s=set(range(9))
for item in s:
    print(item)
for index,item in enumerate(s):#index是序号，不是索引
    print(index,item)

#生成式
s={item for item in range(1,10)}
print(s)
s={item*2 for item in range(1,10) }
print(s)
