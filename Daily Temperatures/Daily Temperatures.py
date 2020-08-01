class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        deq = collections.deque()
        ans = [0]*len(T)
        for i,v in enumerate(T):
            while len(deq)>0 and T[deq[-1]]<v:
                ans[deq[-1]] = i-deq[-1]
                deq.pop()
            deq.append(i)
        return ans