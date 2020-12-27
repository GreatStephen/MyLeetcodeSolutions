class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie = {}
        
        for n in nums:
            binary = []
            while n:
                binary.append(n&1)
                n >>= 1
            binary = list(reversed(binary))
            if not binary:
                binary = [0]
            print(binary)
            cur = trie
            for bit in binary:
                if bit not in cur:
                    cur[bit] = {}
                cur = cur[bit]
            cur['#'] = '#'
        # print(trie)
        
        for target,MAX in queries:
            