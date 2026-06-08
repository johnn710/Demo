class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif target<nums[i]:
                return i
            elif target>nums[len(nums)-1]:
                return len(nums)
            elif nums[i]<target and nums[i+1]>target:
                return i+1    
            else:
                pass
if __name__ == "__main__":    s = Solution()
print(s.searchInsert([1,3,5,6],5))  