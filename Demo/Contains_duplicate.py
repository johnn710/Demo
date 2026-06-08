class Solution(object):
    def containsDuplicate(self, nums):
        s=set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
if __name__ == "__main__":    s = Solution()
print(s.containsDuplicate([1,2,3,1]))