a=int(input("Enter Any Number: "))
b=int(input("Enter Any Number: "))
operator=int(input("Type pf operation"))
if(operator==1):
    print(a+b)
elif(operator==2):
    print(a-b)
elif(operator==3):
    print(a/b)
elif(operator==4):
    print(a*b)
else:
    print("Enter Valid operator sequence")