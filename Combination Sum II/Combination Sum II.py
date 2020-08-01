class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target==0: return [[]]
        def backtracking(can, target):
            ans = []
            for i in range(len(can)):
                if can[i]>target: break
                if i>0 and can[i]==can[i-1]: continue
                if can[i]==target:
                    ans.append([target])
                    break
                new_can = can[i+1:]
                next_ans = backtracking(new_can, target-can[i])
                if len(next_ans)>0:
                    for na in next_ans:
                        ans.append([can[i]]+na)            
            return ans
                
        candidates.sort()
        return backtracking(candidates, target)
