r=int(input())
for i in range(r+1):
    for j in range(i,r):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for k in range(i,r):
        print(" ",end="")
    for l in range(i+1):
        print("*",end="")
    print()