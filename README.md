## Johnny's LeetCode Solutions Repository

### About

个人 LeetCode 刷题仓库，主要使用 **Python**、**JavaScript** 和 **TypeScript**。持续更新中。

---

### 项目结构

```
LeetCode-Playground/
├── Easy/                        # 简单题
│   └── 题号-英文题目名称/        # 如 1-Two-Sum/
│       ├── py/                  # Python 实现
│       │   ├── solution.py      # 标准答案
│       │   ├── draft.py         # 空白草稿
│       │   └── test.py          # 测试文件
│       └── js/                  # JS 实现（部分题目有）
│           ├── solution.js      # 标准答案
│           ├── draft.js         # 空白草稿
│           └── test.js          # 测试文件
├── Med/                         # 中等题
│   └── 题号-英文题目名称/
│       └── ...
├── Hard/                        # 困难题
│   └── 题号-英文题目名称/
│       └── ...
├── ds_utils/                    # 共享工具类（ListNode, LinkedList 等）
├── Reference/                   # 参考资料（独立维护）
└── README.md
```

> `py/` 目录每道题都有；`js/` 目录只有部分题目有实现。

### 命名规则

| 项目 | 规则 | 示例 |
|------|------|------|
| 题目文件夹 | `题号-英文题目名称` | `1-Two-Sum/`, `707-Design-Linked-List/` |
| Python 标准答案 | `py/solution.py` | `Easy/1-Two-Sum/py/solution.py` |
| Python 空白草稿 | `py/draft.py` | `Easy/1-Two-Sum/py/draft.py` |
| Python 测试文件 | `py/test.py` | `Easy/1-Two-Sum/py/test.py` |
| JS 标准答案 | `js/solution.js` | `Easy/1-Two-Sum/js/solution.js` |
| JS 空白草稿 | `js/draft.js` | `Easy/1-Two-Sum/js/draft.js` |
| JS 测试文件 | `js/test.js` | `Easy/1-Two-Sum/js/test.js` |

---

### 运行方式

#### Python

| 命令 | 说明 |
|------|------|
| `python3 Easy/1-Two-Sum/py/solution.py` | 直接运行标准答案，自动跑测试 |
| `python3 Easy/1-Two-Sum/py/draft.py` | 直接运行草稿，自动跑测试 |
| `python3 Easy/1-Two-Sum/py/test.py` | 运行测试（默认测 solution.py） |
| `python3 Easy/1-Two-Sum/py/test.py draft.py` | 运行测试，指定测 draft.py |

#### JavaScript（Bun）

| 命令 | 说明 |
|------|------|
| `bun Easy/1-Two-Sum/js/solution.js` | 直接运行标准答案，自动跑测试 |
| `bun Easy/1-Two-Sum/js/draft.js` | 直接运行草稿，自动跑测试 |
| `bun Easy/1-Two-Sum/js/test.js` | 运行测试（默认测 solution.js） |
| `bun Easy/1-Two-Sum/js/test.js draft.js` | 运行测试，指定测 draft.js |

---

### 文件内容规范

#### py/solution.py（Python 标准答案）

- 顶部用 `#` 注释写中文题目说明（题目描述 + 示例 + 提示）
- 使用 LeetCode 标准格式：`class Solution` + 标准方法签名
- 底部 `if __name__ == "__main__"` 块：通过 subprocess 调用 `test.py`，传入自身文件名
- 可包含额外 import（如 `ds_utils`）

```python
# LeetCode 1 — 两数之和
#
# 题目描述：给定一个整数数组 nums 和一个整数目标值 target ...
#
# 示例 1：输入: nums = [2,7,11,15], target = 9 → 输出: [0,1]
# 示例 2：输入: nums = [3,2,4], target = 6 → 输出: [1,2]
# 示例 3：输入: nums = [3,3], target = 6 → 输出: [0,1]

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ...

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
```

#### py/draft.py（Python 空白草稿）

- 顶部中文题目说明与 solution.py 一致
- 使用 LeetCode 标准格式：`class Solution` + 标准方法签名
- 方法体只有 `pass` 或默认返回值，确保可编译运行
- 底部 `if __name__ == "__main__"` 块：与 solution.py 相同，调用 test.py

```python
# LeetCode 1 — 两数之和
# ...（同 solution.py 的题目说明）

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass

if __name__ == "__main__":
    import subprocess
    from pathlib import Path
    subprocess.run(
        ["python3", str(Path(__file__).parent / "test.py"), Path(__file__).name],
        check=True,
    )
```

#### py/test.py（Python 测试文件）

- 使用 `importlib.util` 动态加载同目录下的 Python 文件
- 通过 `sys.argv[1]` 选择加载 `solution.py`（默认）或 `draft.py`
- 使用 `assert` 断言验证题目示例

```python
import importlib.util
import sys
from pathlib import Path

filename = sys.argv[1] if len(sys.argv) > 1 else "solution.py"
spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / filename)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert sol.twoSum([3, 2, 4], 6) == [1, 2]
assert sol.twoSum([3, 3], 6) == [0, 1]

print("All tests passed!")
```

#### js/solution.js（JS 标准答案）

- 顶部用 `//` 注释写英文题目说明
- 使用 JSDoc 标注参数和返回值类型
- 使用 `export` 导出函数或类
- 底部 `if (import.meta.main)` 块：通过 `import` 动态加载 test.js

```javascript
// LeetCode 1 — Two Sum
//
// Given an array of integers nums and an integer target ...

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
    ...
}

export { twoSum };

if (import.meta.main) {
    await import("./test.js");
}
```

#### js/draft.js（JS 空白草稿）

- 与 solution.js 相同的结构，方法体返回默认值
- 底部同样有 `if (import.meta.main)` 块

```javascript
// LeetCode 1 — Two Sum
// ...（同 solution.js 的题目说明）

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
    return [];
}

export { twoSum };

if (import.meta.main) {
    await import("./test.js");
}
```

#### js/test.js（JS 测试文件）

- 使用动态 `import()` 加载 `solution.js` 或 `draft.js`（通过 `process.argv[2]` 选择）
- 使用自定义 `assertEqual` 断言

```javascript
const file = process.argv[2] || "solution.js";
const mod = await import(`./${file}`);
const { twoSum } = mod;

function assertEqual(actual, expected, label) {
    const pass = JSON.stringify(actual) === JSON.stringify(expected);
    console.log(pass ? `✓ ${label}` : `✗ ${label}`);
}

assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1], "Example 1");
assertEqual(twoSum([3, 2, 4], 6), [1, 2], "Example 2");
assertEqual(twoSum([3, 3], 6), [0, 1], "Example 3");
```

---

### 设计说明：solution / draft 直接运行测试

所有 `solution.py` / `draft.py` / `solution.js` / `draft.js` 底部都有一个 `__main__` 入口块，作用是调用同目录下的 `test.py` / `test.js`，并把自身文件名作为参数传入：

```
python solution.py  →  subprocess 调用 test.py solution.py  →  加载 solution.py 并测试
python draft.py     →  subprocess 调用 test.py draft.py     →  加载 draft.py 并测试
```

这样测试逻辑只在 `test.py` 中维护一份，solution 和 draft 无需重复测试代码。

---

### 特殊目录（不参与规范）

| 目录 | 说明 |
|------|------|
| `Reference/` | 参考资料，独立维护 |
| `Easy/DD-2020011-Bubble-Sort/` | 自定义练习题 |
| `Med/Sell-Stocks/` | 无标准 LeetCode 题号 |
