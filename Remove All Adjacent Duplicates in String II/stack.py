class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # 用deque好了很多
        ans, count, i, j =  collections.deque(), collections.deque(), 0, 0
        for j in range(len(s)):
            if len(ans)==0:
                count.append(1)
                ans.append(s[j])
                continue
            if s[j] == ans[-1]:
                if count[i-1]==k-1:
                    for _ in range(k-1):
                        count.pop()
                        ans.pop()
                else:
                    count.append(count[-1]+1)
                    ans.append(s[j])
            else:
                count.append(1)
                ans.append(s[j])
        return ''.join(ans)