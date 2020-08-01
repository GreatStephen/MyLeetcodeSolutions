class StreamChecker:
    # 学习一下python怎么写trie，还是很简单的
    def __init__(self, words: List[str]):
        self.trie = dict()
        self.waitlist = []
        for word in words:
            node = self.trie
            for c in word:
                node = node.setdefault(c, dict())
            node[1] = 1

    def query(self, c: str) -> bool:
        wl = []
        ans = False
        if c in self.trie:
            wl.append(self.trie[c])
            if 1 in self.trie[c]: ans = True
        for item in self.waitlist:
            if c in item:
                new_item = item[c]
                if 1 in new_item: ans = True
                wl.append(new_item)
        self.waitlist = wl
        return ans


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)