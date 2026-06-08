class Solution(object):
    def mySqrt(self, x):
       import math
       a=int(math.sqrt(x))
       return a
if __name__ == "__main__":    s = Solution()
print(s.mySqrt(8))