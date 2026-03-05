country=input("Enter the country name")
name=input("Enter the name")
letter="hey my name is {1} and i am from{0}"
print(letter.format(name,country))
print(f"hey my name is {name} and i am from{country}")
price=49.09999
txt="{price:.2f}dollars"
print(txt)