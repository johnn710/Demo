class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        max_count=0
        if len(nums)==1 and nums[0]==1:
            return 1
        if 1 not in nums:
            return 0
        for i in range(len(nums)):
            if i+1==len(nums):
                return max_count+1
            if nums[i]==nums[i+1] and nums[i]==1:
                count+=1
                if count>max_count:
                    max_count=count
            elif nums[i]!=nums[i+1]:
                count=0
        return max_count+1      
if __name__ == "__main__":    s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))  