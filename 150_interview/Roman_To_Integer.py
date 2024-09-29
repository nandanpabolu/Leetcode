class Solution:
    def romanToInt(self, s: str) -> int:
        # Direct values for each Roman numeral
        total = 0
        n = len(s)
        
        # Iterate through the string
        for i in range(n):
            # For subtractive cases
            if i < n - 1:
                if s[i] == 'I' and s[i + 1] in ('V', 'X'):
                    total -= 1
                elif s[i] == 'X' and s[i + 1] in ('L', 'C'):
                    total -= 10
                elif s[i] == 'C' and s[i + 1] in ('D', 'M'):
                    total -= 100
                else:
                    # Normal cases
                    if s[i] == 'I':
                        total += 1
                    elif s[i] == 'V':
                        total += 5
                    elif s[i] == 'X':
                        total += 10
                    elif s[i] == 'L':
                        total += 50
                    elif s[i] == 'C':
                        total += 100
                    elif s[i] == 'D':
                        total += 500
                    elif s[i] == 'M':
                        total += 1000
            else:
                # Last character handling
                if s[i] == 'I':
                    total += 1
                elif s[i] == 'V':
                    total += 5
                elif s[i] == 'X':
                    total += 10
                elif s[i] == 'L':
                    total += 50
                elif s[i] == 'C':
                    total += 100
                elif s[i] == 'D':
                    total += 500
                elif s[i] == 'M':
                    total += 1000
        
        return total
