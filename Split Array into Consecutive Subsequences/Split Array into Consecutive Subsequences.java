class Solution {
    public boolean isPossible(int[] nums) {
        int c1=0, c2=0, c3=0; // 以nums[i]结尾，长度为1,2,>=3的串的个数
        int p1=0, p2=0, p3=0;
        
        int count = 0;
        boolean firstNum = true;
        int pre = 0;

        // 贪心。计算当前数字num和次数count。把num优先填满长度为1的p1，和长度为2的p2
        // 如果有剩余，再去填长度>=3的p3
        // 如果还有剩余，作为新的p1
        for(int i=0; i<nums.length; i++){
            count += 1;
            if (i+1<nums.length && nums[i]==nums[i+1]) {
                continue;
            }
            if (firstNum) {
                c1 = count;
                firstNum = false;                
            }
            else {
                p1=c1; 
                p2=c2; 
                p3=c3;
                if (nums[i]!=pre+1){ // 如果当前数字不跟前一个数字连续，那么之前的所有串都必须长度>=3
                    if (p1!=0 || p2!=0){
                        return false;
                    }
                    c1 = count;
                }
                else{ // 当前数字和前面连续，那么优先填满短的串
                    if (count<p1+p2) { // nums[i]的个数必须大于1的串和2的串，否则他们就永远不可能成为3了
                        return false;                    
                    }
                    c2 = p1; // 1的串增加一个数字，长度变成2
                    c3 = p2 + Math.min(count-p1-p2, p3); // 2的串变成3，如果还有剩余，再延长3的串，但是注意总数不能超过原有的3的个数
                    c1 = Math.max(0, count-p1-p2-p3);  // 如果还有剩余则变成1. 没有剩余的话，1的数量就是0
                }
                
                
            }
            pre = nums[i];
            count = 0;
        }
        
        if (c1==0 && c2==0){ // 所有串都必须长度>=3
            return true;
        }
        else{
            return false;
        }
    }
}