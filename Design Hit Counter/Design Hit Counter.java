class HitCounter {
    // use a Deque to store the ordered hit timestamp
    
    private Deque<Integer> q;
    /** Initialize your data structure here. */
    public HitCounter() {
        q = new LinkedList();
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        while(!q.isEmpty() && q.peekFirst()<=timestamp-300){
            q.pollFirst();
        }
        q.offerLast(timestamp);
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        while(!q.isEmpty() && q.peekFirst()<=timestamp-300){
            q.pollFirst();
        }
        return q.size();
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */