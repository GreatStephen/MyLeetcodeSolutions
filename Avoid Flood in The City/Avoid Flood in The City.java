
class Solution {
    public int[] avoidFlood(int[] rains) {
        HashMap<Integer, Integer> map = new HashMap();
        ArrayList<Integer> zerolist = new ArrayList();

        int[] ans = new int[rains.length];
        for(int i=0; i<rains.length; i++){
            if(rains[i]!=0){
                ans[i]=-1;
                if(map.containsKey(rains[i])){
                    int pos = map.get(rains[i]);
                    int j=0;
                    while(!zerolist.isEmpty() && j<zerolist.size() && zerolist.get(j)<pos){
                        j++;
                        
                    }
                    // invalid
                    if(j==zerolist.size()) return new int[0];

                    // valid
                    int zero_pos = zerolist.get(j);
                    ans[zero_pos] = rains[i];
                    map.put(rains[i], i);
                    zerolist.remove(j);
                } 
                else{
                    map.put(rains[i], i);
                }
            }
            else{
                ans[i]=1;
                zerolist.add(i);
            }
            // System.out.println(map);
            // System.out.println(zerolist);
        }

        return ans;
    }
}

//[2,3,0,0,3,1,0,1,0,2,2]