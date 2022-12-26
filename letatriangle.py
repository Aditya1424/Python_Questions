r=int(input())
for i in range(r):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(r):
    for l in range(i,r):
        print("*",end="")
    print()