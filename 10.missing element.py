a1=[1,2,3,4,5,6,7,8]
a2=[1,2,4,5]
s1=set(a1)
s2=set(a2)
missing_element = s1 - s2
print(f'missing element = {missing_element}')