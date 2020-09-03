class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # bucket算法。每个bucket存放t+1个数字，每个bucket里的数字都是符合题意的，他们之间的距离都<=t
        # 所以，一旦发现当前的index已经有数字存在在bucket中，就可以判定符合题意。
        # index的计算：因为有负数出现，所以用所有数字减去MIN_VALUE得到一个整数，然后除以t+1，即得到bucket id
        # 检查这个id是否已经存在数字。检查前一个id存在的数字，和当前的数字之差是否<=t。检查后一个id存在的数字之差是否<=t

        if k==0 or t<0:
            return False
        bucket = {}
        for i,n in enumerate(nums):
            val = n-(-10**9)
            idx = val//(t+1)
            if idx in bucket: return True
            if idx-1 in bucket and val-bucket[idx-1]<=t: return True
            if idx+1 in bucket and bucket[idx+1]-val<=t: return True
            if len(bucket)>=k:
                lastidx = (nums[i-k]-(-10**9))//(t+1)
                bucket.pop(lastidx)
            bucket[idx] = val
        
        return False