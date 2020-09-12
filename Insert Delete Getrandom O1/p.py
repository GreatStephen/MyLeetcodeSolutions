class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [] # 记录现有的数组
        self.idx = {} # 记录每个数和它的下标
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.idx: return False
        self.idx[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.idx: return False
        pos = self.idx[val] # 找出它的下标
        if pos==len(self.arr)-1: # 如果这个数字是arr的最后一个，直接删除即可
            self.idx.pop(self.arr[pos])
            self.arr.pop()
        else: # 如果这个数位于arr中间，把它的数字改成arr的最后一个数，然后删掉最后一个数。再把这个位置的新数的下标改成pos。
            # 实际上就是把数字换到末尾再删除。           
            self.arr[pos] = self.arr[-1]
            self.arr.pop()
            self.idx.pop(val)
            self.idx[self.arr[pos]] = pos # 记得把曾经的最后一个数的下标改成pos
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        pos = random.randint(0,len(self.arr)-1)
        return self.arr[pos]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()