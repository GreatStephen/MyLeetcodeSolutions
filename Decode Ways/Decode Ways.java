class Solution {
    // time limit exceeded
    public int numDecodings(String s) {
        return parse_string(s);
    }
    private int parse_string(String s){
        if(s.length()==0) return 1;
        if(s.charAt(0)=='0') return 0;
        if(s.length()==1) return 1;
        int res1 = parse_string(s.substring(1));
        int res2 = 0;
        String num = s.substring(0,2);
        int number = Integer.parseInt(num);
        if(number>=1 && number<=26) res2 = parse_string(s.substring(2));

        return res1 + res2;
    }
    
}