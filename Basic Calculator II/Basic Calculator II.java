class Solution {
    public int calculate(String s) {
        int len;
        if(s==null || (len = s.length())==0) return 0;
        Stack<Integer> stack = new Stack<Integer>();
        int num=0;
        char prev_sign='+';
        s = s.replaceAll(" ","");
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(Character.isDigit(c)){
                num = num*10 + (c-'0');
            }
            if(!Character.isDigit(c)|| i==s.length()-1){
                if(prev_sign=='+') stack.push(num);
                else if(prev_sign=='-') stack.push(-1*num);
                else if(prev_sign=='*') stack.push(stack.pop()*num);
                else if(prev_sign=='/') stack.push(stack.pop()/num);
                num=0;
                prev_sign=c;
            }
            // step is to save some time
            if(c=='+' || c=='-'){
                if(stack.size()==2){
                    int num1 = stack.pop();
                    stack.push(num1+stack.pop());
                }
                
            }
            
            System.out.println(stack);
            // System.out.println(c);
        }

        int res = 0;
        for(int i:stack){
            res += i;
        }
        return res;
    }
}