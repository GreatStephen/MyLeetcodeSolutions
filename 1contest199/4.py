class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        times = defaultdict(int) # {1:?, 2:?, 3:?}
        data = []
        total_length = 0
        temp_s = ''
        
        c, count = None,0
        for i,ch in enumerate(s):
            if ch!=c:
                if c: 
                    data.append({c:count})
                    total_length += (len(c+str(count)) if count>1 else len(c) )
                    temp_s+=c
                c = ch
                count = 1
            else:
                count += 1
        if c: data.append({c:count})
        total_length += (len(c+str(count)) if count>1 else len(c) )
        temp_s+=c
        # print(total_length)
        
        temp_ans = 10**9
        for i in range(1, len(temp_s)-1):
            if temp_s[i-1]==temp_s[i+1]:
                d = data[i]
                for c,count in d.items():
                    if count<=3 and k-3>=0:
                        l, r = 0, 0
                        for k in range(i):
                            for kc, kcount in data[k].items():
                                l+=kcount
                        r = l+count
                        temp_ans = min(temp_ans, self.getgetLengthOfOptimalCompression(s[:l]+s[r:], k-3))
        
        for d in data:
            for c,count in d.items():
                # print(c,count)
                while count>0:
                    if count==100:
                        times[1]+=1
                        count=99
                    elif 9<count<100:
                        times[count-9]+=1
                        count=9
                    elif 1<count<10:
                        times[count-1]+=1
                        count=1
                    elif count==1:
                        times[1]+=1
                        count=0
        print(times)
        print(total_length)
        
        for kk in sorted(times):
            reduce, count = kk, times[kk]
            while k>=0:
                k-=reduce
                if k>=0: total_length-=1
                else: return total_length
        
        return min(total_length, temp_ans)