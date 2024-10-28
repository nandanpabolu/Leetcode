class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        idx = 0 
        missing_count = 0 
        current = 1

        while missing_count < k:
            if idx < len(arr) and arr[idx] == current:
                idx += 1 
            else:
                missing_count += 1 
            
            if missing_count == k:
                return current
            
            current += 1
