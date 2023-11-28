nums=[1,2,2,3]
c=0
j=1
for i in range(len(nums)-1):
    if i<=j:
        if nums[i]<=nums[j]:
            c+=1
            print(c)
            j=j+1
if c==len(nums)-1:
    print(True)
else:
    print(False)