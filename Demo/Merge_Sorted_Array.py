class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums_1=[]
        for i in range(m):
            nums_1.append(nums1[i])
        nums_2=[]
        for i in range(n):
            nums_2.append(nums2[i])

        for i in range(len(nums_2)):
            nums_1.append(nums_2[i])
        nums_1.sort()
        for i in range(len(nums_1)):
            nums1[i]=nums_1[i]
if __name__ == "__main__":    s = Solution()
s.merge([1,2,3,0,0,0],3,[2,5,6],3)