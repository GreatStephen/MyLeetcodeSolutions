class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        d = {}
        for i,v in enumerate(s):
            if v not in d:
                d[v] = [i,i]
            else:
                d[v][1] = i
        # print(d)
        
        
        # check if each area is appropriate
        a = collections.defaultdict(list)
        for c,l in d.items():
            ok = True
            seen = set()
            seen.add(c)
            for i in range(l[0]+1, l[1]):
                if s[i] in seen: continue
                if not (l[0]<d[s[i]][0]<l[1] and l[0]<d[s[i]][1]<l[1]):
                    ok = False
                    break
                seen.add(s[i])
            if ok:
                a[l[1]-l[0]+1].append(l)
        print(a)
        
        # choose the shortest one from a, in same length, strings are guaranteed not to overlap with each other
        st,e,ans = [],[],[]
        for length in sorted(a):
            l = a[length]
            # print(l)
            done = False
            for idx in l:
                pos = bisect.bisect_left(st, idx[0])
                # print(st,e, pos)
                
                if pos==0:
                    if len(e)==0 or idx[1]<st[pos]:
                        st.insert(pos, idx[0])
                        e.insert(pos, idx[1])
                    else:    
                        done = True
                        break
                elif pos==len(st):
                    if idx[0]>e[pos-1]:
                        st.append(idx[0])
                        e.append(idx[1])
                    else:
                        done = True
                        break
                else:
                    if idx[0]>e[pos-1] and idx[1]<st[pos]:
                        st.insert(pos, idx[0])
                        e.insert(pos, idx[1])
                    else:    
                        done = True
                        break
            if done:
                break
        for start, end in zip(st,e):
            ans.append(s[start:end+1])
        return ans
        
        
        return ''