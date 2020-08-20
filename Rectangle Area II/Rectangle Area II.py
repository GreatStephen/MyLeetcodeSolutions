class Solution(object):
    def rectangleArea(self, rectangles):
        ans, MOD = 0, 10**9+7
        
        # 这题的思路是逐行扫描，看cur_y这一行有多少个x是标记为正的
        pq, x = [], []
        heapq.heapify(pq)
        for r in rectangles:
            x.append(r[0])
            x.append(r[2])
            heapq.heappush(pq, (r[1], r[0], r[2], 1)) # 1说明这是矩形的底边
            heapq.heappush(pq, (r[3], r[0], r[2], -1)) # -1说明这是矩形的顶边
        
        # 这里是一个节省空间的方法。把所有x的count记录下来，而不是把整个横坐标扒下来
        # 同时要记录每个x对应的下标，下标之差就是矩形的宽度
        x.sort()
        x_i = {v:i for i,v in enumerate(x)}
        count = [0]*len(x)
        
        last_y = -1
        while pq:
            cur_y, x1, x2, flag = heapq.heappop(pq)
            if last_y>=0 and cur_y>last_y:
                l = r = -1
                for i in xrange(len(x)):
                    if count[i]>0:
                        if l<0: l = i
                        r = i
                    elif l>=0: # 遇到count=0说明一个底边结束了
                        ans += (x[i]-x[l])*(cur_y-last_y)
                        ans %= MOD
                        l = -1
                if l>=0:
                    ans += (x[r]-x[l])*(cur_y-last_y)
                    ans %= MOD
                            
            # 这里很巧妙，不把矩形宽度[i:j]的j也加1，不加1相当于标记了宽度的结束位置
            # 如果把j也置1，会导致两个底边并排时被当做一个整体，无法分开
            for i in xrange(x_i[x1], x_i[x2]):
                count[i] += flag
            last_y = cur_y
        
        return ans