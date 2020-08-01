class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        self.d = collections.defaultdict(list)
        self.idx = 0
        self.loop = False
        self.cycle = 0
        while N>0:
            cells = self.nextDay(cells)
            N -=1
            if self.loop:
                N %= self.cycle
                break
        while N>0:
            cells = self.nextDay(cells)
            N -= 1
            
        return cells
    
    def nextDay(self, cells):
        nd = [0]*8
        for i in range(1,7):
            nd[i] = 1 if (cells[i-1]==cells[i+1]) else 0
        if not self.loop and tuple(nd) in self.d:
            self.loop = True
            self.cycle = self.idx - self.d[tuple(nd)]           
        elif not self.loop and tuple(nd) not in self.d:
            self.d[tuple(nd)] = self.idx
            self.idx+=1
        return nd