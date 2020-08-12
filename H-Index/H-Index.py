class Solution:
    def hIndex(self, citations: List[int]) -> int:
        b = [0]*(len(citations)+1)
        for n in citations:
            b[min(n,len(citations))]+=1
        
        s = 0
        for i in range(len(citations), -1, -1):
            s += b[i]
            # 目前为止总共有s篇引用次数>=i。s中只要有i篇>=i，i就是答案
            if s>=i:
                return i        
        return 0