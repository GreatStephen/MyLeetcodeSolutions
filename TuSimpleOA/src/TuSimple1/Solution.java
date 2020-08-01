package TuSimple1;

public class Solution {
    public static int segment(int x, List<Integer> arr) {
        // Write your code here
        List<Integer> templist = new ArrayList<Integer>();
        List<Integer> minlist = new ArrayList<Integer>();
        for(int i=0; i<arr.size()-x+1; i++){
            // fetch the templist with length x
            templist.clear();
            for(int j=i; j<i+x; j++){
                templist.add(arr.get(j));
            }

            // find the minimum number, put into minlist
            minlist.add(Collections.min(templist));
        }

        return Collections.max(minlist);
    }
}
