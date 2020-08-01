class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack();
        boolean exist = true;
        for (int ast: asteroids) {
            exist = true;
            while (!stack.isEmpty() && ast < 0 && stack.peek()>0) {
                if ( stack.peek() < -ast) {
                    stack.pop();
                }
                else if(stack.peek() == -ast){
                    stack.pop();
                    exist=false;
                    break;
                }
                else{
                    exist=false;
                    break;
                } 
            }
            if(exist) stack.push(ast);
        }

        int[] ans = new int[stack.size()];
        for (int t = ans.length - 1; t >= 0; --t) {
            ans[t] = stack.pop();
        }
        return ans;
    }
}