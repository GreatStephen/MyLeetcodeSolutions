
class Solution {
    public int maximalRectangle(char[][] matrix) {
        // dp maximum height solution
        if(matrix.length==0){
            return 0;
        }
        int r = matrix.length;
        int c = matrix[0].length;
        int[] height = new int[c];
        int[] left = new int[c];
        int[] right = new int[c];

        int max = 0;
        Arrays.fill(right, c);

        for(int i=0; i<r; i++){
            // update height
            for(int j=0; j<c; j++){
                if(matrix[i][j]=='1'){
                    height[j]++;
                }
                else{
                    height[j]=0;
                }
            }

            // update left
            // cur_left = current left side of current rectangle in current row
            int cur_left=0;
            for(int j=0; j<c; j++){
                if(matrix[i][j]=='0'){
                    left[j] = 0;
                    cur_left = j+1;
                }
                else{
                    left[j] = Math.max(left[j], cur_left);
                }
            }

            // update right
            int cur_right=c;
            for(int j=c-1; j>=0; j--){
                if(matrix[i][j]=='0'){
                    cur_right = j;
                    right[j] = c;
                }
                else{
                    right[j] = Math.min(right[j], cur_right);
                }
            }

            // compute max
            for(int j=0; j<c; j++){
                max = Math.max(max, height[j]*(right[j]-left[j]));
            }
        }

        return max;
    }
}