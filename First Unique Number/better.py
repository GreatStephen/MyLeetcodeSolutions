class FirstUnique:
    # 自己创建双向链表，用一个dict存储value:节点，以便任何一个value可以马上找到对应的节点
    # 必须自己建class，否则dict里没法存东西。如果用list之类的存，value放下标，这个下标会随着list删除东西而变化。只有自建节点的引用是亘古不变的。
    class DoublyLinkedList:
        def __init__(self, value, pre=None, nex=None):
            self.value = value
            self.pre = pre
            self.nex = nex

    def __init__(self, nums: List[int]):
        self.seen = set()
        self.d = {}
        self.dummy = self.DoublyLinkedList(0) # dummy head
        self.tail = self.dummy
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        return self.dummy.nex.value if self.dummy.nex else -1

    def add(self, value: int) -> None:
        if value in self.seen:
            return
        else:
            if value in self.d: # appear once
                node = self.d[value]
                if not node.nex:
                    self.tail = self.tail.pre
                node.pre.nex = node.nex
                if node.nex: node.nex.pre = node.pre
                self.d.pop(value, None)
                self.seen.add(value)
            
            else: # never appeared
                self.tail.nex = self.DoublyLinkedList(value, self.tail, None)
                self.tail = self.tail.nex
                self.d[value] = self.tail


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)