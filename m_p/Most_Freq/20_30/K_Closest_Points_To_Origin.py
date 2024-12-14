import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        diastances = []
        
        for point in points:
            x, y = point
            
            distance = math.sqrt(x ** 2 + y ** 2)  # Distance from origin (0, 0)
            distances.append((distance, point))  # Store distance and point as a tuple

        # Sort the list by distance
        distances.sort(key=lambda x: x[0])

        # Get the first 'k' points based on the closest distances
        return [point for _, point in distances[:k]]