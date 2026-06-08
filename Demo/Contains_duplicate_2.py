class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
      s={} #s={value:index} 
      for i in range(len(nums)):
        if nums[i] in s:
            if i - s[nums[i]] <=k: #s[2] gives the index where 2 is present
                return True
        s[nums[i]]=i
      return False 
if __name__ == "__main__":    s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1],3))