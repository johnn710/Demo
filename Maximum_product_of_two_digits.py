class Solution(object):
    def maxProduct(self, n):
        list_digit=[]
        while(n>0):
            digit=n%10
            list_digit.append(digit)
            n//=10
        maximum=0
        second_maximum=0
        if 0 in list_digit and len(list_digit)==2:
            return 0
        for i in range(len(list_digit)):
            if list_digit[i]>maximum:
                maximum=list_digit[i]
        list_digit.remove(maximum)
        for i in range(len(list_digit)):        
            if list_digit[i]>second_maximum:
                second_maximum=list_digit[i]
        return maximum * second_maximum
if __name__=="__main__":
    n=29
    obj=Solution()
    print(obj.maxProduct(n))