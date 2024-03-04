n1=int(input("enter binary 1:"))
n2=int(input("enter binary 2:"))
sn1=str(n1)
sn2=str(n2)
length1=len(sn1)
length2=len(sn2)
sum1=0
sum2=0
for i in range(0,(length1+1)):
    num=n1%10
    sum1=sum1+(num*(2**i))
    n1=n1//10
for i in range(0,(length2+1)):
    num=n2%10
    sum2=sum2+(num*(2**i))
    n2=n2//10
fsum=sum1+sum2
def bin(fsum):
    if fsum>=1:
        bin(fsum//2)
    print(fsum%2,end='')
bin(fsum)