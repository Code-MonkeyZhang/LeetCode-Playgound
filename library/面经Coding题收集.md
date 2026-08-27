# 面经 Coding 题收集

> 来源：个人面经 + 收集的面经中所有被问到的 coding 类型题目，按类型分类组织。
>
> 格式与本目录其他题库文件保持一致。
>
> 注：与三套题库（HOT100 / 面试经典150 / NeetCode150）完全重合的题不在此收录，已直接在对应题库文件中标注「面经出现」。

---

## 目录

- [字符串](#字符串)
- [手写函数](#手写函数)
- [ML 手撕](#ml-手撕)
- [算法题](#算法题)
- [输出顺序题](#输出顺序题)
- [场景设计](#场景设计)
- [代码 Review](#代码-review)
- [智力题](#智力题)

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

**追问（当场）：** "9 后面再加几个 9"什么时候会溢出？`int` / `string` 的数据类型上限是多少？

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

### 交通信号灯模拟 · 简单

**来源：** 字节跳动 - 前端开发二面（手撕翻车点）

实现交通信号灯模拟：红 1s → 绿 1s → 黄 1s 循环切换（控制台打印或页面切换均可）。

**考点：**

-   `setTimeout` / `setInterval` / `async-await` / 递归 Promise 串行的精确控制
-   手撕翻车实录：画蛇添足多写了一个 `setTimeout` 导致一直报错，越慌越乱——事后发现去掉那一行就对了
-   前端特色手撕要保持手感：长期只刷力扣、疏于写前端题，这类定时器/异步题反而容易成短板

**参考思路：**

```js
async function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function trafficLight() {
  const lights = ['红', '绿', '黄'];
  let i = 0;
  while (true) {
    console.log(lights[i]);
    await sleep(1000);
    i = (i + 1) % lights.length;
  }
}
```

---

### 手写 Promise.race() · 简单

**来源：** 字节跳动 - 前端开发二面

手写 `Promise.race()` 实现：接收一个 promise 数组，返回第一个 settle（无论 fulfilled 还是 rejected）的 Promise 结果。

**考点：**

-   Promise A+ 基础：`then` 对 fulfilled / rejected 的分发
-   只需把 `resolve` / `reject` 同时挂到每个 promise 的 then 上，第一个先到先赢
-   空数组的行为（永远 pending）、非 Promise 值的处理

**参考解：**

```js
function race(promises) {
  return new Promise((resolve, reject) => {
    promises.forEach((p) => Promise.resolve(p).then(resolve, reject));
  });
}
```

---

### 手写防抖函数 debounce · 简单

**来源：** 拼多多 - AI 全栈一面

手写一个防抖函数（debounce），并说明实际使用场景。

**考点：**

-   防抖语义：事件停止触发 n 秒后执行一次；期间再触发则重新计时
-   `this` 指向与参数透传（用箭头函数或 `fn.apply(this, args)`）
-   立即执行版（leading）与延迟执行版（trailing）
-   使用场景：搜索输入联想、窗口 resize、按钮防重复提交（对比节流 throttle 的场景差异）

**参考解：**

```js
function debounce(fn, delay) {
  let timer = null;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}
```

---

### 固定容量环形队列（多线程版） · 中等

**来源：** 腾讯微信支付 - Agent 开发一面（题 1，禁 AI）

实现固定容量队列：初始化传 `capacity`，实现 `push` / `pop`。

进阶要求：O(1) 复杂度、多线程正确性、`close` 语义、统计 push 成功 / 失败次数。

**当场追问（共 9 层）：**

1. head 指针的设计目的是什么？
2. 插入元素的时候头部要不要变？
3. 一个头指针能不能满足环形队列？
4. 泛型下 pop 失败返回什么，怎么和合法的假值区分开？（哨兵值 / Optional / 错误码）
5. 多线程怎么保证正确性，锁应该加在哪，粒度怎么定？
6. close 之后 push 和 pop 分别是什么语义？
7. 你打算构建哪些测试用例？异常用例具体有哪些？
8. 你的用例只覆盖了单一场景，满足所有异常场景了吗？

**考点：** 数组环形缓冲（head/tail 指针 + 取模回绕）、满/空判断的两种策略（留空一位 or 计数器）、泛型哨兵值设计、锁粒度（粗锁 vs 两把锁分离读写）、close 广播唤醒（waiters 全部唤醒并返回错误）、测试用例设计（并发压测、边界、异常路径）。

---

### 带重试的下游调用封装（AI 出码） · 中等

**来源：** 腾讯微信支付 - Agent 开发一面（题 2，指定用 AI 写）

实现一个带重试的下游调用封装。options 含：最大尝试次数、总超时、单次超时；仅对可重试错误重试；总时间不足一次尝试时返回超时；两次尝试间休眠。

**当场追问：**

1. 题目丢给 AI 之前，你自己需要给它补哪些 point？（约束补全能力）
2. 这个封装你打算怎么测，测试怎么设计？
3. `max_attempts` 等于 1，到底重不重试？（边界语义澄清）
4. `kTimeout` 和 `kPermissionDeny` 分别该怎么处理？（可重试 vs 不可重试错误分类）
5. AI 生成的代码如果会无限重试，你怎么发现？（AI 产出验收）
6. 你平时用 AI 写代码是什么流程？

**考点：** 这题考的不是代码本身，而是「驾驭 AI 而非被 AI 驾驭」——喂题前补全约束（错误分类、边界语义、休眠策略、超时预算分摊）、设计测试验证 AI 产出、识别 AI 生成代码的无限重试类 bug。

---

### 手写 @Tool 注解 + 处理器 · 中等

**来源：** 恒生电子 - AI Agent 开发岗二面（手撕）

实现一个简单的 Java 注解 `@Tool` 和一个处理器，用于在运行时扫描并注册所有被 `@Tool` 标记的方法，作为 Agent 可用的工具。

**考点：**

-   自定义注解：`@Target(ElementType.METHOD)` + `@Retention(RetentionPolicy.RUNTIME)`
-   反射扫描：包下所有类 → 方法级 `isAnnotationPresent(Tool.class)`
-   注册中心：`Map<String, Method>` 工具名 → 方法的映射、入参 / 返回值元信息抽取（供生成 JSON Schema）
-   执行入口：`invoke(target, args)` + 异常包装
-   面试官评价：比较偏但凭借 Spring 注解与反射的积累可以应对

**参考骨架：**

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Tool {
    String name();
    String description() default "";
}

// 处理器：扫描 + 注册
Map<String, ToolMethod> registry = new HashMap<>();
for (Method m : clazz.getDeclaredMethods()) {
    Tool t = m.getAnnotation(Tool.class);
    if (t != null) registry.put(t.name(), new ToolMethod(m, t.description()));
}
```

---

## ML 手撕

### PyTorch 手写 SFT Loss（shift right） · 中等

**来源：** MiniMax - 大模型 Agent 一面（手撕）

用 PyTorch 写 SFT 的 loss 计算，注意 shift right。

**考点：**

-   自回归训练的错位对齐：`logits[:, :-1]` 对 `labels[:, 1:]`（预测下一个 token）
-   CrossEntropyLoss 的 ignore_index（padding 不计 loss）、仅对 assistant 段计算 loss（补齐 mask）
-   `view(-1)` 展平后逐 token 平均

**参考解：**

```python
shift_logits = logits[:, :-1, :].contiguous().view(-1, vocab_size)
shift_labels = labels[:, 1:].contiguous().view(-1)
loss = F.cross_entropy(shift_logits, shift_labels, ignore_index=-100)
```

---

### 手写 Multi-head Self-Attention forward · 中等

**来源：** 面壁智能 - 算法工程师一面；MiniMax - Agent 开发实习一面（要求公式 + 手搓实现）

给定 `hidden_state (batch, length, hidden_size)` 和 `mask (batch, length, length)`，补全 `__init__` 与 `forward`，实现多头自注意力。

**考点：**

-   QKV 投影与 reshape：`(b, l, d) → (b, h, l, d_head)`
-   注意力公式：`softmax(QK^T / √d_head + mask) V`
-   mask 加法（注意力掩码是加 -inf 而非乘 0）、concat 后输出投影
-   面试常伴随追问：注意力矩阵的维度变换过程、MHA / MQA / GQA 三种注意力的差异、为什么要除以 √d

**参考骨架：**

```python
class MultiHeadSelfAttention(nn.Module):
    def __init__(self, hidden_size, n_heads):
        self.qkv = nn.Linear(hidden_size, hidden_size * 3)
        self.out = nn.Linear(hidden_size, hidden_size)

    def forward(self, x, mask=None):
        B, L, D = x.shape
        q, k, v = self.qkv(x).chunk(3, dim=-1)
        q = q.view(B, L, H, D // H).transpose(1, 2)  # (B, H, L, d_head)
        # k, v 同理
        attn = (q @ k.transpose(-2, -1)) / math.sqrt(D // H)
        if mask is not None:
            attn = attn + mask
        attn = attn.softmax(dim=-1)
        out = (attn @ v).transpose(1, 2).reshape(B, L, D)
        return self.out(out)
```

---

### 手写 PPO / DPO Loss · 困难

**来源：** MiniMax - Agent 开发实习一面（原理、简单手搓、优势对比四件套）

手写 PPO 与 DPO 的损失函数核心项。

**考点：**

-   PPO-Clip：`min(r_t * A_t, clip(r_t, 1-ε, 1+ε) * A_t)`，其中 `r_t = π_θ(a|s) / π_old(a|s)`；需要维护 actor-critic 两套网络与 GAE 优势估计
-   DPO：`-log σ(β [log(π(y_w|x)/π_ref(y_w|x)) - log(π(y_l|x)/π_ref(y_l|x))])`；隐式 KL 约束，无需显式奖励模型
-   对比：PPO 需在线采样 + 奖励模型 + value 网络，DPO 离线偏好对即可训练；追问各自的常见应用场景与 DPO 训练注意事项（β 调节、偏好数据质量、reference model 冻结）

---

## 算法题

> 以下题目均不在 HOT100 / 面试经典150 / NeetCode150 三套题库内，或为题库题的明显变种。

### 约瑟夫环 · 中等

**来源：** 阿里控股 - AI 应用研发一面（开场手撕约 20 分钟）

n 个人围成一圈，从第一个人开始报数，报到 m 的人出列，再由下一个人重新从 1 开始报数，求最后剩下的人的初始编号。

**考点：**

-   经典解：递推公式 `f(1)=0, f(i)=(f(i-1)+m) % i`，O(n) 时间 O(1) 空间
-   模拟解：队列 / 环形链表模拟，O(nm)
-   这场面试以手撕开场后再进入数据结构 / OS / Java 八股连击，流程罕见

---

### 232. 用栈实现队列 · 简单

**链接：** https://leetcode.cn/problems/implement-queue-using-stacks/description/  
**来源：** 字节跳动 - Agent 开发实习一面（常规手撕）

请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（`push`、`pop`、`peek`、`empty`）。

**考点：** 双栈倒腾（in 栈进、out 栈出）、均摊 O(1)、out 栈非空时不许倒灌。

**参考解：**

```python
class MyQueue:
    def __init__(self):
        self.inp, self.out = [], []
    def push(self, x): self.inp.append(x)
    def pop(self):
        self.peek()
        return self.out.pop()
    def peek(self):
        if not self.out:
            while self.inp: self.out.append(self.inp.pop())
        return self.out[-1]
```

---

### 44. 通配符匹配 · 困难

**链接：** https://leetcode.cn/problems/wildcard-matching/description/  
**来源：** 字节跳动 - 全栈开发三面

给你一个输入字符串 (`s`) 和一个字符模式 (`p`)，实现一个支持 `'?'` 和 `'*'` 的通配符匹配：`'?'` 可以匹配任何单个字符，`'*'` 可以匹配任意字符序列（包括空序列）。判断字符串是否完全匹配。

**考点：** 二维 DP（`dp[i][j]` = s 前 i 位与 p 前 j 位是否匹配，`*` 对应「跳过 / 吃一个字符」两种转移）或贪心双指针（记录最近的 `*` 位置回溯）。

---

### 回文串匹配 · 简单（描述模糊）

**来源：** 字节跳动 - 全栈开发二面

回文串匹配（原帖仅此一句，未给出完整题面，疑似验证回文串 / 最长回文子串类题目）。

**关联题库题：** LC 5 最长回文子串、LC 125 验证回文串、LC 131 分割回文串（若拿到确切题面可对号入座）。

---

### 拓扑排序 × 链表（自创题） · 困难

**来源：** 字节跳动 - Agent 算法一面（公司内部自创题，非力扣原题，15 分钟未写完）

拓扑排序结合链表的组合题（原帖未给出完整题面）。

**考点：** 数据结构组合运用的临场能力——Kahn 入度队列 / DFS 染色 + 链表指针操作。评论区证实此类题力扣刷不到原题，重在临场拆解。

---

### BFS 染色求交集最多的点 · 中等

**来源：** 陌陌 - 全栈开发笔试（题二）

> 题意补充（作者置顶评论）：给一批点 m，这些点都各自连着其他点，现在要求跟 m 交集最多的那些点 k。

**考点：** 图遍历（BFS / 多源 BFS）+ 集合统计（对 m 邻居的邻居计数取最大）、用哈希表代替矩阵存稀疏图。

---

### 五子棋填满棋盘（fill + is_over） · 中等

**来源：** 面壁智能 - 算法工程师一面

n×n（n 为奇数）棋盘，设计算法把整个棋盘填满黑白棋子。原代码 `fill` 和 `is_over` 为空，要求完善——`fill` 填满棋盘，`is_over` 判断是否出现五连（横 / 竖 / 两条对角线连成 5 子）。附 `check` 校验：填满 + 黑白数量各半 + 无五连才 correct。

**考点：** 棋盘遍历填充（保证黑白各半的交替放置）、五连检测（四个方向 × 双向延伸计数）、边界与非法输入处理。

---

### 零钱兑换变种：最少个数 + 全部组合 · 中等

**来源：** 面壁智能 - 算法工程师三面

给定面额 `coins`（每种无限个）和总金额 `amount`，求凑成 `amount` 的**最少硬币个数**及**最少个数下的全部组合**；无法凑出返回 -1。

**示例：** `coins = [1, 3, 7]`，`amount = 9` → 最少 3 个，组合 `[3,3,3]` 与 `[1,1,7]`。

**考点：** 动态规划（完全背包求最少硬币数）+ 组合去重（set 存排序后元组去重）+ 回溯收集最优组合。

**关联题库题：** LC 322 零钱兑换（本体在题库，此为要求输出全部组合的变种）。

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

### 手写 Agent 的 Plan 执行器 · Special

**来源：** 字节跳动 - Agent 开发一面（手撕，题库原题）

Agent 规划后生成一个 task 表（每个 task 有 id、name、依赖的 tasks）。要求写代码执行这个 task 表：

- 无依赖关系的 task 可以并行执行；
- 出现错误时中断执行，并返回当前失败的 task id。

**考点（评论区共识）：** 本质是有向无环图（DAG）任务调度，综合考查拓扑排序（确定可执行顺序）、环检测（依赖成环识别）、状态流转（待执行 / 执行中 / 已完成 / 失败）、依赖检测（前置依赖是否完成）、线程池（无依赖 task 并行）、阻塞队列 / 回调（task 完成后唤醒后续）、错误中断（出错立即中断并返回失败 task id）。

---

### 实时平均耗时统计（内存受限） · 困难

**来源：** 字节跳动 - 后端开发一面（场景设计）

AI 异步生成的链路里，假设每分钟有几万个生成请求，需要统计每个任务的耗时，并在服务里实时展示这些任务平均耗时的波动情况，但因为样本很大，内存不可能都存下，怎么实现？

**考点：** 流式统计（不需要存全量样本）——滑动窗口分桶（每秒一个桶，桶内只存 count 和 sum，窗口滑动时加减桶即可）、或 P2 / t-digest 等分位数近似算法（如果要求 P99）、环形数组复用桶内存。

---

### vibe coding 一个分布式限流系统 · 困难

**来源：** 字节跳动 - 后端开发一面（场景设计）

用 vibe coding（AI 辅助编程）的方式实现一个分布式限流系统。

**考点：** 限流算法选型（固定窗口 / 滑动窗口 / 漏桶 / 令牌桶）、分布式实现（Redis + Lua 原子扣减令牌）、阈值配置与热更新、限流后的拒绝策略（快速失败 / 排队）、AI 辅助拆解与验收。

---

### 流式追加消息的聊天列表 · 中等

**来源：** 拼多多 - AI 全栈一面（手撕）

实现一个支持流式追加消息的聊天列表（AI 对话场景下消息内容持续追加）。

**考点：** 虚拟列表 / 只渲染可视区、追加内容时的局部更新（避免整个列表重渲染）、自动吸底与用户上滑时禁止吸底的判定、Markdown 增量渲染、滚动性能（transform / rAF 批量更新）。

---

### 多轮对话 + 流式返回的 API 接口 · 中等

**来源：** 拼多多 - AI 全栈二面（手撕）

实现一个支持多轮对话和流式返回的 API 接口。

**考点：** SSE 协议（`text/event-stream`、`data:` 帧、断线重连 Last-Event-ID）vs WebSocket 选型、多轮上下文的会话管理（session id → 历史存储）、流式透传（上游 chunk → 下游 flush，注意禁用缓冲）、错误码约定与中途出错的中断处理。

---

### TUI 交互式视频剪辑工具 MVP · 困难

**来源：** 腾讯 - Agent 开发二面（场景设计）

开发一个带 TUI 界面的交互式视频剪辑工具（MVP 版），怎么设计分层架构？核心功能怎么实现？

**考点：** 分层架构（TUI 渲染层 / 交互命令层 / 剪辑业务层 / FFmpeg 执行层）、命令模式管理编辑操作（undo/redo）、TUI 框架选型（如 Textual / blessed）、进度反馈（子进程流式输出解析）、MVP 范围裁剪。

---

### 自然语言驱动的端到端开发 Agent · 困难

**来源：** 阿里控股 - AI 应用研发一面（场景设计）

如果换成一个自然语言描述的新推荐需求（例如「新增一路召回」），想要通过 Agent 实现这么一个端到端的开发需求（理解需求 → 定位代码 → 修改 → 测试 → 提测），你会怎么设计？

**考点：** NL → 需求结构化（意图与验收标准抽取）、代码库定位（索引 / 检索 / 仓库地图）、修改计划与 diff 审查、测试生成与回归验证、人工确认门（high-risk 操作审批）、失败回滚。

---

### AI Coding 实操：模拟读写锁升级死锁 · Special

**来源：** 寒武纪 - Agent 开发一面（现场用 AI 写代码）

现场用 AI 写代码，模拟一个死锁场景（候选人写的是读写锁升级死锁），并回答后续追问。

**考点：** 死锁四条件（互斥 / 持有等待 / 不可剥夺 / 循环等待）与场景构造、读写锁升级（读锁未释放直接申请写锁 = 自等待死锁）、对 AI 产出的驾驭（先把约束讲清楚再生成、review 生成的并发代码）、脱离 AI 的手写能力（「不用 AI 能不能自己手撕出来」）。相关八股：线上怎么查最近一次死锁、MVCC 能不能解决死锁。

---

### 电商客服 Agent 的工具接入 · 困难

**来源：** 拼多多 - AI 全栈二面（场景设计）

如果设计一个电商客服 Agent，如何接入商品、订单和售后工具？

**考点：** 工具域建模（商品查询 / 订单状态 / 售后工单的粒度划分与权限边界）、工具鉴权（用户只能查自己的订单）、敏感操作的确认门（退款类工具需人工 / 用户确认）、工具结果到 LLM 的数据拼装（截断与脱敏）、多工具编排（先查订单再查物流的依赖链）。

---

### 高并发 AI 对话系统的服务拆分 · 困难

**来源：** 拼多多 - AI 全栈二面（场景设计）

从零设计一套高并发 AI 对话系统，你会怎么拆服务？

**考点：** 接入层（SSE 网关 / 长连接）→ 会话服务（上下文存储 Redis + 持久化）→ 编排服务（Agent / RAG 链路）→ 模型推理层（GPU 池化、队列削峰）、按会话粘性路由、流式转发与背压、限流降级（模型层过载时降级到小模型 / 排队话术）、监控（首 token 延迟 / 吞吐 / 幻觉率）。

---

### 前端与算法团队的流式接口约定 · 中等

**来源：** 拼多多 - AI 全栈二面（场景设计）

前端如何和算法团队约定流式接口、错误码和数据结构？

**考点：** 帧格式设计（event type：token / tool_call / done / error）、错误码分级（可重试 / 不可重试 / 需转人工）、断线重连与续传（Last-Event-ID / 消息序号）、版本兼容（字段只增不改）、Mock 协议让前端先行开发。

---

## 代码 Review

### 支付转账代码 Review · 困难

**来源：** 腾讯微信支付 - Agent 开发一面（题 3，禁 AI）

一段支付转账代码，含 `Transfer` 结构（from / to / amount）。找逻辑问题为主，风格问题权重低。

**当场追问：**

1. 这段代码有哪些逻辑上的问题？
2. 金额这样存储和比较有没有风险？（浮点精度 → 用整数分 / decimal）
3. 转账单号这样生成有什么问题？（随机数冲突 / 无幂等性）
4. 只有扣款没有加钱，语义上对吗？
5. 下游调用这里缺了什么保护？（超时 / 重试 / 幂等）
6. 超时了，你怎么判断扣款有没有真的成功？
7. 题干里有告诉你 Debit 是幂等的吗？
8. 接口幂等性未知 + 又是资金操作，超时未决下你的策略是什么？（冲正 / 挂起对账 / 查询补偿）
9. 如果下游连查询接口都没有呢？（对账兜底 + 人工处理队列）

**考点：** 支付业务的经典风险清单——金额精度、幂等性、超时未决、冲正与对账兜底、扣款加钱的事务完整性。

---

## 智力题

### 100 人 2 试纸找病人 · 困难

**来源：** 字节跳动 - Agent 开发实习一面

100 个人里有 1 个有病，有 2 个试纸，试纸一变色就不能再用了。如何最优地找出这个病人？

**考点：** 分治 / 编码思想——每份样本混合分组测试，一次排除一半（二分 → 7 次内定位）；更优解用二进制编码（100 人用 7 bit，理论上少量试纸组合定位）。候选人当时理解错题意，面试官提醒「最差也可以一个个试」——先确认题意中的最优目标（最少试纸数 vs 最少轮数）再作答。

---
