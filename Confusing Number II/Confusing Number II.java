class Solution {
    HashMap<Integer, Integer> map = new HashMap();
    int res = 0;
    public int confusingNumberII(int N) {
        map.put(0,0);
        map.put(1,1);
        map.put(9,6);
        map.put(8,8);
        map.put(6,9);
        helper(N, 0);
        return res;
    }
    
    // 当前数字在个位加上所有confusing number，然后递归
    // 这道题没有回溯，只有递归
    private void helper(int N, long cur){
        if(isCN(cur)){
            res++;
        }
        
        for(int n: map.keySet()){
            long next = cur*10+n;
            if(next>=1 && next<=N){
                helper(N, next);
            }
        }
        
        return;
    }
    
    private boolean isCN(long num){
        long cn = 0;
        long n = num;
        while(n>0){
            cn = cn*10+ map.get((int)n%10);
            n /= 10;
        }
        return num!=cn;
    }
}