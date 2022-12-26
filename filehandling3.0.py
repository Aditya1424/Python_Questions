'''fp=open("d.txt","w")
for i in range(50,501):
    s=str(i)+ ' '
    fp.write(s)
fp.close()
fp=open("d.txt","r")
print(fp.read())'''


#'''fp=open("z.txt","w")
#s='''python is an interpreter language
#and debugging is easy'''
#fp.write(s)
#print(s)
#fp.close()
#fp=open("z.txt","r")
#s=fp.read()
#print(s)'''

fp=open("poems.txt","w")
s="Twinkle Twinkle little star how I wonder what you are !"
fp.write(s)
poems=s.split()
c=[]
for i in s:
    if s[i] is "Twinkle":
        c.append(i)
fp.close()
#fp=open("poems.txt","r")
#print(fp.read())

