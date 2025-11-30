lst=[]
for i in range(5):
    goods=input('GOODS=')
    lst.append(goods)
print(lst)
car=[]
while True:
    flag = False
    num=input('要购买几号？')
    for item in lst:
        if item[0]==num:
            flag = True
            car.append(item)
            print('已成功添加')
            break
    if num=='q':
        break
    if flag==False:
        print('未找到商品')
car.reverse()
print(car)