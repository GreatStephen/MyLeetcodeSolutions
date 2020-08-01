import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        for(char c: s.toCharArray()){
            map.put(c, map.getOrDefault(c, 0)+1);
        }

        ArrayList<Integer> list = new ArrayList<>();
        for(char key : map.keySet()){
            list.add(map.get(key));
        }
        
        int sum=0;

        for(int i=0; i<list.size(); i++){
            int num = list.get(i);
            if(num%2==0){
                sum+=num;
                list.remove(i);
                i--;
            }
            else{
                sum+=(num-1);
            }
        }
        if(list.size()!=0) sum+=1;

        return sum;
    }
}