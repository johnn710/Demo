class Solution(object):
    def addDigits(self, num):
        sum_=0
        while(num>0):
            digit=num%10
            sum_+=digit
            num//=10
            if(sum_<10 and num==0):
                return sum_
            elif sum_>9 and num==0:
                num=sum_
                sum_=0
            else:
                pass
        return 0
if __name__ == "__main__":    s = Solution()
print(s.addDigits(38))  