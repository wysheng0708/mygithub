class Student:
    school='学校'

    def __init__(self,num,age):
        self.age=age
        self.num=num

    def show(self):
        print(f'{self.name},{self.num}')
#python是动态语言，可以动态绑定实例属性
stu1=Student(1,18)
stu2=Student(2,19)
stu2.color='green'
print(stu2.color)
#print(stu1.color)
#也可以动态绑定方法
def normalff():
    print('我是一个普通方法，被动态绑定了')
stu2.fun=normalff
stu2.fun()

