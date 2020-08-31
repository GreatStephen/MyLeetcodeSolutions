class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # Lee的方法，很巧妙。这道题存在负数，所以cum不一定递增，有可能后面的cum反而更小
        # 但是！如果cum[i]<cum[i-1]，那么cum[i-1]就没有存在的必要了，因为cum[i]一定能使i后面的cum最大并且长度最短
        # 所以这道题碰到cum[i]<cum[i-1]，可以直接删掉cum[i-1]. 用一个deque保存递增的cum作为窗口即可
        # 检查deque的第一个元素，用两个cum相减，如果大于k就更新ans，并弹出第一个元素。重复直到<k
        # 把当前cum压栈时，弹出栈顶所有>=cum的元素，因为我想保持deque的最小递增
        d = deque()
        ans,summ = float('inf'), 0
        d.append([-1,0])
        for i,a in enumerate(A):
            summ += a
            while d and summ-d[0][1]>=K:
                ans = min(ans, i-d[0][0])
                d.popleft()
            while d and d[-1][1]>=summ:
                d.pop()
            d.append([i,summ])
        
        return ans if ans<float('inf') else -1
            