class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=10000
        max_ben=0

        for price in prices:
            if price - min_price> max_ben:
                max_ben = price - min_price
            if price < min_price:
                min_price = price
                
        return max_ben
            