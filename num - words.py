n=int(input("enter number"))
if(n//100000>0):
    print(n//100000,"lakhs",end =' ')
    n=n%100000
if(n//1000>0):
    print(n//1000,"Thousand",end=' ')
    n=n%1000
if(n//100>0):
    print(n//100,"Hundred",end='')
    n=n%100
if(n//10>0):
    print(n//10,"ten",end='')
    n=n%10
if(n//1>0):
    print(n)

