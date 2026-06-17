class Solution(object):
    def checkIfPangram(self, sentence):
        eng_alphabet="qwertyuiopasdfghjklzxcvbnm"
        for ch in eng_alphabet:
            if ch not in sentence:
                return False
        return True
if __name__ == "__main__":    s = Solution()
print(s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))