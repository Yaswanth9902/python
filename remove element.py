a=[]
b=[]
n=int(input("enter no.of elements:"))
for i in range(0,n):
    ele=int(input())
    a.append(ele)
num=int(input("enter the element to remove:"))
for i in a:
    if(i!=num):
        b.append(i)
print(b)
