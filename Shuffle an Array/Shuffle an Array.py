class Solution:

    def __init__(self, nums: List[int]):
        self.save = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.save
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        if len(self.save)==0: return []
        ans, idx_l = [], [i for i in range(len(self.save))]
        for i in range(len(self.save)):
            ind = random.choice(idx_l)
            ans.append(self.save[ind])
            idx_l.remove(ind)        
        
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()