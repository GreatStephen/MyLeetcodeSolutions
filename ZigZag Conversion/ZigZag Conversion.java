class Solution {
    public String convert(String s, int numRows) {
        if(numRows==1) return s;
        int[] row_idx = new int[s.length()];
        int offset = 1;
        int idx = 0;
        for(int i=0; i<row_idx.length; i++){
            row_idx[i] = idx;
            idx+=offset;
            if(idx<0){
                offset = 1;
                idx = 1;
            }
            else if(idx>=numRows){
                idx = numRows-2;
                offset = -1;
            }
        }
        StringBuilder[] sb_arr = new StringBuilder[numRows];
        for(int i=0; i<sb_arr.length; i++){
            sb_arr[i] = new StringBuilder();
        }
        for(int i=0; i<row_idx.length; i++){
            sb_arr[row_idx[i]].append(s.charAt(i));
        }
        String ans = "";
        for(int i=0; i<numRows; i++){
            ans += sb_arr[i].toString();
        }

        return ans;
    }
}