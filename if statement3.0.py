sub1=int(input("enter marks of 1st subject: "))
sub2=int(input("enter marks of 2nd subject: "))
sub3=int(input("enter marks of 3rd subject: "))
if(sub1>33 or sub2>33 or sub3>33):
    print("you are pass")
elif(((sub1+sub2+sub3)/3)>40):
    print("you are pass")
else:
    print("sorry you are fail")
