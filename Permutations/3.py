class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for n in nums:
            if not ans:
                ans.append([n])
                continue
            N = len(ans)
            for i in range(N):
                temp = ans.pop(0)
                for pos in range(len(temp)+1):
                    ans.append(temp[:pos]+[n]+temp[pos:])
        return ans
            