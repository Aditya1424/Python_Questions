# 1.
'''try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except ValueError:
    print("error 1")
except ZeroDivisionError:
    print("error 2")
     '''
# 2.
'''try:
    n=int(input())
    l=[1,2,3,4,5,6,7,8]
    print(l[n])
except IndexError:
    print("tata bye bye")'''

# 3.
'''try:
    a=int(input())
    b=int(input())
    print(a+b)
except ValueError:
    print("sorry, nikal")'''

# 4.
'''try:
    s=(input())+ 30.5
    print(s)
except TypeError:
    print("error")'''


# 5.
try:
    fp=open("c.txt","r")
    fp.write("hello")
except IOError:
    print("try again")






