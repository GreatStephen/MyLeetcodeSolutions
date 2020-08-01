class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        d_s = set(deadends)
        seen = set()
        deq = collections.deque()
        deq.append('0000')
        ans = 0
        while len(deq)>0:
            length = len(deq)
            for _ in range(length):
                cur = deq.popleft()
                if cur in d_s: continue
                if cur==target: return ans
                next_step = self.getNextStep(target, cur)
                for n_s in next_step:
                    if n_s not in d_s and n_s not in seen:
                        deq.append(n_s)
                        seen.add(n_s)

            ans += 1
        return -1

    def getNextStep(self, target, cur):
        ans = []
        for i in range(4):
            less_num = str(int(cur[i])-1) if cur[i]!='0' else '9'
            large_num = str((int(cur[i])+1)%10)
            next_str = cur[:i] + less_num +cur[i+1:]
            ans.append(next_str)
            next_str = cur[:i] + large_num +cur[i+1:]
            ans.append(next_str)
        return ans