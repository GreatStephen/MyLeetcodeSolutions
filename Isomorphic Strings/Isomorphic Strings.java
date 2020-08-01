
class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length() != t.length()) return false;
        HashMap<Character, Integer> map1 = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();

        int length = s.length();
        for(int i=0; i<length; i++){
            char curs = s.charAt(i);
            char curt = t.charAt(i);
            if(map1.containsKey(curs) && map2.containsKey(curt)){
                if(map1.get(curs) != map2.get(curt)) return false;
            }
            else if(!map1.containsKey(curs) && !map2.containsKey(curt)){
                map1.put(curs, i+1);
                map2.put(curt, i+1);
            }
            // for Kargo OA, add this else-if
            // else if(!map1.containsKey(curs) && map2.containsKey(curt)){
            //     map1.put(curs, map2.get(curt));
            // }
            else return false;
        }

        return true;
    }
}