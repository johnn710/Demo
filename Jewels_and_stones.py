class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        for i in jewels:
            if i in stones:
                count=count+stones.count(i)
        return count
if __name__=="__main__":
    jewels="aA"
    stones="aAAbbbb"
    obj=Solution()
    print(obj.numJewelsInStones(jewels,stones))