class Solution {
    // <bitmap, index>
    HashMap<Integer, Integer> map = new HashMap();
    public int[] prisonAfterNDays(int[] cells, int N) {
        // fast forwarding, record the state as a bitmap
        int cur_idx = 1;
        int cycle = -1;
        boolean forward = false;
        while(N!=0){
            int cur_state = state(cells);            
            if(!forward){
                if(map.containsKey(cur_state)){
                    cycle = cur_idx - map.get(cur_state);
                    //System.out.println(cycle);
                    N = N%cycle;
                    forward = true;
                    continue;
                }
                else{
                    map.put(cur_state, cur_idx++); 
                }
            }
            N--;   
            cells = next_day(cells);
        }

        return cells;
    }

    private int state(int[] cells){
        int state = 0;
        for(int cell: cells){
            state <<= 1;
            if(cell==1) state++;
        }
        return state;
    }

    private int[] next_day(int[] cells){
        int[] new_cells = new int[cells.length];
        new_cells[0] = 0;
        new_cells[cells.length-1]=0;
        for(int i=1; i<cells.length-1; i++){
            new_cells[i] = cells[i-1]==cells[i+1]?1:0;
        }
        return new_cells;
    }
}