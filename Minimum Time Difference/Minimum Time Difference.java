class Solution {
    public int findMinDifference(List<String> timePoints) {
        int[] time = new int[timePoints.size()];
        for(int i=0; i<time.length; i++){
            time[i] = parseTime(timePoints.get(i));
        }
        Arrays.sort(time);
        int res = Integer.MAX_VALUE;
        for(int i=1; i<time.length; i++){
            res = Math.min(res, time[i]-time[i-1]);
        }
        res = Math.min(res, time[0]+ 24*60 - time[time.length-1]);
        return res;
    }
    private int parseTime(String s){
        String[] t = s.split(":");
        int res=0;
        for(int i=0; i<2; i++){
            int value = Integer.parseInt(t[i]);
            res+=i==0?value*60 : value;
        }
        return res;
    }
}