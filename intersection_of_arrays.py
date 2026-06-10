class Solution(object):
    def intersection(self, nums1, nums2):
        s=set(nums1)
        s_new=set()
        for i in range(len(nums2)):
            if nums2[i] in s:
               s_new.add(nums2[i])

        return list(s_new)
if __name__ == "__main__":    s = Solution()
print(s.intersection([1,2,2,1],[2,2]))  