class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        n = len(s)
        result = 0
        sign = 1

        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Check sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Convert digits
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Check overflow and underflow conditions
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return result * sign