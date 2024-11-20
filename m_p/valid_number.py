class Solution:
    def isNumber(self, s: str) -> bool:
        def is_integer(str_to_test):
            # Helper to check if a string is a valid integer
            if not str_to_test:
                return False

            if str_to_test[0] in ['+', '-']:
                str_to_test = str_to_test[1:]  # Remove sign if present

            return str_to_test.isdigit()

        def is_decimal(str_to_test):
            # Helper to check if a string is a valid decimal
            if not str_to_test:
                return False

            if str_to_test[0] in ['+', '-']:
                str_to_test = str_to_test[1:]  # Remove sign if present

            # Split the string by the decimal point
            if '.' not in str_to_test:
                return False
            
            left, _, right = str_to_test.partition('.')

            # At least one side of the decimal must have digits
            if not left and not right:
                return False

            if left and not left.isdigit():
                return False

            if right and not right.isdigit():
                return False

            return True

        # Handle scientific notation
        s = s.strip()  # Remove leading and trailing whitespaces
        if 'e' in s or 'E' in s:
            base, _, exponent = s.partition('e') if 'e' in s else s.partition('E')
            return (is_integer(base) or is_decimal(base)) and is_integer(exponent)

        # Otherwise, check for decimals or integers
        return is_integer(s) or is_decimal(s)
