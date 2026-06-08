class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]    
                k+=1
        return k
if __name__ == "__main__":    s = Solution()
print(s.removeDuplicates([1,1,2]))  