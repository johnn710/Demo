class Solution(object):
    def arraySign(self, nums):
        import math
        multi=1
        for i in range(len(nums)):
            multi*=nums[i]
        if multi==0:
            return 0
        elif multi>0:
            return 1
        else:
            return -1
if __name__=="__main__":
    nums=[-1,-2,-3,-4,3,2,1]
    obj=Solution()
    print(obj.arraySign(nums))  