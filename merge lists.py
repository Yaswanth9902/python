a=[]
b=[]
c=[]
n1=int(input("enter the no.of input in 1st list:"))
for i in range (0,n1):
    ele=int(input(""))
    a.append(ele)
n2=int(input("enter the no.of input in 2nd list:"))
for i in range(0,n2):
    ele=int(input(""))
    b.append(ele)
for i in a:
    c.append(i)
for i in b:
    c.append(i)
print("merged list:",c)