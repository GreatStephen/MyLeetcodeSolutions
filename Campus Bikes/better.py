class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # bucket sort，只有2000个长度。因为i，j是从小到大遍历的，所以对于每个arr[i]，里面的元素自然是按i递增j递增排好序，只需要从前到后遍历即可
        arr = [None for i in range(2001)]       
       
        for i,w in enumerate(workers):
            for j,b in enumerate(bikes):
                dis = abs(w[0]-b[0])+abs(w[1]-b[1])
                if not arr[dis]:
                    arr[dis] = []
                arr[dis].append([i,j])
        
        
        ans = [-1]*len(workers)
        seenb = set()        
        for i in range(2001):
            if not arr[i]: continue
            for w,b in arr[i]:
                if b in seenb or ans[w]!=-1:
                    continue
                ans[w] = b
                seenb.add(b)
        
        return ans