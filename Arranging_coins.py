class Solution(object):
    def arrangeCoins(self, n):
        i=1
        while(n>0):
            n=n-i
            if n<0:
                return i-1
            elif n==0:
                return i
            i+=1
    
if __name__=="__main__":
    n=5
    obj=Solution()
    print(obj.arrangeCoins(n))