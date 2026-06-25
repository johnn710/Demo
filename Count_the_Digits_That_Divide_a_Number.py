class Solution(object):
    def countDigits(self, num):
        count=0
        original=num
        while(num>0):
            
            val=num%10
            if val==0:
                num//=10
                continue
            if original%val==0:
                count+=1
            num//=10
        return count
if __name__=="__main__":
    num=1248
    obj=Solution()
    print(obj.countDigits(num))