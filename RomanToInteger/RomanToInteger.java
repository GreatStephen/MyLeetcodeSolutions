
class Solution {
public int romanToInt(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        map.put('I', 1);
        map.put('V',5);
        map.put('X',10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        int value=0;
        int index=0;
        while(index<s.length()){
            if(index!=s.length()-1 && s.charAt(index)=='I' && s.charAt(index+1)=='V'){
                value+=4;
                index+=2;
            }
            else if(index!=s.length()-1 && s.charAt(index)=='I' && s.charAt(index+1)=='X'){
                value+=9;
                index+=2;
            }
            else if(index!=s.length()-1 && s.charAt(index)=='X' && s.charAt(index+1)=='L'){
                value+=40;
                index+=2;
            }
            else if(index!=s.length()-1 && s.charAt(index)=='X' && s.charAt(index+1)=='C'){
                value+=90;
                index+=2;
            }
            else if(index!=s.length()-1 && s.charAt(index)=='C' && s.charAt(index+1)=='D'){
                value+=400;
                index+=2;
            }
            else if(index!=s.length()-1 && s.charAt(index)=='C' && s.charAt(index+1)=='M'){
                value+=900;
                index+=2;
            }
            else{
                value+=map.get(s.charAt(index));
                index++;
            }
        }

        return value;
    }
};