#有key和value对
#字典的key（键）是无序的、不重复的，可以是字符串、数字、bool值、元组，都是不可变的，列表不可以，字典和集合不可以
# value都行
#字典用{}
#字典是可变序列，但是key不能直接修改

#创建
#1.{}
d={'key1':'value1',10:30,43:'zoo','d':30,10:4324}#key重复会覆盖
print(d)
#2.zip()和dict()
lst1=list('hello')
lst2=list(range(3))
d=zip(lst1,lst2)
print(d)#zip输出的结果是zip格式 看不到 要转换
# print(list(d))#转成列表，字典里面的键值对转化为元组类型
# [('h', 0), ('e', 1), ('l', 2)]
d=dict(d)#用dict转成字典
print(d)

#key
t=('dd',2,3)
d={t:1}
print(d)
# lst=[1,2,3]
# d={lst:1}
# print(d)

#字典的访问
#1.用d[key]
d={'h': 0, 'e': 1, 'l': 2}
print(d['h'])
#2. d.get()
print(d.get('h'))
print(d.get('java','不存在'))
#两者区别在于：1如果没有key会报错，2会返回默认值，可以修改

#字典的遍历
for item in d.items():
    print(item)#可以发现，遍历字典得到的是每一个元素对都是元组类型
#也可以分别获取key和value
for key,value in d.items():
    print(key,value)#直接得到元素

#字典的函数：.keys().values().items()
d={1001:'lm',1002:'wh',1003:'nn'}
d[1004]='zll'#直接添加新元素对
#获取key
keys=d.keys()
print(keys)#结果是dict_keys([1001, 1002, 1003, 1004])，可以转为其他类型
print(list(keys))
print(tuple(keys))
#获取value
values=d.values()
print(values)
print(list(values))
print(tuple(values))
#获取键值对 用items（） 可以转化为lst或者元组
lst=list(d.items())
print(lst)
t=tuple(d.items())
print(t)

#把别的类型转为字典：
d=dict(t)
print(d)
# d=dict(list)
# print(d)

#POP函数会取出某个元素对然后删除
print(d.pop(1004))
print(d)
print(d.pop(1008,'不存在'))

#字典生成式：
#d={key:value for item in range}
#d={key:value for key,value in zip(lst1,lst2)}
import random
d={item:random.randint(1,100) for item in range(4)}
print(d)
d={key:value for key,value in zip(lst1,lst2)}
print(d)



