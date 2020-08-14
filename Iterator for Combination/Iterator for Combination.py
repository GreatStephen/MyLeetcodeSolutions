class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.ans = []
        self.idx = 0
        
        # 用递归的方法做combinations还不错，递归深度=目标字符串长度。
        # 从当前idx开始，填加一个idx之后的元素，然后从这个元素的后一个位置递归
        def coms(s, cur, k):
            if len(cur)==k:
                self.ans.append(str(cur))
                return
            for i in range(s, len(characters)):
                if len(characters)-i<k-len(cur):
                    break
                coms(i+1, cur+characters[i], k)
        
        coms(0, '', combinationLength)
            

    def next(self) -> str:
        a = self.ans[self.idx]
        self.idx += 1
        return a
    

    def hasNext(self) -> bool:
        return self.idx!=len(self.ans)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()