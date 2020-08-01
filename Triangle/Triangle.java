class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        // DP bottom up
        List<Integer> dp = new ArrayList();
        int index = triangle.size()-1;
        for(int num: triangle.get(index--)) dp.add(num);

        while(index>=0){
            List<Integer> layer = triangle.get(index);
            for(int i=0; i<index+1; i++){
                int temp = layer.get(i) + Math.min(dp.get(i), dp.get(i+1));
                dp.set(i, temp);
            }
            index--;
            dp.remove(dp.size()-1);
        }

        return dp.get(0);
    }
}