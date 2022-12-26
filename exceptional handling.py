


try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except ValueError:
    print("error 2")
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
n=int(input())
fact(n)

