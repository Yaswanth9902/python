n=int(input("enter no.of input:"))
a=[]
for i in range (0,n):
    ele=int(input(""))
    a.append(ele)
a.sort()
print("3rd largest:",a[n-3])
    
