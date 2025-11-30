#封装、继承和多态
''''''
'''
封装：隐藏内部细节，对外提供操作方式
继承：在函数调用的时候，用“形参名称=值”的方式传参/子类可以继承父类的特性
多态：函数定义的时候设置默认值，如果没传这个参数用默认值/不同对象对同一消息做出不同响应

封装——权限控制：
对属性或者方法添加下划线，单下划线开头表示私有，但实际上可以被外部访问；
双下划线私有，不能被外部访问；首尾双下划线一般是特殊的方法。

'''
#权限控制
class Student():
    def __init__(self,name,age,gender):
        self._name=name#受保护的实例属性（私有但是外部可访问）
        self.__age=age#私有实例属性
        self.gender=gender#普通实例属性
    def _fun1(self):
        print('子类及其本身可以访问')
    def __fun2(self):
        print('只有定义它的类可以访问')
    def show(self):#普通的实例方法
        self._fun1()#类本身访问受保护的方法
        self.__fun2()#类本身访问私有方法
        print('self._name')#就是说在类内部这些受保护什么的都可以访问，外部不一样
        print('self.__age')#

#创建对象
stu=Student('hmm',18,'女')
print(stu._name)
#print(stu.__age) 不能访问
stu._fun1()
#stu.__fun2() 不能访问

#但是实际私有的也可以访问,就是方法不一样（不推荐）
print(stu._Student__age)
stu._Student__fun2()