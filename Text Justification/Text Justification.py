class Solution(object):
    def fullJustify(self, words, maxWidth):
        # 字符串处理问题。cur存放当前处于同一行的单词，numofletters是字母的数量，因此masWidth-numofletters=还剩多少个空格要处理
        # 从cur的第一个单词到倒数第二个单词（如果只有一个单词，那就到他自己），每个单词后面轮流添加一个空格
        # 当for循环结束时，cur里正好存放最后一行，最后一行特殊处理。每个单词之间添加一个空格，其余空格全部添加到末尾
        # 可以用python的ljust快速实现


        ans, cur, num_of_letters = [], [], 0
        
        for w in words:
            # 一行已经拼好
            if len(w)+len(cur)+num_of_letters > maxWidth:
                for i in range(maxWidth-num_of_letters): # 从左到右添加空格，一人一个，
                    idx = (i%(len(cur)-1 or 1))
                    cur[idx] += ' '
                ans.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur.append(w)
            num_of_letters += len(w)

        # 最后一行特殊处理，cur里正好存放最后一行，因为最后一行不触发if条件    
        last_line = ''
        for w in cur:
            last_line += w + ' '
        last_line = last_line[:-1].ljust(maxWidth) # ljust很方便
        ans.append(last_line)
        
        
        return ans