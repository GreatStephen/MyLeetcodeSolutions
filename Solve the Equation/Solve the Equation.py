class Solution:
    def solveEquation(self, equation: str) -> str:
        e = equation.split('=')
        digits = {'1','2','3','4','5','6','7','8','9','0'}
        coe = [0,0,0]
        cons = [0,0,0]
        
        for i in range(1,3):
            s = e[i-1]
            num = 0
            flag = 1
            numbered = False
            for c in s:
                if c=='+' or c=='-':                     
                    if num:
                        cons[i] += flag*num
                        num = 0
                        numbered = False
                    flag = 1 if c=='+' else -1                    
                elif c in digits:
                    num = num*10+int(c)
                    numbered = True
                elif c=='x':
                    if not numbered: num = 1
                    coe[i] += flag*num
                    num = 0
                    numbered = False
            if num: 
                cons[i] += flag*num
                
        coetotal = coe[1]-coe[2]
        constotal = cons[2]-cons[1]
        if coetotal==0: 
            if constotal: return "No solution"
            else: return "Infinite solutions"
        else: return "x="+str(int(constotal/coetotal))
                