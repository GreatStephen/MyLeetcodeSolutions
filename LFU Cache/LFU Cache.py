class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.count_key = {}
        self.key_count = {}
        self.cap = capacity
        self.min = 0

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        
        # add 1 to this key's count
        count = self.key_count[key]
        self.key_count[key] = count+1
        
        # move this key from set[count] to set[count+1]
        del self.count_key[count][key]
        if len(self.count_key[count])==0:
            # if key is the only one with minimum count, update min
            if self.min==count: self.min+=1
            del self.count_key[count]
        if count+1 not in self.count_key:
            self.count_key[count+1] = OrderedDict()
        self.count_key[count+1][key]=0
        
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if self.cap<=0: return
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
            return 
        
        # make one spare space
        if len(self.cache)>=self.cap:
            minkey = list(self.count_key[self.min].keys())[0]
            del self.cache[minkey]            
            del self.key_count[minkey]
            del self.count_key[self.min][minkey]
            if len(self.count_key[self.min])==0:
                del self.count_key[self.min]
        
        # insert this key, and make min=1
        self.cache[key] = value
        self.key_count[key] = 1
        self.min = 1
        if 1 not in self.count_key:
            self.count_key[1] = OrderedDict()
        self.count_key[1][key]=0
            


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)