class Solution(object):
    def dominantIndex(self, nums):
        max_value=0
        for i in range(len(nums)):
            if nums[i]>max_value:
                max_value=nums[i]
                index=i
        
        for i in range(len(nums)):
            if max_value<2*nums[i]:
                if nums[i]!=max_value:
                    return -1   
        
        return index
if __name__=="__main__":
    nums=[3,6,1,0]
    obj=Solution()
    print(obj.dominantIndex(nums))
    