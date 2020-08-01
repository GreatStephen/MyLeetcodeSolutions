class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # backtracking，分支比较多，但逻辑不复杂
        # 注意点：选择*时，要用current value减去之前的乘法结果，再加上新的乘法结果，避免重复
        # 注意点：当第一个数字为0时，不能扩展了，以0开头的数字只有0自身
        ans = []
        def helper(path, curval, pos, mulval):
            if pos==len(num) and target==curval: # exit condition
                ans.append(path[1:])
                return 
            cur = 0
            for i in range(pos, len(num)):
                cur = int(num[pos:i+1])
                # plus
                helper(path+'+'+str(cur), curval+cur, i+1, cur)
                if pos>0: # first number must be positive
                    # subtract
                    helper(path+'-'+str(cur), curval-cur, i+1, -1*cur)                    
                    # multiply
                    helper(path+'*'+str(cur), curval-mulval+mulval*cur, i+1, mulval*cur)
                if i==pos and cur==0: # if see leading 0, just stop 
                    break        
        helper('', 0, 0, 0)
        return ans