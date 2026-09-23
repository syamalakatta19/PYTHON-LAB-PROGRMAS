#reduce(function,sequence)
import functools
def s(a,b):
    return a*b
num=[1,2,3,4,5,6]
print(num)
new=functools.reduce(s,num)
print(new)