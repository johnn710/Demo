class Solution(object):
    def reverseVowels(self, s):
        vowel="aeiouAEIOU"
        rev=[]
        for i in s:
            if i in vowel:
                rev.append(i)
        rev.reverse()    
        list_s=list(s)
        k=0
        for i in range(len(s)):
            if list_s[i] in vowel:
                list_s[i]=rev[k]
                k+=1
        
        return ("".join(list_s))
if __name__ == "__main__":    s = Solution()
print(s.reverseVowels("hello")) 