class Solution:
    def reverse(self, x: int) -> int:
        # Initialize variables
        temp = 0
        is_negative = x < 0  # Check if the number is negative
        x = abs(x)  # Work with the absolute value of x
        
        # Reverse the integer
        while x != 0:
            digit = x % 10  # Get the last digit
            temp = temp * 10 + digit  # Append the digit
            x //= 10  # Remove the last digit from x
        
        # Handle negative numbers
        if is_negative:
            temp = -temp
        
        # Check for 32-bit signed integer overflow
        if temp < -2**31 or temp > 2**31 - 1:
            return 0
        
        return temp

# Example usage
sol = Solution()
print(sol.reverse(123))   # Output: 321
print(sol.reverse(-123))  # Output: -321
print(sol.reverse(120))   # Output: 21
print(sol.reverse(0))     # Output: 0
