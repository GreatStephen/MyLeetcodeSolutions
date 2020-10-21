class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        Maxq, ansi, ansj = 0, 0, 0
        # 这题坑啊，返回的点不一定是tower，可能是坐标系中任何一个点
        # 曼哈顿距离和欧氏距离不要搞混

        for x in range(51):
            for y in range(51):
                q = 0
                for tx, ty, tq in towers:
                    dis = math.sqrt((x-tx)**2+(y-ty)**2)
                    if dis>radius:
                        continue
                    q += tq//(1+dis)
                if q>Maxq:
                    ansi = x
                    ansj = y
                    Maxq = q
        
        return [ansi, ansj]