#1.
'''a=input("")
b=a.split()
c=[]
for i in b:
    c.append(i[::-1])
s=' '.join(c)
print(s)'''

'''2.
out=print('hello') or print('python')
print(out,type(out))'''



from ast import Or


3.
'''fp=open("sample.txt","w")
a=''Adi is good.''
But he is bad also'''
'''b=a.split()
c=[]
print(b)

i="A"
for i in b:
    c.append(i)
print(c)


    #fp.write(a)
fp.close()
fp=open("sample.txt","r")
print(fp.read())'''


'''import numpy as np
n,m=map(int,input().split())
a=np.array([input().strip().split() for i in range(n)],int)
print(np.zeros((2,2)))'''



'''fp=open("z.txt","r")
for i in fp:
    if i[0]=='a':
        print(fp.readlines())
fp.close()'''

'''import math as m
a,b,c=1,-3,2
x1= (-b+ m.sqrt((b**2)-4*a*c))/2*a
x2= (-b- m.sqrt((b**2)-4*a*c))/2*a
print(x1,x2)'''

'''
#d={1:1,2:2,3:3}
d1={i:i*i for i in range(1,4) }
print(d1)'''

'''l=eval(input())
print(*(set(l)))'''


'''x=[[1,2],[3,4]]
y=[[5,6],[7,8]]
res=[[x[i][j]+y[i][j] for j in range(len(x[0]))]for i in range(len(x))]
for i in res:
    print(i)'''


'''a=input()
d={i:a.count(i) for i in set(a)}
print(d)'''

# swap two element in  list
'''a=eval(input())
(a[0],a[-1])=(a[-1],a[0])
print(a)'''

# 1. string is pallindrom or not
'''a= input()
if a==a[::-1]:
    print("pallindrome")
else:
    print("not pallindrome")'''

# 2. reverse a word in python
'''a=input()
res=a[::-1]
print(res)'''

# 3. remove ith character from string (left)
'''a=input()
for i in a:
    k=a.replace(i,'i')
print(k)'''

# 4. elements exist in the list or not
'''a=eval(input())
i=int(input())
if i in a:
    print("element exist")
else:
    print("element does not exist")'''

# 5. print all even numbers separately in the list
'''l=eval(input())
a=[]
for i in l:
    if i%2==0:
        a.append(i)
print(a)'''

# 6. sum and multiply of number of digits in list (doubt)
'''l=eval(input())
res=0
pro=1
for i in l:
    res=res+l[i-1]
    pro=pro*l[i-1]
    s=sum(l)
print(res)
print(pro)
print(s)'''

# 7. count even and odd numbers in a list
'''l=eval(input())
l1=[i for i in l if i%2==0]
print(len(l1))
print(len(l)-len(l1))'''

#other method:
'''l=eval(input())
even,odd=0,0
for i in l:
    if i%2==0:
        even=even+1
    else:
        odd+=1
print(even)
print(odd)'''

# 8. remove multiple elements in a list
'''l=[1,34,5,6,8,66,34,78]
print(*set(l))'''

# 9.
'''l=eval(input())
l1=[(i,i*i*i) for i in l]
print(l1)'''

# function question
'''def isSorted(l):
    if sorted(l):
        return True
l=eval(input())
res=isSorted(l)
print(res)'''

# list comprehension 
'''l=eval(input())
l1=[i*i for i in l if i%2!=0]
print(*l1)'''

# remove all duplicate in a string
a=input()
print(*set(a))
   


