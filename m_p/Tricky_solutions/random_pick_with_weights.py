class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []

        total = 0 

        for weights in w:
            total += weights

            self.prefix_sums.append(total)

        self.total = total
    def pickIndex(self) -> int:
        #[1,2,4] --> [1,3,7] --> 4 
        target = random.uniform(0, self.total) # picking random number
        l = 0 
        r = len(self.prefix_sums)

        while l < r:
            mid = (l + r) // 2
            
            if self.prefix_sums[mid] < target:
                l = mid + 1 
            else:
                r = mid
        return l 
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Time Complexity is 0(nlogn) n is cumulating weights, logn is searching
#Space complexity is O(n)