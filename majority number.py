n=int(input("enter no.of input:"))
a=[]
b=[]
c=[]
count=0
for i in range(0,n):
    ele=int(input(""))
    a.append(ele)
for i in a:
    count=a.count(i)
    b.append(count)
for i in a:
    if(a.count(i)==max(b)):
        if(i not in c):
            c.append(i)
print(c)

