a=[]
b=[]
c=[]
n=int(input("enter no.of input"))
for i in range(0,n):
    ele=int(input())
    a.append(ele)
a.sort()
for i in range(1,(n+1)):
    b.append(i)
for i in b:
    if(i not in a):
       c.append(i)
print(c)