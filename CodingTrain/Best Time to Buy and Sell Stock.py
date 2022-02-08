class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        lowest_val_seen = prices[0]
        
        for i in range(len(prices)):
            curr_price = prices[i]
            if curr_price < lowest_val_seen:
                lowest_val_seen = curr_price
            else:
                max_profit = max(max_profit, curr_price - lowest_val_seen)

        return max_profit