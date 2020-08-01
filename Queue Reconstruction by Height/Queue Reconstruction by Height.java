
class Solution {
    public int[][] reconstructQueue(int[][] people) {
        // first sort as descending h and ascending k
        Arrays.sort(people, new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2){
                if(o1[0]!=o2[0]){
                    // h descending order, let o2-o1
                    return o2[0]-o1[0];
                }
                else{
                    // k ascending order, default o1-o2
                    return o1[1]-o2[1];
                }
            }
        });

        // for(int i=0; i<people.length; i++){
        //     System.out.println(Arrays.toString(people[i]));
        // }

        // then insert into list as array order, [1] is the current index
        List<int[]> list = new ArrayList();
        for(int i=0; i<people.length; i++){
            list.add(people[i][1], people[i]);
        }

        int n = people.length;
        return list.toArray(new int[n][2]);
    }
}