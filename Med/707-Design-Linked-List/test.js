import { MyLinkedList } from "./solution.js";

function runTest(name, ops, expected) {
  const list = new MyLinkedList();
  const actual = [];
  for (const [method, ...args] of ops) {
    const result = list[method](...args);
    if (method === "get") actual.push(result);
  }
  const passed = JSON.stringify(actual) === JSON.stringify(expected);
  console.log(`[${passed ? "PASS" : "FAIL"}] ${name}`);
  if (!passed) {
    console.log(`  Expected: ${JSON.stringify(expected)}`);
    console.log(`  Actual  : ${JSON.stringify(actual)}`);
  }
}

function main() {
  const line = "=".repeat(50);
  console.log(line);
  console.log("LeetCode 707 — Design Linked List | JS Test Harness");
  console.log(line);
  console.log();

  runTest("Example / Basic Flow", [
    ["addAtHead", 1],
    ["addAtTail", 3],
    ["addAtIndex", 1, 2],
    ["get", 1],
    ["deleteAtIndex", 1],
    ["get", 1],
  ], [2, 3]);

  runTest("Invalid get on empty list", [
    ["get", 0],
    ["get", 5],
  ], [-1, -1]);

  runTest("addAtIndex(0, val) inserts at head", [
    ["addAtIndex", 0, 10],
    ["get", 0],
  ], [10]);

  runTest("addAtIndex(len, val) appends", [
    ["addAtHead", 1],
    ["addAtTail", 3],
    ["addAtIndex", 2, 5],
    ["get", 2],
  ], [5]);

  runTest("addAtIndex(>len) does nothing", [
    ["addAtHead", 7],
    ["addAtIndex", 5, 9],
    ["get", 0],
    ["get", 1],
  ], [7, -1]);

  runTest("deleteAtIndex on head", [
    ["addAtHead", 4],
    ["addAtTail", 5],
    ["deleteAtIndex", 0],
    ["get", 0],
    ["get", 1],
  ], [5, -1]);

  runTest("Mixed operations", [
    ["addAtHead", 1],
    ["addAtHead", 2],
    ["addAtTail", 3],
    ["addAtIndex", 1, 9],
    ["get", 0],
    ["get", 1],
    ["get", 2],
    ["get", 3],
  ], [2, 9, 1, 3]);

  console.log();
  console.log(line);
  console.log("Done.");
  console.log(line);
}

main();
