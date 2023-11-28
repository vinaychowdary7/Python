nums=[1,7,3,6,5,6] 
  
for i in range (len(nums)):
    left=0
    right=0
    #print(nums[i],"hi")
    for j in range (i+1,len(nums)):
       left+=nums[j]
      # print(left)
    for k in range (i-1,-1,-1):
        right+=nums[k]
       # print(right)
    if (left==right):
        print(i)