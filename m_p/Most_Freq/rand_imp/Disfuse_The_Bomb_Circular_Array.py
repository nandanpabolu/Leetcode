from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n  # Return a list of zeros if k is 0

        output = [0] * n

        for i in range(n):
            if k > 0:  # Sum the next k elements
                output[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
            elif k < 0:  # Sum the previous |k| elements
                output[i] = sum(code[(i + j) % n] for j in range(k, 0))

        return output
    
    # Time Complexity O(n * |k|)
    # Space Complecity O(n)
    
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n  # Return a list of zeros if k is 0
        
        output = [0] * n
        window_sum = 0
        start = 1 if k > 0 else k  # Start of the sliding window
        end = k if k > 0 else -1  # End of the sliding window (exclusive)

        # Compute initial window sum
        for i in range(start, end + 1):
            window_sum += code[i % n]

        # Slide the window across the array
        for i in range(n):
            output[i] = window_sum
            # Slide the window: Remove the element that's sliding out
            window_sum -= code[(i + start) % n]
            # Add the element that's sliding in
            window_sum += code[(i + end + 1) % n]

        return output