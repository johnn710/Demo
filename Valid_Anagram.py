class Solution(object):
    def isAnagram(self, s, t):
        len_s=0
        len_t=0
        for i in s:
            len_s+=1
        for j in t:
            len_t+=1
        if len_s>len_t or len_s==len_t:
            for i in s:
                if i in t:
                    if s.count(i)==t.count(i):
                        pass
                    else:
                        return False
                else:
                    return False
            if len_s==len_t:
                return True
            return False
        elif len_s<len_t or len_s==len_t:
            for i in s:
                if i in t:
                    if s.count(i)==t.count(i):
                        pass
                    else:
                        return False
                else:
                    return False
            if len_s==len_t:
                return True
            return False
if __name__ == "__main__":    s = Solution()
print(s.isAnagram("anagram", "nagaram"))    