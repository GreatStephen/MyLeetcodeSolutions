class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # 2 pointers. 用list记录count比较慢
        ans, count, i, j =  [], [], 0, 0
        for j in range(len(s)):
            if i==0:
                count.insert(i, 1)
                ans.insert(i, s[j])
                i += 1
                continue
            if s[j] == ans[i-1]:
                if count[i-1]==k-1:
                    i = i-k+1
                else:
                    count.insert(i, count[i-1]+1)
                    ans.insert(i, s[j])
                    i += 1
            else:
                count.insert(i, 1)
                ans.insert(i, s[j])
                i += 1
        return ''.join(ans[:i])