class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = None, None
        s,e = newInterval[0], newInterval[1]
        # 3个edge cases
        # intervals为空，新区间在所有老区间左边，新区间在所有老区间右边
        if len(intervals)==0: return [newInterval]
        if intervals[0][0]>e: return [newInterval]+intervals
        if intervals[-1][1]<s: return intervals+[newInterval]        
        
        # left是左侧最后一个不被覆盖的区间下标，right是右侧第一个不被覆盖的区间的下标
        for i,inter in enumerate(intervals):
            if inter[1]<s: left = i
            if inter[0]>e: right = i
            if right!=None: break
        
        newinterval = [None, None]
        newinterval[0] = min(s, intervals[(left if left!=None else -1)+1][0])
        newinterval[1] = max(e, intervals[(right if right!=None else len(intervals))-1][1])
        
        # 如果left, right都等于None，说明新区间整个包住所有老区间，一段式
        # 如果left等于None，说明新区间位于答案的头部，两段式
        # 如果right等于None，说明新区间位于答案的尾部，两段式
        # 如果两者都不等于None，说明答案是三段式，拼起来
        if left==None and right==None:
            return [newinterval]
        if left==None:
            return [newinterval]+intervals[right:]
        if right==None:
            return intervals[:left+1]+[newinterval]
        return intervals[:left+1]+[newinterval]+intervals[right:]