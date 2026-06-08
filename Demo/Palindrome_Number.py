class Solution(object):
    def isPalindrome(self, x):
        count=0
        y=str(x)
        for i in range(len(y)):
            if(y[i]==y[len(y)-i-1]):
               count+=1
        if (count==len(y)):
            return True
        else:
            return False
if __name__ == "__main__":    s = Solution()
print(s.isPalindrome(121))