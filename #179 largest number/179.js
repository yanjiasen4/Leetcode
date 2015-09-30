/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    nums.sort(function(a, b) {
        return (b + '' + a ) - (a + '' + b);
    })
    var result = "";
    for(var tmp in nums){
        result += nums[tmp];
    }
    return result.replace(/0*/,'') || '0'; // [0,0]¼òÖ±µ°ÌÛ
};