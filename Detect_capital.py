class Solution(object):
    def detectCapitalUse(self, word):
        count_upper=0
        count_lower=0
        for ch in word:
            if ch.isupper():
                count_upper+=1
            if ch.islower():
                count_lower+=1
        if count_upper==len(word) or count_lower==len(word):
            return True
        else:
            return word.istitle()
if __name__=="__main__":
    word="USA"
    obj=Solution()
    print(obj.detectCapitalUse(word))
    