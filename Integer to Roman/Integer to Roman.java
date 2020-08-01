class Solution {
    public String intToRoman(int num) {
        int[] val = new int[]{1000,900,500,400,100,90,50,40,10,9,5,4,1};
        String[] sym = new String[]{"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};

        int idx = 0;
        StringBuilder sb = new StringBuilder();
        while(num>0){
            if(val[idx]>num){
                idx++;
                continue;
            }
            else{
                sb.append(sym[idx]);
                num-=val[idx];
            }
        }
        return sb.toString();
    }
}