st=input()
count=0
for i in range(len(st)):
    if(st[i]==' '):
        count=0
    else:
        count=count+1
print(count)