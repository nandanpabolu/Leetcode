import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequencies of each number
        frequency = {}  # Frequency dictionary
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        # Step 2: Use a heap to find the top k frequent elements
        # The heap will store tuples (-frequency, num) so we can get the largest frequencies
        heap = []
        for num, freq in frequency.items():
            heapq.heappush(heap, (-freq, num))  # Push negative frequency to simulate max-heap

        # Step 3: Extract the top k elements from the heap
        output = []
        for _ in range(k):
            output.append(heapq.heappop(heap)[1])  # Get the element with the largest frequency
        
        return output
