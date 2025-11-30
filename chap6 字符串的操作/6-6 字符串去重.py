s='helloworldhelloworldhwlloworld'

#1.遍历+notin
new_s=''
for item in s:
    if item not in new_s:
        new_s+=item
print(new_s)

#2.集合
new_s1=set(s)
lst=list(new_s1)
lst.sort(key=s.index)
print(lst)
print(''.join(lst))