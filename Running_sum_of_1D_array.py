class Solution(object):
    def runningSum(self, nums):
        sum_nums=0
        list_sum=[]
        for i in range(len(nums)):
            sum_nums+=nums[i]
            list_sum.append(sum_nums)
        return list_sum
if __name__ == "__main__":    s = Solution()
print(s.runningSum([1,2,3,4]))  