class Solution(object):
    def shuffle(self, nums, n):
        arr_x=[]
        arr_y=[]
        arr=[]
        for i in range(n):
            arr_x.append(nums[i])
        for j in range(n,2*n):
            arr_y.append(nums[j])
        
        for i in range(len(nums)):
            nums[i]=0
        i=0
        for k in range(n):
            arr.insert(i,arr_x[k])
            i+=2
        i=1
        for k in range(n):
            arr.insert(i,arr_y[k])
            i+=2
        return arr
if __name__=="__main__":
    nums=[2,5,1,3,4,7]
    n=3
    obj=Solution()
    print(obj.shuffle(nums,n))