class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # Number of flowers we can plant
        for i in range(len(flowerbed)):
            # Check if the current plot is empty and the adjacent plots are also empty
            if flowerbed[i] == 0:
                prev = (i == 0 or flowerbed[i-1] == 0)  # True if first plot or previous plot is empty
                next = (i == len(flowerbed) - 1 or flowerbed[i+1] == 0)  # True if last plot or next plot is empty
                if prev and next:
                    flowerbed[i] = 1  # Plant a flower here
                    count += 1
                    if count >= n:  # Early exit if we have planted enough flowers
                        return True
        return count >= n
