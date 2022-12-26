r=int(input())
for i in range(r):
    for j in range(i):
        print(" ",end="")
    for k in range(i,r):
        print("*",end="")
    print()