class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # 两种情况，不重复时算kadane，重复时算prefix+suffix+max(sum,0)*(k-2)
        # 注意点，如果sum<0，那么上面的式子要对sum取0
        def kadane(arr):
            m, temp = 0, 0
            for v in arr:
                temp = max(temp+v, v)
                m = max(m, temp)
            return m
        
        val1 = max(kadane(arr), 0)%(10**9+7)
        
        def prefixsum(arr):
            m, temp = 0, 0
            for v in arr:
                temp+=v
                m = max(temp, m)
            return m
        def suffixsum(arr):
            m, temp = 0, 0
            for v in reversed(arr):
                temp+=v
                m = max(temp, m)
            return m
        val2 = max(prefixsum(arr)+suffixsum(arr)+max(sum(arr)*(k-2),0), 0)%(10**9+7)

        if k==1: return val1
        else: return max(val1, val2)
        