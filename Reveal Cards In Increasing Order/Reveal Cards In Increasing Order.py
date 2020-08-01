class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deq = collections.deque()
        for n in sorted(deck)[::-1]:
            deq.rotate()
            deq.appendleft(n)
        return deq