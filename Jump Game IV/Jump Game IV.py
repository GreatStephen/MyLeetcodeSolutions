class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # 这题是一个简单的BFS

        d = defaultdict(set)
        for i,a in enumerate(arr):
            d[a].add(i)
        seen = [0]*len(arr)
        deq = deque()
        deq.append((0,0)) # (idx, steps)
        seen[0] = 1
        
        while deq:
            idx, steps = deq.popleft()
            if idx==len(arr)-1:
                return steps
            if idx-1>=0 and not seen[idx-1]:
                deq.append((idx-1, steps+1))
                seen[idx-1] = 1
            if idx+1<len(arr) and not seen[idx+1]:
                deq.append((idx+1, steps+1))
                seen[idx+1] = 1
            for nextidx in d[arr[idx]]:
                if not seen[nextidx]:
                    deq.append((nextidx, steps+1))
                    seen[nextidx] = 1
            d[arr[idx]] = set() # 这一步太重要了，遍历过的num从dict里删除，否则后面的元素还会再遍历一遍这个set
            # 简单的一行代码，节约了大量时间. 比如TC = [7,7,7,7,7,...,7]五万个7，没这行绝对超时！
        
        return -1