class StockSpanner:

    def __init__(self):
        self.deq = collections.deque()
        self.deq.append((10**5+1,0)) # (value, idx)
        self.idx = 1

    def next(self, price: int) -> int:        
        while self.deq[-1][0]<=price:
            self.deq.pop()
        ans = self.idx - self.deq[-1][1]
        self.deq.append((price, self.idx))
        self.idx += 1
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)