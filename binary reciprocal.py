bin = input("Enter a binary number: ")
com= ''
dec=0
for i in bin:
    if i == '0':
        com=com+ '1'
    else:
        com=com+ '0'
p = len(com) - 1
for i in com:
    if i == '1':
        dec=dec+2**p
    p=p-1
print("ones complement:", com)
print("decimal :", dec)
