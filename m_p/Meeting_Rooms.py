from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Check for overlaps
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False  # Overlap found

        return True  # No overlaps
