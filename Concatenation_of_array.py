class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[i])
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans
if __name__=="__main__":
    nums=[1,2,1]
    obj=Solution()
    print(obj.getConcatenation(nums))