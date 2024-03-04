x=int(input("enter the x:"))
y=int(input("enter the y:"))
if(x<y):
    h=y-x
else:
    h=x-y
print("Hamming distance:",h-1)
