#抛出一个异常，提醒程序出现异常，让成簇能够正确处理异常
# raise [exception的类型（异常描述信息）]

try:
    gender=input('请输入性别')
    if gender!='男' and gender!='女':
        raise Exception('性别只能是男或女')
    else:
        print(gender)
except Exception as e:
    print(e)
