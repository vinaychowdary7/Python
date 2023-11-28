points=[[3,3],[5,-1],[-2,4]]
k=2
kClosest=[]
lens=[]
for i in range(len(points)):
    dist=(points[i][0])**2+(points[i][1])**2
    lens.append(dist)
print(lens)
for j in range(2):
    low=min(lens)
    index=lens.index(low)
    lens.pop(index)
    kClosest.append(points[index])
    points.pop(index)
print(kClosest)
st=["flower","flow"]
print(len(max(st)))