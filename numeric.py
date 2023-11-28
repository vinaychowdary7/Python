num=int(input("entrr njm"))
st=str(num)
for i in range(len(st)-3,0,-3):
    st=st[:i]+","+st[i:]
print(st)