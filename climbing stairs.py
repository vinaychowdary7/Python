n=4
first=0
second=1
temp=first+second
for i in range (1,n):
    print(first,"  ",second,"  ",temp)
    first=second
    second=temp
    temp=first+second
if(n==0):
     print(0)
elif(n==1):
    print(1)
else:
    print(temp)