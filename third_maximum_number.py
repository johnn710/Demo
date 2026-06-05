class Solution(object):
    def thirdMax(self, nums):
        max1=nums[0]
        for i in range(len(nums)):
            if nums[i]>=max1:
                max1=nums[i]
        count_max1=nums.count(max1)
        for i in range(count_max1):
            nums.remove(max1)
        if len(nums)==0:
            return max1 
        max2=nums[0]   
        for i in range(len(nums)):
            if nums[i]>=max2:
                max2=nums[i]
        count_max2=nums.count(max2)
        for i in range(count_max2):
            nums.remove(max2) 
        if len(nums)==0:
            return max1 
        max3=nums[0]
        for i in range(len(nums)):
            if nums[i]>max3:
                max3=nums[i]
        return max3

if __name__ == "__main__":    s = Solution()
print(s.thirdMax([3,2,1]))