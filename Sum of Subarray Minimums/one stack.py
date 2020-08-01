class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        # 只需要一个Stack，就能找到左右山峰
        # stack[i-1]是stac[i]左手边的第一个更小数字的下标
        # 当前数字大于stack[-1]，压栈。当前数字小于stack[-1]，则左山峰下标是stack[-2]，右山峰下标是当前i
        deq = collections.deque()
        A = [0] + A + [0]
        ans, MOD = 0, 10**9+7
        for i,n in enumerate(A):
            if len(deq)==0:
                deq.append(i)
                continue
            while A[deq[-1]] > n:
                t = deq.pop()
                ans += A[t]*(t-deq[-1])*(i-t)
            deq.append(i)
        return ans%MOD