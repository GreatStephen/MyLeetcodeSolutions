
/*
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
*/
class MedianFinder {
    // use a sorted linked list, and two pointers
    // time limit exceed
    private LinkedList<Integer> list;
    private int lo_median = -1, hi_median = -1;

    /** initialize your data structure here. */
    public MedianFinder() {
        list = new LinkedList();
    }
    
    public void addNum(int num) {
        if(list.size()==0){
            list.add(num);
            lo_median = hi_median = 0;
            return;
        } 
        insertList(num);
        int lo_num = list.get(lo_median);
        int hi_num = list.get(hi_median);
        if(num>=hi_num){
            if(lo_median==hi_median) hi_median++;
            else lo_median = hi_median;
        }
        else if(lo_num<=num && num<hi_num){
            lo_median = hi_median;
        }
        else{
            if(lo_median==hi_median) hi_median++;
            else lo_median++;
        }

    }
    
    public double findMedian() {
        if(list.isEmpty()) return 0;
        if(lo_median==hi_median){
            return list.get(lo_median)*1.0;
        }
        else{
            int a = list.get(lo_median);
            int b = list.get(hi_median);
            return (a+b)*0.5;
        }
    }

    private void insertList(int num){
        for(int i=0; i<list.size(); i++){
            if(list.get(i)>=num){
                list.add(i, num);
                break;
            }
        }

    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */