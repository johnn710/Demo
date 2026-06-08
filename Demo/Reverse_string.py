class Solution(object):
    def reverseString(self, s):
        s_rev=[]
        s.reverse()
        for i in range(len(s)):
            s_rev.append(s[i])
        return s_rev
if __name__ == "__main__":    s = Solution()
print(s.reverseString(["h","e","l","l","o"]))