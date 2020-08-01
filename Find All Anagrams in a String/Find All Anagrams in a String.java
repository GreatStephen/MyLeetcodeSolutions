import java.util.Map;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int ns = s.length(), np = p.length();
        if (ns < np) return new ArrayList();

        List<Integer> list = new ArrayList();
        Map<Character, Integer> p_map = new HashMap();
        Map<Character, Integer> temp_map = new HashMap();

        // build p map
        for(char c: p.toCharArray()){
            p_map.put(c, p_map.getOrDefault(c, 0)+1);
        }

        for(int i=0; i<ns; i++){
            // add one letter
            char c = s.charAt(i);
            temp_map.put(c, temp_map.getOrDefault(c, 0)+1);

            // remove one letter
            if(i>=np){
                char prev_c = s.charAt(i-np);
                if(temp_map.get(prev_c)==1){
                    temp_map.remove(prev_c);
                }
                else{
                    temp_map.put(prev_c, temp_map.get(prev_c)-1);
                }
            }

            // compare the 2 hashmaps
            if(temp_map.equals(p_map)){
                list.add(i-np+1);
            }
        }

        return list;
    }
}