class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            if i not in nums:
                return i
if __name__ == "__main__":    s = Solution()
print(s.missingNumber([3,0,1])) 