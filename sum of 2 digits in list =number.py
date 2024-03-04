a=[]
count=0
n=int(input("enter no.of input:"))
for i in range(0,n):
    num=int(input())
    a.append(num)
print(a)
digit=int(input("enter the target"))
for i in a:
    for j in a:
        if(i+j==digit):
            print(a.index(i),a.index(j))
            count=count+1
if(count==0):
    print("no elements found")

