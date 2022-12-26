a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
d=int(input("enter fourth number: "))
if(a>b and a>c and a>d):
    print(a)
elif(b>c and b>d):
    print(b)
elif(c>d):
    print(c)
else:
    print(d)   