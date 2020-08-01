class Solution {
    public int evalRPN(String[] tokens) {
        // use a stack to solve postfix expression
        Stack<Integer> stack = new Stack();
        for(String str: tokens){
            boolean isNum = true;
            int flag = 1;
            if(str.charAt(0)=='+' || str.charAt(0)=='*' || str.charAt(0)=='/'){
                isNum = false;
            }
            else if(str.charAt(0)=='-'){
                String val = str.substring(1, str.length());
                if(val.length()==0) isNum = false;
                else flag=-1;
            }

            if(isNum){
                int a = Integer.valueOf(str); 
                stack.push(a);
            }
            else{
                int b = stack.pop();
                int a = stack.pop();
                if(str.equals("+")) stack.push(a+b);
                else if(str.equals("-")) stack.push(a-b);
                else if(str.equals("*")) stack.push(a*b);
                else if(str.equals("/")) stack.push(a/b);
            }
            
        }

        return stack.peek();
    }
}