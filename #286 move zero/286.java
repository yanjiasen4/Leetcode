public class Solution {
    public void moveZeroes(int[] nums) {
        int size = nums.length;
        if(size <= 1){
            return;
        }
        int i = 0;
        int swap = 1;
        for(; i <swap && swap < size; ){
            if(nums[i] == 0 && nums[swap] != 0){
                nums[i] = nums[swap];
                nums[swap] = 0;
                i++;
                swap++;
            }
            else if(nums[i] == 0 && nums[swap] == 0){
                swap++;
            }
            else if(nums[i] != 0){
                i++;
                swap++;
            }
        }
    }
}