class Solution {
    public boolean isAnagram(String s, String t) {
        // this one is a special hash method, very fast
        int[] counter = new int[26];
        Arrays.fill(counter, 0);

        for(char c: s.toCharArray()){
            counter[c-'a']++;
        }
        for(char c: t.toCharArray()){
            counter[c-'a']--;
        }

        for(int num: counter){
            if(num!=0) return false;
        }
        return true;
    }
}