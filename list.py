lst=[2,3,4,5,6,7,8,9,0]
lst.append(39)
print(lst)
print(lst[0])
lst[1]=100
print(lst[1])
print(lst[::4])
print(lst[2::4])
print(lst[-1])
print(lst[:6:5])
del lst[0]
print(lst)
del lst[:]
print(lst)
lst1=[1,2,3,['a','b','c'],4] #nested list
print(lst1)
lst1.append(4)
print(lst1)
print(lst1.index(2))
print(lst1.count(4))
z=[10,40,50]
x=z.pop()
print(x)
print(z)
