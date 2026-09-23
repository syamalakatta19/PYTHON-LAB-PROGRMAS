#filter(function name, sequence)
def check(a):
    if a%2==0:
        return 1
even=list(filter(check,range(1,100)))
print(even)
