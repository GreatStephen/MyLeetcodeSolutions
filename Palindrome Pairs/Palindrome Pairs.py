class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {}
        for i,w in enumerate(words):
            d[w] = i # 每个串和它的下标
        
        def isPalindrome(w):
            return w==w[::-1]
        
        ans = []
        for idx,w in enumerate(words):
            for i in range(len(w)+1):
                # 对每一个word，检查它的所有分割，包括空字符串，word=prefix+suffix
                prefix = w[:i]
                suffix = w[i:]
                
                # 如果prefix是回文，检查suffix的逆串是否存在，如果存在，这是一个结果
                if isPalindrome(prefix):
                    candidate = suffix[::-1]
                    if candidate!=w and candidate in d: # 逆串不能等于w自己，因为要prefix=''是要检查的，所以这种错误可能出现
                        ans.append([d[candidate], idx])
                
                # 如果suffix是回文，同样的过程
                # 需要注意的是，prefix=''和suffix=''只能检查一个，如果两个都检查，回产生重复结果
                if len(suffix)>0 and isPalindrome(suffix):
                    candidate = prefix[::-1]
                    if candidate!=w and candidate in d:
                        ans.append([idx, d[candidate]])
        
        return ans