class Solution(object):
    def findNumbers(self, nums):
        count=0
        even_digit_count=0
        for i in range(len(nums)):
            while (nums[i]>0):
                nums[i]//=10
                count +=1
            if count%2==0:
                even_digit_count+=1
            count=0
        return even_digit_count
if __name__ == "__main__":    s = Solution()
print(s.findNumbers([12,345,2,6,7896])) 