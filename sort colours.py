n=int(input("enter the no.of colours:"))
a=[]
for i in range(0,n):
    ele=int(input("0.red 1.blue 2.white"))
    a.append(ele)
temp=0
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)