import java.util.HashMap;

class Solution {
    HashMap<Integer, ArrayList<String>> map;
    HashMap<String, Boolean> visited;

    public int longestStrChain(String[] words) {
        map = new HashMap<>();
        visited = new HashMap<>();
        int min_length=words[0].length();
        int max_length=words[0].length();

        for(String word:words){
            min_length = Math.min(min_length, word.length());
            max_length = Math.max(max_length, word.length());
            ArrayList<String> item = map.getOrDefault(word.length(), new ArrayList<String>());
            item.add(word);
            map.put(word.length(), item);

            boolean b = false;
            visited.put(word, b);
        }
        // System.out.println(map);

        int res=0;
        for(int i=min_length; i<=max_length; i++){
            res = Math.max(res, backtrack("", i, 0));
        }
        return res;
    }

    private boolean isOneCharacterDif(String short_s, String long_s){
        for(int i=0; i<long_s.length(); i++){
            String temp = long_s.substring(0, i) + long_s.substring(i+1);
            if(short_s.compareTo(temp)==0) return true;
        }
        return false;
    }

    private int backtrack(String prev, int length, int chain_length){
        ArrayList<String> list = map.getOrDefault(length, null);
        if(list == null) return chain_length;
        int MAX=chain_length;
        for(String s : list){
            if(prev.length()==0 && ! visited.get(s)){
                visited.put(s, true);
                int temp_length = backtrack(s, length+1, chain_length+1);
                MAX = Math.max(MAX, temp_length);
            }
            else if(isOneCharacterDif(prev, s)){
                visited.put(s, true);
                int temp_length = backtrack(s, length+1, chain_length+1);
                MAX = Math.max(MAX, temp_length);
            }
        }
        return MAX;
    }
}