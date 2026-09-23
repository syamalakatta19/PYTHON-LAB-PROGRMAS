#map(function name, sequence)
def add(a):
    a**=0
    return a
num=[1,2,3,4,5,6,]
print("original list :",num)
new_num=list(map(add,num))
print("final list:",new_num)