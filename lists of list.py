n=int(input())
l=[]
for i in range (n):
    a=int(input())
    l.append(a)
for i in range (n):
    for j in range(0,10):
        for k in range(0,10):
            if(((j*j)+(k*k))-l[i])==0:
                print(k,j)
            elif(j==9 and k==9):
                print(-1)