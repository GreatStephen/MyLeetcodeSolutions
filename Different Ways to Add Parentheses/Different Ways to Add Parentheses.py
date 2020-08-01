class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        self.operators = {'+':operator.add,'-':operator.sub,'*':operator.mul}
        nums, ops = [], []
        while len(input)>0:
            done = True
            for i,c in enumerate(input):
                if c in self.operators:
                    nums.append(int(input[:i]))
                    ops.append(c)
                    input = input[i+1:]
                    done = False
                    break
            if done: 
                nums.append(int(input))
                input = ''
        
        def DC(nums, ops):
            if len(nums)==1: return [nums[0]]
            ans = []
            for i in range(len(ops)):
                l = DC(nums[:i+1], ops[:i])
                r = DC(nums[i+1:], ops[i+1:])
                for l_num in l:
                    for r_num in r:
                        ans.append(self.operators[ops[i]](l_num, r_num))
            return ans
        
        return DC(nums, ops)