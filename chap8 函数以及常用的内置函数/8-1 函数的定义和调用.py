def get_sum(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    print(f'1到{num}之间的累加和为{sum}')
    return sum#return都可以不写，写的话就返回到调用处

get_sum(10)

#位置参数，关键字参数，默认值参数（就是说定义函数的时候可以写上默认值）；注意默认值参数最好写在右边；

#个数可变的位置参数：
def fun(*param):
    print(type(param))
    for item in param:
        print(item)
fun(1,2,3,4,5,'gh')
fun([1223,21,3])
fun(*[1,2,3]) #传参数的时候在列表前面加一个*，就可以把列表元素作为独立参数传进去

'''
定义函数的时候，（*args）就是元组，也是个数可变的位置传参，回头调用的时候这里是（）里面很多参数；
（**args）就是字典，也是个数可变的关键字传参，会把（name=1,qs=2)用的时候是name:1,qs:2这样
调用的时候，如果实在想用列表字典之列的，用*或者**，起到一个解包的作用，不能直接传
'''

def complete_function(required_arg, *args, default_arg="默认值", **kwargs):
    """
    完整的参数定义:
    - required_arg: 必需的位置参数
    - *args: 额外的位置参数
    - default_arg: 带默认值的关键字参数
    - **kwargs: 额外的关键字参数
    """
    print(f"必需参数: {required_arg}")
    print(f"默认参数: {default_arg}")
    print(f"额外位置参数: {args}")
    print(f"额外关键字参数: {kwargs}")

# 调用示例
complete_function("必需值")
# 输出:
# 必需参数: 必需值
# 默认参数: 默认值
# 额外位置参数: ()
# 额外关键字参数: {}

complete_function("必需值", "额外1", "额外2", default_arg="新值", name="张三", age=25)
# 输出:
# 必需参数: 必需值
# 默认参数: 新值
# 额外位置参数: ('额外1', '额外2')
# 额外关键字参数: {'name': '张三', 'age': 25}

'''
return 的值可以是很多个，就变成元组类型
可以进行解包，直接写a,b,c=func(xxx)
'''


