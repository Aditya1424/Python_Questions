num=int(input("enter a number: "))
i=1
s=0
temp=num
while i<=num:
    
    lv=num%10
    s=(s*10)+lv
    num=num//10
if s==temp:
    print("pally")
else:
    print("not pally")