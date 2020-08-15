class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ans = range(1, len(s)+2) # ans = [1,2,3,4,5,...]
        # print ans

        # 这题纯粹智商题。遇到连续D，[i,j]，把ans[i,j+1]翻转
        # 这完全就是考智商，也没什么算法，想到了就想到了，想不到就做不出来
        
        l = r = -1
        for i in xrange(len(s)):
            if s[i]=='D':
                if r!=-1: 
                    r+=1
                else:
                    l = i
                    r = l+1
            else:
                if r!=-1:
                    ans[l:r+1] = ans[l:r+1][::-1]
                    l = r = -1
        if r!=-1:
            ans[l:r+1] = ans[l:r+1][::-1]
        
        
        
        return ans