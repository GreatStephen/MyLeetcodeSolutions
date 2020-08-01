class MyCalendar:

    def __init__(self):
        self.start, self.end = [], []

    def book(self, start: int, end: int) -> bool:
        if len(self.start)==0:
            self.start.append(start)
            self.end.append(end)
            return True
        pos = bisect.bisect(self.start, start)
        if pos==0:
            if end<=self.start[0]:
                self.start.insert(0, start)
                self.end.insert(0, end)
                return True
            else: return False
        elif pos==len(self.start):
            if self.end[-1]<=start:
                self.start.append(start)
                self.end.append(end)
                return True
            else: return False
        else:
            if self.end[pos-1]<=start and end<=self.start[pos]:
                self.start.insert(pos, start)
                self.end.insert(pos, end)
                return True
            else: return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)