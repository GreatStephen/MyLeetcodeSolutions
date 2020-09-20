class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # 一道简单的backtracking，把所有可能罗列出来即可
        def Build(length, start):
            if start+length>10:
                return None
            ans = 0
            for i in range(start, start+length):
                ans = ans*10+i
            if low<=ans<=high:
                return ans
            return None
        
        # starting digit从1到9，总长从小到大，即可保证答案的递增性
        ans = []
        for length in range(len(str(low)), len(str(high))+1):
            for start in range(1, 10):
                num = Build(length, start)
                if num: ans.append(num)
        return ans