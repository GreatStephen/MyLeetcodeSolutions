class Solution {
    public String longestPalindrome(String s) {
        if(s.length()==0) return s;
        int length = s.length();
        int[] res = new int[]{0,0,0};
        for(int i=0; i<length; i++){
            int[] length1 = expand(s, i, i);
            int[] length2 = expand(s, i, i+1);
            if(length1[2]>length2[2] && length1[2]>res[2]) res=length1;
            else if(length2[2]>length1[2] && length2[2]>res[2]) res = length2;
            
        }
        return s.substring(res[0], res[1]+1);
        
    }
    
    public int[] expand(String s, int left, int right){
        int L=left, R=right;
        while(L>=0 && R< s.length() && s.charAt(L)==s.charAt(R)){
            L--;
            R++;
        }
        return new int[]{L+1, R-1, R-L-1};
    }
}