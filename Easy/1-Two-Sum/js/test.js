const file = process.argv[2] || "solution.js";
const mod = await import(`./${file}`);
const { twoSum } = mod;

function assertEqual(actual, expected, label) {
  const pass =
    actual.length === expected.length &&
    [...actual].sort().every((v, i) => v === [...expected].sort()[i]);
  console.log(pass ? `✓ ${label}` : `✗ ${label} — expected [${expected}], got [${actual}]`);
}

assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1], "Example 1");
assertEqual(twoSum([3, 2, 4], 6), [1, 2], "Example 2");
assertEqual(twoSum([3, 3], 6), [0, 1], "Example 3");
assertEqual(twoSum([1, 5, 3, 7], 10), [2, 3], "Custom 1");
assertEqual(twoSum([0, 4, 3, 0], 0), [0, 3], "Custom 2");
