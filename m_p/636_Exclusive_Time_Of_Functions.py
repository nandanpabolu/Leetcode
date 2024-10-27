from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n  # Initialize result array with zeroes
        stack = []        # Stack to keep track of active function calls
        prev_time = 0     # Track the previous time

        for log in logs:
            # Split the log by ':' to extract function_id, action, and time
            function_id, action, time = log.split(':')
            function_id = int(function_id)  # Convert function_id to integer
            time = int(time)               # Convert time to integer

            if action == 'start':
                # Update the time spent on the function currently on top of the stack
                if stack:
                    result[stack[-1]] += time - prev_time

                # Add the current function to the stack
                stack.append(function_id)
                prev_time = time  # Update previous time
            else:
                # Pop the last function and calculate its total time
                last_function = stack.pop()
                result[last_function] += time - prev_time + 1  # Include end time by adding 1
                prev_time = time + 1  # Move past the end time

        return result
        