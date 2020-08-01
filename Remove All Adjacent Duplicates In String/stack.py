class Solution:
    def removeDuplicates(self, S: str) -> str:
        # 甚至比2pointer还慢
        deq = collections.deque()
        for i,v in enumerate(S):
            if len(deq)>0 and deq[-1]==v: deq.pop()
            else: deq.append(v)
        return ''.join(deq)