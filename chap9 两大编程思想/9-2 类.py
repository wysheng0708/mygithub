class Student:
# 类属性：定义在类之中，方法之外
    school='学校'

    #初始方法：固定名称__init__
    def __init__(self,num,age):#name,age是方法的参数，方法之外不能使用
        self.name=age #左侧是实例属性，把局部变量age赋值给实例属性
        self.num=num

    #定义在类中的函数，称为方法，自带一个参数self
    def show(self):
        print(f'{self.name},{self.num}')#实例属性是整个class可用的
        #print(num) #不行，bum是局部变量

    #静态方法
    @staticmethod
    def jtfangfa():
        print('这是一个静态方法，可以没有self参数，不能调用实例属性，不能调用实例方法')
        #print(self.name)
        #show()
        #self.show()

    #类方法
    @classmethod
    def leifangf(cls):
        print('这是一个类方法，也不能调用实例属性，不能调用实例方法')

#上面的方法都是图纸，我们需要传入对象
stu=Student(1,18) #self不用传
#只是这样的话，仅仅传入了而已

print(stu.num,stu.name) #实例属性，对象名大点调用
print(Student.school)#类属性，类名打点调用
stu.show() #实例方法，对象名打点调用
Student.leifangf()#类方法，类名打点调用
Student.jtfangfa()#静态方法，类名打点调用

Student.school='1234'#类属性是可以直接赋值的
print(Student.school)

stu1=Student(2,18)
stu2=Student(11,18)
stu3=Student(3,18)
stu4=Student(4,18)
lst=[stu1,stu2,stu3,stu4]#这几个元素是Student类型的对象
for item in lst:
    item.show()
