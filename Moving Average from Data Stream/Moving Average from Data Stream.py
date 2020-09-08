class MovingAverage:

    def __init__(self, size: int):
        self.arr = []
        self.size = size
        self.summation = 0
        

    def next(self, val: int) -> float:
        self.arr.append(val)
        self.summation += val
        if len(self.arr)>self.size:
            self.summation -= self.arr[0]
            self.arr.pop(0)
        return self.summation/len(self.arr)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)