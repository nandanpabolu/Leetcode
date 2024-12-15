from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda x: x[0] - x[1])
        
        total_cost = 0 
        n = len(costs) // 2
        
        for i in range(n):
            total_cost += costs[i][0]
        for i in range(n, 2*n):
            total_cost += costs[i][1]
        
        return total_cost
    
    
# Time Complexity is O(n log n) due to sorting and modifying list in place is O(n)
# Space Complexiyt will be O(1)