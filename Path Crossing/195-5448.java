class Solution {
    public boolean isPathCrossing(String path) {
        // HashSet<int[]> set = new HashSet();
        HashMap<Integer, Set<Integer>> map = new HashMap();

        int x = 0, y = 0;
        Set<Integer> temp_set = new HashSet();
        temp_set.add(y);
        map.put(x, temp_set);
        for(char c: path.toCharArray()){
            // System.out.println(x);
            if(c=='N') y++;
            else if(c=='E') x++;
            else if(c=='S') y--;
            else if(c=='W') x--;

            Set<Integer> get_set = map.getOrDefault(x, new HashSet());
            if(get_set.contains(y)) return true;
            else{
                get_set.add(y);
                map.put(x, get_set);
            }
        }
        // for(int[] arr:set)
        //     System.out.println(Arrays.toString(arr));
        return false;
    }
}