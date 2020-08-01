/*
// Definition for an Interval.
class Interval {
    public int start;
    public int end;

    public Interval() {}

    public Interval(int _start, int _end) {
        start = _start;
        end = _end;
    }
};
*/

class Solution {
    public List<Interval> employeeFreeTime(List<List<Interval>> schedule) {
        List<Interval> ans = new ArrayList();
        List<Interval> events = new ArrayList();
        for(List<Interval> emp: schedule){
            for(Interval inter: emp){
                events.add(inter);
            }
        }

        // ascending start, ascending end
        Collections.sort(events, new Comparator(){
            @Override
            public int compare(Object o1, Object o2){
                Interval a = (Interval)o1;
                Interval b = (Interval)o2;
                if(a.start!=b.start){
                    return a.start-b.start;
                }
                else{
                    return a.end-b.end;
                }
            }
        });

        for(Interval in: events){
            System.out.println(in.start+" "+in.end);
        }
        

        // sweep through
        int start=Integer.MIN_VALUE, end=Integer.MIN_VALUE;
        for(Interval inter: events){
            if(inter.start > end){
                if(end!=Integer.MIN_VALUE){
                    ans.add(new Interval(end, inter.start));
                }
                start = inter.start;
                end = inter.end;
            }
            else{
                end = Math.max(end, inter.end);
            }
        }

        return ans;
    }
}