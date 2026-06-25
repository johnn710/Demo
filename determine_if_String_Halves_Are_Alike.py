class Solution(object):
    def halvesAreAlike(self, s):
        m=len(s)
        n=m//2
        vowel="aeiouAEIOU"
        count1=0
        count2=0
        for i in range(n):
            if s[i] in vowel:
                count1+=1
        for i in range(m-1,n-1,-1):
            if s[i] in vowel:
                count2+=1
        if count1==count2:
            return True
        return False
if __name__=="__main__":
    s="book"
    obj=Solution()
    print(obj.halvesAreAlike(s))    