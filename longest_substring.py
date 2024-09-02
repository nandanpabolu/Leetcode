class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_2 = ""  # To store the current substring without repeating characters
        max_length = 0  # To store the length of the longest substring

        for i in range(len(s)):
            if s[i] not in s_2:
                # If the character is not in the current substring, add it
                s_2 += s[i]
                print(s_2)  # Optional: To see the current substring
            else:
                # If a repeating character is found, update max_length if needed
                max_length = max(max_length, len(s_2))
                # Start a new substring from the character after the first occurrence of s[i]
                s_2 = s_2[s_2.index(s[i]) + 1:] + s[i]
        
        # After the loop, check the length one last time
        max_length = max(max_length, len(s_2))
        
        return max_length

# Example usage
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3 ("abc")
print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1 ("b")
print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3 ("wke")
