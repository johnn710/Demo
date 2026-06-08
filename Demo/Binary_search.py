class Solution(object):
    def search(self, nums, target):
       for i in range(len(nums)):
        if nums[i]==target:
            return i
       return -1 
if __name__ == "__main__":    s = Solution()
print(s.search([-1,0,3,5,9,12],9))
