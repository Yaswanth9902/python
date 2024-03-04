n=int(input("enter the number:"))
count=0
for i in range(1,(n//2)):
    if(i**2==n):
        print(i)
        count=count+1
if(count==0):
    print(n,"is not a perfect square") 