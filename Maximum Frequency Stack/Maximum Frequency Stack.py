class FreqStack:
    # 每个频率对应的数字queue，以及每个数字的最高freq，再记录当前的最高freq
    def __init__(self):
        self.xtof = {}
        self.ftox = {}
        self.maxf = 0

    def push(self, x: int) -> None:
        if x not in self.xtof:
            self.xtof[x] = 0
        self.xtof[x] += 1
        self.maxf = max(self.maxf, self.xtof[x])
        if self.xtof[x] not in self.ftox:
            self.ftox[self.xtof[x]] = []
        self.ftox[self.xtof[x]].append(x)
        # print(self.xtof, self.ftox)

    def pop(self) -> int:
        ans = self.ftox[self.maxf].pop()
        if len(self.ftox[self.maxf])==0:
            self.maxf -= 1
        self.xtof[ans] -= 1
        # print(self.xtof, self.ftox)
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()