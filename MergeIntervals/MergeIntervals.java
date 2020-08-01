class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] x, int[] y) {
                if(x[0] < y[0]){
                    return -1;
                } else if(x[0] > y[0]){
                    return 1;
                } else {
                    return 0;
                }
            }
        });
        
        LinkedList<ArrayList<Integer>> merged = new LinkedList<ArrayList<Integer>>();
        for(int i=0; i<intervals.length; i++){
            if (merged.isEmpty() || merged.getLast().get(1) < intervals[i][0]) {
                ArrayList<Integer> temp_list = new ArrayList<Integer>();
                temp_list.add(intervals[i][0]);
                temp_list.add(intervals[i][1]);
                merged.add(temp_list);
            }
            else{
                merged.getLast().set(1, Math.max(merged.getLast().get(1), intervals[i][1]));
            }
        }
        System.out.println(merged);

        int[][] res = new int[merged.size()][2];
        int length=merged.size();
        // System.out.println(length);
        for(int i=0; i<length; i++){
            res[i][0]=merged.get(0).get(0);
            res[i][1]=merged.get(0).get(1);
            merged.removeFirst();
        }
        
        return res;
    }
}