class SnapshotArray:

    def __init__(self, length: int):
        self.vault = {}
        self.snap_id = 0
        self.vault[0] = {}
        for i in range(length):
            self.vault[0][i] = 0

    def set(self, index: int, val: int) -> None:
        self.vault[self.snap_id][index] = val

    def snap(self) -> int:
        self.snap_id += 1
        self.vault[self.snap_id] = {}
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:        
        while index not in self.vault[snap_id]:
            snap_id -= 1
        return self.vault[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)