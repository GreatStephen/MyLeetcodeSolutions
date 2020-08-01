class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        for(int i=0; i<order.length(); i++){
            map.put(order.charAt(i), i);
        }
        
        for(int i=0; i<words.length-1; i++){
            // string[i+1] should come later than string[i]
            String s1 = words[i];
            String s2 = words[i+1];
            int index=0;
            while(s1.charAt(index)==s2.charAt(index)){
                index++;
                if(index==s1.length() || index==s2.length()) break;
            } 
            if(index==s1.length()) continue;
            else if(index==s2.length()) return false;
            if(map.get(s2.charAt(index)) < map.get(s1.charAt(index))) return false;
        }
        return true;
        
    }
}