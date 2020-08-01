class Solution {
    private static int HALF_INT_MIN = -1073741824;
    public int divide(int dividend, int divisor) {
        // add power of 2, with bit-shifting
        // convert to negative, in case of overflow [-2^31, 2^31-1]
        if (dividend == -2147483648 && divisor == -1) {
            return 2147483647;
        }
        int num_of_neg = 0;
        if(dividend<0){
            num_of_neg++;
        }
        else{
            dividend = -dividend;
        }

        if(divisor<0){
            num_of_neg++;
        }
        else{
            divisor = -divisor;
        }

        int ans = 0;
        // find the max exponent
        int exp = 1;
        int temp_divisor = divisor;
        int temp_dividend = dividend;
        while(temp_divisor>=HALF_INT_MIN && temp_divisor+temp_divisor>=temp_dividend){
            temp_divisor += temp_divisor;
            exp += exp;
        }
        System.out.println(exp);
;
        while(divisor>=temp_dividend){
            
            //if(exp==0) break;
            if(temp_divisor>=temp_dividend){
                ans += exp;
                temp_dividend-=temp_divisor;
            }   
            exp>>=1;
            temp_divisor>>=1;     
            if(exp==0) break;   
        }

        return num_of_neg==1?-1*ans: ans;
    }
}