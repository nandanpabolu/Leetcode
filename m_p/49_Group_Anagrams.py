from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26  # Create a count array for 26 letters (a-z)

            for char in s:
                index = ord(char) - ord('a')
                count[index] += 1  # Update count for each character
            
            key = tuple(count)  # Use the count tuple as a unique key
            anagrams[key].append(s)  # Append the word to the corresponding key

        return list(anagrams.values())