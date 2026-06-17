class Solution(object):
    def isPowerOfTwo(self, n):
        while(n>0 and n%2==0):
            n//=2
        if n==1:
            return True
        return False
if __name__ == "__main__":    s = Solution()
print(s.isPowerOfTwo(16))   