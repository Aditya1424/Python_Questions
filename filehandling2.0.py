fp=open("a.txt","w")
s=''' DATE   USA    INDIA
12/05/22     14.3   15.6
13/05/22     11.5   95.3
14/05/22     64.2   10.3 '''
fp.write(s)
fp.close()
fp=open("a.txt","r")
s=fp.read()
a=s.split()
sum1= (float(a[4])+float(a[7])+float(a[10]))/3
print("usa",sum1)
sum2= (float(a[5])+float(a[8])+float(a[11]))/3
print("india",sum2)


