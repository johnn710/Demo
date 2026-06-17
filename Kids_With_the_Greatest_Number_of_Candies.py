class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_=0
        for i in candies:
            if i > max_:
                max_=i
        list_bool=[]
        for i in candies:
            if (i+extraCandies>=max_):
                list_bool.append(True)
            else:
                list_bool.append(False)
        return list_bool
if __name__ == "__main__":    s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))