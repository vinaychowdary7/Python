s="amanaplanacanalpanama"
n=len(s)
c=0
for i in range (len(s)):
    if s[i]==s[n-1]:
        c=c+1
if n//2 == c:
    print("True")
else:
    print("False")