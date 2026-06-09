## Johnny's LeetCode Solutions Repository

### About

个人 LeetCode 刷题仓库，主要使用 **Python**、**JavaScript** 和 **TypeScript**。持续更新中。

---

### 项目结构

```
LeetCode-Playground/
├── Easy/                    # 简单题
│   └── #题号-英文题目名称/    # 如 #1-Two-Sum/, #707-Design-Linked-List/
│       ├── solution.py      # Python 标准答案
│       ├── draft.py         # Python 空白草稿
│       ├── test.py          # Python 测试
│       ├── solution.js      # JS/TS 标准答案（部分题目）
│       ├── draft.js         # JS/TS 空白草稿（部分题目）
│       └── test.js          # JS/TS 测试（部分题目）
├── Med/                     # 中等题
│   └── #题号-英文题目名称/
│       └── ...
├── Hard/                    # 困难题
│   └── #题号-英文题目名称/
│       └── ...
├── ds_utils/                # 共享工具类（ListNode, LinkedList 等）
├── Reference/               # 参考资料（独立维护）
└── README.md
```

### 命名规则

| 项目 | 规则 | 示例 |
|------|------|------|
| 文件夹名 | `#题号-英文题目名称` | `#1-Two-Sum/`, `#707-Design-Linked-List/` |
| Python 标准答案 | `solution.py` | `Easy/#1-Two-Sum/solution.py` |
| Python 空白草稿 | `draft.py` | `Easy/#1-Two-Sum/draft.py` |
| Python 测试文件 | `test.py` | `Easy/#1-Two-Sum/test.py` |
| JS/TS 标准答案 | `solution.js` | `Med/#707-Design-Linked-List/solution.js` |
| JS/TS 空白草稿 | `draft.js` | `Med/#707-Design-Linked-List/draft.js` |
| JS/TS 测试文件 | `test.js` | `Med/#707-Design-Linked-List/test.js` |

> JS/TS 文件不是每道题都有，有实现的题目才放。

### 文件内容规范

#### solution.py（Python 标准答案）

- 顶部用 `#` 注释写中文题目说明（题目描述 + 示例 + 提示）
- 使用 LeetCode 标准格式：`class Solution` + 标准方法签名
- 可包含额外 import（如 `ds_utils`）

```python
# LeetCode 1 — 两数之和
#
# 给定一个整数数组 nums 和一个整数目标值 target ...
#
# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ...
```

#### draft.py（Python 空白草稿）

- 顶部中文题目说明与 solution.py 一致
- 使用 LeetCode 标准格式：`class Solution` + 标准方法签名
- 方法体只有 `pass` 或默认返回值，确保可编译运行

```python
# LeetCode 1 — 两数之和
# ...（同 solution.py 的题目说明）

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass
```

#### test.py（Python 测试文件）

- 使用 `importlib.util` 加载同目录下的 `solution.py`
- 使用 `assert` 断言验证题目示例
- 运行命令：`python3 {Easy|Med|Hard}/#题号-题目名称/test.py`

```python
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("solution", Path(__file__).parent / "solution.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

sol = mod.Solution()

assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert sol.twoSum([3, 2, 4], 6) == [1, 2]
assert sol.twoSum([3, 3], 6) == [0, 1]

print("All tests passed!")
```

#### solution.js（JS/TS 标准答案）

- 使用 `export` 导出类或函数
- 运行环境：Bun

```javascript
export class Solution {
    twoSum(nums, target) {
        ...
    }
}
```

#### draft.js（JS/TS 空白草稿）

- 与 solution.js 相同的类/函数签名，方法体为空或返回默认值

```javascript
export class Solution {
    twoSum(nums, target) {
        return [];
    }
}
```

#### test.js（JS/TS 测试文件）

- 使用 `import` 加载同目录下的 `solution.js`
- 使用 `assert` 断言验证题目示例
- 运行命令：`bun {Easy|Med|Hard}/#题号-题目名称/test.js`

```javascript
import { Solution } from "./solution.js";

const sol = new Solution();

console.assert(JSON.stringify(sol.twoSum([2, 7, 11, 15], 9)) === JSON.stringify([0, 1]));
console.assert(JSON.stringify(sol.twoSum([3, 2, 4], 6)) === JSON.stringify([1, 2]));
console.assert(JSON.stringify(sol.twoSum([3, 3], 6)) === JSON.stringify([0, 1]));

console.log("All tests passed!");
```

### 运行命令总结

| 语言 | 测试命令 | 示例 |
|------|----------|------|
| Python | `python3` | `python3 Easy/#1-Two-Sum/test.py` |
| JS/TS | `bun` | `bun Med/#707-Design-Linked-List/test.js` |

### 特殊目录（不参与规范）

- `Reference/` — 参考资料，独立维护
- `DD-2020011-Bubble-Sort/` — 自定义练习题
- `Sell-Stocks/` — 无标准 LeetCode 题号
