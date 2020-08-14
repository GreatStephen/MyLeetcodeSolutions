class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        # 思路是对nums里任意两个数字，做所有可能的组合，然后用这个新数和剩下的数字组成新nums，参与递归
        # 遍历所有可能，如果找到24，就返回True。所有可能都不是24，就False
        def tempres(a,b):
            ans = [a+b, a-b, b-a, a*b]
            if b: ans.append(a/b)
            if a: ans.append(b/a)
            return ans
        
        def helper(nums):
            if len(nums)==1:
                return math.isclose(nums[0], 24)
            for i in range(len(nums)-1):
                for j in range(i+1, len(nums)):
                    for r in tempres(nums[i],nums[j]):
                        if helper([r]+nums[:i]+nums[i+1:j]+nums[j+1:]):
                            return True
            return False
        
        
        return helper(nums)