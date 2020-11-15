class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.data = [None]*n
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        self.data[id-1] = value
        ans = []
        if self.ptr==id:
            while self.ptr-1<self.n and self.data[self.ptr-1]:
                ans.append(self.data[self.ptr-1])
                self.ptr += 1
        # print(ans)
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)