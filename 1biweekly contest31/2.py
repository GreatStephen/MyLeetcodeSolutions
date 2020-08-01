class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # cum = reduce(lambda x,y: x+y, arr)
        # 超时
        cum = []
        MOD = 10**9+7
        for i,v in enumerate(arr):
            if i==0: cum.append(arr[i])
            else: cum.append(arr[i]+cum[-1])
        # print(cum)
        
        ans = 0
        for i in range(len(cum)):
            for j in range(-1, i):
                if j<0:
                    if cum[i]&1: ans+=1
                else:
                    if (cum[i]-cum[j])&1: ans+=1
        
        
        return ans