class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        l = len(nums)+1
        self.d = [[-1]*l for _ in range(l)]
        def ways(x,y): # 用DP计算两个list交织有多少种结果
            if not x or not y:
                return 1
            if self.d[x][y]!=-1:
                return self.d[x][y]
            ans = ways(x-1, y) # 第一个list的第一个元素作为第一个
            ans += ways(x, y-1) # 第二个list的第一个元素作为第一个
            self.d[x][y] = ans
            return ans
            
        def helper(nums):
            if not nums:
                return 1
            smaller, larger = [], []
            MOD = 10**9+7
            ans = 0
            # 把小于head和大于head的所有数字，按顺序拿出来，放进两个list
            for i in range(1, len(nums)):
                if nums[i]>nums[0]:
                    larger.append(nums[i])
                else:
                    smaller.append(nums[i])
            if not smaller: # 如果一个list为空，那么答案就是另一个list
                return helper(larger)
            if not larger:
                return helper(smaller)
            num1, num2 = helper(smaller), helper(larger) # 两个list分别递归，得到子结果

            len1, len2 = max(len(smaller), len(larger)), min(len(smaller), len(larger))
            temp = ways(len1, len2) # 然后计算小list和大list互相交叉，有多少种结果
            
            return (temp*num1*num2)%MOD # 最终结果是当前结果*左结果*右结果
        
        return int(helper(nums)-1) # 减去自己，因为自己占了一个结果，所以减1
            
            