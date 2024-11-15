class Solution:
    def countSubstrings(self, s: str) -> int:
        # Helper function to count palindromes around a center
        def count_palindromes_around_center(left: int, right: int) -> int:
            count = 0
            # Expand outward while the substring is a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1  # Found a palindrome
                left -= 1   # Move left pointer outward
                right += 1  # Move right pointer outward
            return count

        total_count = 0  # Initialize the total count of palindromic substrings
        
        # Loop through each character in the string
        for i in range(len(s)):
            # Count odd-length palindromes (centered on a single character)
            total_count += count_palindromes_around_center(i, i)
            # Count even-length palindromes (centered between two characters)
            total_count += count_palindromes_around_center(i, i + 1)
        
        return total_count
