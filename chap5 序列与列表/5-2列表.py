#列表是可变的序列类型,元素可变内存地址不变
''''''
'''
创建方法：
1. lst1=[l1,l2,l3...]
2. lst1=list('acdcvv')  则lst1=['a','c',...]
   lst2=list(range(10))
'''
'''
函数：
len(),max(),min(),相加lst1+lst2，乘法，.count(),.index()第一次出现的地方
del()删除，enumerate函数
'''
'''
遍历：
for item in lst:  后面是lst，item是里面的元素
for i in range(0,len(lst)): i是0到最后的序号
for index,item in enumerate(lst): index是序号，item是元素
这里的序号不是索引，因为起始地方等都可以修改
'''
'''
列表的函数：
.append(x) 在最后面加一个元素x
.insert(index,x)在index位置加一个元素x
.clear(x)全删掉
.pop(index)取出,然后删掉
.remove(x)去掉第一个出现的x
.reverse()
.copy() 深拷贝
'''
lst=[1,2,3]
lst.append(4)
print(lst)
lst.insert(2,5)
print(lst)
print(lst.pop(2))
print(lst)
lst.reverse()
print(lst)
'''
排序：
lst.sort(key=None,reverse=False)  key表示排序规则，reverse表示排序方式，默认是升序
sorted()
'''
lst1=[1,2,3,2]
lst1.sort()
print(lst1)
lst2=sorted(lst1)
print(lst2)

'''
列表生成式
lst=[expression for item in range if condition]
'''
lst3=[item*item for item in range(1,11) if item%2==0]
print(lst3)


# 二维列表
# 创建：
lst_=[ [1,2],
        [3,4],
        [5,6], 
        ['shaanghai','beijing']]
#遍历：
for row in lst_:
    for item in row:(
      print(item,end=' '))
    print()
#生成式：
lst_1=[[j for j in range(5)]for i in range(4)]
print(lst_1)
