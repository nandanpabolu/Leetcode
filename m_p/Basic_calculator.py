class Solution:
    def calculate(self, s: str) -> int:
        # Remove all spaces from the input string
        s_no_spaces = s.replace(" ", '')
        
        # Initialize a stack to store intermediate results
        stack = []
        
        # Temporary variable to store the current number being processed
        temp_num = 0
        
        # Variable to store the last operator, initialized to '+'
        operator = '+'
        
        # Convert the string to a list of characters (after removing spaces)
        s_list = list(s_no_spaces)

        # Loop through the list of characters
        for i in range(len(s_list)):
            # If the current character is a digit, accumulate the number
            if s_list[i].isdigit():
                temp_num = temp_num * 10 + int(s_list[i])

            # If the current character is an operator or the last character
            if s_list[i] in "+-*/" or i == len(s_list) - 1:
                # Perform the operation based on the previous operator
                if operator == '+':
                    stack.append(temp_num)
                elif operator == '-':
                    stack.append(-temp_num)
                elif operator == '*':
                    stack.append(stack.pop() * temp_num)
                elif operator == '/':
                    # Use integer division as per the problem description
                    stack.append(int(stack.pop() / temp_num))
                
                # Reset the number for the next iteration
                temp_num = 0
                # Update the operator for the next iteration
                operator = s_list[i]

        # Sum all the elements in the stack to get the final result
        return sum(stack)
