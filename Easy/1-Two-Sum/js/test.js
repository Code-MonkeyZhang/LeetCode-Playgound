const file = process.argv[2] || "solution.js";
const mod = await import(`./${file}`);
const { twoSum } = mod;

function check(actual, expected, label) {
  const match =
    actual.length === expected.length &&
    actual[0] === expected[0] &&
    actual[1] === expected[1];
  if (!match) {
    console.log(`✗ ${label} — expected [${expected}], got [${actual}]`);
    process.exit(1);
  }
  if (actual[0] >= actual[1]) {
    console.log(`✗ ${label} — indices not in ascending order: [${actual}]`);
    process.exit(1);
  }
  console.log(`✓ ${label}`);
}

check(twoSum([2, 7, 11, 15], 9), [0, 1], "Example 1");
check(twoSum([3, 2, 4], 6), [1, 2], "Example 2");
check(twoSum([3, 3], 6), [0, 1], "Example 3");
check(twoSum([1, 2], 3), [0, 1], "Min input");
check(twoSum([-1, -2, -3, -4, -5], -8), [2, 4], "All negative");
check(twoSum([-3, 4, 3, 90], 0), [0, 2], "Mixed pos/neg");
check(twoSum([1, 2, 3, 9], 10), [0, 3], "First & last");
check(twoSum([1, 2, 3], 3), [0, 1], "Adjacent pair");
check(twoSum([10, 20, 30, 40, 50], 90), [3, 4], "Last two");
check(twoSum([0, 4, 3, 0], 0), [0, 3], "Contains zero");
