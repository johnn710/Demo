class Solution(object):
    def sortArrayByParity(self, nums):
      list_new=[]
      for i in range(len(nums)):
        if nums[i]%2==0:
            list_new.append(nums[i])
      for i in range(len(nums)):
        if nums[i]%2!=0:
            list_new.append(nums[i])
      return list_new 
if __name__=="__main__":
    nums=[3,1,2,4]
    obj=Solution()
    print(obj.sortArrayByParity(nums))