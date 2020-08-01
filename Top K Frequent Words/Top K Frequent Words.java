import java.util.PriorityQueue;

class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> count = new HashMap();
        for (String word: words) {
            count.put(word, count.getOrDefault(word, 0) + 1);
        }
        PriorityQueue<String> heap = new PriorityQueue<String>(
            (w1, w2) -> count.get(w1).equals(count.get(w2)) ?
            w2.compareTo(w1) : count.get(w2) - count.get(w1) 
        );

        for (String word: count.keySet()) {
            heap.offer(word);
        }

        List<String> ans = new ArrayList();
        for(int i=0; i<k; i++)
            ans.add(heap.poll());
        return ans;
    }
}