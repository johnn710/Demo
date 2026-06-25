class Solution(object):
    def findDifference(self, nums1, nums2):
        li1=[]
        li2=[]
        for i in range(len(nums1)):
            if nums1[i] not in nums2:
                if nums1[i] not in li1:
                    li1.append(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                if nums2[i] not in li2:
                    li2.append(nums2[i])
        return [li1,li2]
if __name__=="__main__":
    nums1=[1,2,3]
    nums2=[2,4,6]
    obj=Solution()
    print(obj.findDifference(nums1,nums2))








    
    