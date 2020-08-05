class Solution:
    def calculate(self, F: str) -> int:
        # 坑比较多
        stack = deque()
        res = 0
        sign = None
        number = 0
        s = {'+':operator.add, '-':operator.sub}
        
        for c in F:
            if c==' ': continue
                
            elif c=='(':
                stack.append(res)
                stack.append(sign) # 存上一次的结果和运算符
                res = 0 # 注意压栈之后清零
                sign = None
            
            elif c==')':
                if sign: # 如果括号内出现了运算，就计算出来
                    res = sign(res, number)
                else: # 括号里可能没有运算，只是一个单独的数字，那就不需要晕眩
                    if number and not res: # 注意res=0时，才把number拿出来，因为res可能因为其他运算而不等于0，比如嵌套括号，里层括号计算出了res，但对于外层括号而言，相当于只有一个数字，这时候是不更新res的
                        res = number
                sign = stack.pop() # 取之前的结果和运算符
                last = stack.pop()
                if sign: 
                    res = sign(last, res) # 注意运算顺序，前面的结果+/-现在的结果
                    number = 0 # 运算之后，number和sign都要清零
                sign = None
                
            elif c in ('+','-'):
                if sign: # 如果前面还有运算，现在这个符号不是第一个运算符，就先把前面的运算算出来
                    res = sign(res, number)
                    number = 0
                    sign = None
                else: # 当前运算符可能是第一个运算符
                    if not res: # 如果res不=0，就把nubmer直接赋给res
                        res = number
                    number = 0 # 注意number清零
                sign = s[c] # 更新当前的sign
            
            
            else:
                # numbers
                number = 10*number+int(c) # number是当前遇到的数字
        
        if sign: # 结束的时候还有一次运算没算完
            res = sign(res, number)
            number = 0
        if number and not res: # 结束时虽然没有运算符，但整个式子只是一个单独的数字，所以把这个数字赋给res
            res = number
        
        return res