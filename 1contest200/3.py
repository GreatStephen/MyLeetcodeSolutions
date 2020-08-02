class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)
        l = []
        seen = set()
        for i in range(N):
            count = 0
            row = grid[i]
            # print(row)
            for j in range(N-1, -1, -1):
                if row[j]==0: count+=1
                else: 
                    # print(count)
                    if count in seen: return -1
                    seen.add(count)
                    l.append(N-1-count)
                    break
        # print(l)
        
        ans = 0
        for i in range(N):
            if l[i]==i: continue
            for j in range(i+1, N):
                if l[j]==i:
                    t = l[i]
                    l[i] = l[j]
                    l[j] = t
                    ans += 1
        
        return 



class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)
        l = []
        # seen = set()
        for i in range(N):
            count = 0
            row = grid[i]
            # print(row)
            for j in range(N-1, -1, -1):
                if row[j]==0: count+=1
                else: 
                    # print(count)
                    # if count in seen: return -1
                    # seen.add(count)
                    l.append(count)
                    break
        print(l)
        
#         ans = 0
#         for i in range(N):
#             for j in range(i+1, N):
#                 if l[j]<l[i]: ans+=1
            
        
        return None