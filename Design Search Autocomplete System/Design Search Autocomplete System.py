class AutocompleteSystem:
    
    def addTrie(self, s, t, node):
        for c in s:
            if c not in node:
                node[c] = {}
            node = node[c]
            if '#' not in node:
                node['#'] = {}
            if s not in node['#']:
                node['#'][s] = 0
            node['#'][s] += t

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = {}
        self.cur = ''        
        for s,t in zip(sentences, times):
            self.addTrie(s, t, self.root)

    def input(self, c: str) -> List[str]:
        if c=='#':
            word = self.cur
            self.cur = ''
            self.addTrie(word, 1, self.root)
            return []
        self.cur += c
        node = self.root
        for c in self.cur:
            if c not in node: return []
            node = node[c]
        
        # 用priority queue来选3个最hot的
        h = []
        heapq.heapify(h)
        for s,t in node['#'].items():
            heapq.heappush(h, (-t, s))
        
        ans = []
        for i in range(3):
            if h:
                ans.append(heapq.heappop(h)[1])
            else: break
        
        return ans
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)