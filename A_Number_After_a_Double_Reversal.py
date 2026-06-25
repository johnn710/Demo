class Solution(object):
    def isSameAfterReversals(self, num):
        original1=num
        rev=0
        while (num>0):
            digit=num%10
            rev=rev*10 + digit
            num//=10
        original2=rev
        reverse=0
        while(rev>0):
            rem=rev%10
            reverse=reverse*10 + rem
            rev//=10
        if original1==reverse:
            return True
        return False
if __name__=="__main__":
    num=526
    obj=Solution()
    print(obj.isSameAfterReversals(num))