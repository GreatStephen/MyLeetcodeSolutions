import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
        for(int i=0; i<numCourses; i++){
            ArrayList<Integer> list = new ArrayList<>();
            map.put(i, list);
        }

        for(int[] relation : prerequisites){
            ArrayList<Integer> list = map.get(relation[0]);
            list.add(relation[1]);
            map.put(relation[0], list);
        }
        // System.out.println(map);

        boolean detected=true;
        while(detected){
            detected = false;
            ArrayList<Integer> start_list = new ArrayList<>();
            for(int key : map.keySet()){
                if(map.get(key).isEmpty()){
                    start_list.add(key);
                }
            }
            for(int index:start_list){
                map.remove(index);
            }
            detected = start_list.isEmpty()? false: true;
            if(!detected) break;
            for(int key:map.keySet()){
                ArrayList<Integer> temp_list = map.get(key);
                temp_list.removeAll(start_list);
                map.put(key, temp_list);
            }

        }

        if(!map.isEmpty()) return false;
        else return true;

    }
}