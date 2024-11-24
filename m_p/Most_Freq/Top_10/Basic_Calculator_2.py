class Solution:
    def calculate(self, s: str) -> int:
        s_no_spaces = s.replace(" ", "")  # Remove spaces
        stack = []  # Stack to hold intermediate results
        temp_nums = 0  # Temporary number accumulator
        operator = "+"  # Initial operator (default to addition)

        s_list = list(s_no_spaces)  # Convert string to list for iteration

        for i, char in enumerate(s_list):
            if char.isdigit():  # Build the current number
                temp_nums = temp_nums * 10 + int(char)
            
            # If the character is an operator or the end of the string
            if char in "+-*/" or i == len(s_list) - 1:
                # Process the current number with the last operator
                if operator == "+":
                    stack.append(temp_nums)
                elif operator == "-":
                    stack.append(-temp_nums)
                elif operator == "*":
                    stack.append(stack.pop() * temp_nums)
                elif operator == "/":
                    stack.append(int(stack.pop() / temp_nums))  # Integer division
                
                # Reset temp_nums and update operator
                temp_nums = 0
                operator = char

        return sum(stack)  # Sum the results in the stack
