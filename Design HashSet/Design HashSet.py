class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.MOD = 2**15-1
        self.arr = [None]*self.MOD

    def add(self, key: int) -> None:
        pos = key%self.MOD
        if not self.arr[pos]: 
            self.arr[pos]=[key]
        else:
            for n in self.arr[pos]:
                if n==key: return 
            self.arr[pos].insert(0, key)

    def remove(self, key: int) -> None:
        pos = key%self.MOD
        if self.arr[pos]:
            for i,n in enumerate(self.arr[pos]):
                if n==key:
                    self.arr[pos] = self.arr[:i]+self.arr[i+1:]
                    break

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        pos = key%self.MOD
        if not self.arr[pos]: return False
        for n in self.arr[pos]:
            if n==key: return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)