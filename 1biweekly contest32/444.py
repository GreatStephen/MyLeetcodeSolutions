class Solution:
    def longestAwesome(self, s: str) -> int:
        ans = 1
        
        dp = []
        for i,c in enumerate(s):
            if 1==0:
                res = [1,c]
                dp.append(res)
                continue
            else:
                # lastres = dp[-1]
                res = [1,c]
                idx = i-1
                while idx>=0:
                    lastres = dp[idx]
                    if lastres[0]&1==0:
                        res[0]+=lastres[0]
                        idx-=lastres[0]
                    else:
                        if res[0]&1==0:
                            res[0]+=lastres[0]
                            res[1] = lastres[1]
                            idx -= lastres[0]
                            continue
                        if lastres[1]==c:
                            res[0]+=lastres[0]
                            res[1] = None
                            idx -= lastres[0]
                        else:
                            break
        
        return ans            
                    