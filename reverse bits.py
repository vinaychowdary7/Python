n=1111111111111111111111111111110
s=str(n)
l=list(s)
print(l)
sum=0
for i in range (len(l)):
    sum=sum+int(l[i])*2**i
print(sum)
print(n&1)