import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        
        # Initialize the heap with the first element of each row
        for i in range(n):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))  # (value, row, col)
        
        # Extract the smallest element k times
        for _ in range(k - 1):
            val, row, col = heapq.heappop(min_heap)
            # If there's a next element in the same row, add it to the heap
            if col + 1 < n:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
        
        # The root of the heap is the k-th smallest element
        return heapq.heappop(min_heap)[0]
