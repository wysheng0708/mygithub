#语法：lambda 参数1, 参数2, ... : 表达式

def clc(a,b):
     return a+b
print(clc(10,20))

#
s=lambda a,b:a+b
print(type(s))
print(s(10,20))
#
lst=(12,212,33,'d')
for i in range(len(lst)):
    result=lambda x:x[i]
    print(result(lst))
#
print('-'*20)
result_=lambda x:x[2]
print(result_(lst))
#还可以用来对列表进行排序
print('-'*20)
student_scores=[{'name':'cmm','score':98},
                {'name':'jim','score':99},
                {'name':'jm','score':100}]
student_scores.sort(key=lambda x:x.get('score'),reverse=True)
print(student_scores)
