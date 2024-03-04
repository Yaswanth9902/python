n=int(input("enter the no.of input:"))
a=[]
b=[]
for i in range(0,n):
    ele=int(input(""))
    a.append(ele)

a.sort()
print("sorted list:",a)
for i in a:
    if(i not in b):
        b.append(i)
print(b)
            
           
          
