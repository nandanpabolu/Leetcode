class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        # Add a trailing '/' to ensure the last part of the path is processed
        for c in path + "/":
            if c == "/":
                if cur == "..":
                    # If cur is "..", pop from the stack (go one directory up) if possible
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    # If cur is a valid directory name, add it to the stack
                    stack.append(cur)
                # Reset cur after processing the current part
                cur = ""
            else:
                # Accumulate characters into cur
                cur += c

        # Join the stack with '/' and prepend '/' to form the simplified path
        return "/" + "/".join(stack)
