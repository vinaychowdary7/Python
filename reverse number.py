x=-120
if x>0:
    num=[int(y) for y in str(x)]
    num.reverse()
    print(num)
    def convert(list):
        s=[str(i) for i in list] 
        return int("".join(s))
    ans=convert(num)
    print(ans)
else:
    x=abs(x)
    num=[int(y) for y in str(x)]
    num.reverse()
    print(num)
    def convert(list):
        s=[str(i) for i in list] 
        return int("".join(s))
    ans=-(convert(num))
    print(ans)