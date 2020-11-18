class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        a = []
        heapq.heapify(a)
        for n in nums:
            heapq.heappush(a, -n)
        
        n_freq = {}
        for start, end in requests:
            for i in range(start, end+1):
                if i not in n_freq:
                    n_freq[i] = 0
                n_freq[i]+= 1
        
        freq_n = {}
        for n,freq in n_freq.items():
            if freq not in freq_n:
                freq_n[freq] = 0
            freq_n[freq] += 1
        # print(freq_n)
        
        ans = 0
        for freq in sorted(freq_n.keys(), key=lambda x:-x):
            # print(freq)
            for i in range(freq_n[freq]):
                num = heapq.heappop(a)*-1
                ans += num*freq
        
        return ans%(10**9+7)