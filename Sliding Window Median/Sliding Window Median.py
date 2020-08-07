class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxh, minh = [], []
        heapq.heapify(maxh)
        heapq.heapify(minh)
        
        def push(n):
            if not maxh:
                heapq.heappush(maxh, -1*n)
            else:
                if n<(-1*maxh[0]):
                    heapq.heappush(maxh, -1*n)
                    if len(maxh)-len(minh)>=2:
                        heapq.heappush(minh, -1*heapq.heappop(maxh))
                else:
                    heapq.heappush(minh, n)
                    if len(minh)>len(maxh):
                        heapq.heappush(maxh, -1*heapq.heappop(minh))
        
        ans = []
        for i,n in enumerate(nums):
            if i<k:
                push(n)                    
                if i==k-1:
                    median = -1*maxh[0] if k&1 else (minh[0]-maxh[0])/2
                    ans.append(median)
            
            else:
                left = i-k
                if nums[left]<=ans[-1]: # remove element from maxh
                    idx=0
                    while idx<len(maxh) and maxh[idx]!=(-1*nums[left]):
                        idx += 1
                    maxh[idx] = maxh[-1]
                    maxh.pop()
                    if len(minh)>len(maxh): # 注意，从maxh删除元素后，有可能导致minh>maxh，需要重新平衡
                        heapq.heappush(maxh, -1*heapq.heappop(minh))
                    heapq.heapify(maxh)                                      
                else: # remove element from minh
                    idx = 0
                    while idx<len(minh) and minh[idx]!=nums[left]:
                        idx += 1
                    minh[idx] = minh[-1]
                    minh.pop()
                    heapq.heapify(minh)
                
                push(n)
                median = -1*maxh[0] if k&1 else (minh[0]-maxh[0])/2
                ans.append(median)
        return ans
                    