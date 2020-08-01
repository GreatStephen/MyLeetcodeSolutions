import java.util.Set;

class Solution {
    private Set<Integer> set = new HashSet();
        
    // greedy solution, smart
    public int numSquares(int n) {
        // prepare the square numbers
        for(int i=1; i*i<=n; i++){
            set.add(i*i);
        }

        // try greedy
        for(int i=1; i<=n; i++){
            if(isDividedby(n, i)){
                return i;
            }
        }
        return -1;
    }

    private boolean isDividedby(int num, int n){
        // just check if num is a square number
        if(n==1){
            if(set.contains(num)){
                return true;
            }
            else{
                return false;
            }
        }
        // let num subtract a square number, and try (n-1)
        // need to check every square number
        else{
            for(int snum:set){
                if(isDividedby(num-snum, n-1)){
                    return true;
                }
            }
        }
        return false;
    }
}