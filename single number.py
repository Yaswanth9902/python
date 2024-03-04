n=int(input("enter no.of input:"))
a=[]
count=0
for i in range(0,n):
    ele=int(input(""))
    a.append(ele)
print(a)
for i in a:
    if(a.count(i)==1):
        print(i)

