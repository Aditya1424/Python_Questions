from re import I


a=int(input("enter first number: "))
b=int(input("enter second number: "))
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        res=i
print(f"hcf is: {res}")
                                              