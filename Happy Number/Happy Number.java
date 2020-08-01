class Solution {
    public boolean isHappy(int n) {
        int temp = n;
        Set<Integer> set = new HashSet<>();
        do{
            int temp_sum=0;
            while(temp!=0){
                temp_sum+=Math.pow(temp%10, 2);
                temp/=10;
            }
            temp=temp_sum;
            if(temp==1) return true;
            if(set.contains(temp)) return false;
            else set.add(temp);
        }while(temp!=n);
        return false;
    }
}