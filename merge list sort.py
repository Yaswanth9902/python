a=[]
b=[]
c=[]
n1=int(input("enter the size of list 1:"))
for i in range(0,n1):
    ele=int(input(""))
    a.append(ele)
n2=int(input("enter the size of list 2 "))
for i in range(0,n2):
    ele=int(input(""))
    b.append(ele)
for i in a:
    c.append(i)
for  i in b:
    c.append(i)


print(sorted(c))
