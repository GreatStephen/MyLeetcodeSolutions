class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        can1, can2, c1, c2 = 0,1,0,0
        for i,v in enumerate(nums):
            if can1==v:
                c1+=1             
            elif can2==v:
                c2+=1  
            elif c1==0:
                can1 = v
                c1 = 1     
            elif c2==0:
                can2 = v
                c2 = 1
            else:
                c1, c2 = c1-1, c2-1
        ans = []
        if c1>0:
            ans.append(can1)
        if c2>0:
            ans.append(can2)
        return [n for n in ans if nums.count(n)>(len(nums)//3)]