countries=(1,2,3,4,5,6,7)
temp=list(countries)
temp.append("Russia")
temp.pop(2)
temp[2]="finland"
countries=tuple(temp)
print(countries)
countriesname=("India","Russia")
new_countries=countries+countriesname
print(new_countries)                    #concatenation
t1=countries.count(2)
print(t1)                               #count method
res=countries.index(4)
print(res)                              #index method
#slicing can be done in counting values in the given range(number to be found , range starting, ending range)
temo=len(countries)
print(temo)                             #length method