class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=4: return 0
        nums.sort()
        d = collections.defaultdict(int)
        for i in range(1,len(nums)):
            d[(i-1,i)] = nums[i]-nums[i-1]
        d = sorted(d, key = lambda x: d[x])
        # print(d)
        
        ans = 10**10
        for i in range(len(d)):
            ld, rd = d[i][0], d[i][1]
            if ld-rd >= ans: break
            l, r = 0, len(nums)-1
            res = nums[r]-nums[l]
            for j in range(3):
                if l==ld and r==rd: return 0
                ldiff, rdiff = nums[ld]-nums[l], nums[r]-nums[rd]
                # print(ldiff, rdiff)
                if ldiff>=rdiff and l!=ld: l+=1
                elif rdiff>ldiff and r!=rd: r-=1
                res = nums[r]-nums[l]
            ans = min(ans, res)
            if ans==0: return 0
        
        return ans