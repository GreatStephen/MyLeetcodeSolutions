class Solution {
    public String longestCommonPrefix(String[] strs) {
        // vertical comparison

        if(strs.length==0) return "";
        StringBuilder sb = new StringBuilder();

        int idx=0;
        while(true){
            boolean valid = true;
            if(idx>=strs[0].length()){
                break;
            }
            char c = strs[0].charAt(idx);

            for(String str: strs){
                if(idx>=str.length()){
                    valid = false;
                    break;
                }
                if(str.charAt(idx)!=c){
                    valid = false;
                    break;
                }
            }
            if(valid){
                sb.append(c);
                idx++;
            } 
            else break;
        }

        return sb.toString();
    }
}