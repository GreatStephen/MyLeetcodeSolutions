
class Solution {
    private HashMap<Integer, ArrayList<Integer>> adjlist = new HashMap();
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // node in-degree
        int[] indegree = new int[numCourses];
        Arrays.fill(indegree, 0);
        int[] ans = new int[numCourses];

        // initialize adjlist and indegree
        for(int[] edge: prerequisites){
            indegree[edge[0]]++;
            ArrayList<Integer> temp = adjlist.getOrDefault(edge[1], new ArrayList<Integer>());
            temp.add(edge[0]);
            adjlist.put(edge[1], temp);
        }
        
        //System.out.println(adjlist);
        //System.out.println(Arrays.toString(indegree));

        // algorithm
        Deque<Integer> q = new LinkedList();
        for(int i=0; i<numCourses; i++){
            if(indegree[i]==0) q.addLast(i);
        }
        
        //System.out.println(q);

        int index = 0;
        while(!q.isEmpty()){
            int course = q.pollFirst();
            ArrayList<Integer> edges = adjlist.getOrDefault(course, new ArrayList<Integer>());
            for(int next_node: edges){
                indegree[next_node]--;
                if(indegree[next_node]==0) q.addLast(next_node);
            }
            ans[index++] = course;
        }
        
        //System.out.println(Arrays.toString(ans));

        if(index!=numCourses) return new int[0];
        return ans;
    }
}