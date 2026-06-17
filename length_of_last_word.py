class Solution(object):
    def lengthOfLastWord(self, s):
        t=s.strip()
        count=0
        for i in t:
            if i.isalpha():
                count+=1
            else:
                count=0
        return count
if __name__ == "__main__":    s = Solution()
print(s.lengthOfLastWord("Hello World"))
