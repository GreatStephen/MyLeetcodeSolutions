class Solution:
    def minInsertions(self, s: str) -> int:
        
        stack = deque()
        ans = 0
        
        idx = 0
        while idx<len(s):
            c1 = s[idx]
            if c1=='(':
                stack.append('(')
                idx += 1
            else:
                idx += 1
                c2 = s[idx] if idx<len(s) else '#'
                lastc = stack.pop() if stack else '#'
                if lastc=='#':
                    ans += 1
                if c2!=')':
                    ans += 1
                else:
                    idx += 1
        
        ans += len(stack)*2
        
        return ans