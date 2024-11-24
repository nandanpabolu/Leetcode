import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []  # Min-heap to store the top k largest elements
        for num in nums:
            heapq.heappush(self.min_heap, num)  # Add each number to the heap
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)  # Maintain heap size at most k

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)  # Add the new value to the heap
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)  # Maintain heap size at most k
        return self.min_heap[0]  # The smallest element in the heap is the k-th largest
