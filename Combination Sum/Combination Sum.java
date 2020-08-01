
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        if(candidates.length==0) return null;
        Arrays.sort(candidates);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for(int i=0; i<candidates.length; i++){
            if(candidates[i]<=target){
                ArrayList<Integer> cur_res = new ArrayList<>();
                cur_res.add(candidates[i]);
                res = dfs(candidates, i, target-candidates[i], res, cur_res);
            }
            else break;
        }
        return res;
    }

    public List<List<Integer>> dfs(int[] candidates,int index, int target, List<List<Integer>> res, ArrayList<Integer> cur_res){
        if(target==0){
            ArrayList<Integer> cur_res_copy = new ArrayList<>();
            cur_res_copy.addAll(cur_res);
            res.add(cur_res_copy);
            return res;
        }
        else{
            for(int i=index; i<candidates.length; i++){
                if(candidates[i]<=target){
                    cur_res.add(candidates[i]);
                    res = dfs(candidates, i, target-candidates[i], res, cur_res);
                    cur_res.remove(cur_res.size()-1);
                }
                else break;
            }
        }


        return res;
    }
}