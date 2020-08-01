
class Solution {
    public List<String> wordBreak(String s, List<String> wordDict) {
        // DP bottom-up
        // TLE! iteration still TLE!
        HashSet<String> set = new HashSet();
        for(String str: wordDict){
            set.add(str);
        }
        List<String>[] dp = new ArrayList[s.length()];

        for(int i=s.length()-1; i>=0; i--){
            List<String> temp_res = new ArrayList();
            for(int j=i; j<s.length(); j++){
                String word = s.substring(i, j+1);
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
    
            dp[i] = temp_res;
        }

        
        return dp[0];
    }
}