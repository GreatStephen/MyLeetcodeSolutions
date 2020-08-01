class Solution {
    public double average(int[] salary) {
        int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;
        double n = salary.length;
        double sum = 0;

        for(int num: salary){
            sum+=num;
            max = Math.max(max, num);
            min = Math.min(min, num);
        }

        sum-= max-min;

        return sum/(n-2);
    }
}