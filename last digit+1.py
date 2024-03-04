n=int(input("enter no.of input:"))
a=[]
for i in range (0,n):
    ele=int(input(""))
    a.append(ele)
a[n-1]=(a[n-1]+1)
print(a)
