class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        adj = {}
        for r in roads:
            if r[0] not in adj:
                adj[r[0]] = set()
            if r[1] not in adj:
                adj[r[1]] = set()
            adj[r[0]].add(r[1])
            adj[r[1]].add(r[0])
        
        # DP。记录当前的city的id，注意这里必须记录id而不是城市名，因为城市名可能重名。再记录path的遍历id。
        # 用DP保存当前城市和当前path的最小距离，以及路径path。
        # 取最小路径和其对应的路径，返回路径即可
        # 这个题要路径，有点麻烦，如果只要距离就简单多了
        dp = [[-1]*len(targetPath) for _ in range(n)]
        def DP(city_idx, path_idx):
            if dp[city_idx][path_idx]!=-1:
                return dp[city_idx][path_idx]
            if path_idx==len(targetPath)-1:
                if names[city_idx]==targetPath[path_idx]:
                    dp[city_idx][path_idx] = [0,[city_idx]]
                    return [0,[city_idx]] # [距离，路径list]
                else:
                    dp[city_idx][path_idx] = [1,[city_idx]]
                    return [1,[city_idx]]
            temp = 0 if names[city_idx]==targetPath[path_idx] else 1
            tempdis, temppath = float('inf'), []
            for nextcity in adj[city_idx]:
                dis, path = DP(nextcity, path_idx+1)
                if temp+dis<tempdis:
                    tempdis = temp+dis
                    temppath = [city_idx]+path
            dp[city_idx][path_idx] = [tempdis, temppath] # 拼接出最新的路径list
            return dp[city_idx][path_idx]
        
        ans = float('inf')
        path = [] # 这道题要路径
        for i in range(n):
            dis, p = DP(i,0)
            if dis<ans:
                ans = dis
                path = p
        return path