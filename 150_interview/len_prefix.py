from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: if the list is empty, return an empty string
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Compare the prefix with each subsequent string in the list
        for string in strs[1:]:
            # Reduce the prefix until it matches the current string
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]  # Remove the last character from the prefix
                # If the prefix becomes empty, return an empty string
                if not prefix:
                    return ""
        
        return prefix
