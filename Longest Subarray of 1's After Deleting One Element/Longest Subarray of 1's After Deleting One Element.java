class Solution {
    public int longestSubarray(int[] nums) {
        List<int[]> list = new ArrayList();
        int num_1 = 0;
        int num_0 = 0;

        for(int num: nums){
            if(num==0){
                if(num_1!=0){
                    list.add(new int[]{num_1, num_0});
                    num_1=0;
                    num_0=0;
                }
                num_0++;
            }
            else if(num==1){
                num_1++;
            }
        }
        if(num_1!=0){
            list.add(new int[]{num_1, num_0});
        }

        // for(int[] arr: list)
        //     System.out.println(Arrays.toString(arr));
        if(list.isEmpty()) return 0;
        if(list.size()==1){
            int[] item = list.get(0);
            if(item[1]-1>=0 || num_0>0) return item[0];
            else return item[0]-1;
        }

        int ans = 0;
        while(list.size()>=2){
            int[] prev = list.get(0);
            int[] post = list.get(1);
            if(post[1]==1) ans = Math.max(ans, prev[0]+post[0]);
            else ans = Math.max(ans, Math.max(prev[0], post[0]));
            list.remove(0);
        }

        return ans;
    }
}