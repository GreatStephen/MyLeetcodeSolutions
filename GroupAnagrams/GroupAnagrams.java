import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs.length==0) return new ArrayList();
        Map<String,List> map = new HashMap<>();
        int[] count = new int[26];
        for(String str : strs){
            Arrays.fill(count, 0);
            char[] chars = str.toCharArray();
            for(char c : chars) count[c-'a']++;

            String key = Arrays.toString(count);
            if(!map.containsKey(key)) map.put(key,new ArrayList());
            map.get(key).add(str);
        }

        return new ArrayList(map.values());
    }