class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        s1=""
        s2=""
        for i in word1:
            s1+=i
        for i in word2:
            s2+=i
        if s1==s2:
            return True
        return False
if __name__=="__main__":
    word1=["ab","c"]
    word2=["a","bc"]
    obj=Solution()
    print(obj.arrayStringsAreEqual(word1,word2))