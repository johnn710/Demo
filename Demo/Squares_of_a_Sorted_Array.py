class Solution(object):
    def sortedSquares(self, nums):
       nums_new=[]
       for i in range(len(nums)):
            squared_value=nums[i]*nums[i]
            nums_new.append(squared_value)
       nums_new.sort()
       return nums_new
if __name__ == "__main__":    s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))