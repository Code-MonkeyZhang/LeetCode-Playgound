// LeetCode 1 — Two Sum
//
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
  const numMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    numMap.set(nums[i], i);
  }
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (numMap.has(complement) && numMap.get(complement) !== i) {
      return [numMap.get(complement), i];
    }
  }
  return [];
}

export { twoSum };

if (import.meta.main) {
  await import("./test.js");
}
