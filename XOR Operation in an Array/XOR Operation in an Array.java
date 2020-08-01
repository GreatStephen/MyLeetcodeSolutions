class Solution {
    public int xorOperation(int n, int start) {
        int[] arr = new int[n];
        int res = 0;
        for(int i=0; i<n; i++){
            arr[i] = start + 2*i;
            if(i==0) res = arr[i];
            else res = res^arr[i];
        }

        return res;
    }
}