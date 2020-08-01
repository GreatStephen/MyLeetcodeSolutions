class Solution {
    List<Integer> ans = new ArrayList();
    public List<Integer> countSmaller(int[] nums) {
        // [[value, original index, count]]
        // mergesort this data[][], then use the original index and count 
        //  to build the answer
        if(nums.length==0) return ans;
        int[][] data = new int[nums.length][3];
        for(int i=0; i<nums.length; i++){
            data[i][0] = nums[i];
            data[i][1] = i;
            data[i][2] = 0;
        }

        data = mergesort(data, 0, data.length-1);

        int[] ans_arr = new int[nums.length];
        for(int[] item: data){
            ans_arr[item[1]] = item[2];
        }
        for(int res: ans_arr){
            ans.add(res);
        }

        return ans;
    }

    private int[][] mergesort(int[][] data, int left, int right){
        if(left==right) return data;

        int mid = left + (right-left)/2;
        data = mergesort(data, left, mid);
        data = mergesort(data, mid+1, right);

        int[][] temp = new int[right-left+1][3];
        int idx = 0;
        int count = 0;
        int lp = left, rp = mid+1;
        while(lp<=mid && rp<=right){
            // merge
            if(data[lp][0]<=data[rp][0]){
                // left[], add count to [][2]
                data[lp][2]+=count;
                temp[idx++] = data[lp++];
            }
            else{
                // right[], count++
                count++;
                temp[idx++] = data[rp++];
            }                      
        }

        // deal with the remaining
        if(lp>mid){
            // right[] remains
            int idx2 = 0;
            for(int i=left; i<rp; i++){
                data[i] = temp[idx2++];
            }
        }
        else if(rp>right){
            // left[] remains
            while(idx<right-left+1){
                data[lp][2]+=count;
                temp[idx++] = data[lp++];
            }
            idx = 0;
            for(int i=left; i<=right; i++){
                data[i] = temp[idx++];
            }
        }

        return data;
    }
}