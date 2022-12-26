a=int(input("enter first number: "))
b=int(input("enter second number: "))
for i in range(max(a,b),(a*b)+1):
    if i%a==0 and i%b==0:
        res=i
        print("lcm is: ",res)
        break