# type: ignore

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = Deque()
        self.avg = 0

    def next(self, val: int) -> float:
        if self.size == len(self.queue):
            n = self.queue.popleft()
            self.avg -= n
        self.queue.append(val)
        self.avg += val
        return self.avg / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)