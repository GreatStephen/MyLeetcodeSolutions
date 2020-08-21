class Solution(object):
    def removeComments(self, source):
        # 字符串题。在block mode之外，碰到//直接结束一行。
        # 碰到/*进入block mode, 并且不再接受任何字符
        # 在block mode之中遇到*/结束block mode, 并开始接受字符
        ans, cur = [], ''
        in_block = False
        jump = False
        for s in source:
            for i in xrange(len(s)):
                if jump:
                    jump = False
                    continue
                c = s[i]
                if c=='/' and i+1<len(s) and s[i+1]=='/':
                    if not in_block:
                        break
                
                elif c=='/' and i+1<len(s) and s[i+1]=='*':
                    if not in_block:
                        in_block = True
                        jump = True
                
                elif c=='*' and i+1<len(s) and s[i+1]=='/' and in_block:
                    if in_block:
                        in_block = False
                        jump = True
                
                
                else:
                    if not in_block:
                        cur += c
            
            
            if not in_block:
                if len(cur)>0:
                    ans.append(cur)
                    cur = ''
        
        return ans

