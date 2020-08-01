class Solution:
    def minInteger(self, num: str, k: int) -> str:
        ind = [[] for _ in range(10)]
        for i in range(len(num)-1, -1, -1):
            ind[int(num[i])].append(i)
        i = 0
        res = []
        picked = []
        moveright = {}
        for i in range(len(num) - 1):
            for _ in range(10):
                if ind[_]:
                    if _  not in moveright:
                        moveright[_] = len(picked) - bisect.bisect(picked, ind[_][-1])
                    if ind[_][-1] + moveright[_] - i <= k:
                        k -= ind[_][-1] + moveright[_] - i
                        insort(picked, ind[_][-1])
                        res.append(str(_))
                        ind[_].pop()
                        moveright.pop(_)
                        break
            if k == 0:
                break
        unpicked = []
        pickedset = set(picked)
        for i in range(len(num)):
            if i not in pickedset:
                unpicked.append(i)
        return "".join(res) + "".join([num[j] for j in unpicked])