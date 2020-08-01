class Solution {
    public int[][] kClosest(int[][] points, int K) {
        Arrays.sort(points, (p1, p2)->{
            int sum1 = Math.pow(p1[0], 2) + Math.pow(p1[1], 2);
            int sum2 = Math.pow(p2[0], 2) + Math.pow(p2[1], 2);
            if(sum1 < sum2) return -1;
            else if(sum1 == sum2) return 0;
            else return 1;
        });

        int[][] res = new int[K][2];
        for(int i=0; i<K; i++){
            res[i] = points[i];
        }
        return res;
    }
}