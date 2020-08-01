class SnapshotArray:

    def __init__(self, length: int):
        self.vault = []
        self.sid = 0
        for i in range(length):
            self.vault.append([[0,0]])

    def set(self, index: int, val: int) -> None:
        self.vault[index].append([self.sid, val])

    def snap(self) -> int:
        self.sid += 1
        return self.sid-1

    def get(self, index: int, snap_id: int) -> int:        
        his = self.vault[index]
        # print(his)
        pos = bisect.bisect(his, [snap_id+1])
        # print(pos)
        return his[pos-1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)