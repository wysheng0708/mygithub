i=0
while i < 3:
    i+=1
    address=input('请输入用户名')
    key=input('请输入密码')
    if address=='1' and key=='1':
        print('登录成功')
        break
    elif address=='1' and key!='1':
        print(f'密码错误，请重新输入，您还有{3-i}次机会')
    elif address!='1' and key=='1':
        print(f'用户名错误，请重新输入，您还有{3-i}次机会')
    else:
        print(f'错误，请重新输入，您还有{3-i}次机会')
if i==3:
  print('三次均错误，已锁定')