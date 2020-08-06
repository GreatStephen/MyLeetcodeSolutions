# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    
    def DFS(self, curdir, curpos, robot):
        robot.clean()
        self.visited.add(curpos)
        # robot.turnLeft()

        for i in range(curdir, curdir+4):
            d = i%4
            # robot.turnRight()
            newr, newc = curpos[0]+self.DIR[d][0], curpos[1]+self.DIR[d][1]
            if (newr, newc) not in self.visited:
                if robot.move():
                    self.DFS(d, (newr, newc),robot)
            robot.turnRight()

        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()
        
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.visited = set()
        self.DIR = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}        
        
        self.DFS(0, (0,0), robot)
        