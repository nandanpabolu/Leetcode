class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # Step 1: Find the smaller of the two numbers
        min_num = min(a, b)
        
        # Step 2: Count common factors
        count = 0
        for x in range(1, min_num + 1):
            if a % x == 0 and b % x == 0:
                count += 1
        
        return count
