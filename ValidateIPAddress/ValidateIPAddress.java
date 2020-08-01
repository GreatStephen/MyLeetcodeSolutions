class Solution {
    public String validIPAddress(String IP) {
        String IPv4="0123456789";
        String IPv6="0123456789ABCDEFabcdef";

        if(IP.contains(".")){
            if(IP.lastIndexOf('.')+1 == IP.length()) return "Neither";
            String[] numbers=IP.split("\\.");
            if(numbers.length!=4) return "Neither";
            for(int i=0;i<4;i++){
                String num=numbers[i];
                if(num.length()>3 || num.length()==0) return "Neither";
                if(num.length()>1 && num.charAt(0)=='0') return "Neither";
                int value=0;
                for(int j=0;j<num.length();j++){
                    if(IPv4.contains(String.valueOf(num.charAt(j))))
                        value=value*10+(num.charAt(j)-'0');
                    else return "Neither";
                }
                if(value>255) return "Neither";
            }
            return "IPv4";
        } 
        else if(IP.contains(":")){
            if(IP.lastIndexOf(':')+1 == IP.length()) return "Neither";
            String[] numbers=IP.split(":");
            if(numbers.length!=8) return "Neither";
            for(int i=0;i<8;i++){
                String num=numbers[i];
                if(num.length()>4 || num.length()==0) return "Neither";
                for(int j=0;j<num.length();j++) if(!IPv6.contains(String.valueOf(num.charAt(j)))) return "Neither";
            }
            return "IPv6";
        } 
        else return "Neither";

    }
}