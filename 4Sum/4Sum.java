class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        if(nums.length<4) return new ArrayList();
        List<List<Integer>> ans = new ArrayList();
        Arrays.sort(nums);
        for(int i=0; i<nums.length-3; i++){
            if(i>0 && nums[i]==nums[i-1]) continue;
            if(4*nums[i]>target) break;
            ans.addAll(three(nums, i+1, target-nums[i], nums[i]));
        }
        return ans;
    }

    public List<List<Integer>> three(int[] nums, int start, int target, int first_num) {
        List<List<Integer>> ans = new ArrayList();
        for(int i=start; i<nums.length-2; i++){
            if(i>start && nums[i]==nums[i-1]) continue;
            int l = i+1, r = nums.length-1;
            while(l<r){
                int sum = nums[i]+nums[l]+nums[r];
                if(sum<target){
                    while(l<r&&nums[l]==nums[l+1]) l++;
                    l++;
                }
                else if(sum>target){
                    while(l<r&&nums[r]==nums[r-1]) r--;
                    r--;
                }
                else{
                    List<Integer> list = new ArrayList();
                    list.add(first_num);
                    list.add(nums[i]);
                    list.add(nums[l]);
                    list.add(nums[r]);
                    ans.add(list);
                    while(l<r&&nums[l]==nums[l+1]) l++;
                    l++;
                    while(l<r&&nums[r]==nums[r-1]) r--;
                    r--;
                }
            }
        }
        return ans;
    }
}