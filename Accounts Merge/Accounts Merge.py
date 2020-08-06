class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        etog = {} # email对应的group
        groups = {} # 每个group包括的email
        for i in range(len(accounts)):
            name = accounts[i][0]
            emails = accounts[i][1:]
            groups[i] = []
            for e in emails:
                if e not in etog:
                    etog[e] = i
                    groups[i].append(e)
                else:
                    # union last group with this group
                    lastg = etog[e]
                    if lastg==i: continue
                    for laste in groups[lastg]: # 做两件事，把前一个group所有的email对应的group全部换成现在的。然后把他们全部加进现在的group。
                        etog[laste] = i
                        groups[i].append(laste)
                    groups.pop(lastg)
        
#         print(etog)
#         print(groups)
        
        ans = []
        for idx,s in groups.items():
            temp = []
            temp.append(accounts[idx][0]) # name
            s.sort()
            temp += s # sort the emails
            ans.append(temp)
        return ans
        