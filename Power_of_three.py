class Solution(object):
    def isPowerOfThree(self, n):
        while (n>0 and n%3==0):
            n//=3
        if n==1:
            return True
        return False
if __name__ == "__main__":    s = Solution()
print(s.isPowerOfThree(27))
