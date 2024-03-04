n=int(input("enter no.of input:"))
t=int(input("enter target:"))
a=[] #sum of 3 elements need to be target
for i in range(0,n):
    ele=int(input(""))
    a.append(ele)
for i in a:
    for j in a:
        for k in a:
            if(i!=j and i!=k and j!=k):
                if(i+(j+1)+(k+2)==t):
                    print(a[i],a[j],a[k])