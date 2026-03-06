#factorial of a number
def factorial(x):
    if (x==0 or x==1):
        return 1
    else:
        return x * factorial(x-1)
        
x=int(input("enter the number of whom factorial is needed: "))
y=factorial(x)
print(y)