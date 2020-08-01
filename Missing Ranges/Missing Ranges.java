
class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> ans = new ArrayList();
        int left = lower;
        int right = lower;
        boolean REACH_MAX = false;

        for(int n: nums){
            if(n>upper){
                break;
            } 
            if(n>right){
                if(!REACH_MAX){
                    right = n-1;
                    period(ans, left, right);
                }
                
                if(n<Integer.MAX_VALUE){
                    left = n+1;
                    right = n+1;
                }
                else{
                    REACH_MAX = true;
                }
                
            }
            else{
                if(n<Integer.MAX_VALUE){
                    left = n+1;
                    right = n+1;
                }
                else{
                    REACH_MAX = true;
                }
            }
        }
        //System.out.println(REACH_MAX);
        if(!REACH_MAX && left<=upper && right<=upper){
            right = upper;
            period(ans, left, right);
        }

        return ans;
    }

    private void period(List<String> list, int left, int right){
        String str = "";
        if(left!=right)
            str = String.valueOf(left)+"->"+String.valueOf(right);
        else 
            str = String.valueOf(left);
        list.add(str);
    }
}