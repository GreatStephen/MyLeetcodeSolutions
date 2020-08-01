class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.deq = collections.deque()
        self.deq.append((0,0))
        self.food_l = food
        self.food_idx = 0
        self.body_s = set([(0,0)])
        self.dir = {'U':[-1,0], 'L':[0,-1], 'R':[0,1], 'D':[1,0]}
        self.eats = 0
        self.width = width
        self.height = height
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        tail = self.deq[0]
        head = self.deq[-1]
        self.body_s.remove(tail)
        new_head = (head[0]+self.dir[direction][0], head[1]+self.dir[direction][1])
        if new_head in self.body_s:
            return -1   # collide with body
        if new_head[0]<0 or new_head[0]>=self.height or new_head[1]<0 or new_head[1]>=self.width:
            return -1   # out of bound            
        if self.food_idx<len(self.food_l) and new_head==tuple(self.food_l[self.food_idx]):
            self.food_idx+=1
            self.eats+=1
            self.deq.append(new_head)
            self.body_s.add(new_head)
            self.body_s.add(self.deq[0])
            return self.eats
        else:
            self.deq.append(new_head)
            self.body_s.add(new_head)
            self.deq.popleft()
            return self.eats
        return 0
            
            
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)