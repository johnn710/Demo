class Solution(object):
    def sumOfUnique(self, nums):
        list_new=[]
        for i in nums:
            if nums.count(i)==1:
                list_new.append(i)
        sum_list_new=0
        for i in range(len(list_new)):
            sum_list_new+=list_new[i]
        return sum_list_new
if __name__=="__main__":
    nums=[1,2,3,2]
    obj=Solution()
    print(obj.sumOfUnique(nums))