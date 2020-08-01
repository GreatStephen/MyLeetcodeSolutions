class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        l, r = 0, len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]>target:
                while l<r and numbers[r]==numbers[r-1]:
                    r-=1
                r-=1
            elif numbers[l]+numbers[r]<target:
                while l<r and numbers[l]==numbers[l+1]:
                    l+=1
                l+=1
            else:
                ans+=[l+1, r+1]
                break
        return ans