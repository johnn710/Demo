class Solution(object):
    def largestAltitude(self, gain):
        total=0
        max_total=0 #initialize with zero
        for i in range(len(gain)):
            total+=gain[i]
            if total>=max_total:
               max_total=total
        return max_total
if __name__=="__main__":
    gain=[-5,1,5,0,-7]
    obj=Solution()
    print(obj.largestAltitude(gain))