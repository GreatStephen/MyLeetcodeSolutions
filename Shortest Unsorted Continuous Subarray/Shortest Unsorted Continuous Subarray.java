class Solution {
    public int findUnsortedSubarray(int[] nums) {
        Stack<Integer> stack = new Stack<Integer>();
        int k1 = nums.length;
        int k2 = -1;

        for(int i=0; i<nums.length; i++){
            if(stack.isEmpty()){
                stack.push(i);
            }
            else{
                if(nums[i]>=nums[stack.peek()]){
                    stack.push(i);
                }
                else{
                    while(!stack.isEmpty() && nums[stack.peek()]>nums[i]){
                        stack.pop();
                    }
                    k1 = Math.min(stack.isEmpty()?-1:stack.peek(), k1);
                }
            }
        }

        for(int j=nums.length-1; j>=0; j--){
            if(stack.isEmpty()){
                stack.push(j);
            }
            else{
                if(nums[j]<=nums[stack.peek()]){
                    stack.push(j);
                }
                else{
                    while(!stack.isEmpty() && nums[stack.peek()]<nums[j]){
                        stack.pop();
                    }
                    k2 = Math.max(k2, stack.isEmpty()?nums.length:stack.peek());
                }
            }
        }

        // System.out.println(k1);
        // System.out.println(k2);

        return k2-k1>0?k2-k1-1:0;
    }
}