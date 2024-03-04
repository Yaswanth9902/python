n=int(input("enter the no.of input:"))
a=[]
b=[]
s=0
sum1=0
for i in range(0,n):
    ele=int(input("enter value "))
    a.append(ele)
    s=s+a[i]
k=int(input("enter k value:"))
for i in range(0,k):
    b.append(a[i])
    sum1=sum1+b[i]
sum2=s-sum1
if(sum1>sum2):
    r=sum1//4
else:
    r=sum2//4
print(r)

