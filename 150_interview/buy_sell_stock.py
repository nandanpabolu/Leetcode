"approach 1, i didnt realize this is about stock prices and by mistake just calculated difference between highest and lowest. However, i cant neglect the initial higher days coming up with upograded code soon. "

class Solution:
    def maxProfit(self, prices: list[int]) -> int:  # Use 'list[int]' instead of 'List[int]'
        n = len(prices)  # Define 'n'
        
        for i in range(n):  # Loop over the length of prices
            for j in range(0, n - i - 1):  # Correct use of 'n' instead of undefined variable
                if prices[j] < prices[j + 1]:  # Swap if the element is smaller (this would sort in descending order)
                    prices[j], prices[j + 1] = prices[j + 1], prices[j]
        
        print(prices)
        max_profit = prices[0]- prices[len(prices) - 1]
        return max_profit
          # Ensure print is indented properly within the method


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize smallest to a very large value and greatest (max profit) to 0
        min_price = float('inf')  # Set to a large value initially
        max_profit = 0  # Max profit starts at 0

        # Loop through all the prices
        for price in prices:
            # Update the minimum price encountered so far
            if price < min_price:
                min_price = price
            
            # Calculate the potential profit with the current price
            potential_profit = price - min_price
            
            # Update the maximum profit if the current profit is greater than the previous max
            if potential_profit > max_profit:
                max_profit = potential_profit
        
        return max_profit
