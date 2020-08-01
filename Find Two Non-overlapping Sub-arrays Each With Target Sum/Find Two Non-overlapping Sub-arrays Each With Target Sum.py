class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # b[] 累计到i为止出现的最短等于t的子串
        # 用累计和只差+dict的方法，i向后移动，当发现j结尾的子串等于cur-target时，b[j]存放着<=j的局部结果
        # 将i-j 和b[j]相加，得到一个局部结果。取最小的局部结果
        c, b, d = [], [], {0:-1}
        MAX = 10**9
        ans = MAX
        for i,v in enumerate(arr):
            c.append(arr[i] if i==0 else arr[i]+c[-1])
            temp_b = MAX
            t = c[-1]-target
            if t not in d:
                d[c[-1]] = i
            else:
                ans = min(ans, (b[d[t]] if d[t]>=0 else MAX) + (i-d[t]))
                temp_b = min(temp_b, i-d[t])
                d[c[-1]] = i
            b.append(min((b[-1] if b else MAX), temp_b))
        return ans if ans<MAX else -1
                                  