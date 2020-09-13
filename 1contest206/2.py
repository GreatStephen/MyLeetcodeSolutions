class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        unhp = set()
        pair = {}
        for x,y in pairs:
            pair[x] = y
            pair[y] = x
            
        def comes_before(a,b, node):
            pref = preferences[node]
            meeta, meetb = False, False
            for n in pref:
                if n==a and not meetb: return True
                if n==b and not meeta: return False
        
        for x in range(n):
            if x in unhp: continue
            u = pair[x]
            # print(x,u)
            for f in preferences[x]:
                # print(f)
                if f==u: break
                if comes_before( x, pair[f], f):
                    # print('f is better')
                    unhp.add(x)
                    unhp.add(f)
                    break
        
        return len(unhp)