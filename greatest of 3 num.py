num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
if(num1>num2):
    if(num1>num3):
        print(num1)
    else:
        print(num3)
if(num2>num3):
    print(num2)
else:
    print(num3)    