num=int(input("enter a number: "))
sum=0
temp=num
while(num>0):
    fac=1
    lv=num%10
    for i in range(1,(lv+1)):
        fac=fac*i       
    sum=sum+fac
    num=num//10
if(sum==temp):
    print("Strong number")
else:
    print("Not a strong number")


