
class Solution {
    // a logic error in this problem: ["ab","a"] is wrong
    // this problem has a flaw
    public String alienOrder(String[] words) {
        HashMap<Character, HashSet<Character>> adjlist = new HashMap();
        HashMap<Character, Integer> indegree = new HashMap();
        Deque<Character> queue = new LinkedList();
        String ans = "";

        // extract the dependencies
        for(String str: words){
            for(int i=0; i<str.length(); i++){
                if(!indegree.containsKey(str.charAt(i))){
                    indegree.put(str.charAt(i), 0);
                }
            }
        }

        for(int i=0; i<words.length-1; i++){
            for(int j=0; j<Math.min(words[i].length(), words[i+1].length()); j++){
                char c1 = words[i].charAt(j);
                char c2 = words[i+1].charAt(j);
                
                if(c1 != c2){
                    HashSet<Character> temp = adjlist.getOrDefault(c1, new HashSet<Character>());
                    if(temp.contains(c2)) break;
                    temp.add(c2);
                    adjlist.put(c1, temp);
                    indegree.put(c2, Math.max(indegree.get(c2), 0)+1);
                    break;
                }
            }
        }

        // algorithm
        scan(indegree, queue);
        
        while(!queue.isEmpty()){
            //System.out.println(queue);
            char key = queue.pollFirst();
            ans += key;
            HashSet<Character> set = adjlist.getOrDefault(key, new HashSet<Character>());
            subtract(indegree, set);
            scan(indegree, queue);
        }

        return ans;
    }

    private void scan(HashMap<Character, Integer> indegree, Deque<Character> queue){
        for(char key: indegree.keySet()){
            if(indegree.get(key)==0){
                queue.offerLast(key);
                indegree.put(key, -1);
            }
        }
    }

    private void subtract(HashMap<Character, Integer> indegree, HashSet<Character> set){
        for(char c: set){
            indegree.put(c, indegree.get(c)-1);
        }
    }

}