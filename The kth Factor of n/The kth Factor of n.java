
// class Solution {
//     public int kthFactor(int n, int k) {
//         List<Integer> list = new ArrayList();
//         list.add(1);

//         int cur = 2;
//         int remain = n;
//         while(remain!=1){
//             if(remain%cur==0){
//                 if(list.get(list.size()-1)<cur){
//                     list.add(cur);
//                 }     
//                 remain /= cur;
//             }
//             else{
//                 cur++;
//             }
//         }
//         // System.out.println(list);


//         return 0;
//     }
// }

class Solution{
    public int kthFactor(int n, int k){
        int count = 1;
        int ans = 0;

        int cur = 1;
        while(cur<=n){
            if(n%cur==0){
                ans = cur;
                count++;
                if(count>k) return ans;
            }
        }
        return -1;
    }
}