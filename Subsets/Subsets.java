// for length = 1 to n, use DFS to build all the possible strings
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>(){{
            add(new ArrayList<Integer>());
        }};
        for(int length=1; length<=nums.length; length++){
            List<Integer> cur_res = new ArrayList<>();
            res = dfs(nums, res, cur_res, 0, length);
        }
        return res;
        
    }

    public List<List<Integer>> dfs(int[] nums, List<List<Integer>> res, List<Integer> cur_res, int index, int length){
        if(length==0){
            List<Integer> cur_res_copy = new ArrayList<>(cur_res);
            res.add(cur_res_copy);
            return res;
        }
        for(int i=index; i<nums.length; i++){
            cur_res.add(nums[i]);
            res = dfs(nums, res, cur_res, i+1, length-1);
            cur_res.remove(cur_res.size()-1);
        }

        return res;
    }
}