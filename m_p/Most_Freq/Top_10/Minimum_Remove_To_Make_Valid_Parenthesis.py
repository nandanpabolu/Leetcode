class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        
        for i in stack:
            s[i] = ""
        return "".join(s)
        
        
#Time Complexity is O(n) as depends on input, complete parse through list s