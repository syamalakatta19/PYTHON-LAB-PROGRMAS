#set_variable={val1,val2,.....}
s={1,4.5,"syamala",'s'}
print(s)
coders=set(["syamala","bhanu","sham",])
analyst=set(["syamala","munni","hema"])
print(coders)
print(analyst)
print(coders.intersection(analyst))
print(coders.union(analyst))
print(coders.difference(analyst))
print(analyst.difference(coders))
print(coders.symmetric_difference(analyst))
s=set([1,2,3,4,5,6])
s1=set([7,8,9,10,11,12])
s.update(s1)
print(s)
s={1,2,3,4,5,6}
s1={7,8,9,10,11,12}
s.update(s1)
print(s)
s={1,2,3,4,5,6,6}
s.add(6)
s.add(7)
print(s)





