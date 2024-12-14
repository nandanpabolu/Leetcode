class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0 
        j = 0 
        overlap = []
        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            
            if start1 <= end2 and start2 <= end1:
                start_overlap = max(start1, start2)
                end_overlap = min(end1, end2)
                overlap.append([start_overlap, end_overlap])
                
            if end1 < end2:
                i += 1 
            else:
                j += 1 
        return overlap
                
 #Time Complexity is O(M+N) where M and N are the 2 lists
 #Space Complexity is O(K) where k is the number of merging intervals as it stores those many outputs in final output list
 
                