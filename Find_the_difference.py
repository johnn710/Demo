class Solution(object):
    def findTheDifference(self, s, t):
        for i in t:
            if i in s:
                if t.count(i)>s.count(i):
                    return i
            else:
                return i
if __name__ == "__main__":    s = Solution()
print(s.findTheDifference("abcd", "abcde"))     