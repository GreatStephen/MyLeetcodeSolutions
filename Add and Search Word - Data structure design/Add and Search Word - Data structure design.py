class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.d
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['#']='#'   
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # 非常简洁有效的递归写法
        def find(word, node):
            if not word:
                return '#' in node
            char, word = word[0], word[1:]
            if char != '.':
                return char in node and find(word, node[char])
            return any(find(word, kid) for kid in node.values() if kid!='#')
        return find(word, self.d)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)