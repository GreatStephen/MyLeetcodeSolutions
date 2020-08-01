class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList();
        for(int i=0; i<numRows; i++){
            List<Integer> list = new ArrayList();
            list.add(1);
            if(i==0){
                ans.add(list);
                continue;
            }
            List<Integer> prev = ans.get(ans.size()-1);
            for(int j=1; j<i+1; j++)
                list.add(prev.get(j-1) + (j>=prev.size()?0:prev.get(j)));
            ans.add(list);
        }
        return ans;
    }
}