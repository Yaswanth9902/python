n=int(input("enter the size of the array"))
l1=[]

print("enter the elements in l1:")
for i in range(0,n):
    ele=int(input(""))
    l1.append(ele)
for i in l1:
    for j in l1:
          for k in l1:
              if(i!=j and j!=k and k!=i):
                     if(i+j+k==0):
                        print("--->",i,j,k)
                        break
