lst=[88,89,90,98,00,99]
lst1=[]
#要在lst中00前面加20，其他加19
for item in lst:
    if item==00:
        lst1.append('200'+str(item))
    else:
        lst1.append('19'+str(item))
print(lst1)