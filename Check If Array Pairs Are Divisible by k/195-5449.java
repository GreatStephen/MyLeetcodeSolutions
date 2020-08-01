class Solution {
    public boolean canArrange(int[] arr, int k) {
        List<Integer> list = new ArrayList();
        for(int num: arr) list.add(num);
        // System.out.println(list.size());
        return DFS(list, k);
    }

    private boolean DFS(List<Integer> list, int k){
        // System.out.println(list);
        if(list.isEmpty()) return true;
        int num1 = list.get(0);
        list.remove(0);
        for(int i=0; i<list.size(); i++){
            int num2 = list.get(i);
            // System.out.println(num2);
            if((num2+num1) % k ==0){
                
                list.remove(i);
                // System.out.println(list.size());
                boolean res = DFS(list, k);
                if(res) return true;
                // System.out.println(list.size());
                // System.out.println(num1);
                list.add(i,num2);
            }
        }
        list.add(0, num1);
        return false;
    }
}