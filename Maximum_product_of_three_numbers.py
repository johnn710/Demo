class Solution(object):
    def maximumProduct(self, nums):
        largest=float('-inf')
        second_largest=float('-inf')
        third_largest=float('-inf')
        first_minimum=float('inf')
        second_minimum=float('inf')
        temp=list(nums)          
        for i in range(len(temp)):
            if temp[i]>largest:
                largest=temp[i]
        temp.remove(largest)
        
        for i in range(len(temp)):
            if temp[i]>second_largest:
                second_largest=temp[i]
        temp.remove(second_largest)
        for i in range(len(temp)):
            if temp[i]>third_largest:
                third_largest=temp[i]
        product1=largest*second_largest*third_largest
        temp=list(nums)
        for i in range(len(temp)):
            if temp[i]<first_minimum:
                first_minimum=temp[i]
        temp.remove(first_minimum)
        for i in range(len(temp)):
            if temp[i]<second_minimum:
                second_minimum=temp[i]
        product2= largest*first_minimum*second_minimum
        
        return max(product1,product2) 
if __name__=="__main__":
    nums=[1,2,3]
    obj=Solution()
    print(obj.maximumProduct(nums))