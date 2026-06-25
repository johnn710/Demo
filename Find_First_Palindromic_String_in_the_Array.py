class Solution(object):
    def firstPalindrome(self, words):
       for i in words:
            s=i
            count=0
            for j in range(len(s)):
                if s[j]==s[len(s)-j-1]:
                    count+=1
            if count==len(s):
                return s
       s=""
       return s
if __name__=="__main__":
    words=["abc","car","ada","racecar","cool"]
    obj=Solution()
    print(obj.firstPalindrome(words))