class Solution {
    // BFS solution

    private int ans = Integer.MAX_VALUE;
    // Queue< [index, depth] >
    private Deque<int[]> q = new LinkedList();
    private Set<Integer> path = new HashSet();
    private int N = 0;

    public int snakesAndLadders(int[][] board) {
        int index = 1;
        N = board.length;
        q.offerLast(new int[]{index, 0});
        path.add(index);
        while(!q.isEmpty()){
//             System.out.println("----------");
//             for(int[] item: q){
//                 System.out.println(Arrays.toString(item));
//             }
            
            int[] q_item = q.pollFirst();
            int cur_index = q_item[0];
            int cur_depth = q_item[1];

            // check if ended
            if(cur_index==N*N){
                // This is BFS, so ans is sure to be minimum
                ans = Math.min(ans, cur_depth);
                return ans;
            } 

            for(int i=1; i<=6; i++){
                int next_index = cur_index+i;
                // don't overflow
                if(next_index>N*N) break;

                int[] next_cor = parse(next_index);
                if(board[next_cor[0]][next_cor[1]]>0){
                    next_index = board[next_cor[0]][next_cor[1]];
                    // don't enter a cycle
                    if(path.contains(next_index)) continue;
                    path.add(next_index);
                } 
                else{
                    // don't enter a cycle
                    if(path.contains(next_index)) continue;
                    path.add(next_index);
                }
                
                q.offerLast(new int[]{next_index, cur_depth+1});
            }
        }
        return -1;

    }

    private int[] parse(int index){
        int[] cor = new int[2];
        cor[0] = (N-1) - (index-1)/N;
        if(N%2==0)
            cor[1] = (cor[0]%2==0)?(N-1)-(index-1)%N:(index-1)%N;
        else    
            cor[1] = (cor[0]%2==1)?(N-1)-(index-1)%N:(index-1)%N;
        return cor;
    }
}