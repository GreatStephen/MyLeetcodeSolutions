class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def findmax(nums, k):
            deq = deque()
            drop = len(nums)-k
            for n in nums:
                while drop and deq and deq[-1]<n: 
                    deq.pop()
                    drop -= 1
                deq.append(n)
            return list(deq)[:k]
        
        def merge(nums1, nums2):
            # ans = []
            # while nums1 or nums2:
            #     if (nums1 or [-1])[0] >= (nums2 or [-1])[0]:
            #         ans.append(nums1[0])
            #         nums1 = nums1[1:]
            #     else:
            #         ans.append(nums2[0])
            #         nums2 = nums2[1:]
            # return ans
            # print(max(nums1, nums2))
            # 这个方法来自stephan，将nums1和nums2中字典序更大的提取最左侧数字
            return [max(nums1, nums2).pop(0) for _ in nums1+nums2]
        
        def greater(ans):            
            for idx in range(k):
                temp = []
                for a in ans:
                    if not temp: temp.append(a)
                    elif a[idx]>temp[-1][idx]:
                        temp = [a]
                    elif a[idx]==temp[-1][idx]:
                        temp.append(a)
                ans = temp
                if len(ans)==1: break
            return ans[0]
        
        
        ans = []
        for len1 in range(k+1):
            len2 = k-len1
            if len1>len(nums1) or len2>len(nums2): continue
            ans.append(merge(findmax(nums1, len1), findmax(nums2, len2)))
        return greater(ans)