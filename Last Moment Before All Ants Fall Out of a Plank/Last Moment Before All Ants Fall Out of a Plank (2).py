class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left.sort()
        right.sort()
        if len(left)==0: return right[-1]
        if len(right)==0: return n-left[1]
        if right[0]<left[-1]: return left[-1]-right[0]+right
        else: return max(right[-1], n-left[1])