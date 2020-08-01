class Solution {
    public int largestRectangleArea(int[] heights) {
        // if println() too much data, it may exceed the time limit

        Stack<Integer> stack = new Stack<Integer>();
        int max = 0;
        int length = heights.length;

        for(int i=0; i<length; i++){
            while(!stack.isEmpty() && heights[stack.peek()]>=heights[i]){
                int temp_height_index = stack.pop();
                int temp_index = stack.isEmpty()?-1:stack.peek();
                max = Math.max(max, (i-1-temp_index)*heights[temp_height_index]);
            }
            stack.push(i);
        }


        while(!stack.isEmpty()){
            int temp_height_index = stack.pop();
            int temp_index = stack.isEmpty()?-1:stack.peek();
            max = Math.max(max, (heights.length-1-temp_index)*heights[temp_height_index]);
        }

        return max;
    }
}