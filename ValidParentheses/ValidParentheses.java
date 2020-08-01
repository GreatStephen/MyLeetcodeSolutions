class Solution {
    public boolean isValid(String s) {
        List<Character> list = new ArrayList<Character>();
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)=='(') list.add(0, s.charAt(i));
            else if(s.charAt(i)=='[') list.add(0, s.charAt(i));
            else if(s.charAt(i)=='{') list.add(0, s.charAt(i));
            else if(s.charAt(i)==')'){
                if(list.size()==0 || list.get(0)!='(') return false;
                else list.remove(0);
            }
            else if(s.charAt(i)==']'){
                if(list.size()==0 || list.get(0)!='[') return false;
                else list.remove(0);
            }
            else if(s.charAt(i)=='}'){
                if(list.size()==0 || list.get(0)!='{') return false;
                else list.remove(0);
            }
        }
        if(list.size()!=0) return false;
        return true;
        
    }
}