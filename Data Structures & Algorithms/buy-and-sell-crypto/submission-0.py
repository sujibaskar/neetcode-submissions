class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprice =0
        minprice=prices[0]

        for sell in prices:
            maxprice = max(maxprice,sell-minprice)
            minprice = min(minprice,sell)
        return maxprice