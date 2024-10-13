class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)  # Convert string to list for mutability
        for i, char in enumerate(s):  # Correct: first i is index, char is the character
            if char == '(':
                stack.append(i)  # Append index of '(' to stack
            elif char == ')':
                if stack:
                    stack.pop()  # Pop the index of the last unmatched '('
                else:
                    s[i] = ""  # Remove unmatched ')'
        
        while stack:
            s[stack.pop()] = ""  # Remove unmatched '(' by setting it to ""

        return "".join(s)  # Convert list back to string
    
#Problem Notes are in M_lc Directory of OneNote