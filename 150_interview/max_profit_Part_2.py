class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cum_profit = 0  # Initialize cumulative profit
        
        # Loop through prices from the second day onwards
        for i in range(1, len(prices)):
            # If there's an upward trend (i.e., a price increase)
            if prices[i] > prices[i - 1]:
                # Add the difference to the cumulative profit
                cum_profit += prices[i] - prices[i - 1]
        
        # Return the total cumulative profit
        return cum_profit
