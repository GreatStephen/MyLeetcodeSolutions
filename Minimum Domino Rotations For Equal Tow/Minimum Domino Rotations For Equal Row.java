class Solution {
    public int minDominoRotations(int[] A, int[] B) {
        int A_rotate = 0, B_rotate = 0, mutual=0;
        int res = -1;
        int[] alltarget = new int[]{A[0], B[0]};
        for(int i=0; i<=1; i++){
            // iterate twice
            int target = alltarget[i];
            A_rotate = 0; 
            B_rotate = 0;
            mutual=0;
            // temp_rotate is the minimum number of rotatation
            int temp_rotate=0;
            for(int j=0; j<A.length; j++){
                if(A[j]==target && B[j]==target) mutual++;
                else if(A[j]==target && B[j]!=target) A_rotate++;
                else if(A[j]!=target && B[j]==target) B_rotate++;
            }
            if(A_rotate + B_rotate + mutual == A.length){
                temp_rotate = Math.min(A_rotate, B_rotate);
                res = res<0?temp_rotate: Math.min(res, temp_rotate);
                // if(res<0) res = temp_rotate;
                // else res = Math.min(res, temp_rotate);
            }
            
        }
        return res;
    }
}