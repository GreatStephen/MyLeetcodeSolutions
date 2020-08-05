class FirstUnique:

    def __init__(self, nums: List[int]):
        self.res = {}
        self.seen = set()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        return next(iter(self.res), -1)

    def add(self, value: int) -> None:
        if value in self.seen:
            self.res.pop(value, None)
            return
        else:
            self.res[value] = 1
            self.seen.add(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)