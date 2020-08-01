import java.util.Arrays;

class Solution {
    public boolean isPalindrome(String s) {
        int i=0, j=s.length()-1;
        String alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
        String number="1234567890";
        while(i<j){
            while(!alphabet.contains(Character.toString(s.charAt(i)) ) && !number.contains(Character.toString(s.charAt(i)) )){
                i++;
                if(i>s.length()-1) return true;
            } 
            while(!alphabet.contains(Character.toString(s.charAt(j))) && !number.contains(Character.toString(s.charAt(j)))){
                j--;
                if(j<0) return true;
            } 
            System.out.println("left="+s.charAt(i)+"right="+s.charAt(j));
            if(alphabet.contains(Character.toString(s.charAt(i))) && number.contains(Character.toString(s.charAt(j)))) return false;
            else if(alphabet.contains(Character.toString(s.charAt(j))) && number.contains(Character.toString(s.charAt(i)))) return false;
            else if(Math.abs(s.charAt(i)-s.charAt(j)) != 32 && s.charAt(i)!=s.charAt(j)) return false;
            else{
                i++;
                j--;
            }
        }
        return true;
    }
}