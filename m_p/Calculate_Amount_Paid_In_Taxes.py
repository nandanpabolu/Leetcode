from typing import List

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0.0
        prev_upper = 0  # Initialize the lower bound of the first bracket

        for upper, percent in brackets:
            # Taxable income for the current bracket
            taxable = min(income, upper - prev_upper)
            tax += taxable * (percent / 100)

            # Subtract the taxable amount from income
            income -= taxable
            if income <= 0:
                break  # All income has been taxed

            # Update prev_upper for the next bracket
            prev_upper = upper

        return tax
