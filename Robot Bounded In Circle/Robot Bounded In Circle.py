class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 数学题。运行一个seq之后，如果待在原地或者改变了方向，那么最终一定会回到起点形成circle，需要1或3个循环即可
        x,y = 0,0
        dirs = [[0,1],[-1,0],[0,-1],[1,0]]
        curdir = 0
        for ins in instructions:
            if ins=='G':
                x,y = x+dirs[curdir][0], y+dirs[curdir][1]
            elif ins=='L':
                curdir = (curdir+1)%4
            elif ins=='R':
                curdir = (curdir+3)%4
        
        if (x,y)==(0,0) or curdir!=0:
            return True
        return False