# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:     
        
        def match(w1, w2):
            ans = 0
            for i in range(6):
                if w1[i]==w2[i]: ans += 1
            return ans
            
        dist = 0
        while dist<6:
            freq = []
            for i in range(6):
                l = []
                for w in wordlist:
                    l.append(w[i])
                freq.append(Counter(l))
            # print(freq)
            
            # pick one with maximum score
            maxscore, word = 0, None
            for w in wordlist:
                score = 0
                for i,c in enumerate(w):
                    score += freq[i][c]
                if score>maxscore:
                    maxscore = score
                    word = w
            
            dist = master.guess(word)
            
            # keep the words that has distance==dist to our guess
            wordlist = [w for w in wordlist if match(w, word)==dist]