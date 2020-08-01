class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        // Divide and Conquer, [0, n/2-1] and [n/2, n-1], then merge like mergesort
        if(buildings.length==0){
            return new ArrayList();
        } 
        int n = buildings.length;
        List<List<Integer>> left_list = recurSkyline(buildings, 0, n/2-1);
        List<List<Integer>> right_list = recurSkyline(buildings, n/2, n-1);
        System.out.println(left_list);

        List<List<Integer>> ans = mergeSkyline(left_list, right_list);
        return ans;
    }

    private List<List<Integer>> recurSkyline(int[][] buildings, int left, int right){
        if(left>right) return null;
        if(left==right){
            // exit, return the List for a single building
            List<List<Integer>> res = new ArrayList();
            // points = [left, right, height]
            int[] points = buildings[left];
            List<Integer> p1 = new ArrayList(){{
                add(points[0]);
                add(points[2]);
            }};
            List<Integer> p2 = new ArrayList(){{
                add(points[1]);
                add(0);
            }};
            res.add(p1);
            res.add(p2);

            return res;
        }
        else{
            // Divide and Conquer
            int mid = left+(right-left)/2;
            List<List<Integer>> left_list = recurSkyline(buildings, left, mid);
            List<List<Integer>> right_list = recurSkyline(buildings, mid+1, right);
            List<List<Integer>> res = mergeSkyline(left_list, right_list);
            return res;
        }
    }

    private List<List<Integer>> mergeSkyline(List<List<Integer>> left_list, List<List<Integer>> right_list){
        if(left_list==null) return right_list;
        if(right_list==null) return left_list;

        int left_idx=0, right_idx=0;
        int left_height=0, right_height=0;
        List<List<Integer>> ans = new ArrayList();

        while(left_idx<left_list.size() && right_idx<right_list.size()){
            List<Integer> left_point = left_list.get(left_idx);
            List<Integer> right_point = right_list.get(right_idx);
            if(left_point.get(0)<right_point.get(0)){
                // left point comes first
                left_height = left_point.get(1);
                int max_height = Math.max(left_height, right_height);
                if(ans.isEmpty() || max_height!=ans.get(ans.size()-1).get(1)){
                    List<Integer> temp = new ArrayList();
                    temp.add(left_point.get(0));
                    temp.add(max_height);
                    ans.add(temp);
                }
                left_idx++;
            }
            else if(left_point.get(0)>right_point.get(0)){
                // right point comes first
                right_height = right_point.get(1);
                int max_height = Math.max(left_height, right_height);
                if(ans.isEmpty() || max_height!=ans.get(ans.size()-1).get(1)){
                    List<Integer> temp = new ArrayList();
                    temp.add(right_point.get(0));
                    temp.add(max_height);
                    ans.add(temp);
                }
                right_idx++;
            }
            else{
                // overlap
                left_height = left_point.get(1);
                right_height = right_point.get(1);
                int max_height = Math.max(left_height, right_height);
                if(ans.isEmpty() || max_height!=ans.get(ans.size()-1).get(1)){
                    List<Integer> temp = new ArrayList();
                    temp.add(left_point.get(0));
                    temp.add(max_height);
                    ans.add(temp);
                }
                left_idx++;
                right_idx++;
            }            
        }

        // if right_list remains, append it to the list
        if(left_idx==left_list.size()){
            // append remaining right_list
            while(right_idx<right_list.size()){
                ans.add(right_list.get(right_idx++));
            }
        }

        // if left_list remains, append it to the list
        if(right_idx==right_list.size()){
            // append remaining left_list
            while(left_idx<left_list.size()){
                ans.add(left_list.get(left_idx++));
            }
        }

        // return the merge result
        return ans;
    }
}