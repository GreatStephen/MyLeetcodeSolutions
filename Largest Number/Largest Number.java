
class Solution {
    public String largestNumber(int[] nums) {
        // string a, string b -> take max(a+b, b+a) when sorting
        // the result is the answer

        String[] nums_str = new String[nums.length];
        for(int i=0; i<nums.length; i++){
            nums_str[i] = String.valueOf(nums[i]);
        }

        Arrays.sort(nums_str, new Comparator<String>(){
            @Override
            public int compare(String o1, String o2){
                String order1 = o1+o2;
                String order2 = o2+o1;
                return order2.compareTo(order1);
            }
        });

        if(nums_str[0].equals("0")) return "0";

        String ans = "";
        for(String str: nums_str){
            ans += str;
        }

        return ans;
    }
}