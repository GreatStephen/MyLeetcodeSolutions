class Solution {
    public int numDecodings(String s) {
        int[] dp = new int[s.length()+1];
        dp[0]=1;
        if(s.charAt(0)!='0') dp[1] = 1;
        else dp[1]=0;
        
        for(int i=1; i<s.length(); i++){
            int num1 = Integer.parseInt(String.valueOf(s.charAt(i)));
            int num2 = 0;
            if(s.charAt(i-1)!='0') num2 = Integer.parseInt(s.substring(i-1, i+1));
            int temp1 = num1!=0?dp[i]:0;
            int temp2 = num2>=1?(num2<=26?dp[i-1]:0):0;
            dp[i+1] = temp1 + temp2;
            //System.out.println(dp[i+1]);
        }
        return dp[s.length()];
    }
}