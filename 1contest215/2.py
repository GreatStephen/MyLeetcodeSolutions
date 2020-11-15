class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        def helper(word):
            c_freq, freq_c = {}, {}
            for c in word:
                if c not in c_freq:
                    c_freq[c] = 1
                    if 1 not in freq_c:
                        freq_c[1] = set()
                    freq_c[1].add(c)
                else:
                    freq = c_freq[c]+1
                    c_freq[c] += 1
                    freq_c[freq-1].remove(c)
                    if not freq_c[freq-1]:
                        freq_c.pop(freq-1)
                    if freq not in freq_c:
                        freq_c[freq] = set()
                    freq_c[freq].add(c)
            return [c_freq, freq_c]
        
        c_freq1, freq_c1 = helper(word1)
        c_freq2, freq_c2 = helper(word2)
        
        if len(c_freq1.keys())!=len(c_freq2.keys()):
            return False
        for k in c_freq1.keys():
            if k not in c_freq2:
                return False
        
        for f in freq_c1.keys():
            if f not in freq_c2:
                return False
            if len(freq_c1[f])!=len(freq_c2[f]):
                return False
        
        return True
        
        
        
        