class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        count = []
        for i in range(len(mat)):
            v, l = 0, []
            for n in mat[i][::-1]:
                v = v+1 if n==1 else 0
                l.insert(0,v)
            count.append(l)
        
        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if count[i][j]>0:
                    val = count[i][j]
                    sum = val
                    for i1 in range(i+1,len(mat)):
                        val = min(val, count[i1][j])
                        sum += val
                    ans += sum
        return ans