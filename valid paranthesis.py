s="{()}"
l=list(s)
print(l)
i=1
while len(l)>0:
    print(l[i])
    print(l[i-1])
    if (l[i]=="]" and l[i-1]=="(" ) or (l[i]=="}" and l[i-1]=="[") or (l[i]==")" and l[i-1]=="{"):
        break
    if (l[i]==")" and l[i-1]=="(" ) or (l[i]=="]" and l[i-1]=="[") or (l[i]=="}" and l[i-1]=="{") :
        l.remove(l[i])
        l.remove(l[i-1])
    else:
        i=i+1
if len(l)==0:
    print(True)
else:
    print(False)        