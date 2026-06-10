class Solution(object):
    def findDisappearedNumbers(self, nums):
        
        s=set(nums)
        ans=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                ans.append(i)
                
        return ans
if __name__ == "__main__":    s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))