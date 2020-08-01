
class Solution {
    List<int[]> temp_list = new ArrayList();
    public int minNumberOfSemesters(int n, int[][] dependencies, int k) {
        int[] indegree = new int[n+1];
        Arrays.fill(indegree, 0);
        HashMap<Integer, Set<Integer>> map = new HashMap();
        for(int i=1; i<=n; i++){
            map.put(i,new HashSet());
        }
        for(int[] d: dependencies){
            Set<Integer> temp = map.get(d[0]);
            if(!temp.contains(d[1])){
                temp.add(d[1]);
                map.put(d[0], temp);
            }
            indegree[d[1]]++;
        }

        int count=0;
        int ans = 0;
        while(count<n){
            findTempList(indegree, map);
            if(temp_list.size()>k){
                Collections.sort(temp_list, new Comparator(){
                    @Override
                    public int compare(Object o1, Object o2){
                        int[] n1 = (int[])o1;
                        int[] n2 = (int[])o2;
                        return n2[1]-n1[1];
                    }
                });

                // greedy, if >k elements are chosen, choose the ones with maximum out-degree
                while(temp_list.size()>k){
                    int[] back = temp_list.get(temp_list.size()-1);
                    indegree[back[0]]=0;
                    temp_list.remove(temp_list.size()-1);
                }
            }
            count+=temp_list.size();
            for(int[] c: temp_list){
                Set<Integer> set = map.get(c[0]);
                for(int next: set) indegree[next]--;
            }
            temp_list = new ArrayList();

            ans++;
        }

        return ans;
    }

    private void findTempList(int[] indegree, HashMap<Integer, Set<Integer>> map){
        for(int i=1; i<indegree.length; i++){
            if(indegree[i]==0){
                Set<Integer> set = map.get(i);
                temp_list.add(new int[]{i, set.size()});
                indegree[i] = -1;
            }
        }
    }
}