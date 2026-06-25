class Solution(object):
    def selfDividingNumbers(self, left, right):
        list_new=[]
        for i in range(left,right+1):
            original=i
            count=0
            while(i>0):
                digit=i%10
                if digit==0:
                    break
                elif original%digit!=0:
                    break
                elif original%digit==0:
                    count+=1
                s=str(original)
                if count==len(s):
                    list_new.append(original)
                i//=10
        return list_new
if __name__=="__main__":
    left=1
    right=22
    obj=Solution()
    print(obj.selfDividingNumbers(left,right))  