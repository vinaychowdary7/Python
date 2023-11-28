sum=""
s='abc'
t='ahbgdc'
for i in s:
    if i in t:
        sum+=i
        print(i)
        if i==t[len(t)-1]:
            break
if(sum==s):
    print("True")
else:
    print("False")