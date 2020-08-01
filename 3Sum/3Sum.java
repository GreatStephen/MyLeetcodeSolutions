class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        // System.out.println(Arrays.toString(nums));

        int index=0;
        int m,n;
        List list = new ArrayList<>();
        int target=0;
        if(nums.length<3) return list;
        
        while(nums[index]<=0){
            if(index>nums.length-3) break;
            m=index+1;
            n=nums.length-1;
            target = -1*nums[index];

            while(n>m){
                if(nums[n]+nums[m]>target){
                    do{
                        n--;
                    }while(nums[n]==nums[n+1] && n>m);
                }
                else if(nums[n]+nums[m]<target){
                    do{
                        m++;
                    }while(nums[m]==nums[m-1]&& m<n);
                }
                else{
                    List templist = new ArrayList<>();
                    templist.add(nums[index]);
                    templist.add(nums[m]);
                    templist.add(nums[n]);
                    list.add(templist);
                    do{
                        m++;
                    }while(nums[m]==nums[m-1] && m<n);
                }
            }

            do{
                index++;
            }while(nums[index]==nums[index-1] && index<m);
            if(index>nums.length-3) break;
        }

        return list;
    }
}