import java.util.HashMap;
import java.util.Map;

class Solution {

    Map<Integer, String> magnitude = new HashMap<>();
    Map<Integer, String> numbers = new HashMap<>();    
    Map<Integer, String> tens = new HashMap<>();
    Map<Integer, String> twenties = new HashMap<>();

    public String numberToWords(int num) {
        String s = String.valueOf(num);
        int length = s.length();
        int index = length-1;
        int digit1, digit2, digit3;
        String res="";
        magnitude.put(0, "");
        magnitude.put(1, "Thousand");
        magnitude.put(2, "Million");
        magnitude.put(3, "Billion");
        numbers.put(0, "Zero");
        numbers.put(1, "One");
        numbers.put(2, "Two");
        numbers.put(3, "Three");
        numbers.put(4, "Four");
        numbers.put(5, "Five");
        numbers.put(6, "Six");
        numbers.put(7, "Seven");
        numbers.put(8, "Eight");
        numbers.put(9, "Nine");
        tens.put(10, "Ten");
        tens.put(11, "Eleven");
        tens.put(12, "Twelve");
        tens.put(13, "Thirteen");
        tens.put(14, "Fourteen");
        tens.put(15, "Fifteen");
        tens.put(16, "Sixteen");
        tens.put(17, "Seventeen");
        tens.put(18, "Eighteen");
        tens.put(19, "Nineteen");
        twenties.put(20, "Twenty");
        twenties.put(30, "Thirty");
        twenties.put(40, "Forty");
        twenties.put(50, "Fifty");
        twenties.put(60, "Sixty");
        twenties.put(70, "Seventy");
        twenties.put(80, "Eighty");
        twenties.put(90, "Ninety");

        int count=0;
        while(index>=0){
            digit3=Character.getNumericValue(s.charAt(index--));
            digit2=(index<0)?-1:Character.getNumericValue(s.charAt(index--));
            digit1=(index<0)?-1:Character.getNumericValue(s.charAt(index--));

            String temp = ThreeNumberToWords(digit1, digit2, digit3);
            if(count==0){
                res = temp;
                count++;
            } 
            else if(temp.length()!=0) res=ThreeNumberToWords(digit1, digit2, digit3)+" "+magnitude.get(count++)+(res.length()==0?"":" ")+res;
            else count++;
        }

        return res;
    }

    public String ThreeNumberToWords(int digit1, int digit2, int digit3){
        // --x
        if(digit1==-1 && digit2==-1 && digit3!=-1){
            if(numbers.containsKey(digit3)) return numbers.get(digit3);
            else return "";
        }
        // -xx
        else if(digit1==-1 && digit2!=-1 && digit3!=-1){
            if(digit2==1){
                if(tens.containsKey(digit2*10+digit3)){
                    return tens.get(digit2*10+digit3);
                } 
            } 
            else if(twenties.containsKey(digit2*10+digit3)) return twenties.get(digit2*10+digit3);
            else if(twenties.containsKey(digit2*10)&&numbers.containsKey(digit3)) return twenties.get(digit2*10)+" "+numbers.get(digit3);
            else return "";
        }
        // 0xx
        else if(digit1==0){
            // 000
            if(digit2==0 && digit3==0) return "";
            // 00x
            else if(digit2==0 && digit3!=0) return numbers.get(digit3);
            // 01x
            else if(digit2==1) return tens.get(digit2*10+digit3);
            // 020 030 ... 090
            else if(twenties.containsKey(digit2*10+digit3)) return twenties.get(digit2*10+digit3);
            // 0xx
            else return twenties.get(digit2*10)+" "+numbers.get(digit3);
        }
        // xxx
        else{
            // x00
            if(digit2==0 && digit3==0) return numbers.get(digit1)+" Hundred";
            // x0x
            else if(digit2==0 && digit3!=0) return numbers.get(digit1)+" Hundred "+numbers.get(digit3);
            // x1x
            else if(digit2==1) return numbers.get(digit1)+" Hundred "+tens.get(digit2*10+digit3);
            // x20 x30 ... x90
            else if(twenties.containsKey(digit2*10+digit3)) return numbers.get(digit1)+" Hundred "+twenties.get(digit2*10+digit3);
            // xxx
            else return numbers.get(digit1)+" Hundred "+twenties.get(digit2*10)+" "+numbers.get(digit3);
        }

        return "";
    }
}