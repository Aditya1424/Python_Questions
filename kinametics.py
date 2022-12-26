u=input("Enter initial velocity: ")
a=input("Enter acceleration: ")
t=input("Enter time taken: ")
u=int(u)
a=int(a)
t=int(t)
v=u+a*t
s=(u*t)+((a*t*t)/2)
print("the final velocity is:",v)
print("the displacement is:",s)

