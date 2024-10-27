class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize pointers for both strings starting from the end
        i, j = len(num1) - 1, len(num2) - 1
        
        carry = 0  # Variable to store carry value during addition
        result = []  # List to accumulate the result
        
        # Continue until both numbers are fully processed or there's a carry left
        while i >= 0 or j >= 0 or carry:
            # Get the current digit from num1 or use 0 if i is out of bounds
            x1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            # Get the current digit from num2 or use 0 if j is out of bounds
            x2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            
            # Compute the sum of the two digits plus any carry
            value = x1 + x2 + carry
            # Compute the carry for the next iteration (if the sum is 10 or more)
            carry = value // 10
            # Add the current digit to the result (we only want the last digit of the sum)
            result.append(str(value % 10))
            
            # Move to the next digit (leftwards) in both num1 and num2
            i -= 1
            j -= 1
        
        # Since we've added digits in reverse order, we need to reverse the result
        return ''.join(result[::-1])
