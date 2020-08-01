class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # how many times of repetition at this position
        total = [1,1]
        for i in range(2,n): total.insert(0, i*total[0])

        # use repetitions to count the digit
        ans, digits = '', [i for i in range(1, n+1)]
        for i in range(n):
            count = k//total[i]-1 if k%total[i]==0 else k//total[i]
            digit = digits[count]
            ans+=str(digit)
            k -= total[i] * count
            digits.remove(digit)

        return ans