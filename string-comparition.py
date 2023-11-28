chars=["a","b","b","b","b","b","b","b","b","b","b","b","b"]
l=[]
for i in chars:
    if i not in l:
        l.append(i)
        a=chars.count(i)
        l.append(str(a))
print(l)
print(len(l))
for i in range(len(chars)):
    chars.pop()
chars.extend(l)
print(chars)