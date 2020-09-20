class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = []
        count, temp = 0, ''
        for c in text:
            if c==' ':
                count += 1
                if temp:
                    words.append(temp)
                    temp = ''
            else:
                temp += c
        
        if temp: words.append(temp)
        # print(words, count)
        
        if len(words)==1:
            return words[0]+' '*count
        interval, last = count//(len(words)-1), count%(len(words)-1)
        # print(interval, last)
        ans = ''
        for i in range(len(words)-1):
            word = words[i]
            ans += word
            ans += ' '*interval
        ans += words[-1]+' '*last
        return ans