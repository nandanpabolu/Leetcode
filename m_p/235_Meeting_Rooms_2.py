from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Extract the start and end times
        start_times = sorted([interval[0] for interval in intervals])
        end_times = sorted([interval[1] for interval in intervals])
        
        # Initialize two pointers and a count for rooms
        start_pointer = 0
        end_pointer = 0 
        rooms_needed = 0
        max_rooms = 0
        
        # Iterate over the start times
        while start_pointer < len(intervals):
            # If the current meeting starts before the earliest meeting ends, we need a new room
            if start_times[start_pointer] < end_times[end_pointer]:
                rooms_needed += 1
                start_pointer += 1
            else:
                # A meeting has ended, so we can reuse the room
                rooms_needed -= 1
                end_pointer += 1
            
            # Track the maximum number of rooms needed
            max_rooms = max(max_rooms, rooms_needed)
        
        return max_rooms
