"""t=(2,"hello",[2,33],{1:5})
t[-1].update({3:7})
t[-2][0]="hi"
print(t)"""
#l=list(map(int,input().split()))
"""l=eval(input())
print(list(set(l)))"""
"""l=list(map(int,input().split()))
l1=[i*i for i in l if i % 2!=0]
print(l1)"""
"""d={"abhay":2,"goyal":4}
d2={}
for i in d.keys():
    a=i.upper()
    
    d[i]=d[a]

print(d)"""
"""fp=open("ab.txt","w")
for i in range(1,11):
    for j in range(1,11):
        

        fp.write(str(i*j)"\n")
        
        
fp.close()
fp=open("ab.txt","r")
print(fp.read())"""


"""from optparse import Values


d={1:2,4:5,3:4}
print(max(d,key=d.get))
"""

import math as m
"""a,b,c=1,-3,2
x1= (-b+m.sqrt(b**2-4*a*c))/2*a
x2= (-b-m.sqrt(b**2-4*a*c))/2*a
print(x1,x2)"""
"""a,h=1,45
sa=6*a*h*(a+h)+m.sin(m.degrees(2*a*h))
print(sa)"""
print(m.sin(90))