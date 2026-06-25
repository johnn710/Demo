class Solution(object):
    def createTargetArray(self, nums, index):
        target=[]
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target
if __name__=="__main__":
    nums=[0,1,2,3,4]
    index=[0,1,2,2,1]
    obj=Solution()
    print(obj.createTargetArray(nums,index))