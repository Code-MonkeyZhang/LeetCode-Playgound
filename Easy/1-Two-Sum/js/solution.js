// LeetCode 1 — 两数之和
//
// 题目描述：给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
// 你可以假设每种输入只会对应一个答案，并且不能使用同一个元素两次。
//
// 示例 1：输入: nums = [2,7,11,15], target = 9 → 输出: [0,1]
// 示例 2：输入: nums = [3,2,4], target = 6 → 输出: [1,2]
// 示例 3：输入: nums = [3,3], target = 6 → 输出: [0,1]

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
  const numMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (numMap.has(complement)) {
      return [numMap.get(complement), i];
    }
    numMap.set(nums[i], i);
  }
  return [];
}

export { twoSum };

if (import.meta.main) {
  await import("./test.js");
}
