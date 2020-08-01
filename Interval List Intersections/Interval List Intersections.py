class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0, 0
        ans = []
        while p1<len(A) and p2<len(B):
            a, b = A[p1], B[p2]
            if a[0]>b[1]:
                p2 += 1
                continue
            if b[0]>a[1]:
                p1 += 1
                continue
            if a[0]<b[0]:
                if a[1]<b[1]: 
                    ans.append([b[0], a[1]])
                    p1 += 1
                elif a[1]>b[1]: 
                    ans.append(b)
                    p2 += 1
                else:
                    ans.append(b)
                    p1 += 1
                    p2 += 1
            
            elif a[0]>b[0]:
                if a[1]<b[1]: 
                    ans.append(a)
                    p1 += 1
                elif a[1]>b[1]: 
                    ans.append((a[0], b[1]))
                    p2 += 1
                else:
                    ans.append(a)
                    p1 += 1
                    p2 += 1
            else:
                ans.append([a[0], min(a[1],b[1])])
                if a[1]<b[1]: p1+=1
                elif a[1]>b[1]: p2+=1
                else:
                    p1+=1
                    p2+=1
        return ans