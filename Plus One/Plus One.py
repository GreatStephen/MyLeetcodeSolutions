class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # transform the str to int, add 1, transform back to int
        return [int(d) for d in str(int(''.join(str(i) for i in digits))+1)]