package TwoSum;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int[] input = new int[4];
        int sum;
        for(int i=0; i<4; i++){
            input[i]= scanner.nextInt();
        }
        sum=scanner.nextInt();
        System.out.println(Arrays.toString(twoSum(input,sum)));
    }
    static public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int complement = target-nums[i];
            if(map.containsKey(complement)){
                return new int[] {map.get(complement), i};
            }
            else{
                map.put(nums[i],i);
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
