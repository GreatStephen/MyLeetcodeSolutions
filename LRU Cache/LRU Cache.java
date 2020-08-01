class LRUCache {
    
    public LinkedHashMap<Integer, Integer> used;
    public int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        used = new LinkedHashMap<Integer, Integer>(capacity, 0.75F, true){
            @Override
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                return size() > capacity; 
            }
        };
    }
    
    public int get(int key) {
        return used.getOrDefault(key, -1);
    }
    
    public void put(int key, int value) {
        used.put(key, value);
    }
    
    
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */