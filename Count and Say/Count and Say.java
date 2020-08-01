class Solution {
    public String countAndSay(int n) {
        // recursion, not a fast solution, but easy to think of
        if(n==1) return "1";
        String str = countAndSay(n-1);
        String ans = "";

        char number = '*';
        int count = 0;
        for(int i=0; i<str.length(); i++){
            if(str.charAt(i)!=number){
                if(number!='*'){
                    ans += String.valueOf(count)+number;
                }
                number = str.charAt(i);
                count = 1;
            }
            else{
                count++;
            }
        }
        ans += String.valueOf(count)+number;

        return ans;
    }
}