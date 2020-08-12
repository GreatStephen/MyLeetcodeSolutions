class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = deque()
        
        # 直接模拟stack操作
        # 还可以把pushed直接当做stack，用i指向栈顶。压栈时将stack[i]修改为x。这样做会改变原数组。
        idx = 0
        for n in pushed:
            stack.append(n)
            while stack and idx<len(popped) and stack[-1]==popped[idx]:
                stack.pop()
                idx += 1
        
        if len(stack)==0 and idx==len(popped): return True
        return False