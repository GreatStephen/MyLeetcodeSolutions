class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int slength = s.length();
        int tlength = t.length();

        if(slength>tlength) return isOneEditDistance(t, s);

        if(tlength-slength>1) return false;

        for(int i=0;i<slength;i++){
            if(s.charAt(i)!=t.charAt(i)){
                if(tlength>slength) return s.substring(i).equals(t.substring(i+1));
                else return s.substring(i+1).equals(t.substring(i+1));
            }
        }

        return (slength+1==tlength);
    }
}