class Solution(object):
    def removeElement(self, nums, val):
       k=0
       for i in range(len(nums)):
            if (nums[k]==val):
                del(nums[k])
            else:
                k+=1
       return len(nums)
if __name__ == "__main__":    s = Solution()
print(s.removeElement([3,2,2,3],3))