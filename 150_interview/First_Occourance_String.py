class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Special case when needle is an empty string
        if needle == "":
            return 0
        
        # Loop through the haystack and check each substring of length len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        # If needle is not found in haystack, return -1
        return -1
