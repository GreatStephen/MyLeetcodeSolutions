class Solution {
    public double myPow(double x, int n) {
        // use long in case n = -INFINITY = 2^-31
        // 2^31 can not be represented by 32-bit int. +INFINITY = 2^31-1. So use long int.
        long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        double ans = 1;
        double current_product = x;
        for (long i = N; i > 0; i /= 2) {
            if ((i % 2) == 1) {
                ans = ans * current_product;
            }
            current_product = current_product * current_product;
        }
        return ans;
    }
};