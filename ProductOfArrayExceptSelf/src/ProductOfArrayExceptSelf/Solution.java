package ProductOfArrayExceptSelf;

import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    // O(n) but more space complexity
    static public int[] productExceptSelf(int[] nums){
        int[] preproduct = new int[nums.length];
        int[] postproduct = new int[nums.length];
        int[] res = new int[nums.length];
        preproduct[0]=1;
        postproduct[nums.length-1]=1;

        for(int i=1; i<nums.length; i++){
            preproduct[i]=preproduct[i-1]*nums[i-1];
        }
        for(int i=nums.length-2; i>=0; i--){
            postproduct[i]=postproduct[i+1]*nums[i+1];
        }
        for(int i=0;i<nums.length;i++){
            res[i]=preproduct[i]*postproduct[i];
        }

        return res;
    }

    // O(n) and constant space complexity
    static public int[] productExceptSelf2(int[] nums){
//        int[] preproduct = new int[nums.length];
//        int[] postproduct = new int[nums.length];
        int[] res2 = new int[nums.length];
        res2[0]=1;
        int temp=1;
//        preproduct[0]=1;
//        postproduct[nums.length-1]=1;

        for(int i=1; i<nums.length; i++){
            res2[i]=res2[i-1]*nums[i-1];
        }
        for(int i=nums.length-2; i>=0; i--){
            temp=temp*nums[i+1];
            res2[i]=res2[i]*temp;
        }

        return res2;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int[] input = new int[4];
        for(int i=0; i<4; i++){
            input[i]= scanner.nextInt();
        }
        System.out.print(Arrays.toString(productExceptSelf2(input)));
    }


}
