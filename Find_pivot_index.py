class Solution(object):
    def pivotIndex(self, nums):
        total=0
        for i in range(len(nums)):
            total+=nums[i]
        for i in range(len(nums)):
            sum_left=0
            sum_right=0
            for j in range(i):
                sum_left+=nums[j]
            
            sum_right=total-sum_left-nums[i]
            if sum_right==sum_left:
                return i
        return -1
if __name__=="__main__":
    nums=[1,7,3,6,5,6]
    obj=Solution()
    print(obj.pivotIndex(nums))