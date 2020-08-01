import java.util.HashMap;

class Solution {
    public int myAtoi(String str) {
        int index=0;
        int state=0;
        int flag=1;
        int value=0;
        /*  0:whitespace
            1:+-
            2:number
            3:other characters
        */
        HashMap<Character,Integer> map = new HashMap<>();
        map.put('0', 0);
        map.put('1', 1);
        map.put('2', 2);
        map.put('3', 3);
        map.put('4', 4);
        map.put('5', 5);
        map.put('6', 6);
        map.put('7', 7);
        map.put('8', 8);
        map.put('9', 9);
        while(index<str.length()){
            if(state==0){
                if(str.charAt(index)==' ') index++;
                else state=1;
            }
            if(state==1){
                if(str.charAt(index)!='+' && str.charAt(index)!='-'){
                    state=2;
                } 
                else{
                    if(str.charAt(index)=='+'){
                        flag=1;
                        index++;
                        state=2;
                    } 
                    else if(str.charAt(index)=='-'){
                        flag=-1;
                        index++;
                        state=2;
                    } 
                    else state=3;
                    
                } 
            }
            if(state==2){
                if(index>str.length() || !map.containsKey(str.charAt(index))) state=3;
                else{ 
                    if(map.get(str.charAt(index))>Integer.MAX_VALUE/10-value){
                        return flag==1?Integer.MAX_VALUE:Integer.MIN_VALUE;
                    }
                    else value = value*10+map.get(str.charAt(index));
                    index++;
                }
            }
            if(state==3){
                break;
            }
        }
        return value*flag;
    }
}