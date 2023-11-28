n=8
if n%2==0:
    num=n//2
    print(num)
    squares=int((num*(num+1))/2)
    print(squares,(squares-n))
else:
    num=(n+1)//2
    print(num)
    squares=int((num*(num+1))/2)
    print(squares,(squares-n))