class Solution {
    public List<List<Integer>> permute(int[] nums) {
        if(nums.length==0){
            List<Integer> temp = new ArrayList<Integer>();
            List<List<Integer>> res = new ArrayList<List<Integer>>();
            res.add(temp);
            return res;
        } 
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int num : nums) list.add(num);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        
        traverse(list, res);
        return res;
    }
    
    public void traverse(ArrayList<Integer> list, List<List<Integer>> res){
        if(list.isEmpty()) return;
        List<Integer> last_per = res.isEmpty()?null:res.get(res.size()-1);
        if(!res.isEmpty()) res.remove(res.size()-1);
        
        for(int i=0; i<list.size(); i++){
            int temp_num = list.get(i);
            list.remove(i);
            // create a deep copy of last_per to new_list
            List<Integer> new_list = new ArrayList<Integer>();
            if(last_per!=null) for(int num:last_per) new_list.add(num);
            // append the temp_num to the last of new_list
            new_list.add(temp_num);
            res.add(new_list);
            // recursion
            traverse(list, res);
            list.add(i, temp_num);
        }
    }
}