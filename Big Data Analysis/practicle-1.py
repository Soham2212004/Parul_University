#map function example
items=[1,2,3,4,5]
a=list(map((lambda x:x**4),items))
print(a)

#filter function example
b=[1,2,3,4,5]
c=[7,8,5,9]
d=list(filter(lambda x:x in b,c))
print(d)


#reduce function example
from functools import reduce
e=reduce((lambda x,y:x*y),[1,2,3,4])
print(e)