
class Solution {
    private List<String> ans = new ArrayList();

    public List<String> wordBreak(String s, List<String> wordDict) {
        // DFS and backtracking
        // TLE
        HashSet<String> set = new HashSet();
        for(String str: wordDict){
            set.add(str);
        }

        // build dp[i][j]=true if substring(i, j+1) is a valid word
        boolean[][] dp = new boolean[s.length()][s.length()];
        for(int i=0; i<s.length(); i++){
            for(int j=0; j<s.length(); j++){
                if(j<i) dp[i][j] = false;
                else if(set.contains(s.substring(i, j+1))) dp[i][j] = true;
                else dp[i][j] = false;
            }
        }

        // for(int i=0; i<s.length(); i++){
        //     System.out.println(Arrays.toString(dp[i]));
        // }

        ArrayList<String> temp_res = new ArrayList();
        backtracking(s, s.length()-1, temp_res, dp);

        return ans;
    }

    private void backtracking(String s, int cur_idx, ArrayList<String> temp_res, boolean[][] dp){
        if(cur_idx==-1){
            // exit, temp_res contains the final strings
            StringBuilder sb = new StringBuilder();
            for(String str: temp_res){
                sb.append(str);
                sb.append(" ");
            }
            sb.deleteCharAt(sb.length()-1);
            ans.add(sb.toString());
            return;
        }

        for(int i=0; i<s.length(); i++){
            if(dp[i][cur_idx]){
                // a valid word is found
                String word = s.substring(i, cur_idx+1);
                temp_res.add(0, word);
                backtracking(s, i-1, temp_res, dp);
                temp_res.remove(0);
            }
        }
    }
}