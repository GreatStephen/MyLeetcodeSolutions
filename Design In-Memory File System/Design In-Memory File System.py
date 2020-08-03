class FileSystem:

    def __init__(self):
        self.root = {}

    def ls(self, P: str) -> List[str]:
        path = P.split('/')
        node = self.root
        ans = []
        
        for p in path:
            if not len(p): continue
            # print('$'+p)
            if '$'+p in node:
                ans.append(p)
                return ans
            if p not in node:
                return ans
            node = node[p]
        
        for name in node.keys():  
            if name[0]=='$': ans.append(name[1:])
            else: ans.append(name)
        
        return sorted(ans)

    def mkdir(self, P: str) -> None:
        path = P.split('/')
        node = self.root
        
        for p in path:
            if len(p)==0: continue
            if p not in node:
                node[p] = {}
            node = node[p]
                

    def addContentToFile(self, P: str, content: str) -> None:
        path = P.split('/')
        node = self.root
        
        for i,p in enumerate(path):
            if len(p)==0: continue
            if i==len(path)-1:
                fname = '$'+p
                if fname not in node:
                    node[fname] = content
                else:
                    node[fname] += content
                break
                    
            if p not in node:
                node[p] = {}
            node = node[p]
        

    def readContentFromFile(self, P: str) -> str:
        path = P.split('/')
        node = self.root
        
        for i,p in enumerate(path):
            if len(p)==0: continue
            if i==len(path)-1:
                fname = '$'+p
                if fname not in node:
                    return ''
                else:
                    return node[fname]
                    
            if p not in node:
                return ''
            node = node[p]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)