n=int(input())
l=[]
l1=[]
for i in range (n):
    x=int(input())
    l1.append(x)
    a=list(map(int,input()))
    l.append(a)
    a=list(map(int,input()))
    l.append(a)
n=n*2
i=0
while i<n:
    if (l[i].sort() == l[i+1].sort()):
        print(l[i],l[i+1])
        print("YES")
        i=i+2
    else:
        print("NO")
        i=i+2