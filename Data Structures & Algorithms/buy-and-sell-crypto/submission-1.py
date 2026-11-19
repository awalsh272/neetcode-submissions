class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx = 0
        sell_idx = 1
        profit = 0
        while sell_idx < len(prices):
            sell_price = prices[sell_idx]
            buy_price = prices[buy_idx]
            
            if buy_price < sell_price:
                trans_profit = sell_price - buy_price
                profit = max(profit, trans_profit)
                
            else:
                buy_idx = sell_idx
            sell_idx += 1

        return profit

        


        