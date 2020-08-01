class Solution {
    public int longestValidParentheses(String s) {
        // this is solution 4
        // stack without extra space
        int left = 0, right = 0;
        int length = s.length();
        int max1=0, max2=0;
        
        // left -> right
        for(int i=0; i<length; i++){
            if(s.charAt(i)=='('){
                left++;
            }
            else if(s.charAt(i)==')'){
                right++;
                if(right>left){
                    left = 0;
                    right = 0;
                }
            }

            if(left == right){
                max1 = Math.max(max1, left+right);
            }
        }

        // right -> left
        left = 0;
        right = 0;
        for(int i=length-1; i>=0; i--){
            if(s.charAt(i)==')'){
                right++;
            }
            else if(s.charAt(i)=='('){
                left++;
                if(left>right){
                    left = 0;
                    right = 0;
                }
            }

            if(left == right){
                max2 = Math.max(max2, left+right);
            }
        }

        return Math.max(max1, max2);
    }
}