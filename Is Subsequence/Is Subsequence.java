class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length()==0) return true;
        int sindex=0, tindex=0;
        while(tindex<t.length()){
            if(s.charAt(sindex) == t.charAt(tindex)){
                sindex++;
                if(sindex==s.length()) return true;
            }
            tindex++;
        }
        
        return sindex==s.length()?true:false;
    }
}