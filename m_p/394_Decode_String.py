class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                # Accumulate the number for multi-digit cases
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push current accumulated number and string onto stacks
                num_stack.append(current_num)
                str_stack.append(current_string)
                # Reset for the new substring
                current_num = 0
                current_string = ""
            elif char == ']':
                # Pop the number of repetitions and previous string
                repeat_count = num_stack.pop()
                previous_string = str_stack.pop()
                # Repeat the current string and concatenate with the previous string
                current_string = previous_string + current_string * repeat_count
            else:
                # Accumulate current characters
                current_string += char

        return current_string
