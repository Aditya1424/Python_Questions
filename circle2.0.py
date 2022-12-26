c1=int(input("enter x coordinate of centre of circle: "))
c2=int(input("enter y coordinate of centre of circle: "))
x=int(input("enter x coordinate of arbitary point: "))
y=int(input("enter y coordinate of arbitary point: "))
r=int(input("enter radius of a circle: "))
dis= (((x-c1)**2 + (y-c2)**2)**0.5)
print(dis)
if(dis < r):
    print("point is inside the circle")
elif(dis>r):
    print("point is outside the circle")
else:
    print("point lie on the circle")
