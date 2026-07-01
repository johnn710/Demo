class Solution(object):
    def maxProduct(self, nums):
       maximum_product=0
       for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]-1) * (nums[j]-1)>maximum_product:
                     maximum_product=(nums[i]-1) * (nums[j]-1)
       return maximum_product
if __name__=="__main__":
    nums=[3,4,5,2]
    obj=Solution()
    print(obj.maxProduct(nums))