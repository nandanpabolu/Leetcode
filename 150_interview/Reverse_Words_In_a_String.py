class Solution:
    def reverseWords(self, s: str) -> str:
        # Strip leading and trailing spaces
        s = s.strip()

        # Split the string into a list of words, reverse the list, and join it back into a string
        words = s.split()
        reversed_words = ' '.join(reversed(words))

        return reversed_words
