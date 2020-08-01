package LSWRC;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Resolution {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();


        System.out.println(lengthOfLongestSubstring(s));
    }
    static public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map =new HashMap<>();
        int index=0;
        int j=0;
        int maxlength=0;
        for(j=0;j<s.length();j++){
            if(map.containsKey(s.charAt(j))){
                index=Math.max(map.get(s.charAt(j))+1, index);
            }
            maxlength=Math.max(maxlength, j-index+1);
            map.put(s.charAt(j),j);
        }
        return maxlength;
    }
}
