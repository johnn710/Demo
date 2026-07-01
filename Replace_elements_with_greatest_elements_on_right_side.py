class Solution(object):
    def replaceElements(self, arr):    
        max_right=-1
        for i in range(len(arr)-1,-1,-1):
            current=arr[i]
            arr[i]=max_right
            if current>max_right:
                max_right=current
            
        return arr
if __name__=="__main__":
    arr=[17,18,5,4,6,1]
    obj=Solution()
    print(obj.replaceElements(arr))