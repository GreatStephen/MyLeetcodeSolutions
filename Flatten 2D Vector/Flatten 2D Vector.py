class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.deq_l = collections.deque()
        self.deq_i = collections.deque()
        for l in v:
            if len(l)>0:
                self.deq_l.append(l)
                self.deq_i.append(0)

    def next(self) -> int:
        l, i = self.deq_l[0], self.deq_i[0]
        if i+1>=len(l):
            self.deq_l.popleft()
            self.deq_i.popleft()
        else:
            self.deq_i.appendleft(self.deq_i.popleft()+1)
        return l[i]

    def hasNext(self) -> bool:
        return len(self.deq_l)>0


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()