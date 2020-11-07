class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_num, num_freq = {}, {}
        for n in nums:
            if n not in num_freq:
                num_freq[n] = 1
                if 1 not in freq_num:
                    freq_num[1] = set()
                freq_num[1].add(n)
            else:
                freq = num_freq[n]
                num_freq[n] += 1
                freq_num[freq].remove(n)
                if freq+1 not in freq_num:
                    freq_num[freq+1] = set()
                freq_num[freq+1].add(n)
        
        # print(freq_num, num_freq)
        ans = []
        keys = freq_num.keys()
        keys = sorted(keys)
        for k in keys:
            nums = sorted(list(freq_num[k]), key=lambda x: -x)
            for n in nums:
                ans+=([n]*k)
        return ans