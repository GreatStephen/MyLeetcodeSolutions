
class Solution {
    public int longestConsecutive(int[] nums) {
        // smart idea
        Set<Integer> set = new HashSet();
        for(int num: nums){
            set.add(num);
        }
        int ans = 0;

        for(int num: set){
            if(!set.contains(num-1)){
                // this is a start point
                int cur_num = num;
                int streak = 1;
                cur_num++;
                while(set.contains(cur_num)){
                    streak++;
                    cur_num++;
                }

                ans = Math.max(ans, streak);
            }
        }

        return ans;
    }
}