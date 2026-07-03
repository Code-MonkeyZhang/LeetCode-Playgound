# 面经 Coding 题收集

> 来源：个人面经 + 收集的面经中所有被问到的 coding 类型题目，按类型分类组织。
>
> 格式与本目录其他题库文件保持一致。

---

## 目录

- [链表](#链表)
- [字符串](#字符串)
- [栈](#栈)
- [手写函数](#手写函数)
- [输出顺序题](#输出顺序题)
- [场景设计](#场景设计)

---

## 链表

### 206. 反转链表 · 简单

**英文名：** Reverse Linked List  
**链接：** https://leetcode.cn/problems/reverse-linked-list/description/  
**来源：** 番茄小说（字节）- iOS 客户端一面

给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)
```
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)
```
输入：head = [1,2]
输出：[2,1]
```

**示例 3：**

```
输入：head = []
输出：[]
```

**提示：**

-   链表中节点的数目范围是 `[0, 5000]`
-   `-5000 <= Node.val <= 5000`

**进阶：**链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

---

### 141. 环形链表 · 简单

**英文名：** Linked List Cycle  
**链接：** https://leetcode.cn/problems/linked-list-cycle/description/  
**来源：** Enerjoy - iOS 开发一面

给你一个链表的头节点 `head` ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。**注意：`pos` 不作为参数进行传递** 。仅仅是为了标识链表的实际情况。

_如果链表中存在环_ ，则返回 `true` 。 否则，返回 `false` 。

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)

```
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png)

```
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
```

**提示：**

-   链表中节点的数目范围是 `[0, 104]`
-   `-105 <= Node.val <= 105`
-   `pos` 为 `-1` 或者链表中的一个 **有效索引** 。

**进阶：**你能用 `O(1)`（即，常量）内存解决此问题吗？

---

### 142. 环形链表 II · 中等

**英文名：** Linked List Cycle II  
**链接：** https://leetcode.cn/problems/linked-list-cycle-ii/description/  
**来源：** Enerjoy - iOS 开发一面

给定一个链表的头节点 `head` ，返回链表开始入环的第一个节点。 _如果链表无环，则返回 `null`。_

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（**索引从 0 开始**）。如果 `pos` 是 `-1`，则在该链表中没有环。**注意：`pos` 不作为参数进行传递**，仅仅是为了标识链表的实际情况。

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)

```
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
```

**示例 3：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png)

```
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
```

**提示：**

-   链表中节点的数目范围在范围 `[0, 104]` 内
-   `-105 <= Node.val <= 105`
-   `pos` 的值为 `-1` 或者链表中的一个有效索引

**进阶：**你是否可以使用 `O(1)` 空间解决此题？

---

## 字符串

### 415. 字符串相加 · 简单

**英文名：** Add Strings  
**链接：** https://leetcode.cn/problems/add-strings/description/  
**来源：** 深言科技 - Web 前端实习一面

给定两个字符串形式的非负整数 `num1` 和 `num2` ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 `BigInteger`）， 也不能直接将输入的字符串转换为整数形式。

**示例 1：**

```
输入：num1 = "11", num2 = "123"
输出："134"
```

**示例 2：**

```
输入：num1 = "456", num2 = "77"
输出："533"
```

**示例 3：**

```
输入：num1 = "0", num2 = "0"
输出："0"
```

**提示：**

-   `1 <= num1.length, num2.length <= 104`
-   `num1` 和 `num2` 都只包含数字 `0-9`
-   `num1` 和 `num2` 都不包含任何前导零

---

### 16 进制字符串对 100 求余 · 简单

**来源：** 小红书 - 创新项目组 iOS 开发一面

给定一个表示 16 进制数的字符串，将其转换为十进制整数后对 100 求余，返回余数（int 类型）。

**示例 1：**

```
输入："1A"
输出：26
解释：1A(16) = 26(10)，26 mod 100 = 26
```

**示例 2：**

```
输入："FF"
输出：55
解释：FF(16) = 255(10)，255 mod 100 = 55
```

**示例 3：**

```
输入："64"
输出：0
解释：64(16) = 100(10)，100 mod 100 = 0
```

**提示：**

-   输入字符串只包含 `0-9` 和 `A-F`（或 `a-f`）
-   字符串长度可能很长，转换后的十进制数可能超出普通整型范围（需注意溢出处理）

---

## 栈

### 20. 有效的括号 · 简单

**英文名：** Valid Parentheses  
**链接：** https://leetcode.cn/problems/valid-parentheses/description/  
**来源：** Enerjoy - iOS 开发一面

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：

1.  左括号必须用相同类型的右括号闭合。
2.  左括号必须以正确的顺序闭合。
3.  每个右括号都有一个对应的相同类型的左括号。

**示例 1：**

```
输入：s = "()"
输出：true
```

**示例 2：**

```
输入：s = "()[]{}"
输出：true
```

**示例 3：**

```
输入：s = "(]"
输出：false
```

**提示：**

-   `1 <= s.length <= 104`
-   `s` 仅由括号 `'()[]{}'` 组成

---

## 手写函数

### filterArr · 简单

**来源：** B站 - 大会员前端开发面经

手写一个 `filterArr(arr, type)` 函数，按指定类型筛选数组里的基础类型元素，并且要处理好 `null` 的边界情况。

**示例 1：**

```js
输入：filterArr([1, 'a', null, true, {}, undefined], 'number')
输出：[1]
```

**示例 2：**

```js
输入：filterArr([1, 'a', null, true, {}, undefined], 'null')
输出：[null]
```

**考点：**

-   `typeof` 的返回值与基础类型判断（`typeof null === 'object'` 需特殊处理）
-   `null` 的边界情况：需单独判断 `item === null`
-   （追问）如何区分引用类型（`Array`、`Object`）—— 用 `Object.prototype.toString.call()`
-   （追问）如何改造以符合开闭原则、支持后续新增类型

**参考解：**

```js
function filterArr(arr, type) {
  return arr.filter((item) =>
    item === null ? type === 'null' : typeof item === type
  );
}
```

---

### 数组实例方法挂载 · 简单

**来源：** B站 - 大会员前端开发面经

如何让自定义的筛选方法（如 `filterByType`）支持数组实例直接调用？有哪几种挂载方式？要求边说边把几种方式都写出来。

**方式一：挂到原型（所有数组实例共享）**

```js
Array.prototype.filterByType = function (type) {
  /* ... */
};
```

**方式二：仅挂到单个实例**

```js
const arr = [];
arr.filterByType = function (type) {
  /* ... */
};
```

**考点：**

-   原型链：数组实例为什么能直接调用 `filter`，底层原理是什么
-   挂在 `Array.prototype` 上 vs 挂单个实例的区别
-   普通函数、箭头函数、`class` 在原型操作上的差异
-   业务里全局扩展数组工具方法的可行性与优缺点

---

## 输出顺序题

> 以下题目来自面经描述，仅记录考点与题型，不附具体代码。

### 事件循环代码输出顺序

**来源：** B站 - 大会员前端开发面经

给一段包含事件循环相关 API 的代码，要求写出输出打印顺序。

**考点：** 事件循环、宏任务与微任务的执行顺序、`Promise.resolve` 属于微任务还是宏任务、同一轮循环里先后注册两个 `setTimeout` 的执行顺序由什么决定。

---

### Promise + setTimeout 混排顺序题

**来源：** B站 - 前端日常实习面经

给一段 `Promise` 与 `setTimeout` 混排的代码，要求写出输出顺序。

**考点：** 微任务（Promise）与宏任务（setTimeout）的优先级规则、事件循环机制。

---

### Promise + async + setTimeout 顺序题

**来源：** B站 - 前端日常实习面经

给一段同时包含 `Promise`、`async` 函数与 `setTimeout` 的代码，要求写出输出顺序。

**考点：** `async/await` 的本质（语法糖 + 微任务）、与 `Promise.then` 的等价关系、微/宏任务交错执行流程。

---

### Promise.all / allSettled / race 顺序题

**来源：** B站 - 前端日常实习面经

给一段使用 `Promise.all`、`Promise.allSettled`、`Promise.race` 的代码，要求写出输出顺序。

**考点：**

-   `Promise.all`：所有 Promise 都 fulfilled 才 resolve，任一 reject 即 reject
-   `Promise.allSettled`：所有 Promise 都 settle 后才 resolve，不会 reject
-   `Promise.race`：第一个 settle 的 Promise 决定结果

---

## 场景设计

### 列表内视频自动播放（类微信朋友圈/抖音）

**来源：** 小红书 - 创新项目组 iOS 开发一面

在 `UITableView` 或 `UICollectionView` 列表里放视频，类似微信朋友圈或抖音——滚动到某个位置时视频自动播放，离开该位置时暂停。从 0 到 1 思考如何实现。

**需要考虑的点：**

-   播放暂停时机的判定（滚动到哪个位置播放、滚到哪暂停）
-   cell 复用机制与播放器实例管理
-   视频预加载与内存优化
-   多个视频同时出现在屏幕时的优先级处理
-   播放器性能与流畅度

**考点：** 列表滚动事件监听、cell 生命周期管理、播放器复用、性能优化、工程化思维（先 make it work 再优化细节）。

---
