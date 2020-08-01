class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans, i2, i3, i5 = [1], 0, 0, 0
        while len(ans)<n:
            target = min(ans[i2]*2, ans[i3]*3, ans[i5]*5)
            if target==ans[i2]*2: i2+=1
            if target==ans[i3]*3: i3+=1
            if target==ans[i5]*5: i5+=1
            ans.append(target)
        return ans[-1]