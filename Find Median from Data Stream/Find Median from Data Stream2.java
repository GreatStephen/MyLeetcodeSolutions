class MedianFinder {
    // maxheap for lower half, minheap for upper half. 
    // lo.size = hi.size or hi.size+1
    
    private PriorityQueue<Integer> lo_half;
    private PriorityQueue<Integer> hi_half;
    /** initialize your data structure here. */
    public MedianFinder() {
        hi_half = new PriorityQueue();
        lo_half = new PriorityQueue(10, new Comparator<Integer>(){
            @Override
            public int compare(Integer o1, Integer o2){
                return o2-o1;
            }

        });
    }
    
    public void addNum(int num) {
        if(lo_half.isEmpty()){
            lo_half.offer(num);
            return;
        } 
        if(num<lo_half.peek()){
            lo_half.offer(num);
            if(lo_half.size()>hi_half.size()+1){
                int lo_peek = lo_half.poll();
                hi_half.offer(lo_peek);
            }
        }
        else{
            hi_half.offer(num);
            if(lo_half.size()<hi_half.size()){
                int hi_peek = hi_half.poll();
                lo_half.offer(hi_peek);
            } 
            
        }
    }
    
    public double findMedian() {
        if(lo_half.size()>hi_half.size()) return lo_half.peek()*1.0;
        else{
            // System.out.println(lo_half);
            // System.out.println(hi_half);
            int a = lo_half.peek();
            int b = hi_half.peek();
            return (a+b)*0.5;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */