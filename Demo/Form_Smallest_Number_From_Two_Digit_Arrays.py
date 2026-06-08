class Solution(object):
    def minNumber(self, nums1, nums2):
        min1=nums1[0]
        min2=nums2[0]
        minimum=9
        count=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    if nums1[i]<=minimum:
                        minimum=nums1[i]
                        count+=1
        if(count!=0):
            return minimum
        for i in range(len(nums1)):
            if (nums1[i]<min1):
                min1=nums1[i]
        for j in range(len(nums2)):
            if (nums2[j]<min2):
                min2=nums2[j]
   
        a=min1*10 + min2  #logic to combine two digits
        b=min2*10 + min1
        if a<b:
            return a
        return b
if __name__ == "__main__":    s = Solution()
print(s.minNumber([4,1,3],[5,7]))