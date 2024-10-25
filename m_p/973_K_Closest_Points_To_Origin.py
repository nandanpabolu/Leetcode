import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create a list to store points and their distances
        distances = []
        
        # Iterate over the points and calculate the distance from the origin (0, 0)
        for point in points:
            x, y = point
            distance = math.sqrt(x ** 2 + y ** 2)  # Distance from origin (0, 0)
            distances.append((distance, point))  # Store distance and point as a tuple #Highlights the use of tuples in code.

        # Sort the list by distance
        distances.sort(key=lambda x: x[0])

        # Get the first 'k' points based on the closest distances
        return [point for _, point in distances[:k]]