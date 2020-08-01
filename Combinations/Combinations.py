class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        
        def backtracking(nums, k):
            if k==0: return None
            ans = []
            for i in range(len(nums)-k+1):
                new_num = nums[i+1:]
                next_ans = backtracking(new_num, k-1)
                if not next_ans:
                    ans.append([nums[i]])
                    continue
                for na in next_ans:
                    ans.append([nums[i]]+na)
            return ans
        
        return backtracking(nums, k)