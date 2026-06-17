class Solution(object):
    def mostFrequent(self, nums, key):
        list_nums=[]
        for i in range(len(nums)):
            if i==len(nums)-1:
                break
            if nums[i]==key:
                list_nums.append(nums[i+1])
        max_count=0
        for i in range(len(list_nums)):
            count=list_nums.count(list_nums[i])
            if count>max_count:
                max_count=count
                target=list_nums[i]
        return target
if __name__ == "__main__":    s = Solution()    
print(s.mostFrequent([1,100,200,1,100], 1))