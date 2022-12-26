r= int(input())
for i in range(r):
    for j in range(i,r):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end="")
    print()
for i in range(r):
    for j in range(i):
        print(" ",end="")
    for j in range(i+1,r):
        print("*",end="")
    for j in range(i,r):
        print("*",end="")
    print()
