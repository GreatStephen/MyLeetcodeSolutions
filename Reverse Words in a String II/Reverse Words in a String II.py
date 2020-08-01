class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 先把整个list逆序，然后以空格分界，逆序每个word
        def reverse(s, i, j):
            while i<j:
                t = s[i]
                s[i] = s[j]
                s[j] = t
                i+=1
                j-=1
        
        N = len(s)
        reverse(s, 0, N-1)
        l, r = -1, -1
        for i in range(N):
            if s[i]==' ':
                if l!=r: reverse(s, l+1, r)
                l = r = i
            else: r = i
        if l!=r: reverse(s, l+1, r)
            