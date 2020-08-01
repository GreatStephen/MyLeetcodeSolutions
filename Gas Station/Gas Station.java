class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        // an interesting question
        int cur_tank = 0;
        int start = 0;
        int total_tank = 0;

        for(int i=0; i<gas.length; i++){
            cur_tank = cur_tank + gas[i] - cost[i];
            total_tank = total_tank + gas[i] - cost[i];
            // if current tank<0, pick a new starting point as i+1
            if(cur_tank<0){
                start = i+1;
                cur_tank = 0;
            } 
        }

        if(total_tank<0) return -1;
        else return start;
    }
}