class Solution(object):
    def backspaceCompare(self, s, t):
        s_new=[]
        for i in s:
            if i != "#":
                s_new.append(i)
            elif i== "#":
                if len(s_new)==0:
                    pass
                else:
                    s_new.pop()   #key to solve this problem..pop deletes the last element
        t_new=[]
        for i in t:
            if i != "#":
                t_new.append(i)
            elif i== "#":
                if len(t_new)==0:
                    pass
                else:
                    t_new.pop()      
        if s_new == t_new:
            return True
        return False
if __name__=="__main__":
    s="ab#c"
    t="ad#c"
    obj=Solution()
    print(obj.backspaceCompare(s,t))