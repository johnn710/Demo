class Solution(object):   
    def majorityElement(self, nums):
        m=len(nums)
        n=m/2
        s=set()
        for i in range(m):
            if nums[i] not in s:
                s.add(nums[i])
                if nums.count(nums[i])>n:
                    return nums[i]
if __name__ == "__main__":    s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))