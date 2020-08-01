class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for n in nums:
            if len(ans)==0: 
                ans.append([n])
                continue
            N = len(ans)
            for i in range(N):
                l = ans.pop(0)
                for j in range(len(l)+1):
                    new_l = list(l)
                    new_l.insert(j,n)
                    ans.append(new_l)
                    if j<len(l) and n==l[j]: break  # 遇到和自己相同的就停止，这是剔除重复元素的关键
        return ans
