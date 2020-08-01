class Solution {
    public String[] getFolderNames(String[] names) {
        //HashSet<String> set = new HashSet();
        ArrayList<String> reslist = new ArrayList();
        HashMap<String, Integer> map = new HashMap();

        // for(String str: names){
        //     if(!set.contains(str)){
        //         set.add(str);
        //         reslist.add(str);
        //         continue;
        //     }
        //     int k=1;
        //     String temp = str+"("+k+")";
        //     while(set.contains(temp)){
        //         k++;
        //         temp = str+"("+k+")";

        //     }
        //     set.add(temp);
        //     reslist.add(temp);
        // }

        // String res[] = new String[reslist.size()];
        // return reslist.toArray(res);

        for(String str: names){
            if(!map.containsKey(str)){
                map.put(str, 1);
                reslist.add(str);
                continue;
            }

            int times = map.get(str);
            //++times;
            String temp = str+"("+times+")";
            while(map.containsKey(temp)){
                // times = map.get(temp);
                ++times;
                temp = str+"("+times+")";
                //System.out.println(temp);
            }
            reslist.add(temp);
            map.put(temp, 1);
            map.put(str, ++times);
        }
        String res[] = new String[reslist.size()];
        return reslist.toArray(res);
    }
}

//["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]
