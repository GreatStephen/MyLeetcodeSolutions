class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        d = defaultdict(int)
        count = 0
        cur = None
        times = 0
        while True:
            if arr[0]>arr[1]:
                if arr[0] not in d: d[arr[0]] = 0
                if d[arr[0]]==k-1: return arr[0]
                d[arr[0]] += 1
                if d[arr[0]]>len(arr): return arr[0]
                d[arr[1]] = 0
                arr = [arr[0]]+arr[2:]+[arr[1]]
            else:
                if arr[1] not in d: d[arr[1]] = 0
                if d[arr[1]]==k-1: return arr[1]
                d[arr[1]] += 1
                if d[arr[1]]>len(arr): return arr[1]
                d[arr[0]] = 0
                arr = arr[1:]+[arr[0]]
            count += 1
            if count==len(arr): return arr[0]


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        d = defaultdict(int)
        count = 0
        cur = None
        times = 0
        while True:
            if arr[0]>arr[1]:
                if arr[0]==cur: times+=1
                else:
                    cur = arr[0]
                    times = 1
                arr = [arr[0]]+arr[2:]+[arr[1]]
            else:
                if arr[1]==cur:
                    times+=1
                else:
                    cur = arr[1]
                    times = 1
                arr = arr[1:]+[arr[0]]
                
            if times==k: return cur
            
            count += 1
            if count==len(arr): return arr[0]