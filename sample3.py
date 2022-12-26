n=list(map(int,input().split()))
list=[]
m=0
s=0
l=len(n)
for i in range(l-1):
    a=n[i]
    b=n[i+1]
    c=abs(a-b)
    #print(a,b,c)
    list.append(c)
    d=len(list)
for j in range(d-1):
    if list[j] >= list[j+1]:
        print("not")
        break
    else:
        print("yes")

