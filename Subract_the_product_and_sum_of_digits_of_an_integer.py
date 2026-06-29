class Solution(object):
    def subtractProductAndSum(self, n):
        sum_digits=0
        pro_digits=1
        while(n>0):
            i=n%10
            sum_digits+=i
            pro_digits*=i
            n//=10
        return pro_digits-sum_digits
if __name__=="__main__":
    n=234
    obj=Solution()
    print(obj.subtractProductAndSum(n))