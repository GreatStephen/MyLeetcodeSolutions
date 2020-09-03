class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # O(NlogN),维护一个长度为k的窗口，对窗口排序，用BS找到当前数字应该在的位置。
        # 对这个窗口判断是否符合条件。如果新元素超出了窗口最大值，就去掉窗口坐标的数字
        arr = []
        for i in range(k):
            if i==len(nums): return False
            pos = bisect.bisect(arr, nums[i])
            if pos==len(arr): arr.append(nums[i]) # 放进排序好的数组
            else: arr.insert(pos, nums[i])
            if pos-1>=0 and abs(arr[pos-1]-arr[pos])<=t: return True
            if pos+1<len(arr) and abs(arr[pos+1]-arr[pos])<=t: return True
        
        for i in range(k, len(nums)):
            pos = bisect.bisect(arr, nums[i])
            if pos==len(arr): arr.append(nums[i])
            else: arr.insert(pos, nums[i])
            if pos-1>=0 and abs(arr[pos-1]-arr[pos])<=t: return True
            if pos+1<len(arr) and abs(arr[pos+1]-arr[pos])<=t: return True
            pre = i-k
            pos = bisect.bisect_left(arr, nums[pre]) # 删除一个元素，以维持窗口size=k
            arr.pop(pos)
        
        return False