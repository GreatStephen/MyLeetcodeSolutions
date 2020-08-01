
class Solution {
    // Too complicated


    private List<String> res = new ArrayList();
    private Set<String> set = new HashSet();
    public List<String> removeInvalidParentheses(String s) {
        // positive order
        check(s, 0, 0);
        
        // reverse order, because '(' may be more than ')'
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<s.length(); i++){
            sb.insert(0, s.charAt(i)=='('?')':s.charAt(i)==')'?'(':s.charAt(i));
        }
        String rev_str = sb.toString();
        check(rev_str, 0, 0);

        // no way to build a parenthesis string
        // thus remove all parentheses
        if(res.isEmpty()){
            sb = new StringBuilder();
            for(int i=0; i<s.length(); i++){
                if(s.charAt(i)!='(' && s.charAt(i)!=')'){
                    sb.append(s.charAt(i));
                }
            }
            res.add(sb.toString());
        }
        
        return res;
    }

    private void check(String s, int cur_idx, int last_idx){
        int temp_idx;
        int val = 0;
        for(temp_idx=cur_idx; temp_idx<s.length(); temp_idx++){
            if(s.charAt(temp_idx)=='('){
                ++val;
            }
            else if(s.charAt(temp_idx)==')'){
                --val;
            }
            else{
                // other letters
                continue;
            }
            if(val>=0){
                continue;
            }
            else{
                break;
            }
        }

        if(temp_idx==s.length()){
            if(val==0 && !s.isEmpty()){
                // a valid solution, add to res[]
                if(!set.contains(s)){
                    res.add(s);
                    set.add(s);
                }
                
            }
            return;
        }

        // remove a ')' from last_idx
        // remove the FIRST ')' from consecutive ')'s. it MUST be the first one, because
        // the following ')'s are also removable in the next recursion. if remove the last ')',
        // some solutions may be missing.
        boolean consec = false;
        for(int i=last_idx; i<=temp_idx; i++){            
            if(s.charAt(i)==')'){
                // consecutive
                if(consec){
                    continue;
                }
                // remove this ')', and recurse
                consec = true;
                String new_str = s.substring(0, i)+s.substring(i+1, s.length());
                check(new_str, temp_idx, i);
            }
            else{
                consec = false;
                continue;
            }
        }

    }
}