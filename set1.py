#sets
#no repeated entries
arj={2,3,4,6,5,2} # will return single values and arranged way
print(arj)
s={}
print(type(s))
empty_set=set()
print(type(empty_set))
y={1,4,6,7,8}
print(type(y))
for value in arj:
    print(value)
print(arj.union(y))