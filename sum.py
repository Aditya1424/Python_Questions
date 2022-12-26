"""n=int(input())
fp=open("ab.txt","r")

l=len(fp.readlines())"""


"""import random as rand
a=rand.random()
print(a)"""
"""
import random as rand
a=rand.randrange(1,4)
print(a)"""
"""
import random as rand
a=rand.randint(1,5)
print(a)"""

'''import random as rand
a=rand.shuffle([1,2,4,5,6])
print(a)'''



'''
# Identity Matrix 
import numpy as np
n,m=map(int,input().split())
a=np.array([input().strip().split() for i in range(n)],int)
print(np.eye(3))'''



'''
# reverse and float
import numpy as np
l=eval(input())
a=np.array(l[::-1],dtype=float)

#l.reverse()
print(a)'''


"""
# reshaping a list
import numpy as np
l=list(map(int,input().split()))
a=np.array(l)
print(a.reshape(3,3))"""




