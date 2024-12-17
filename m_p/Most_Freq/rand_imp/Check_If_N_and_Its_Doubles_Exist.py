
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()  # To store the numbers we have seen
        
        for num in arr:
            # Check if double or half of the current number exists in the set
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            
            # Add the current number to the set
            seen.add(num)
        
        return False