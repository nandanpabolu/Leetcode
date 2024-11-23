from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_count = Counter(s)
        odd_count = 0 

        for count in char_count.values():
            if count % 2 != 0:
                odd_count += 1
        
        return odd_count <= 1 
