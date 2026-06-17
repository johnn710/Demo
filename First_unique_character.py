class Solution(object):
    def firstUniqChar(self, s):
        seen_once=set()
        seen_multiple=set()
        for i in s:
            if i not in seen_once and i not in seen_multiple:
                seen_once.add(i)
            elif i in seen_once:
                seen_once.remove(i)
                seen_multiple.add(i)
        for i in range(len(s)):
            if s[i] in seen_once:
                return i
        return -1
if __name__ == "__main__":    s = Solution()
print(s.firstUniqChar("leetcode"))  