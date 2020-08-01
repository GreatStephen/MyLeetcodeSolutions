class Solution:
    def maximumSwap(self, num: int) -> int:
        l, r = (-1,-1), (-1,-1)
        cur_max, cur_min = (0,-1), (0, 10**8+1)
        for i,v in enumerate(reversed(str(num))):
            # print(i,v)
            if int(v)>cur_max[1]:
                cur_max = cur_min = (i,int(v))
            elif int(v)<=cur_max[1]:
                cur_min = (i,int(v))
                l = cur_min
                r = cur_max
        
        print(l,r)
        if l == (-1,-1): return num
        s = str(num)
        return int(s[:l[0]] + str(r[1]) + s[l[0]+1:r[0]] + str(l[1]) + s[r[0]+1:])