nums1=[1,2]
nums2=[3,4]
nums1=nums1+nums2
nums1.sort()
m=len(nums1)
print(m)
if m%2==0:
    m=m//2
    print(m)
    print(float((nums1[m]+nums1[m+1])/2))
else:
    m=m//2
    print(m)
    print((float(nums1[m])))