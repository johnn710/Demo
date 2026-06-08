class Solution(object):
    def isPalindrome(self, s):
        s1=s.lower()
        ch=""
        for s2 in s1:
            if s2.isalnum():
                ch=ch+s2
        
        if ch==ch[::-1]:
            return True
        else:
            return False
if __name__ == "__main__":    s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))