class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        reached = set()
        wordSet = set(wordList)
        wordMap = {}
        ans = []
        deq = collections.deque()
        deq.append([beginWord])
        reached.add(beginWord)  # in case beginWord is in wordList
        end = False
        while len(deq)!=0 and not end:
            N = len(deq)
            level_reached = set()
            for i in range(N):
                cur_path_l = deq.popleft()
                cur_node = cur_path_l[-1]
                next_nodes_l = self.findNext(cur_node, reached, wordSet, wordMap)
                for next_node in next_nodes_l:
                    new_path_l = list(cur_path_l)
                    new_path_l.append(next_node)
                    deq.append(new_path_l)
                    if next_node==endWord:
                        ans.append(new_path_l)
                        end = True  # reach the shortest path, no need for next loop
                level_reached = level_reached.union(set(next_nodes_l))
            reached = reached.union(level_reached)
        return ans
    
    def findNext(self, cur_node, reached, wordSet, wordMap) -> List[str]:
        if cur_node in wordMap:
            return wordMap.get(cur_node)        
        res = []
        for i in range(len(cur_node)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                temp_word = cur_node[0:i] + j + cur_node[i+1:]
                if temp_word not in reached and temp_word in wordSet:
                    res.append(temp_word)
        wordMap[cur_node] = res
        return res