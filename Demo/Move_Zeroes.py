class Solution(object):
    def moveZeroes(self, nums):
        if len(nums)==1:
            return nums
        count_zero=nums.count(0)
        k=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[k]=nums[i]
                k+=1
        for j in range(count_zero):
            nums[len(nums)-j-1]=0
        return nums
if __name__ == "__main__":    s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
