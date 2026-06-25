class Solution(object):
    def uniqueOccurrences(self, arr):
      for i in range(len(arr)):
        for j in range(i+1,len(arr)):  #range should be correct to avoid TLE
            if arr[i]!=arr[j]:
               if arr.count(arr[i])==arr.count(arr[j]):
                    return False
                  
      return True
if __name__=="__main__":
        arr=[1,2,2,1,1,3]
        obj=Solution()
        print(obj.uniqueOccurrences(arr))
