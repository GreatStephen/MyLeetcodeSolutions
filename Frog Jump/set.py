class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # 普通的用set的方法
        d = defaultdict(set)
        d[stones[0]].add(1)
        # stone_index = defaultdict(int)
        # for i,s in enumerate(stones):
        #     stone_index[s] = i
        stones_set = set(stones)
        
        for i,s in enumerate(stones):
            steps = d[s]
            for step in steps:
                if s+step in stones:
                    if s+step==stones[-1]: return True
                    if step-1>0: d[s+step].add(step-1)
                    d[s+step].add(step)
                    d[s+step].add(step+1)
        
        return False