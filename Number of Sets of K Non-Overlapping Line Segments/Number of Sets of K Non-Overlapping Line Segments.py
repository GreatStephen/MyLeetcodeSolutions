class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # 这题太巧妙了，先在n个点中增加k-1个点，让线段收尾不相连
        # 然后在n+k-1中取k个线段，怎么取呢？取2k个端点即可。
        # 因为收尾不相连，所以2k个端点刚好uniquely define k个线段
        # 整个代码变成C(n+k-1, 2k)
        return ((math.factorial(n+k-1)//(math.factorial(n-1-k)*math.factorial(2*k))))%(10**9+7)