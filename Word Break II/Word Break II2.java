
class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        // DP bottom-up
        // TLE! maybe use iteration?
        HashSet<String> set = new HashSet();
        for(String str: wordDict){
            set.add(str);
        }
        List<String>[] dp = new ArrayList[s.length()];

        for(int i=s.length()-1; i>=0; i--){
            DP(set, s, i, dp);
        }

        
        return dp[0];
    }

    private void DP(HashSet<String> set, String s, int idx, List<String>[] dp){
        List<String> temp_res = new ArrayList();
        for(int j=idx; j<s.length(); j++){
            String word = s.substring(idx, j+1);
            if(set.contains(word)){
                // a valid word
                List<String> last_dp;
                if(j+1<dp.length) last_dp = dp[j+1];
                else last_dp = new ArrayList();

                if(last_dp.size()==0 && j==dp.length-1){
                    temp_res.add(word);
                }
                else{
                    for(String str: last_dp){
                        temp_res.add(word+" "+str);
                    }
                }
            }
        }

        dp[idx] = temp_res;
    }
}