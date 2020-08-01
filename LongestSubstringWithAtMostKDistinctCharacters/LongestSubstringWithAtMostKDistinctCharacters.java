import java.util.LinkedHashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if(s.length()==0 || k==0) return 0;
        int left=0, right=0, max_len=0;
        LinkedHashMap<Character, Integer> map = new LinkedHashMap<>();

        while(right<s.length()){
            if(map.containsKey(s.charAt(right))) map.remove(s.charAt(right));
            map.put(s.charAt(right), right++);

            if(map.size()>k){
                Map.Entry<Character,Integer> leftmost = map.entrySet().iterator().next();
                map.remove(leftmost.getKey());
                left=leftmost.getValue()+1;
            }
            max_len = Math.max(max_len, right-left);
        }

        return max_len;
    }
}