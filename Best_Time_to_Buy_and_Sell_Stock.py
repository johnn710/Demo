class Solution(object):
    def maxProfit(self, prices):
      profit=0 
      minimum=float('inf')
      for price in prices:
        if price<minimum:
            minimum=price
        elif price-minimum>profit:
            profit=price-minimum
      return profit
if __name__=="__main__":
    prices=[7,1,5,3,6,4]
    obj=Solution()
    print(obj.maxProfit(prices))