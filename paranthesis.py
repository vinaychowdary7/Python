s="()"
c=0
for i in range (1,len(s)-1):
    if s[i-1]=="(" and s[i]==")":
        c=c+1
        i=i+2 
    if s[i-1]=="{" and s[i]=="}":
        c=c+1
        i=i+2 
    if s[i-1]=="[" and s[i]=="]":
        c=c+1
        i=i+2 
if len(s)==2:
    if s[0] in "({[" and s[1] in ")}]":
        c=c+1
if c==(len(s)//2):
    print(c)
    print("true")
else:
    print(c)
    print("False")