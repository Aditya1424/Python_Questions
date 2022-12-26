fp=open("a.txt","w")
for i in range(1,11):
    s=str(i)+' '
    fp.write(s)
fp.close()
fp=open("a.txt","r")
print(fp.read())

