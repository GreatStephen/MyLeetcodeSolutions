class Solution {
    public int reverse(int x) {
        StringBuilder sb = new StringBuilder();
        if(x<0){
            sb.append("-");
            x*=-1;
        } 
        do{
            sb.append(String.valueOf(x%10));
            x /= 10;
        }while(x!=0);
        try{
            return Integer.parseInt(sb.toString());
        } catch(Exception e){
            return 0;
        }
    }
}