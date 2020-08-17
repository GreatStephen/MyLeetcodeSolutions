class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        # 这题没啥好说的，就按题目描述做
        A = zip(indexes, sources, targets)
        A.sort()
        idx, ans = 0, ''
        
        def check(idx, s):
            i,j = idx, 0
            while i<len(S) and j<len(s):
                if S[i]==s[j]:
                    i += 1
                    j += 1
                else:
                    return False
            return True  
        
        while idx<len(S):
            if not A:
                ans += S[idx:]
                break
            if idx<A[0][0]:
                ans += S[idx]
            elif idx==A[0][0]:
                if check(idx, A[0][1]):
                    ans += A[0][2]
                    idx += len(A[0][1])
                    idx -= 1                    
                else:
                    ans += S[idx]
                A.pop(0)
            idx += 1
        
        
        return ans