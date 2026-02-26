import time
timestamp=time.strftime('%H:%M:%S')
a=time.strftime('%H')
print(a)
if(int(a)>=12):
    print("It's not morning")
else:
    print("Good Morning")