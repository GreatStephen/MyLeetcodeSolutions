
class Solution {
    List<List<String>> ans = new ArrayList();
    public List<List<String>> partition(String s) {
        backtracking(s, new ArrayList());
        return ans;
    }

    private void backtracking(String s, List<String> temp){
        if(s.length()==0){
            // save hardcopy of temp to ans
            List<String> res = new ArrayList(temp);
            ans.add(res);
            return;
        } 
        for(int i=0; i<s.length(); i++){
            if(isPalindrome(s.substring(0, i+1))){
                temp.add(s.substring(0, i+1));
                backtracking(s.substring(i+1, s.length()), temp);
                temp.remove(temp.size()-1);
            }
        }
    }

    private boolean isPalindrome(String s){
        int left = 0, right = s.length()-1;
        while(right>=left){
            if(s.charAt(right)!=s.charAt(left)){
                return false;
            }
            right--;
            left++;
        }
        return true;
    }
}