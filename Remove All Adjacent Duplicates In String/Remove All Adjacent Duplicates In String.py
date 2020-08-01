class Solution:
    def removeDuplicates(self, S: str) -> str:
        # 2 pointers algorithm，python的string不能修改原始值，只能开新list，所以速度慢一些
        i = j = 0
        ans = []
        for j in range(len(S)):
            if i>0 and ans[i-1]==S[j]:
                i -= 1
            else:
                ans.insert(i, S[j])
                i += 1
        return ''.join(ans[:i])