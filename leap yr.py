yr=int(input("enter a year: "))
if(yr%100!=0 or yr%400==0 and yr%4==0):
    print("leap year")
else:
    print("not a leap year")