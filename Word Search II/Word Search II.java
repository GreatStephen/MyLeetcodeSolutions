class Solution {
    List<String> ans = new ArrayList();
    public List<String> findWords(char[][] board, String[] words) {
        // Trie and backtracking, very clear structure
        // build Trie
        TrieNode root = new TrieNode();
        for(String word: words){
            TrieNode node = root;
            for(int i=0; i<word.length(); i++){
                char c = word.charAt(i);
                if(node.children.containsKey(c)){
                    // go down a level
                    node = node.children.get(c);
                }
                else{
                    TrieNode new_node = new TrieNode();
                    node.children.put(c, new_node);
                    node = new_node;
                }
            }
            // the last node of the word contains the string
            node.word = word;
        }

        // backtracking
        for(int i=0; i<board.length; i++){
            for(int j=0; j<board[0].length; j++){
                if(root.children.containsKey(board[i][j])){
                    backtracking(i, j, root, board);
                }
            }
        }

        return ans;
    }

    private void backtracking(int i, int j, TrieNode last_node, char[][] board){
        int[] row_offset = new int[]{-1,0,1,0};
        int[] col_offset = new int[]{0,1,0,-1};
        char c = board[i][j];
        //if(c=='*') return; // repeated path

        // get the Trie node for this letter
        TrieNode node = last_node.children.get(c);
        if(node.word!=null){
            // found an existing word
            ans.add(new String(node.word));
            // delete this word to prune, optimization
            node.word = null;
        }

        // mark as read
        board[i][j] = '*';

        for(int offset=0; offset<4; offset++){
            // up, right, down, left
            int new_i=i+row_offset[offset];
            int new_j=j+col_offset[offset];
            if(new_i>=0 && new_i<board.length && new_j>=0 && new_j<board[0].length){
                if(node.children.containsKey(board[new_i][new_j])){
                   backtracking(new_i, new_j, node, board); 
                }
            }
        }

        // recover the matrix from '*'
        board[i][j] = c;
    }
}

class TrieNode {
    HashMap<Character, TrieNode> children = new HashMap<Character, TrieNode>();
    String word = null;
    public TrieNode() {}
}