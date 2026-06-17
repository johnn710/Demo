class Solution(object):
    def isPowerOfFour(self, n):
        while (n>0 and n%4==0):
            n//=4
        if n==1:
            return  True
        return False
if __name__ == "__main__":    s = Solution()
print(s.isPowerOfFour(16))
