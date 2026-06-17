class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        for i in ransomNote:
            if magazine.count(i)>=ransomNote.count(i):
                pass
            else:
                return False
        return True
if __name__ == "__main__":    s = Solution()
print(s.canConstruct("a", "b")) 