/* The knows API is defined in the parent class Relation.
      boolean knows(int a, int b); */

      public class Solution extends Relation {
        public int findCelebrity(int n) {
            // smart O(n) idea, not actually an algorithm
            
            // find a candidate
            int cur = 0;
            int target = 1;
            for(int i=0; i<n-1; i++){
                if(knows(cur, target)){
                    cur = target;
                }
                else{

                }
                target++;
            }

            // check if this candidate is a celebrity
            for(int i=0; i<n; i++){
                if(i==cur) continue;
                if(!knows(i, cur) || knows(cur, i)) return -1;
            }
            return cur;
        }
    }