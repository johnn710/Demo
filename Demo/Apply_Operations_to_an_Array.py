class Solution(object):
    def applyOperations(self, nums):
        for i in range(len(nums)):
            if i+1==len(nums):
                break
            elif nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
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
print(s.applyOperations([1,2,2,1,1,0]))
