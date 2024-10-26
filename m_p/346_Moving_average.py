class MovingAverage:

    def __init__(self, size: int):
        self.size = size 
        self.queue = deque()
        self.current_sum = 0 


    def next(self, val: int) -> float:
        self.queue.append(val)
        self.current_sum += val

        if len(self.queue) > self.size:
            removed_value = self.queue.popleft()
            self.current_sum -= removed_value

        return self.current_sum / len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)