low=3
high=7
if low%2==0 and high%2==0:
    print((high-low)//2)
elif low%2==0 or high%2==0:
    print((high-low)//2+1)
else:
    print((high-low)//2+1)