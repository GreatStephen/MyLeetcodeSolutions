
class Solution {
    public int leastInterval(char[] tasks, int n) {
        // sort every n steps. arrange as the descending order.
        int[] arr = new int[26];
        Arrays.fill(arr, 0);
        for(char c: tasks){
            arr[c-'A']++;
        }

        int res=0;
        int counter=0;
        Arrays.sort(arr);
        while(arr[25]>0){
            counter=0;
            while(counter<=n){
                if(arr[25]==0){
                    break;
                }
                res++;
                if(counter<26){
                   arr[25-counter]--; 
                }
                
                counter++;
            }
            Arrays.sort(arr);
        }

        return res;
    }
}