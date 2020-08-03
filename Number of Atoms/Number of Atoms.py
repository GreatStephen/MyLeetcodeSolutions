class Solution:
    def countOfAtoms(self, F: str) -> str:
        # 经典stack题。当需要层级计算+跨层计算时，stack是好方法
        # 这题把(之前的dict放进stack，计算括号中的部分，再把栈顶dict和当前dict合并
        N = len(F)
        idx = 0
        stack = deque()
        d = {}
        NUMS = '0123456789'
        UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        LOWWER = 'abcdefghijklmnopqrstuvwxyz'
        
        def val(F, idx): # calcute the number after an element or ()
            idx += 1
            l,r = idx, -1
            while idx<N and F[idx] in NUMS:
                idx += 1
                r = idx
            count = int(F[l:r]) if r!=-1 else 1
            return idx, count
        
        while idx<N:
            if F[idx]=='(':
                stack.append(d)
                d = {}
                idx += 1
            
            elif F[idx]==')':
                temp = d
                d = stack.pop()
                
                # compute the number
                idx, count = val(F, idx)
                
                # add temp*count to d
                for k,v in temp.items():
                    if k not in d: d[k] = 0
                    d[k] += v*count
            
            else:
                # letters and numbers
                ele = ''
                if F[idx] in UPPER: 
                    ele+=F[idx]
                    idx += 1
                    while idx<N and F[idx] in LOWWER:
                        ele+=F[idx]
                        idx += 1
                
                # compute the number
                idx, count = val(F, idx-1)
                
                if ele not in d: d[ele] = 0
                d[ele] += count
        
        eles = sorted(d.keys())
        ans = ''
        for k in eles:
            ans += k
            if d[k]>1: ans += str(d[k])
        return ans
