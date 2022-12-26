num=int(input("enter a number: "))
print("half pyramids of stars: ")
for i in range(num):
    for j in range(i+1):     
        print("*",end=" ")
    print()