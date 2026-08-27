# NeetCode 150

> 来源：https://neetcode.io/practice (NeetCode 150)
>
> 本文档收录 NeetCode 150 全部 150 道题目及其完整题面，按 NeetCode 官方分类组织。
>
> 说明：题目以英文题面为准（NeetCode 原始列表），同时尽量补全力扣中文翻译。少数 LeetCode 付费题（如 Alien Dictionary、Meeting Rooms 等）在力扣中国可能没有对应中文页面，会标注英文原题链接。

---

## 目录

- [Arrays & Hashing](#arrays-hashing)
- [Two Pointers](#two-pointers)
- [Sliding Window](#sliding-window)
- [Stack](#stack)
- [Binary Search](#binary-search)
- [Linked List](#linked-list)
- [Trees](#trees)
- [Heap / Priority Queue](#heap-priority-queue)
- [Backtracking](#backtracking)
- [Tries](#tries)
- [Graphs](#graphs)
- [Advanced Graphs](#advanced-graphs)
- [1-D Dynamic Programming](#1-d-dynamic-programming)
- [2-D Dynamic Programming](#2-d-dynamic-programming)
- [Greedy](#greedy)
- [Intervals](#intervals)
- [Math & Geometry](#math-geometry)
- [Bit Manipulation](#bit-manipulation)

---

## Arrays & Hashing

### 1. Contains Duplicate · 简单

**链接（CN）：** https://leetcode.cn/problems/contains-duplicate/description/  
**链接（EN）：** https://leetcode.com/problems/contains-duplicate/

给你一个整数数组 `nums` 。如果任一值在数组中出现 **至少两次** ，返回 `true` ；如果数组中每个元素互不相同，返回 `false` 。

**示例 1：**

**输入：**nums = \[1,2,3,1\]

**输出：**true

**解释：**

元素 1 在下标 0 和 3 出现。

**示例 2：**

**输入：**nums = \[1,2,3,4\]

**输出：**false

**解释：**

所有元素都不同。

**示例 3：**

**输入：**nums = \[1,1,1,3,3,4,3,2,4,2\]

**输出：**true

**提示：**

-   `1 <= nums.length <= 105`
-   `-109 <= nums[i] <= 109`

---

### 2. Valid Anagram · 简单

**链接（CN）：** https://leetcode.cn/problems/valid-anagram/description/  
**链接（EN）：** https://leetcode.com/problems/valid-anagram/

给定两个字符串 `s` 和 `t` ，编写一个函数来判断 `t` 是否是 `s` 的 字母异位词。

**示例 1:**

```
输入: s = "anagram", t = "nagaram"
输出: true
```

**示例 2:**

```
输入: s = "rat", t = "car"
输出: false
```

**提示:**

-   `1 <= s.length, t.length <= 5 * 104`
-   `s` 和 `t` 仅包含小写字母

**进阶:** 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

---

### 3. Two Sum · 简单

**链接（CN）：** https://leetcode.cn/problems/two-sum/description/  
**链接（EN）：** https://leetcode.com/problems/two-sum/

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** _`target`_  的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例 2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例 3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]
```

**提示：**

-   `2 <= nums.length <= 104`
-   `-109 <= nums[i] <= 109`
-   `-109 <= target <= 109`
-   **只会存在一个有效答案**

**进阶：**你可以想出一个时间复杂度小于 `O(n2)` 的算法吗？

---

### 4. Group Anagrams · 中等

**链接（CN）：** https://leetcode.cn/problems/group-anagrams/description/  
**链接（EN）：** https://leetcode.com/problems/group-anagrams/

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

**示例 1:**

**输入:** strs = \["eat", "tea", "tan", "ate", "nat", "bat"\]

**输出:** \[\["bat"\],\["nat","tan"\],\["ate","eat","tea"\]\]

**解释：**

-   在 strs 中没有字符串可以通过重新排列来形成 `"bat"`。
-   字符串 `"nat"` 和 `"tan"` 是字母异位词，因为它们可以重新排列以形成彼此。
-   字符串 `"ate"` ，`"eat"` 和 `"tea"` 是字母异位词，因为它们可以重新排列以形成彼此。

**示例 2:**

**输入:** strs = \[""\]

**输出:** \[\[""\]\]

**示例 3:**

**输入:** strs = \["a"\]

**输出:** \[\["a"\]\]

**提示：**

-   `1 <= strs.length <= 104`
-   `0 <= strs[i].length <= 100`
-   `strs[i]` 仅包含小写字母

---

### 5. Top K Frequent Elements · 中等

**链接（CN）：** https://leetcode.cn/problems/top-k-frequent-elements/description/  
**链接（EN）：** https://leetcode.com/problems/top-k-frequent-elements/

给你一个整数数组 `nums` 和一个整数 `k` ，请你返回其中出现频率前 `k` 高的元素。你可以按 **任意顺序** 返回答案。

**示例 1：**

**输入：**nums = \[1,1,1,2,2,3\], k = 2

**输出：**\[1,2\]

**示例 2：**

**输入：**nums = \[1\], k = 1

**输出：**\[1\]

**示例 3：**

**输入：**nums = \[1,2,1,2,1,2,3,1,3,2\], k = 2

**输出：**\[1,2\]

**提示：**

-   `1 <= nums.length <= 105`
-   `-104 <= nums[i] <= 104`
-   `k` 的取值范围是 `[1, 数组中不相同的元素的个数]`
-   题目数据保证答案唯一，换句话说，数组中前 `k` 个高频元素的集合是唯一的

**进阶：**你所设计算法的时间复杂度 **必须** 优于 `O(n log n)` ，其中 `n` 是数组大小。

---

### 6. Encode and Decode Strings · 中等

**链接（CN）：** https://leetcode.cn/problems/encode-and-decode-strings/description/  
**链接（EN）：** https://leetcode.com/problems/encode-and-decode-strings/


(无题干)

---

### 7. Product of Array Except Self · 中等

**链接（CN）：** https://leetcode.cn/problems/product-of-array-except-self/description/  
**链接（EN）：** https://leetcode.com/problems/product-of-array-except-self/

给你一个整数数组 `nums`，返回 数组 `answer` ，其中 `answer[i]` 等于 `nums` 中除了 `nums[i]` 之外其余各元素的乘积 。

题目数据 **保证** 数组 `nums`之中任意元素的全部前缀元素和后缀的乘积都在  **32 位** 整数范围内。

请 **不要使用除法，**且在 `O(n)` 时间复杂度内完成此题。

**示例 1:**

```
输入: nums = [1,2,3,4]
输出: [24,12,8,6]
```

**示例 2:**

```
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
```

**提示：**

-   `2 <= nums.length <= 105`
-   `-30 <= nums[i] <= 30`
-   输入 **保证** 数组 `answer[i]` 在  **32 位** 整数范围内

**进阶：**你可以在 `O(1)` 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 **不被视为** 额外空间。）

---

### 8. Valid Sudoku · 中等

**链接（CN）：** https://leetcode.cn/problems/valid-sudoku/description/  
**链接（EN）：** https://leetcode.com/problems/valid-sudoku/

请你判断一个 `9 x 9` 的数独是否有效。只需要 **根据以下规则** ，验证已经填入的数字是否有效即可。

1.  数字 `1-9` 在每一行只能出现一次。
2.  数字 `1-9` 在每一列只能出现一次。
3.  数字 `1-9` 在每一个以粗实线分隔的 `3x3` 宫内只能出现一次。（请参考示例图）

**注意：**

-   一个有效的数独（部分已被填充）不一定是可解的。
-   只需要根据以上规则，验证已经填入的数字是否有效即可。
-   空白格用 `'.'` 表示。

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714svg.png)
```
输入：board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：true
```

**示例 2：**

```
输入：board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：false
解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
```

**提示：**

-   `board.length == 9`
-   `board[i].length == 9`
-   `board[i][j]` 是一位数字（`1-9`）或者 `'.'`

---

### 9. Longest Consecutive Sequence · 中等

**链接（CN）：** https://leetcode.cn/problems/longest-consecutive-sequence/description/  
**链接（EN）：** https://leetcode.com/problems/longest-consecutive-sequence/

给定一个未排序的整数数组 `nums` ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

**示例 1：**

```
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
```

**示例 2：**

```
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
```

**示例 3：**

```
输入：nums = [1,0,1,2]
输出：3
```

**提示：**

-   `0 <= nums.length <= 105`
-   `-109 <= nums[i] <= 109`

---


## Two Pointers

### 10. Valid Palindrome · 简单

**链接（CN）：** https://leetcode.cn/problems/valid-palindrome/description/  
**链接（EN）：** https://leetcode.com/problems/valid-palindrome/

如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 **回文串** 。

字母和数字都属于字母数字字符。

给你一个字符串 `s`，如果它是 **回文串** ，返回 `true` ；否则，返回 `false` 。

**示例 1：**

```
输入: s = "A man, a plan, a canal: Panama"
输出：true
解释："amanaplanacanalpanama" 是回文串。
```

**示例 2：**

```
输入：s = "race a car"
输出：false
解释："raceacar" 不是回文串。
```

**示例 3：**

```
输入：s = " "
输出：true
解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
由于空字符串正着反着读都一样，所以是回文串。
```

**提示：**

-   `1 <= s.length <= 2 * 105`
-   `s` 仅由可打印的 ASCII 字符组成

---

### 11. Two Sum II Input Array Is Sorted · 中等

**链接（CN）：** https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/  
**链接（EN）：** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

给你一个下标从 **1** 开始的整数数组 `numbers` ，该数组已按 **非递减顺序排列**  ，请你从数组中找出满足相加之和等于目标数 `target` 的两个数。如果设这两个数分别是 `numbers[index1]` 和 `numbers[index2]` ，则 `1 <= index1 < index2 <= numbers.length` 。

以长度为 2 的整数数组 `[index1, index2]` 的形式返回这两个整数的下标 `index1` 和 `index2`。

你可以假设每个输入 **只对应唯一的答案** ，而且你 **不可以** 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。

 

**示例 1：**

```
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
```

**示例 2：**

```
输入：numbers = [2,3,4], target = 6
输出：[1,3]
解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。
```

**示例 3：**

```
输入：numbers = [-1,0], target = -1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
```

**提示：**

-   `2 <= numbers.length <= 3 * 104`
-   `-1000 <= numbers[i] <= 1000`
-   `numbers` 按 **非递减顺序** 排列
-   `-1000 <= target <= 1000`
-   **仅存在一个有效答案**

---

### 12. 3Sum · 中等

**链接（CN）：** https://leetcode.cn/problems/3sum/description/  
**链接（EN）：** https://leetcode.com/problems/3sum/

给你一个整数数组 `nums` ，判断是否存在三元组 `[nums[i], nums[j], nums[k]]` 满足 `i != j`、`i != k` 且 `j != k` ，同时还满足 `nums[i] + nums[j] + nums[k] == 0` 。请你返回所有和为 `0` 且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

**示例 1：**

```
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
```

**示例 2：**

```
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
```

**示例 3：**

```
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
```

**提示：**

-   `3 <= nums.length <= 3000`
-   `-105 <= nums[i] <= 105`

---

### 13. Container With Most Water · 中等

**链接（CN）：** https://leetcode.cn/problems/container-with-most-water/description/  
**链接（EN）：** https://leetcode.com/problems/container-with-most-water/

给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

**说明：**你不能倾斜容器。

**示例 1：**

![](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg)

```
输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
```

**示例 2：**

```
输入：height = [1,1]
输出：1
```

**提示：**

-   `n == height.length`
-   `2 <= n <= 105`
-   `0 <= height[i] <= 104`

---

### 14. Trapping Rain Water · 困难

**链接（CN）：** https://leetcode.cn/problems/trapping-rain-water/description/  
**链接（EN）：** https://leetcode.com/problems/trapping-rain-water/

给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png)

```
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
```

**示例 2：**

```
输入：height = [4,2,0,3,2,5]
输出：9
```

**提示：**

-   `n == height.length`
-   `1 <= n <= 2 * 104`
-   `0 <= height[i] <= 105`

---


## Sliding Window

### 15. Best Time to Buy And Sell Stock · 简单

**链接（CN）：** https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/  
**链接（EN）：** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

**示例 1：**

```
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```

**示例 2：**

```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```

**提示：**

-   `1 <= prices.length <= 105`
-   `0 <= prices[i] <= 104`

---

### 16. Longest Substring Without Repeating Characters · 中等

**链接（CN）：** https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/  
**链接（EN）：** https://leetcode.com/problems/longest-substring-without-repeating-characters/  
**面经出现：** 高德 - 大模型算法一面；恒生电子 - AI Agent 开发岗一面（手撕）

给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长 子串** 的长度。

**示例 1:**

```
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
```

**示例 2:**

```
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

**示例 3:**

```
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

**提示：**

-   `0 <= s.length <= 5 * 104`
-   `s` 由英文字母、数字、符号和空格组成

---

### 17. Longest Repeating Character Replacement · 中等

**链接（CN）：** https://leetcode.cn/problems/longest-repeating-character-replacement/description/  
**链接（EN）：** https://leetcode.com/problems/longest-repeating-character-replacement/

给你一个字符串 `s` 和一个整数 `k` 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 `k` 次。

在执行上述操作后，返回 _包含相同字母的最长子字符串的长度。_

**示例 1：**

```
输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。
```

**示例 2：**

```
输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。
可能存在其他的方法来得到同样的结果。
```

**提示：**

-   `1 <= s.length <= 105`
-   `s` 仅由大写英文字母组成
-   `0 <= k <= s.length`

---

### 18. Permutation In String · 中等

**链接（CN）：** https://leetcode.cn/problems/permutation-in-string/description/  
**链接（EN）：** https://leetcode.com/problems/permutation-in-string/

给你两个字符串 `s1` 和 `s2` ，写一个函数来判断 `s2` 是否包含 `s1` 的 排列。如果是，返回 `true` ；否则，返回 `false` 。

换句话说，`s1` 的排列之一是 `s2` 的 **子串** 。

**示例 1：**

```
输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").
```

**示例 2：**

```
输入：s1= "ab" s2 = "eidboaoo"
输出：false
```

**提示：**

-   `1 <= s1.length, s2.length <= 104`
-   `s1` 和 `s2` 仅包含小写字母

---

### 19. Minimum Window Substring · 困难

**链接（CN）：** https://leetcode.cn/problems/minimum-window-substring/description/  
**链接（EN）：** https://leetcode.com/problems/minimum-window-substring/

给定两个字符串 `s` 和 `t`，长度分别是 `m` 和 `n`，返回 s 中的 **最短窗口 子串**，使得该子串包含 `t` 中的每一个字符（**包括重复字符**）。如果没有这样的子串，返回空字符串 `""`。

测试用例保证答案唯一。

**示例 1：**

```
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
```

**示例 2：**

```
输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
```

**示例 3:**

```
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
```

**提示：**

-   `m == s.length`
-   `n == t.length`
-   `1 <= m, n <= 105`
-   `s` 和 `t` 由英文字母组成

**进阶：**你能设计一个在 `O(m + n)` 时间内解决此问题的算法吗？

---

### 20. Sliding Window Maximum · 困难

**链接（CN）：** https://leetcode.cn/problems/sliding-window-maximum/description/  
**链接（EN）：** https://leetcode.com/problems/sliding-window-maximum/

给你一个整数数组 `nums`，有一个大小为 `k` 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。

返回 _滑动窗口中的最大值_ 。

**示例 1：**

```
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

**示例 2：**

```
输入：nums = [1], k = 1
输出：[1]
```

**提示：**

-   `1 <= nums.length <= 105`
-   `-104 <= nums[i] <= 104`
-   `1 <= k <= nums.length`

---


## Stack

### 21. Valid Parentheses · 简单

**链接（CN）：** https://leetcode.cn/problems/valid-parentheses/description/  
**链接（EN）：** https://leetcode.com/problems/valid-parentheses/  
**面经出现：** Enerjoy - iOS 开发一面

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：

1.  左括号必须用相同类型的右括号闭合。
2.  左括号必须以正确的顺序闭合。
3.  每个右括号都有一个对应的相同类型的左括号。

**示例 1：**

**输入：**s = "()"

**输出：**true

**示例 2：**

**输入：**s = "()\[\]{}"

**输出：**true

**示例 3：**

**输入：**s = "(\]"

**输出：**false

**示例 4：**

**输入：**s = "(\[\])"

**输出：**true

**示例 5：**

**输入：**s = "(\[)\]"

**输出：**false

**提示：**

-   `1 <= s.length <= 104`
-   `s` 仅由括号 `'()[]{}'` 组成

---

### 22. Min Stack · 中等

**链接（CN）：** https://leetcode.cn/problems/min-stack/description/  
**链接（EN）：** https://leetcode.com/problems/min-stack/

设计一个支持 `push` ，`pop` ，`top` 操作，并能在常数时间内检索到最小元素的栈。

实现 `MinStack` 类:

-   `MinStack()` 初始化堆栈对象。
-   `void push(int value)` 将元素 `value` 推入堆栈。
-   `void pop()` 删除堆栈顶部的元素。
-   `int top()` 获取堆栈顶部的元素。
-   `int getMin()` 获取堆栈中的最小元素。

**示例 1:**

```
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
```

**提示：**

-   `-231 <= val <= 231 - 1`
-   `pop`、`top` 和 `getMin` 操作总是在 **非空栈** 上调用
-   `push`, `pop`, `top`, and `getMin`最多被调用 `3 * 104` 次

---

### 23. Evaluate Reverse Polish Notation · 中等

**链接（CN）：** https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/  
**链接（EN）：** https://leetcode.com/problems/evaluate-reverse-polish-notation/

给你一个字符串数组 `tokens` ，表示一个根据 [逆波兰表示法](https://baike.baidu.com/item/%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F/128437) 表示的算术表达式。

请你计算该表达式。返回一个表示表达式值的整数。

**注意：**

-   有效的算符为 `'+'`、`'-'`、`'*'` 和 `'/'` 。
-   每个操作数（运算对象）都可以是一个整数或者另一个表达式。
-   两个整数之间的除法总是 **向零截断** 。
-   表达式中不含除零运算。
-   输入是一个根据逆波兰表示法表示的算术表达式。
-   答案及所有中间计算结果可以用 **32 位** 整数表示。

**示例 1：**

```
输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
```

**示例 2：**

```
输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
```

**示例 3：**

```
输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

**提示：**

-   `1 <= tokens.length <= 104`
-   `tokens[i]` 是一个算符（`"+"`、`"-"`、`"*"` 或 `"/"`），或是在范围 `[-200, 200]` 内的一个整数

**逆波兰表达式：**

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。

-   平常使用的算式则是一种中缀表达式，如 `( 1 + 2 ) * ( 3 + 4 )` 。
-   该算式的逆波兰表达式写法为 `( ( 1 2 + ) ( 3 4 + ) * )` 。

逆波兰表达式主要有以下两个优点：

-   去掉括号后表达式无歧义，上式即便写成 `1 2 + 3 4 + *` 也可以依据次序计算出正确结果。
-   适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中

---

### 24. Daily Temperatures · 中等

**链接（CN）：** https://leetcode.cn/problems/daily-temperatures/description/  
**链接（EN）：** https://leetcode.com/problems/daily-temperatures/

给定一个整数数组 `temperatures` ，表示每天的温度，返回一个数组 `answer` ，其中 `answer[i]` 是指对于第 `i` 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 `0` 来代替。

**示例 1:**

```
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
```

**示例 2:**

```
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
```

**示例 3:**

```
输入: temperatures = [30,60,90]
输出: [1,1,0]
```

**提示：**

-   `1 <= temperatures.length <= 105`
-   `30 <= temperatures[i] <= 100`

---

### 25. Car Fleet · 中等

**链接（CN）：** https://leetcode.cn/problems/car-fleet/description/  
**链接（EN）：** https://leetcode.com/problems/car-fleet/

在一条单行道上，有 `n` 辆车开往同一目的地。目的地是几英里以外的 `target` 。

给定两个整数数组 `position` 和 `speed` ，长度都是 `n` ，其中 `position[i]` 是第 `i` 辆车的位置， `speed[i]` 是第 `i` 辆车的速度(单位是英里/小时)。

一辆车永远不会超过前面的另一辆车，但它可以追上去，并以较慢车的速度在另一辆车旁边行驶。

**车队** 是指并排行驶的一辆或几辆汽车。车队的速度是车队中 **最慢** 的车的速度。

即便一辆车在 `target` 才赶上了一个车队，它们仍然会被视作是同一个车队。

返回到达目的地的车队数量 。

**示例 1：**

**输入：**target = 12, position = \[10,8,0,5,3\], speed = \[2,4,1,1,3\]

**输出：**3

**解释：**

-   从 10（速度为 2）和 8（速度为 4）开始的车会组成一个车队，它们在 12 相遇。车队在 `target` 形成。
-   从 0（速度为 1）开始的车不会追上其它任何车，所以它自己是一个车队。
-   从 5（速度为 1） 和 3（速度为 3）开始的车组成一个车队，在 6 相遇。车队以速度 1 移动直到它到达 `target`。

**示例 2：**

**输入：**target = 10, position = \[3\], speed = \[3\]

**输出：**1

**解释：**

只有一辆车，因此只有一个车队。

**示例 3：**

**输入：**target = 100, position = \[0,2,4\], speed = \[4,2,1\]

**输出：**1

**解释：**

-   从 0（速度为 4） 和 2（速度为 2）开始的车组成一个车队，在 4 相遇。从 4 开始的车（速度为 1）移动到了 5。
-   然后，在 4（速度为 2）的车队和在 5（速度为 1）的车成为一个车队，在 6 相遇。车队以速度 1 移动直到它到达 `target`。

**提示：**

-   `n == position.length == speed.length`
-   `1 <= n <= 105`
-   `0 < target <= 106`
-   `0 <= position[i] < target`
-   `position` 中每个值都 **不同**
-   `0 < speed[i] <= 106`

---

### 26. Largest Rectangle In Histogram · 困难

**链接（CN）：** https://leetcode.cn/problems/largest-rectangle-in-histogram/description/  
**链接（EN）：** https://leetcode.com/problems/largest-rectangle-in-histogram/

给定 _n_ 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

**示例 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

```
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

```
输入： heights = [2,4]
输出： 4
```

**提示：**

-   `1 <= heights.length <=105`
-   `0 <= heights[i] <= 104`

---


## Binary Search

### 27. Binary Search · 简单

**链接（CN）：** https://leetcode.cn/problems/binary-search/description/  
**链接（EN）：** https://leetcode.com/problems/binary-search/

给定一个 `n` 个元素有序的（升序）整型数组 `nums` 和一个目标值 `target`  ，写一个函数搜索 `nums` 中的 `target`，如果 `target` 存在返回下标，否则返回 `-1`。

你必须编写一个具有 `O(log n)` 时间复杂度的算法。

  
**示例 1:**

```
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
```

**示例 2:**

```
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
```

**提示：**

1.  你可以假设 `nums` 中的所有元素是不重复的。
2.  `n` 将在 `[1, 10000]`之间。
3.  `nums` 的每个元素都将在 `[-9999, 9999]`之间。

---

### 28. Search a 2D Matrix · 中等

**链接（CN）：** https://leetcode.cn/problems/search-a-2d-matrix/description/  
**链接（EN）：** https://leetcode.com/problems/search-a-2d-matrix/

给你一个满足下述两条属性的 `m x n` 整数矩阵：

-   每行中的整数从左到右按非严格递增顺序排列。
-   每行的第一个整数大于前一行的最后一个整数。

给你一个整数 `target` ，如果 `target` 在矩阵中，返回 `true` ；否则，返回 `false` 。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)
```
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
```

**示例 2：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/25/mat2.jpg)
```
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
```

**提示：**

-   `m == matrix.length`
-   `n == matrix[i].length`
-   `1 <= m, n <= 100`
-   `-104 <= matrix[i][j], target <= 104`

---

### 29. Koko Eating Bananas · 中等

**链接（CN）：** https://leetcode.cn/problems/koko-eating-bananas/description/  
**链接（EN）：** https://leetcode.com/problems/koko-eating-bananas/

珂珂喜欢吃香蕉。这里有 `n` 堆香蕉，第 `i` 堆中有 `piles[i]` 根香蕉。警卫已经离开了，将在 `h` 小时后回来。

珂珂可以决定她吃香蕉的速度 `k` （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 `k` 根。如果这堆香蕉少于 `k` 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 `h` 小时内吃掉所有香蕉的最小速度 `k`（`k` 为整数）。

**示例 1：**

```
输入：piles = [3,6,7,11], h = 8
输出：4
```

**示例 2：**

```
输入：piles = [30,11,23,4,20], h = 5
输出：30
```

**示例 3：**

```
输入：piles = [30,11,23,4,20], h = 6
输出：23
```

**提示：**

-   `1 <= piles.length <= 104`
-   `piles.length <= h <= 109`
-   `1 <= piles[i] <= 109`

---

### 30. Find Minimum In Rotated Sorted Array · 中等

**链接（CN）：** https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/  
**链接（EN）：** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

已知一个长度为 `n` 的数组，预先按照升序排列，经由 `1` 到 `n` 次 **旋转** 后，得到输入数组。例如，原数组 `nums = [0,1,2,4,5,6,7]` 在变化后可能得到：

-   若旋转 `4` 次，则可以得到 `[4,5,6,7,0,1,2]`
-   若旋转 `7` 次，则可以得到 `[0,1,2,4,5,6,7]`

注意，数组 `[a[0], a[1], a[2], ..., a[n-1]]` **旋转一次** 的结果为数组 `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]` 。

给你一个元素值 **互不相同** 的数组 `nums` ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 **最小元素** 。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

**示例 1：**

```
输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
```

**示例 2：**

```
输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
```

**示例 3：**

```
输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
```

**提示：**

-   `n == nums.length`
-   `1 <= n <= 5000`
-   `-5000 <= nums[i] <= 5000`
-   `nums` 中的所有整数 **互不相同**
-   `nums` 原来是一个升序排序的数组，并进行了 `1` 至 `n` 次旋转

---

### 31. Search In Rotated Sorted Array · 中等

**链接（CN）：** https://leetcode.cn/problems/search-in-rotated-sorted-array/description/  
**链接（EN）：** https://leetcode.com/problems/search-in-rotated-sorted-array/

整数数组 `nums` 按升序排列，数组中的值 **互不相同** 。

在传递给函数之前，`nums` 在预先未知的某个下标 `k`（`0 <= k < nums.length`）上进行了 **向左旋转**，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`（下标 **从 0 开始** 计数）。例如， `[0,1,2,4,5,6,7]` 下标 `3` 上向左旋转后可能变为 `[4,5,6,7,0,1,2]` 。

给你 **旋转后** 的数组 `nums` 和一个整数 `target` ，如果 `nums` 中存在这个目标值 `target` ，则返回它的下标，否则返回 `-1` 。

你必须设计一个时间复杂度为 `O(log n)` 的算法解决此问题。

**示例 1：**

```
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
```

**示例 2：**

```
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
```

**示例 3：**

```
输入：nums = [1], target = 0
输出：-1
```

**提示：**

-   `1 <= nums.length <= 5000`
-   `-104 <= nums[i] <= 104`
-   `nums` 中的每个值都 **独一无二**
-   题目数据保证 `nums` 在预先未知的某个下标上进行了旋转
-   `-104 <= target <= 104`

---

### 32. Time Based Key Value Store · 中等

**链接（CN）：** https://leetcode.cn/problems/time-based-key-value-store/description/  
**链接（EN）：** https://leetcode.com/problems/time-based-key-value-store/

设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。

实现 `TimeMap` 类：

-   `TimeMap()` 初始化数据结构对象
-   `void set(String key, String value, int timestamp)` 存储给定时间戳 `timestamp` 时的键 `key` 和值 `value`。
-   `String get(String key, int timestamp)` 返回一个值，该值在之前调用了 `set`，其中 `timestamp_prev <= timestamp` 。如果有多个这样的值，它将返回与最大  `timestamp_prev` 关联的值。如果没有值，则返回空字符串（`""`）。

 

**示例 1：**

```
输入：
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
输出：
[null, null, "bar", "bar", null, "bar2", "bar2"]

解释：
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1   
timeMap.get("foo", 1);         // 返回 "bar"
timeMap.get("foo", 3);         // 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 。
timeMap.set("foo", "bar2", 4); // 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4  
timeMap.get("foo", 4);         // 返回 "bar2"
timeMap.get("foo", 5);         // 返回 "bar2"
```

**提示：**

-   `1 <= key.length, value.length <= 100`
-   `key` 和 `value` 由小写英文字母和数字组成
-   `1 <= timestamp <= 107`
-   `set` 操作中的时间戳 `timestamp` 都是严格递增的
-   最多调用 `set` 和 `get` 操作 `2 * 105` 次

---

### 33. Median of Two Sorted Arrays · 困难

**链接（CN）：** https://leetcode.cn/problems/median-of-two-sorted-arrays/description/  
**链接（EN）：** https://leetcode.com/problems/median-of-two-sorted-arrays/

给定两个大小分别为 `m` 和 `n` 的正序（从小到大）数组 `nums1` 和 `nums2`。请你找出并返回这两个正序数组的 **中位数** 。

算法的时间复杂度应该为 `O(log (m+n))` 。

**示例 1：**

```
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
```

**示例 2：**

```
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
```

**提示：**

-   `nums1.length == m`
-   `nums2.length == n`
-   `0 <= m <= 1000`
-   `0 <= n <= 1000`
-   `1 <= m + n <= 2000`
-   `-106 <= nums1[i], nums2[i] <= 106`

---


## Linked List

### 34. Reverse Linked List · 简单

**链接（CN）：** https://leetcode.cn/problems/reverse-linked-list/description/  
**链接（EN）：** https://leetcode.com/problems/reverse-linked-list/  
**面经出现：** 番茄小说（字节）- iOS 客户端一面（思路对未调通）；虾皮 - Agent 开发一面（手撕 + 复杂度分析）

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

### 35. Merge Two Sorted Lists · 简单

**链接（CN）：** https://leetcode.cn/problems/merge-two-sorted-lists/description/  
**链接（EN）：** https://leetcode.com/problems/merge-two-sorted-lists/

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)
```
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
```

**示例 2：**

```
输入：l1 = [], l2 = []
输出：[]
```

**示例 3：**

```
输入：l1 = [], l2 = [0]
输出：[0]
```

**提示：**

-   两个链表的节点数目范围是 `[0, 50]`
-   `-100 <= Node.val <= 100`
-   `l1` 和 `l2` 均按 **非递减顺序** 排列

---

### 36. Linked List Cycle · 简单

**链接（CN）：** https://leetcode.cn/problems/linked-list-cycle/description/  
**链接（EN）：** https://leetcode.com/problems/linked-list-cycle/  
**面经出现：** Enerjoy - iOS 开发一面

给你一个链表的头节点 `head` ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。**注意：`pos` 不作为参数进行传递** 。仅仅是为了标识链表的实际情况。

_如果链表中存在环_ ，则返回 `true` 。 否则，返回 `false` 。

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

**示例 2：**

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

### 37. Reorder List · 中等

**链接（CN）：** https://leetcode.cn/problems/reorder-list/description/  
**链接（EN）：** https://leetcode.com/problems/reorder-list/  
**面经出现：** 月之暗面 - Agent 开发岗一面（数组解法被识破，考的是链表原地三步操作）

给定一个单链表 `L` 的头节点 `head` ，单链表 `L` 表示为：

```
L0 → L1 → … → Ln - 1 → Ln
```

请将其重新排列后变为：

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```

不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

**示例 1：**

![](https://pic.leetcode.cn/1626420311-PkUiGI-image.png)

```
输入：head = [1,2,3,4]
输出：[1,4,2,3]
```

**示例 2：**

![](https://pic.leetcode.cn/1626420320-YUiulT-image.png)

```
输入：head = [1,2,3,4,5]
输出：[1,5,2,4,3]
```

**提示：**

-   链表的长度范围为 `[1, 5 * 104]`
-   `1 <= node.val <= 1000`

---

### 38. Remove Nth Node From End of List · 中等

**链接（CN）：** https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/  
**链接（EN）：** https://leetcode.com/problems/remove-nth-node-from-end-of-list/

给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)
```
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
```

**示例 2：**

```
输入：head = [1], n = 1
输出：[]
```

**示例 3：**

```
输入：head = [1,2], n = 1
输出：[1]
```

**提示：**

-   链表中结点的数目为 `sz`
-   `1 <= sz <= 30`
-   `0 <= Node.val <= 100`
-   `1 <= n <= sz`

**进阶：**你能尝试使用一趟扫描实现吗？

---

### 39. Copy List With Random Pointer · 中等

**链接（CN）：** https://leetcode.cn/problems/copy-list-with-random-pointer/description/  
**链接（EN）：** https://leetcode.com/problems/copy-list-with-random-pointer/

给你一个长度为 `n` 的链表，每个节点包含一个额外增加的随机指针 `random` ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 **[深拷贝](https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin)**。 深拷贝应该正好由 `n` 个 **全新** 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 `next` 指针和 `random` 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。**复制链表中的指针都不应指向原链表中的节点** 。

例如，如果原链表中有 `X` 和 `Y` 两个节点，其中 `X.random --> Y` 。那么在复制链表中对应的两个节点 `x` 和 `y` ，同样有 `x.random --> y` 。

返回复制链表的头节点。

用一个由 `n` 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 `[val, random_index]` 表示：

-   `val`：一个表示 `Node.val` 的整数。
-   `random_index`：随机指针指向的节点索引（范围从 `0` 到 `n-1`）；如果不指向任何节点，则为  `null` 。

你的代码 **只** 接受原链表的头节点 `head` 作为传入参数。

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e1.png)

```
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**示例 2：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e2.png)

```
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
```

**示例 3：**

**![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/01/09/e3.png)**

```
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
```

**提示：**

-   `0 <= n <= 1000`
-   `-104 <= Node.val <= 104`
-   `Node.random` 为 `null` 或指向链表中的节点。

---

### 40. Add Two Numbers · 中等

**链接（CN）：** https://leetcode.cn/problems/add-two-numbers/description/  
**链接（EN）：** https://leetcode.com/problems/add-two-numbers/

给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节点只能存储 **一位** 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg)
```
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
```

**示例 2：**

```
输入：l1 = [0], l2 = [0]
输出：[0]
```

**示例 3：**

```
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
```

**提示：**

-   每个链表中的节点数在范围 `[1, 100]` 内
-   `0 <= Node.val <= 9`
-   题目数据保证列表表示的数字不含前导零

---

### 41. Find The Duplicate Number · 中等

**链接（CN）：** https://leetcode.cn/problems/find-the-duplicate-number/description/  
**链接（EN）：** https://leetcode.com/problems/find-the-duplicate-number/

给定一个包含 `n + 1` 个整数的数组 `nums` ，其数字都在 `[1, n]` 范围内（包括 `1` 和 `n`），可知至少存在一个重复的整数。

假设 `nums` 只有 **一个重复的整数** ，返回 **这个重复的数** 。

你设计的解决方案必须 **不修改** 数组 `nums` 且只用常量级 `O(1)` 的额外空间。

**示例 1：**

```
输入：nums = [1,3,4,2,2]
输出：2
```

**示例 2：**

```
输入：nums = [3,1,3,4,2]
输出：3
```

**示例 3 :**

```
输入：nums = [3,3,3,3,3]
输出：3
```

**提示：**

-   `1 <= n <= 105`
-   `nums.length == n + 1`
-   `1 <= nums[i] <= n`
-   `nums` 中 **只有一个整数** 出现 **两次或多次** ，其余整数均只出现 **一次**

**进阶：**

-   如何证明 `nums` 中至少存在一个重复的数字?
-   你可以设计一个线性级时间复杂度 `O(n)` 的解决方案吗？

---

### 42. LRU Cache · 中等

**链接（CN）：** https://leetcode.cn/problems/lru-cache/description/  
**链接（EN）：** https://leetcode.com/problems/lru-cache/  
**面经出现：** 快手 - AI 应用开发一面（手撕，ACM 模式）

请你设计并实现一个满足  [LRU (最近最少使用) 缓存](https://baike.baidu.com/item/LRU) 约束的数据结构。

实现 `LRUCache` 类：

-   `LRUCache(int capacity)` 以 **正整数** 作为容量 `capacity` 初始化 LRU 缓存
-   `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1` 。
-   `void put(int key, int value)` 如果关键字 `key` 已经存在，则变更其数据值 `value` ；如果不存在，则向缓存中插入该组 `key-value` 。如果插入操作导致关键字数量超过 `capacity` ，则应该 **逐出** 最久未使用的关键字。

函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。

**示例：**

```
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
```

**提示：**

-   `1 <= capacity <= 3000`
-   `0 <= key <= 10000`
-   `0 <= value <= 105`
-   最多调用 `2 * 105` 次 `get` 和 `put`

---

### 43. Merge K Sorted Lists · 困难

**链接（CN）：** https://leetcode.cn/problems/merge-k-sorted-lists/description/  
**链接（EN）：** https://leetcode.com/problems/merge-k-sorted-lists/

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

**示例 1：**

```
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
```

**示例 2：**

```
输入：lists = []
输出：[]
```

**示例 3：**

```
输入：lists = [[]]
输出：[]
```

**提示：**

-   `k == lists.length`
-   `0 <= k <= 10^4`
-   `0 <= lists[i].length <= 500`
-   `-10^4 <= lists[i][j] <= 10^4`
-   `lists[i]` 按 **升序** 排列
-   `lists[i].length` 的总和不超过 `10^4`

---

### 44. Reverse Nodes In K Group · 困难

**链接（CN）：** https://leetcode.cn/problems/reverse-nodes-in-k-group/description/  
**链接（EN）：** https://leetcode.com/problems/reverse-nodes-in-k-group/

给你链表的头节点 `head` ，每 `k` 个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)
```
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)

```
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
```

**提示：**

-   链表中的节点数目为 `n`
-   `1 <= k <= n <= 5000`
-   `0 <= Node.val <= 1000`

**进阶：**你可以设计一个只用 `O(1)` 额外内存空间的算法解决此问题吗？

---


## Trees

### 45. Invert Binary Tree · 简单

**链接（CN）：** https://leetcode.cn/problems/invert-binary-tree/description/  
**链接（EN）：** https://leetcode.com/problems/invert-binary-tree/

给你一棵二叉树的根节点 `root` ，翻转这棵二叉树，并返回其根节点。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

```
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

```
输入：root = [2,1,3]
输出：[2,3,1]
```

**示例 3：**

```
输入：root = []
输出：[]
```

**提示：**

-   树中节点数目范围在 `[0, 100]` 内
-   `-100 <= Node.val <= 100`

---

### 46. Maximum Depth of Binary Tree · 简单

**链接（CN）：** https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/  
**链接（EN）：** https://leetcode.com/problems/maximum-depth-of-binary-tree/

给定一个二叉树 `root` ，返回其最大深度。

二叉树的 **最大深度** 是指从根节点到最远叶子节点的最长路径上的节点数。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

```
输入：root = [3,9,20,null,null,15,7]
输出：3
```

**示例 2：**

```
输入：root = [1,null,2]
输出：2
```

**提示：**

-   树中节点的数量在 `[0, 104]` 区间内。
-   `-100 <= Node.val <= 100`

---

### 47. Diameter of Binary Tree · 简单

**链接（CN）：** https://leetcode.cn/problems/diameter-of-binary-tree/description/  
**链接（EN）：** https://leetcode.com/problems/diameter-of-binary-tree/

给你一棵二叉树的根节点，返回该树的 **直径** 。

二叉树的 **直径** 是指树中任意两个节点之间最长路径的 **长度** 。这条路径可能经过也可能不经过根节点 `root` 。

两节点之间路径的 **长度** 由它们之间边数表示。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)
```
输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
```

**示例 2：**

```
输入：root = [1,2]
输出：1
```

**提示：**

-   树中节点数目在范围 `[1, 104]` 内
-   `-100 <= Node.val <= 100`

---

### 48. Balanced Binary Tree · 简单

**链接（CN）：** https://leetcode.cn/problems/balanced-binary-tree/description/  
**链接（EN）：** https://leetcode.com/problems/balanced-binary-tree/

给定一个二叉树，判断它是否是 平衡二叉树  

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)
```
输入：root = [3,9,20,null,null,15,7]
输出：true
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)
```
输入：root = [1,2,2,3,3,null,null,4,4]
输出：false
```

**示例 3：**

```
输入：root = []
输出：true
```

**提示：**

-   树中的节点数在范围 `[0, 5000]` 内
-   `-104 <= Node.val <= 104`

---

### 49. Same Tree · 简单

**链接（CN）：** https://leetcode.cn/problems/same-tree/description/  
**链接（EN）：** https://leetcode.com/problems/same-tree/

给你两棵二叉树的根节点 `p` 和 `q` ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)
```
输入：p = [1,2,3], q = [1,2,3]
输出：true
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)
```
输入：p = [1,2], q = [1,null,2]
输出：false
```

**示例 3：**

![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)
```
输入：p = [1,2,1], q = [1,1,2]
输出：false
```

**提示：**

-   两棵树上的节点数目都在范围 `[0, 100]` 内
-   `-104 <= Node.val <= 104`

---

### 50. Subtree of Another Tree · 简单

**链接（CN）：** https://leetcode.cn/problems/subtree-of-another-tree/description/  
**链接（EN）：** https://leetcode.com/problems/subtree-of-another-tree/

给你两棵二叉树 `root` 和 `subRoot` 。检验 `root` 中是否包含和 `subRoot` 具有相同结构和节点值的子树。如果存在，返回 `true` ；否则，返回 `false` 。

二叉树 `tree` 的一棵子树包括 `tree` 的某个节点和这个节点的所有后代节点。`tree` 也可以看做它自身的一棵子树。

**示例 1：**

![](https://pic.leetcode.cn/1724998676-cATjhe-image.png)
```
输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true
```

**示例 2：**

![](https://pic.leetcode.cn/1724998698-sEJWnq-image.png)
```
输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
输出：false
```

**提示：**

-   `root` 树上的节点数量范围是 `[1, 2000]`
-   `subRoot` 树上的节点数量范围是 `[1, 1000]`
-   `-104 <= root.val <= 104`
-   `-104 <= subRoot.val <= 104`

---

### 51. Lowest Common Ancestor of a Binary Search Tree · 中等

**链接（CN）：** https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/description/  
**链接（EN）：** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

[百度百科](https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin)中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

例如，给定如下二叉搜索树:  root = \[6,2,8,0,4,7,9,null,null,3,5\]

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png)

**示例 1:**

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
```

**示例 2:**

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
```

**说明:**

-   所有节点的值都是唯一的。
-   p、q 为不同节点且均存在于给定的二叉搜索树中。

---

### 52. Binary Tree Level Order Traversal · 中等

**链接（CN）：** https://leetcode.cn/problems/binary-tree-level-order-traversal/description/  
**链接（EN）：** https://leetcode.com/problems/binary-tree-level-order-traversal/

给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。 （即逐层地，从左到右访问所有节点）。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)
```
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
```

**示例 2：**

```
输入：root = [1]
输出：[[1]]
```

**示例 3：**

```
输入：root = []
输出：[]
```

**提示：**

-   树中节点数目在范围 `[0, 2000]` 内
-   `-1000 <= Node.val <= 1000`

---

### 53. Binary Tree Right Side View · 中等

**链接（CN）：** https://leetcode.cn/problems/binary-tree-right-side-view/description/  
**链接（EN）：** https://leetcode.com/problems/binary-tree-right-side-view/

给定一个二叉树的 **根节点** `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

**示例 1：**

**输入：**root = \[1,2,3,null,5,null,4\]

**输出：**\[1,3,4\]

**解释：**

![](https://assets.leetcode.com/uploads/2024/11/24/tmpd5jn43fs-1.png)

**示例 2：**

**输入：**root = \[1,2,3,4,null,null,null,5\]

**输出：**\[1,3,4,5\]

**解释：**

![](https://assets.leetcode.com/uploads/2024/11/24/tmpkpe40xeh-1.png)

**示例 3：**

**输入：**root = \[1,null,3\]

**输出：**\[1,3\]

**示例 4：**

**输入：**root = \[\]

**输出：**\[\]

**提示:**

-   二叉树的节点个数的范围是 `[0,100]`
-   `-100 <= Node.val <= 100`

---

### 54. Count Good Nodes In Binary Tree · 中等

**链接（CN）：** https://leetcode.cn/problems/count-good-nodes-in-binary-tree/description/  
**链接（EN）：** https://leetcode.com/problems/count-good-nodes-in-binary-tree/

给你一棵根为 `root` 的二叉树，请你返回二叉树中好节点的数目。

「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。

**示例 1：**

**![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/16/test_sample_1.png)**

```
输入：root = [3,1,4,3,null,1,5]
输出：4
解释：图中蓝色节点为好节点。
根节点 (3) 永远是个好节点。
节点 4 -> (3,4) 是路径中的最大值。
节点 5 -> (3,4,5) 是路径中的最大值。
节点 3 -> (3,1,3) 是路径中的最大值。
```

**示例 2：**

**![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/16/test_sample_2.png)**

```
输入：root = [3,3,null,4,2]
输出：3
解释：节点 2 -> (3, 3, 2) 不是好节点，因为 "3" 比它大。
```

**示例 3：**

```
输入：root = [1]
输出：1
解释：根节点是好节点。
```

**提示：**

-   二叉树中节点数目范围是 `[1, 10^5]` 。
-   每个节点权值的范围是 `[-10^4, 10^4]` 。

---

### 55. Validate Binary Search Tree · 中等

**链接（CN）：** https://leetcode.cn/problems/validate-binary-search-tree/description/  
**链接（EN）：** https://leetcode.com/problems/validate-binary-search-tree/

给你一个二叉树的根节点 `root` ，判断其是否是一个有效的二叉搜索树。

**有效** 二叉搜索树定义如下：

-   节点的左子树只包含 **严格小于** 当前节点的数。
-   节点的右子树只包含 **严格大于** 当前节点的数。
-   所有左子树和右子树自身必须也是二叉搜索树。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)
```
输入：root = [2,1,3]
输出：true
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)
```
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。
```

**提示：**

-   树中节点数目范围在`[1, 104]` 内
-   `-231 <= Node.val <= 231 - 1`

---

### 56. Kth Smallest Element In a Bst · 中等

**链接（CN）：** https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/  
**链接（EN）：** https://leetcode.com/problems/kth-smallest-element-in-a-bst/

给定一个二叉搜索树的根节点 `root` ，和一个整数 `k` ，请你设计一个算法查找其中第 `k` 小的元素（`k` 从 1 开始计数）。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)
```
输入：root = [3,1,4,null,2], k = 1
输出：1
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)
```
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
```

**提示：**

-   树中的节点数为 `n` 。
-   `1 <= k <= n <= 104`
-   `0 <= Node.val <= 104`

**进阶：**如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 `k` 小的值，你将如何优化算法？

---

### 57. Construct Binary Tree From Preorder And Inorder Traversal · 中等

**链接（CN）：** https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/  
**链接（EN）：** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

给定两个整数数组 `preorder` 和 `inorder` ，其中 `preorder` 是二叉树的**先序遍历**， `inorder` 是同一棵树的**中序遍历**，请构造二叉树并返回其根节点。

**示例 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree.jpg)
```
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
```

**示例 2:**

```
输入: preorder = [-1], inorder = [-1]
输出: [-1]
```

**提示:**

-   `1 <= preorder.length <= 3000`
-   `inorder.length == preorder.length`
-   `-3000 <= preorder[i], inorder[i] <= 3000`
-   `preorder` 和 `inorder` 均 **无重复** 元素
-   `inorder` 均出现在 `preorder`
-   `preorder` **保证** 为二叉树的前序遍历序列
-   `inorder` **保证** 为二叉树的中序遍历序列

---

### 58. Binary Tree Maximum Path Sum · 困难

**链接（CN）：** https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/  
**链接（EN）：** https://leetcode.com/problems/binary-tree-maximum-path-sum/  
**面经出现：** 面壁智能 - 算法工程师一面

二叉树中的 **路径** 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 **至多出现一次** 。该路径 **至少包含一个** 节点，且不一定经过根节点。

**路径和** 是路径中各节点值的总和。

给你一个二叉树的根节点 `root` ，返回其 **最大路径和** 。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)
```
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)
```
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
```

**提示：**

-   树中节点数目范围是 `[1, 3 * 104]`
-   `-1000 <= Node.val <= 1000`

---

### 59. Serialize And Deserialize Binary Tree · 困难

**链接（CN）：** https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/description/  
**链接（EN）：** https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

**提示:** 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 [LeetCode 序列化二叉树的格式](https://leetcode.cn/help-center/3812581/)。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg)
```
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
```

**示例 2：**

```
输入：root = []
输出：[]
```

**示例 3：**

```
输入：root = [1]
输出：[1]
```

**示例 4：**

```
输入：root = [1,2]
输出：[1,2]
```

**提示：**

-   树中结点数在范围 `[0, 104]` 内
-   `-1000 <= Node.val <= 1000`

---


## Heap / Priority Queue

### 60. Kth Largest Element In a Stream · 简单

**链接（CN）：** https://leetcode.cn/problems/kth-largest-element-in-a-stream/description/  
**链接（EN）：** https://leetcode.com/problems/kth-largest-element-in-a-stream/

设计一个找到数据流中第 `k` 大元素的类（class）。注意是排序后的第 `k` 大元素，不是第 `k` 个不同的元素。

请实现 `KthLargest` 类：

-   `KthLargest(int k, int[] nums)` 使用整数 `k` 和整数流 `nums` 初始化对象。
-   `int add(int val)` 将 `val` 插入数据流 `nums` 后，返回当前数据流中第 `k` 大的元素。

**示例 1：**

**输入：**  
\["KthLargest", "add", "add", "add", "add", "add"\]  
\[\[3, \[4, 5, 8, 2\]\], \[3\], \[5\], \[10\], \[9\], \[4\]\]

**输出：**\[null, 4, 5, 5, 8, 8\]

**解释：**

KthLargest kthLargest = new KthLargest(3, \[4, 5, 8, 2\]);  
kthLargest.add(3); // 返回 4  
kthLargest.add(5); // 返回 5  
kthLargest.add(10); // 返回 5  
kthLargest.add(9); // 返回 8  
kthLargest.add(4); // 返回 8

**示例 2：**

**输入：**  
\["KthLargest", "add", "add", "add", "add"\]  
\[\[4, \[7, 7, 7, 7, 8, 3\]\], \[2\], \[10\], \[9\], \[9\]\]

**输出：**\[null, 7, 7, 7, 8\]

**解释：**

KthLargest kthLargest = new KthLargest(4, \[7, 7, 7, 7, 8, 3\]);  
kthLargest.add(2); // 返回 7  
kthLargest.add(10); // 返回 7  
kthLargest.add(9); // 返回 7  
kthLargest.add(9); // 返回 8

**提示：**

-   `0 <= nums.length <= 104`
-   `1 <= k <= nums.length + 1`
-   `-104 <= nums[i] <= 104`
-   `-104 <= val <= 104`
-   最多调用 `add` 方法 `104` 次

---

### 61. Last Stone Weight · 简单

**链接（CN）：** https://leetcode.cn/problems/last-stone-weight/description/  
**链接（EN）：** https://leetcode.com/problems/last-stone-weight/

有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块 **最重的** 石头，然后将它们一起粉碎。假设石头的重量分别为 `x` 和 `y`，且 `x <= y`。那么粉碎的可能结果如下：

-   如果 `x == y`，那么两块石头都会被完全粉碎；
-   如果 `x != y`，那么重量为 `x` 的石头将会完全粉碎，而重量为 `y` 的石头新重量为 `y-x`。

最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 `0`。

**示例：**

```
输入：[2,7,4,1,8,1]
输出：1
解释：
先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
```

**提示：**

-   `1 <= stones.length <= 30`
-   `1 <= stones[i] <= 1000`

---

### 62. K Closest Points to Origin · 中等

**链接（CN）：** https://leetcode.cn/problems/k-closest-points-to-origin/description/  
**链接（EN）：** https://leetcode.com/problems/k-closest-points-to-origin/

给定一个数组 `points` ，其中 `points[i] = [xi, yi]` 表示 **X-Y** 平面上的一个点，并且是一个整数 `k` ，返回离原点 `(0,0)` 最近的 `k` 个点。

这里，平面上两点之间的距离是 **欧几里德距离**（ `√(x1 - x2)2 + (y1 - y2)2` ）。

你可以按 **任何顺序** 返回答案。除了点坐标的顺序之外，答案 **确保** 是 **唯一** 的。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg)

```
输入：points = [[1,3],[-2,2]], k = 1
输出：[[-2,2]]
解释： 
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
```

**示例 2：**

```
输入：points = [[3,3],[5,-1],[-2,4]], k = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）
```

**提示：**

-   `1 <= k <= points.length <= 104`
-   `-104 < xi, yi < 104`

---

### 63. Kth Largest Element In An Array · 中等

**链接（CN）：** https://leetcode.cn/problems/kth-largest-element-in-an-array/description/  
**链接（EN）：** https://leetcode.com/problems/kth-largest-element-in-an-array/

给定整数数组 `nums` 和整数 `k`，请返回数组中第 `**k**` 个最大的元素。

请注意，你需要找的是数组排序后的第 `k` 个最大的元素，而不是第 `k` 个不同的元素。

你必须设计并实现时间复杂度为 `O(n)` 的算法解决此问题。

**示例 1:**

```
输入: [3,2,1,5,6,4], k = 2
输出: 5
```

**示例 2:**

```
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
```

**提示：**

-   `1 <= k <= nums.length <= 105`
-   `-104 <= nums[i] <= 104`

---

### 64. Task Scheduler · 中等

**链接（CN）：** https://leetcode.cn/problems/task-scheduler/description/  
**链接（EN）：** https://leetcode.com/problems/task-scheduler/

给你一个用字符数组 `tasks` 表示的 CPU 需要执行的任务列表，用字母 A 到 Z 表示，以及一个冷却时间 `n`。每个周期或时间间隔允许完成一项任务。任务可以按任何顺序完成，但有一个限制：两个 **相同种类** 的任务之间必须有长度为 `n` 的冷却时间。

返回完成所有任务所需要的 **最短时间间隔** 。

**示例 1：**

**输入：**tasks = \["A","A","A","B","B","B"\], n = 2

**输出：**8

**解释：**

在完成任务 A 之后，你必须等待两个间隔。对任务 B 来说也是一样。在第 3 个间隔，A 和 B 都不能完成，所以你需要待命。在第 4 个间隔，由于已经经过了 2 个间隔，你可以再次执行 A 任务。

**示例 2：**

**输入：**tasks = \["A","C","A","B","D","B"\], n = 1

**输出：**6

**解释：**一种可能的序列是：A -> B -> C -> D -> A -> B。

由于冷却间隔为 1，你可以在完成另一个任务后重复执行这个任务。

**示例 3：**

**输入：**tasks = \["A","A","A","B","B","B"\], n = 3

**输出：**10

**解释：**一种可能的序列为：A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B。

只有两种任务类型，A 和 B，需要被 3 个间隔分割。这导致重复执行这些任务的间隔当中有两次待命状态。

**提示：**

-   `1 <= tasks.length <= 104`
-   `tasks[i]` 是大写英文字母
-   `0 <= n <= 100`

---

### 65. Design Twitter · 中等

**链接（CN）：** https://leetcode.cn/problems/design-twitter/description/  
**链接（EN）：** https://leetcode.com/problems/design-twitter/

设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近 `10` 条推文。

实现 `Twitter` 类：

-   `Twitter()` 初始化简易版推特对象
-   `void postTweet(int userId, int tweetId)` 根据给定的 `tweetId` 和 `userId` 创建一条新推文。每次调用此函数都会使用一个不同的 `tweetId` 。
-   `List<Integer> getNewsFeed(int userId)` 检索当前用户新闻推送中最近  `10` 条推文的 ID 。新闻推送中的每一项都必须是由用户关注的人或者是用户自己发布的推文。推文必须 **按照时间顺序由最近到最远排序** 。
-   `void follow(int followerId, int followeeId)` ID 为 `followerId` 的用户开始关注 ID 为 `followeeId` 的用户。
-   `void unfollow(int followerId, int followeeId)` ID 为 `followerId` 的用户不再关注 ID 为 `followeeId` 的用户。

**示例：**

```
输入
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
输出
[null, null, [5], null, null, [6, 5], null, [5]]

解释
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // 用户 1 发送了一条新推文 (用户 id = 1, 推文 id = 5)
twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含一个 id 为 5 的推文
twitter.follow(1, 2);    // 用户 1 关注了用户 2
twitter.postTweet(2, 6); // 用户 2 发送了一个新推文 (推文 id = 6)
twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含两个推文，id 分别为 -> [6, 5] 。推文 id 6 应当在推文 id 5 之前，因为它是在 5 之后发送的
twitter.unfollow(1, 2);  // 用户 1 取消关注了用户 2
twitter.getNewsFeed(1);  // 用户 1 获取推文应当返回一个列表，其中包含一个 id 为 5 的推文。因为用户 1 已经不再关注用户 2
```

**提示：**

-   `1 <= userId, followerId, followeeId <= 500`
-   `0 <= tweetId <= 104`
-   所有推特的 ID 都互不相同
-   `postTweet`、`getNewsFeed`、`follow` 和 `unfollow` 方法最多调用 `3 * 104` 次
-   用户不能关注自己

---

### 66. Find Median From Data Stream · 困难

**链接（CN）：** https://leetcode.cn/problems/find-median-from-data-stream/description/  
**链接（EN）：** https://leetcode.com/problems/find-median-from-data-stream/

**中位数**是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

-   例如 `arr = [2,3,4]` 的中位数是 `3` 。
-   例如 `arr = [2,3]` 的中位数是 `(2 + 3) / 2 = 2.5` 。

实现 MedianFinder 类:

-   `MedianFinder()` 初始化 `MedianFinder` 对象。
    
-   `void addNum(int num)` 将数据流中的整数 `num` 添加到数据结构中。
    
-   `double findMedian()` 返回到目前为止所有元素的中位数。与实际答案相差 `10-5` 以内的答案将被接受。
    

**示例 1：**

```
输入
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
输出
[null, null, null, 1.5, null, 2.0]

解释
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

**提示:**

-   `-105 <= num <= 105`
-   在调用 `findMedian` 之前，数据结构中至少有一个元素
-   最多 `5 * 104` 次调用 `addNum` 和 `findMedian`

---


## Backtracking

### 67. Subsets · 中等

**链接（CN）：** https://leetcode.cn/problems/subsets/description/  
**链接（EN）：** https://leetcode.com/problems/subsets/

给你一个整数数组 `nums` ，数组中的元素 **互不相同** 。返回该数组所有可能的子集（幂集）。

解集 **不能** 包含重复的子集。你可以按 **任意顺序** 返回解集。

**示例 1：**

```
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**示例 2：**

```
输入：nums = [0]
输出：[[],[0]]
```

**提示：**

-   `1 <= nums.length <= 10`
-   `-10 <= nums[i] <= 10`
-   `nums` 中的所有元素 **互不相同**

---

### 68. Combination Sum · 中等

**链接（CN）：** https://leetcode.cn/problems/combination-sum/description/  
**链接（EN）：** https://leetcode.com/problems/combination-sum/

给你一个 **无重复元素** 的整数数组 `candidates` 和一个目标整数 `target` ，找出 `candidates` 中可以使数字和为目标数 `target` 的 所有 **不同组合** ，并以列表形式返回。你可以按 **任意顺序** 返回这些组合。

`candidates` 中的 **同一个** 数字可以 **无限制重复被选取** 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 `target` 的不同组合数少于 `150` 个。

**示例 1：**

```
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
```

**示例 2：**

```
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
```

**示例 3：**

```
输入: candidates = [2], target = 1
输出: []
```

**提示：**

-   `1 <= candidates.length <= 30`
-   `2 <= candidates[i] <= 40`
-   `candidates` 的所有元素 **互不相同**
-   `1 <= target <= 40`

---

### 69. Combination Sum II · 中等

**链接（CN）：** https://leetcode.cn/problems/combination-sum-ii/description/  
**链接（EN）：** https://leetcode.com/problems/combination-sum-ii/

给定一个候选人编号的集合 `candidates` 和一个目标数 `target` ，找出 `candidates` 中所有可以使数字和为 `target` 的组合。

`candidates` 中的每个数字在每个组合中只能使用 **一次** 。

**注意：**解集不能包含重复的组合。 

**示例 1:**

```
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

**示例 2:**

```
输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
```

**提示:**

-   `1 <= candidates.length <= 100`
-   `1 <= candidates[i] <= 50`
-   `1 <= target <= 30`

---

### 70. Permutations · 中等

**链接（CN）：** https://leetcode.cn/problems/permutations/description/  
**链接（EN）：** https://leetcode.com/problems/permutations/  
**面经出现：** 字节跳动 - 算法工程师一面（开场手撕）

给定一个不含重复数字的数组 `nums` ，返回其 _所有可能的全排列_ 。你可以 **按任意顺序** 返回答案。

**示例 1：**

```
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**示例 2：**

```
输入：nums = [0,1]
输出：[[0,1],[1,0]]
```

**示例 3：**

```
输入：nums = [1]
输出：[[1]]
```

**提示：**

-   `1 <= nums.length <= 6`
-   `-10 <= nums[i] <= 10`
-   `nums` 中的所有整数 **互不相同**

---

### 71. Subsets II · 中等

**链接（CN）：** https://leetcode.cn/problems/subsets-ii/description/  
**链接（EN）：** https://leetcode.com/problems/subsets-ii/

给你一个整数数组 `nums` ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。

解集 **不能** 包含重复的子集。返回的解集中，子集可以按 **任意顺序** 排列。

**示例 1：**

```
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
```

**示例 2：**

```
输入：nums = [0]
输出：[[],[0]]
```

**提示：**

-   `1 <= nums.length <= 10`
-   `-10 <= nums[i] <= 10`

---

### 72. Generate Parentheses · 中等

**链接（CN）：** https://leetcode.cn/problems/generate-parentheses/description/  
**链接（EN）：** https://leetcode.com/problems/generate-parentheses/

数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。

**示例 1：**

```
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
```

**示例 2：**

```
输入：n = 1
输出：["()"]
```

**提示：**

-   `1 <= n <= 8`

---

### 73. Word Search · 中等

**链接（CN）：** https://leetcode.cn/problems/word-search/description/  
**链接（EN）：** https://leetcode.com/problems/word-search/

给定一个 `m x n` 二维字符网格 `board` 和一个字符串单词 `word` 。如果 `word` 存在于网格中，返回 `true` ；否则，返回 `false` 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)
```
输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCCED"
输出：true
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)
```
输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "SEE"
输出：true
```

**示例 3：**

![](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)
```
输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCB"
输出：false
```

**提示：**

-   `m == board.length`
-   `n = board[i].length`
-   `1 <= m, n <= 6`
-   `1 <= word.length <= 15`
-   `board` 和 `word` 仅由大小写英文字母组成

**进阶：**你可以使用搜索剪枝的技术来优化解决方案，使其在 `board` 更大的情况下可以更快解决问题？

---

### 74. Palindrome Partitioning · 中等

**链接（CN）：** https://leetcode.cn/problems/palindrome-partitioning/description/  
**链接（EN）：** https://leetcode.com/problems/palindrome-partitioning/

给你一个字符串 `s`，请你将 `s` 分割成一些 子串，使每个子串都是 **回文串** 。返回 `s` 所有可能的分割方案。

**示例 1：**

```
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
```

**示例 2：**

```
输入：s = "a"
输出：[["a"]]
```

**提示：**

-   `1 <= s.length <= 16`
-   `s` 仅由小写英文字母组成

---

### 75. Letter Combinations of a Phone Number · 中等

**链接（CN）：** https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/  
**链接（EN）：** https://leetcode.com/problems/letter-combinations-of-a-phone-number/

给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。答案可以按 **任意顺序** 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![](https://pic.leetcode.cn/1752723054-mfIHZs-image.png)

**示例 1：**

```
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**示例 2：**

```
输入：digits = "2"
输出：["a","b","c"]
```

**提示：**

-   `1 <= digits.length <= 4`
-   `digits[i]` 是范围 `['2', '9']` 的一个数字。

---

### 76. N Queens · 困难

**链接（CN）：** https://leetcode.cn/problems/n-queens/description/  
**链接（EN）：** https://leetcode.com/problems/n-queens/


The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return _all distinct solutions to the **n-queens puzzle**_. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)
```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

**Example 2:**

```
Input: n = 1
Output: [["Q"]]
```

**Constraints:**

-   `1 <= n <= 9`

---


## Tries

### 77. Implement Trie Prefix Tree · 中等

**链接（CN）：** https://leetcode.cn/problems/implement-trie-prefix-tree/description/  
**链接（EN）：** https://leetcode.com/problems/implement-trie-prefix-tree/

**[Trie](https://baike.baidu.com/item/字典树/9825209?fr=aladdin)**（发音类似 "try"）或者说 **前缀树** 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

请你实现 Trie 类：

-   `Trie()` 初始化前缀树对象。
-   `void insert(String word)` 向前缀树中插入字符串 `word` 。
-   `boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true`（即，在检索之前已经插入）；否则，返回 `false` 。
-   `boolean startsWith(String prefix)` 如果之前已经插入的字符串 `word` 的前缀之一为 `prefix` ，返回 `true` ；否则，返回 `false` 。

**示例：**

```
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
```

**提示：**

-   `1 <= word.length, prefix.length <= 2000`
-   `word` 和 `prefix` 仅由小写英文字母组成
-   `insert`、`search` 和 `startsWith` 调用次数 **总计** 不超过 `3 * 104` 次

---

### 78. Design Add And Search Words Data Structure · 中等

**链接（CN）：** https://leetcode.cn/problems/design-add-and-search-words-data-structure/description/  
**链接（EN）：** https://leetcode.com/problems/design-add-and-search-words-data-structure/

请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 `WordDictionary` ：

-   `WordDictionary()` 初始化词典对象
-   `void addWord(word)` 将 `word` 添加到数据结构中，之后可以对它进行匹配
-   `bool search(word)` 如果数据结构中存在字符串与 `word` 匹配，则返回 `true` ；否则，返回  `false` 。`word` 中可能包含一些 `'.'` ，每个 `.` 都可以表示任何一个字母。

**示例：**

```
输入：
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
输出：
[null,null,null,null,false,true,true,true]

解释：
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // 返回 False
wordDictionary.search("bad"); // 返回 True
wordDictionary.search(".ad"); // 返回 True
wordDictionary.search("b.."); // 返回 True
```

**提示：**

-   `1 <= word.length <= 25`
-   `addWord` 中的 `word` 由小写英文字母组成
-   `search` 中的 `word` 由 '.' 或小写英文字母组成
-   最多调用 `104` 次 `addWord` 和 `search`

---

### 79. Word Search II · 困难

**链接（CN）：** https://leetcode.cn/problems/word-search-ii/description/  
**链接（EN）：** https://leetcode.com/problems/word-search-ii/

给定一个 `m x n` 二维字符网格 `board` 和一个单词（字符串）列表 `words`， _返回所有二维网格上的单词_ 。

单词必须按照字母顺序，通过 **相邻的单元格** 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/07/search1.jpg)
```
输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
输出：["eat","oath"]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/07/search2.jpg)
```
输入：board = [["a","b"],["c","d"]], words = ["abcb"]
输出：[]
```

**提示：**

-   `m == board.length`
-   `n == board[i].length`
-   `1 <= m, n <= 12`
-   `board[i][j]` 是一个小写英文字母
-   `1 <= words.length <= 3 * 104`
-   `1 <= words[i].length <= 10`
-   `words[i]` 由小写英文字母组成
-   `words` 中的所有字符串互不相同

---


## Graphs

### 80. Number of Islands · 中等

**链接（CN）：** https://leetcode.cn/problems/number-of-islands/description/  
**链接（EN）：** https://leetcode.com/problems/number-of-islands/

给你一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

**示例 1：**

```
输入：grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
输出：1
```

**示例 2：**

```
输入：grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
输出：3
```

**提示：**

-   `m == grid.length`
-   `n == grid[i].length`
-   `1 <= m, n <= 300`
-   `grid[i][j]` 的值为 `'0'` 或 `'1'`

---

### 81. Max Area of Island · 中等

**链接（CN）：** https://leetcode.cn/problems/max-area-of-island/description/  
**链接（EN）：** https://leetcode.com/problems/max-area-of-island/


You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return _the maximum **area** of an island in_ `grid`. If there is no island, return `0`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)
```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

**Example 2:**

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

**Constraints:**

-   `m == grid.length`
-   `n == grid[i].length`
-   `1 <= m, n <= 50`
-   `grid[i][j]` is either `0` or `1`.

---

### 82. Clone Graph · 中等

**链接（CN）：** https://leetcode.cn/problems/clone-graph/description/  
**链接（EN）：** https://leetcode.com/problems/clone-graph/

给你无向 **[连通](https://baike.baidu.com/item/连通图/6460995?fr=aladdin)** 图中一个节点的引用，请你返回该图的 [**深拷贝**](https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin)（克隆）。

图中的每个节点都包含它的值 `val`（`int`） 和其邻居的列表（`list[Node]`）。

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

**测试用例格式：**

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（`val = 1`），第二个节点值为 2（`val = 2`），以此类推。该图在测试用例中使用邻接列表表示。

**邻接列表** 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 **给定节点的拷贝** 作为对克隆图的引用返回。

**示例 1：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/01/133_clone_graph_question.png)

```
输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
输出：[[2,4],[1,3],[2,4],[1,3]]
解释：
图中有 4 个节点。
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
```

**示例 2：**

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/02/01/graph.png)

```
输入：adjList = [[]]
输出：[[]]
解释：输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。
```

**示例 3：**

```
输入：adjList = []
输出：[]
解释：这个图是空的，它不含任何节点。
```

**提示：**

-   这张图中的节点数在 `[0, 100]` 之间。
-   `1 <= Node.val <= 100`
-   每个节点值 `Node.val` 都是唯一的，
-   图中没有重复的边，也没有自环。
-   图是连通图，你可以从给定节点访问到所有节点。

---

### 83. Walls And Gates · 中等

**链接（CN）：** https://leetcode.cn/problems/walls-and-gates/description/  
**链接（EN）：** https://leetcode.com/problems/walls-and-gates/


(无题干)

---

### 84. Rotting Oranges · 中等

**链接（CN）：** https://leetcode.cn/problems/rotting-oranges/description/  
**链接（EN）：** https://leetcode.com/problems/rotting-oranges/

在给定的 `m x n` 网格 `grid` 中，每个单元格可以有以下三个值之一：

-   值 `0` 代表空单元格；
-   值 `1` 代表新鲜橘子；
-   值 `2` 代表腐烂的橘子。

每分钟，腐烂的橘子 **周围 4 个方向上相邻** 的新鲜橘子都会腐烂。

返回 _直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 `-1`_ 。

**示例 1：**

**![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/02/16/oranges.png)**

```
输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
```

**示例 2：**

```
输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
```

**示例 3：**

```
输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
```

**提示：**

-   `m == grid.length`
-   `n == grid[i].length`
-   `1 <= m, n <= 10`
-   `grid[i][j]` 仅为 `0`、`1` 或 `2`

---

### 85. Pacific Atlantic Water Flow · 中等

**链接（CN）：** https://leetcode.cn/problems/pacific-atlantic-water-flow/description/  
**链接（EN）：** https://leetcode.com/problems/pacific-atlantic-water-flow/


There is an `m x n` rectangular island that borders both the **Pacific Ocean** and **Atlantic Ocean**. The **Pacific Ocean** touches the island's left and top edges, and the **Atlantic Ocean** touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the **height above sea level** of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to** the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return _a **2D list** of grid coordinates_ `result` _where_ `result[i] = [ri, ci]` _denotes that rain water can flow from cell_ `(ri, ci)` _to **both** the Pacific and Atlantic oceans_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg)
```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
```

**Example 2:**

```
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
```

**Constraints:**

-   `m == heights.length`
-   `n == heights[r].length`
-   `1 <= m, n <= 200`
-   `0 <= heights[r][c] <= 105`

---

### 86. Surrounded Regions · 中等

**链接（CN）：** https://leetcode.cn/problems/surrounded-regions/description/  
**链接（EN）：** https://leetcode.com/problems/surrounded-regions/

给你一个 `m x n` 的矩阵 `board` ，由若干字符 `'X'` 和 `'O'` 组成，**捕获** 所有 **被围绕的区域**：

-   **连接：**一个单元格与水平或垂直方向上相邻的单元格连接。
-   **区域：连接所有** `'O'` 的单元格来形成一个区域。
-   **围绕：**如果一个区域中的所有 `'O'` 单元格都不在棋盘的边缘，则该区域被包围。这样的区域 **完全** 被 `'X'` 单元格包围。

通过 **原地** 将输入矩阵中的所有 `'O'` 替换为 `'X'` 来 **捕获被围绕的区域**。你不需要返回任何值。

**示例 1：**

**输入：**board = \[\['X','X','X','X'\],\['X','O','O','X'\],\['X','X','O','X'\],\['X','O','X','X'\]\]

**输出：**\[\['X','X','X','X'\],\['X','X','X','X'\],\['X','X','X','X'\],\['X','O','X','X'\]\]

**解释：**

![](https://pic.leetcode.cn/1718167191-XNjUTG-image.png)

在上图中，底部的区域没有被捕获，因为它在 board 的边缘并且不能被围绕。

**示例 2：**

**输入：**board = \[\['X'\]\]

**输出：**\[\['X'\]\]

**提示：**

-   `m == board.length`
-   `n == board[i].length`
-   `1 <= m, n <= 200`
-   `board[i][j]` 为 `'X'` 或 `'O'`

---

### 87. Course Schedule · 中等

**链接（CN）：** https://leetcode.cn/problems/course-schedule/description/  
**链接（EN）：** https://leetcode.com/problems/course-schedule/

你这个学期必须选修 `numCourses` 门课程，记为 `0` 到 `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 `prerequisites` 给出，其中 `prerequisites[i] = [ai, bi]` ，表示如果要学习课程 `ai` 则 **必须** 先学习课程  `bi` 。

-   例如，先修课程对 `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。

请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。

**示例 1：**

```
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
```

**示例 2：**

```
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
```

**提示：**

-   `1 <= numCourses <= 2000`
-   `0 <= prerequisites.length <= 5000`
-   `prerequisites[i].length == 2`
-   `0 <= ai, bi < numCourses`
-   `prerequisites[i]` 中的所有课程对 **互不相同**

---

### 88. Course Schedule II · 中等

**链接（CN）：** https://leetcode.cn/problems/course-schedule-ii/description/  
**链接（EN）：** https://leetcode.com/problems/course-schedule-ii/

现在你总共有 `numCourses` 门课需要选，记为 `0` 到 `numCourses - 1`。给你一个数组 `prerequisites` ，其中 `prerequisites[i] = [ai, bi]` ，表示在选修课程 `ai` 前 **必须** 先选修 `bi` 。

-   例如，想要学习课程 `0` ，你需要先完成课程 `1` ，我们用一个匹配来表示：`[0,1]` 。

返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 **任意一种** 就可以了。如果不可能完成所有课程，返回 **一个空数组** 。

**示例 1：**

```
输入：numCourses = 2, prerequisites = [[1,0]]
输出：[0,1]
解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
```

**示例 2：**

```
输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
输出：[0,2,1,3]
解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
```

**示例 3：**

```
输入：numCourses = 1, prerequisites = []
输出：[0]
```

**提示：**

-   `1 <= numCourses <= 2000`
-   `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
-   `prerequisites[i].length == 2`
-   `0 <= ai, bi < numCourses`
-   `ai != bi`
-   所有`[ai, bi]` **互不相同**

---

### 89. Graph Valid Tree · 中等

**链接（CN）：** https://leetcode.cn/problems/graph-valid-tree/description/  
**链接（EN）：** https://leetcode.com/problems/graph-valid-tree/


(无题干)

---

### 90. Number of Connected Components In An Undirected Graph · 中等

**链接（CN）：** https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/description/  
**链接（EN）：** https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/


(无题干)

---

### 91. Redundant Connection · 中等

**链接（CN）：** https://leetcode.cn/problems/redundant-connection/description/  
**链接（EN）：** https://leetcode.com/problems/redundant-connection/

树可以看成是一个连通且 **无环** 的 **无向** 图。

给定一个图，该图从一棵 `n` 个节点 (节点值 `1～n`) 的树中添加一条边后获得。添加的边的两个不同顶点编号在 `1` 到 `n` 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 `n` 的二维数组 `edges` ，`edges[i] = [ai, bi]` 表示图中在 `ai` 和 `bi` 之间存在一条边。

请找出一条可以删去的边，删除后可使得剩余部分是一个有着 `n` 个节点的树。如果有多个答案，则返回数组 `edges` 中最后出现的那个。

**示例 1：**

![](https://pic.leetcode.cn/1626676174-hOEVUL-image.png)

```
输入: edges = [[1,2], [1,3], [2,3]]
输出: [2,3]
```

**示例 2：**

![](https://pic.leetcode.cn/1626676179-kGxcmu-image.png)

```
输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]
```

**提示:**

-   `n == edges.length`
-   `3 <= n <= 1000`
-   `edges[i].length == 2`
-   `1 <= ai < bi <= edges.length`
-   `ai != bi`
-   `edges` 中无重复元素
-   给定的图是连通的

---

### 92. Word Ladder · 困难

**链接（CN）：** https://leetcode.cn/problems/word-ladder/description/  
**链接（EN）：** https://leetcode.com/problems/word-ladder/

字典 `wordList` 中从单词 `beginWord` 到 `endWord` 的 **转换序列** 是一个按下述规格形成的序列 `beginWord -> s1 -> s2 -> ... -> sk`：

-   每一对相邻的单词只差一个字母。
-    对于 `1 <= i <= k` 时，每个 `si` 都在 `wordList` 中。注意， `beginWord` 不需要在 `wordList` 中。
-   `sk == endWord`

给你两个单词 `beginWord` 和 `endWord` 和一个字典 `wordList` ，返回 _从 `beginWord` 到 `endWord` 的 **最短转换序列** 中的 **单词数目**_ 。如果不存在这样的转换序列，返回 `0` 。

 

**示例 1：**

```
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
```

**示例 2：**

```
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。
```

**提示：**

-   `1 <= beginWord.length <= 10`
-   `endWord.length == beginWord.length`
-   `1 <= wordList.length <= 5000`
-   `wordList[i].length == beginWord.length`
-   `beginWord`、`endWord` 和 `wordList[i]` 由小写英文字母组成
-   `beginWord != endWord`
-   `wordList` 中的所有字符串 **互不相同**

---


## Advanced Graphs

### 93. Network Delay Time · 中等

**链接（CN）：** https://leetcode.cn/problems/network-delay-time/description/  
**链接（EN）：** https://leetcode.com/problems/network-delay-time/

有 `n` 个网络节点，标记为 `1` 到 `n`。

给你一个列表 `times`，表示信号经过 **有向** 边的传递时间。 `times[i] = (ui, vi, wi)`，其中 `ui` 是源节点，`vi` 是目标节点， `wi` 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 `K` 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 `-1` 。

**示例 1：**

![](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

```
输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2
```

**示例 2：**

```
输入：times = [[1,2,1]], n = 2, k = 1
输出：1
```

**示例 3：**

```
输入：times = [[1,2,1]], n = 2, k = 2
输出：-1
```

**提示：**

-   `1 <= k <= n <= 100`
-   `1 <= times.length <= 6000`
-   `times[i].length == 3`
-   `1 <= ui, vi <= n`
-   `ui != vi`
-   `0 <= wi <= 100`
-   所有 `(ui, vi)` 对都 **互不相同**（即，不含重复边）

---

### 94. Reconstruct Itinerary · 困难

**链接（CN）：** https://leetcode.cn/problems/reconstruct-itinerary/description/  
**链接（EN）：** https://leetcode.com/problems/reconstruct-itinerary/


You are given a list of airline `tickets` where `tickets[i] = [fromi, toi]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from `"JFK"`, thus, the itinerary must begin with `"JFK"`. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

-   For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg)
```
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg)
```
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
```

**Constraints:**

-   `1 <= tickets.length <= 300`
-   `tickets[i].length == 2`
-   `fromi.length == 3`
-   `toi.length == 3`
-   `fromi` and `toi` consist of uppercase English letters.
-   `fromi != toi`

---

### 95. Min Cost to Connect All Points · 中等

**链接（CN）：** https://leetcode.cn/problems/min-cost-to-connect-all-points/description/  
**链接（EN）：** https://leetcode.com/problems/min-cost-to-connect-all-points/


You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`.

The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the **manhattan distance** between them: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return _the minimum cost to make all points connected._ All points are connected if there is **exactly one** simple path between any two points.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/26/d.png)
```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

**Example 2:**

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

**Constraints:**

-   `1 <= points.length <= 1000`
-   `-106 <= xi, yi <= 106`
-   All pairs `(xi, yi)` are distinct.

---

### 96. Swim In Rising Water · 困难

**链接（CN）：** https://leetcode.cn/problems/swim-in-rising-water/description/  
**链接（EN）：** https://leetcode.com/problems/swim-in-rising-water/


You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point `(i, j)`.

It starts raining, and water gradually rises over time. At time `t`, the water level is `t`, meaning **any** cell with elevation less than equal to `t` is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most `t`. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return _the minimum time until you can reach the bottom right square_ `(n - 1, n - 1)` _if you start at the top left square_ `(0, 0)`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/06/29/swim1-grid.jpg)
```
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/06/29/swim2-grid-1.jpg)
```
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
```

**Constraints:**

-   `n == grid.length`
-   `n == grid[i].length`
-   `1 <= n <= 50`
-   `0 <= grid[i][j] < n2`
-   Each value `grid[i][j]` is **unique**.

---

### 97. Alien Dictionary · 困难

**链接（CN）：** https://leetcode.cn/problems/alien-dictionary/description/  
**链接（EN）：** https://leetcode.com/problems/alien-dictionary/


(无题干)

---

### 98. Cheapest Flights Within K Stops · 中等

**链接（CN）：** https://leetcode.cn/problems/cheapest-flights-within-k-stops/description/  
**链接（EN）：** https://leetcode.com/problems/cheapest-flights-within-k-stops/

有 `n` 个城市通过一些航班连接。给你一个数组 `flights` ，其中 `flights[i] = [fromi, toi, pricei]` ，表示该航班都从城市 `fromi` 开始，以价格 `pricei` 抵达 `toi`。

现在给定所有的城市和航班，以及出发城市 `src` 和目的地 `dst`，你的任务是找到出一条最多经过 `k` 站中转的路线，使得从 `src` 到 `dst` 的 **价格最便宜** ，并返回该价格。 如果不存在这样的路线，则输出 `-1`。

**示例 1：**

![](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-3drawio.png)
```
输入: 
n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
输出: 700 
解释: 城市航班图如上
从城市 0 到城市 3 经过最多 1 站的最佳路径用红色标记，费用为 100 + 600 = 700。
请注意，通过城市 [0, 1, 2, 3] 的路径更便宜，但无效，因为它经过了 2 站。
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-1drawio.png)
```
输入: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
输出: 200
解释: 
城市航班图如上
从城市 0 到城市 2 经过最多 1 站的最佳路径标记为红色，费用为 100 + 100 = 200。
```

**示例 3：**

![](https://assets.leetcode.com/uploads/2022/03/18/cheapest-flights-within-k-stops-2drawio.png)
```
输入：n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
输出：500
解释：
城市航班图如上
从城市 0 到城市 2 不经过站点的最佳路径标记为红色，费用为 500。
```

**提示：**

-   `2 <= n <= 100`
-   `0 <= flights.length <= (n * (n - 1) / 2)`
-   `flights[i].length == 3`
-   `0 <= fromi, toi < n`
-   `fromi != toi`
-   `1 <= pricei <= 104`
-   航班没有重复，且不存在自环
-   `0 <= src, dst, k < n`
-   `src != dst`

---


## 1-D Dynamic Programming

### 99. Climbing Stairs · 简单

**链接（CN）：** https://leetcode.cn/problems/climbing-stairs/description/  
**链接（EN）：** https://leetcode.com/problems/climbing-stairs/

假设你正在爬楼梯。需要 `n` 阶你才能到达楼顶。

每次你可以爬 `1` 或 `2` 个台阶。你有多少种不同的方法可以爬到楼顶呢？

**示例 1：**

```
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
```

**示例 2：**

```
输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
```

**提示：**

-   `1 <= n <= 45`

---

### 100. Min Cost Climbing Stairs · 简单

**链接（CN）：** https://leetcode.cn/problems/min-cost-climbing-stairs/description/  
**链接（EN）：** https://leetcode.com/problems/min-cost-climbing-stairs/


You are given an integer array `cost` where `cost[i]` is the cost of `ith` step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `0`, or the step with index `1`.

Return _the minimum cost to reach the top of the floor_.

**Example 1:**

```
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

**Example 2:**

```
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
```

**Constraints:**

-   `2 <= cost.length <= 1000`
-   `0 <= cost[i] <= 999`

---

### 101. House Robber · 中等

**链接（CN）：** https://leetcode.cn/problems/house-robber/description/  
**链接（EN）：** https://leetcode.com/problems/house-robber/

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警**。

给定一个代表每个房屋存放金额的非负整数数组，计算你 **不触动警报装置的情况下** ，一夜之内能够偷窃到的最高金额。

**示例 1：**

```
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

**示例 2：**

```
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```

**提示：**

-   `1 <= nums.length <= 100`
-   `0 <= nums[i] <= 400`

---

### 102. House Robber II · 中等

**链接（CN）：** https://leetcode.cn/problems/house-robber-ii/description/  
**链接（EN）：** https://leetcode.com/problems/house-robber-ii/

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 **围成一圈** ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警** 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 **在不触动警报装置的情况下** ，今晚能够偷窃到的最高金额。

**示例 1：**

```
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
```

**示例 2：**

```
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

**示例 3：**

```
输入：nums = [1,2,3]
输出：3
```

**提示：**

-   `1 <= nums.length <= 100`
-   `0 <= nums[i] <= 1000`

---

### 103. Longest Palindromic Substring · 中等

**链接（CN）：** https://leetcode.cn/problems/longest-palindromic-substring/description/  
**链接（EN）：** https://leetcode.com/problems/longest-palindromic-substring/

给你一个字符串 `s`，找到 `s` 中最长的 回文 子串。

**示例 1：**

```
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
```

**示例 2：**

```
输入：s = "cbbd"
输出："bb"
```

**提示：**

-   `1 <= s.length <= 1000`
-   `s` 仅由数字和英文字母组成

---

### 104. Palindromic Substrings · 中等

**链接（CN）：** https://leetcode.cn/problems/palindromic-substrings/description/  
**链接（EN）：** https://leetcode.com/problems/palindromic-substrings/


Given a string `s`, return _the number of **palindromic substrings** in it_.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

**Example 1:**

```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

**Example 2:**

```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

**Constraints:**

-   `1 <= s.length <= 1000`
-   `s` consists of lowercase English letters.

---

### 105. Decode Ways · 中等

**链接（CN）：** https://leetcode.cn/problems/decode-ways/description/  
**链接（EN）：** https://leetcode.com/problems/decode-ways/

一条包含字母 `A-Z` 的消息通过以下映射进行了 **编码** ：

`"1" -> 'A'   "2" -> 'B'   ...   "25" -> 'Y'   "26" -> 'Z'`

然而，在 **解码** 已编码的消息时，你意识到有许多不同的方式来解码，因为有些编码被包含在其它编码当中（`"2"` 和 `"5"` 与 `"25"`）。

例如，`"11106"` 可以映射为：

-   `"AAJF"` ，将消息分组为 `(1, 1, 10, 6)`
-   `"KJF"` ，将消息分组为 `(11, 10, 6)`
-   消息不能分组为  `(1, 11, 06)` ，因为 `"06"` 不是一个合法编码（只有 "6" 是合法的）。

注意，可能存在无法解码的字符串。

给你一个只含数字的 **非空** 字符串 `s` ，请计算并返回 **解码** 方法的 **总数** 。如果没有合法的方式解码整个字符串，返回 `0`。

题目数据保证答案肯定是一个 **32 位** 的整数。

**示例 1：**

```
输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
```

**示例 2：**

```
输入：s = "226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
```

**示例 3：**

```
输入：s = "06"
输出：0
解释："06" 无法映射到 "F" ，因为存在前导零（"6" 和 "06" 并不等价）。
```

**提示：**

-   `1 <= s.length <= 100`
-   `s` 只包含数字，并且可能包含前导零。

---

### 106. Coin Change · 中等

**链接（CN）：** https://leetcode.cn/problems/coin-change/description/  
**链接（EN）：** https://leetcode.com/problems/coin-change/

给你一个整数数组 `coins` ，表示不同面额的硬币；以及一个整数 `amount` ，表示总金额。

计算并返回可以凑成总金额所需的 **最少的硬币个数** 。如果没有任何一种硬币组合能组成总金额，返回 `-1` 。

你可以认为每种硬币的数量是无限的。

**示例 1：**

```
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
```

**示例 2：**

```
输入：coins = [2], amount = 3
输出：-1
```

**示例 3：**

```
输入：coins = [1], amount = 0
输出：0
```

**提示：**

-   `1 <= coins.length <= 12`
-   `1 <= coins[i] <= 231 - 1`
-   `0 <= amount <= 104`

---

### 107. Maximum Product Subarray · 中等

**链接（CN）：** https://leetcode.cn/problems/maximum-product-subarray/description/  
**链接（EN）：** https://leetcode.com/problems/maximum-product-subarray/

给你一个整数数组 `nums` ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 **32-位** 整数。

**请注意**，一个只包含一个元素的数组的乘积是这个元素的值。

**示例 1:**

```
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
```

**示例 2:**

```
输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
```

**提示:**

-   `1 <= nums.length <= 2 * 104`
-   `-10 <= nums[i] <= 10`
-   `nums` 的任何子数组的乘积都 **保证** 是一个 **32-位** 整数

---

### 108. Word Break · 中等

**链接（CN）：** https://leetcode.cn/problems/word-break/description/  
**链接（EN）：** https://leetcode.com/problems/word-break/

给你一个字符串 `s` 和一个字符串列表 `wordDict` 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 `s` 则返回 `true`。

**注意：**不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

**示例 1：**

```
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
```

**示例 2：**

```
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
```

**示例 3：**

```
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
```

**提示：**

-   `1 <= s.length <= 300`
-   `1 <= wordDict.length <= 1000`
-   `1 <= wordDict[i].length <= 20`
-   `s` 和 `wordDict[i]` 仅由小写英文字母组成
-   `wordDict` 中的所有字符串 **互不相同**

---

### 109. Longest Increasing Subsequence · 中等

**链接（CN）：** https://leetcode.cn/problems/longest-increasing-subsequence/description/  
**链接（EN）：** https://leetcode.com/problems/longest-increasing-subsequence/  
**面经出现：** 小红书 - Agent 实习一面（手撕）

给你一个整数数组 `nums` ，找到其中最长严格递增子序列的长度。

**子序列** 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，`[3,6,2,7]` 是数组 `[0,3,1,6,2,2,7]` 的子序列。

 

**示例 1：**

```
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
```

**示例 2：**

```
输入：nums = [0,1,0,3,2,3]
输出：4
```

**示例 3：**

```
输入：nums = [7,7,7,7,7,7,7]
输出：1
```

**提示：**

-   `1 <= nums.length <= 2500`
-   `-104 <= nums[i] <= 104`

**进阶：**

-   你能将算法的时间复杂度降低到 `O(n log(n))` 吗?

---

### 110. Partition Equal Subset Sum · 中等

**链接（CN）：** https://leetcode.cn/problems/partition-equal-subset-sum/description/  
**链接（EN）：** https://leetcode.com/problems/partition-equal-subset-sum/


Given an integer array `nums`, return `true` _if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or_ `false` _otherwise_.

**Example 1:**

```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**

```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

**Constraints:**

-   `1 <= nums.length <= 200`
-   `1 <= nums[i] <= 100`

---


## 2-D Dynamic Programming

### 111. Unique Paths · 中等

**链接（CN）：** https://leetcode.cn/problems/unique-paths/description/  
**链接（EN）：** https://leetcode.com/problems/unique-paths/

一个机器人位于一个 `m x n` 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

**示例 1：**

![](https://pic.leetcode.cn/1697422740-adxmsI-image.png)
```
输入：m = 3, n = 7
输出：28
```

**示例 2：**

```
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
```

**示例 3：**

```
输入：m = 7, n = 3
输出：28
```

**示例 4：**

```
输入：m = 3, n = 3
输出：6
```

**提示：**

-   `1 <= m, n <= 100`
-   题目数据保证答案小于等于 `2 * 109`

---

### 112. Longest Common Subsequence · 中等

**链接（CN）：** https://leetcode.cn/problems/longest-common-subsequence/description/  
**链接（EN）：** https://leetcode.com/problems/longest-common-subsequence/

给定两个字符串 `text1` 和 `text2`，返回这两个字符串的最长 **公共子序列** 的长度。如果不存在 **公共子序列** ，返回 `0` 。

一个字符串的 **子序列** 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

-   例如，`"ace"` 是 `"abcde"` 的子序列，但 `"aec"` 不是 `"abcde"` 的子序列。

两个字符串的 **公共子序列** 是这两个字符串所共同拥有的子序列。

**示例 1：**

```
输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为 3 。
```

**示例 2：**

```
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
```

**示例 3：**

```
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。
```

**提示：**

-   `1 <= text1.length, text2.length <= 1000`
-   `text1` 和 `text2` 仅由小写英文字符组成。

---

### 113. Best Time to Buy And Sell Stock With Cooldown · 中等

**链接（CN）：** https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/  
**链接（EN）：** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

-   After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

**Example 1:**

```
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

**Example 2:**

```
Input: prices = [1]
Output: 0
```

**Constraints:**

-   `1 <= prices.length <= 5000`
-   `0 <= prices[i] <= 1000`

---

### 114. Coin Change II · 中等

**链接（CN）：** https://leetcode.cn/problems/coin-change-ii/description/  
**链接（EN）：** https://leetcode.com/problems/coin-change-ii/


You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return _the number of combinations that make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

The answer is **guaranteed** to fit into a signed **32-bit** integer.

**Example 1:**

```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

**Example 2:**

```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

**Example 3:**

```
Input: amount = 10, coins = [10]
Output: 1
```

**Constraints:**

-   `1 <= coins.length <= 300`
-   `1 <= coins[i] <= 5000`
-   All the values of `coins` are **unique**.
-   `0 <= amount <= 5000`

---

### 115. Target Sum · 中等

**链接（CN）：** https://leetcode.cn/problems/target-sum/description/  
**链接（EN）：** https://leetcode.com/problems/target-sum/


You are given an integer array `nums` and an integer `target`.

You want to build an **expression** out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.

-   For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `"+2-1"`.

Return the number of different **expressions** that you can build, which evaluates to `target`.

**Example 1:**

```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

**Example 2:**

```
Input: nums = [1], target = 1
Output: 1
```

**Constraints:**

-   `1 <= nums.length <= 20`
-   `0 <= nums[i] <= 1000`
-   `0 <= sum(nums[i]) <= 1000`
-   `-1000 <= target <= 1000`

---

### 116. Interleaving String · 中等

**链接（CN）：** https://leetcode.cn/problems/interleaving-string/description/  
**链接（EN）：** https://leetcode.com/problems/interleaving-string/

给定三个字符串 `s1`、`s2`、`s3`，请你帮忙验证 `s3` 是否是由 `s1` 和 `s2` **交错** 组成的。

两个字符串 `s` 和 `t` **交错** 的定义与过程如下，其中每个字符串都会被分割成若干 **非空** 子字符串：

-   `s = s1 + s2 + ... + sn`
-   `t = t1 + t2 + ... + tm`
-   `|n - m| <= 1`
-   **交错** 是 `s1 + t1 + s2 + t2 + s3 + t3 + ...` 或者 `t1 + s1 + t2 + s2 + t3 + s3 + ...`

**注意：**`a + b` 意味着字符串 `a` 和 `b` 连接。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg)
```
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
```

**示例 2：**

```
输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
```

**示例 3：**

```
输入：s1 = "", s2 = "", s3 = ""
输出：true
```

**提示：**

-   `0 <= s1.length, s2.length <= 100`
-   `0 <= s3.length <= 200`
-   `s1`、`s2`、和 `s3` 都由小写英文字母组成

**进阶：**您能否仅使用 `O(s2.length)` 额外的内存空间来解决它?

---

### 117. Longest Increasing Path In a Matrix · 困难

**链接（CN）：** https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/description/  
**链接（EN）：** https://leetcode.com/problems/longest-increasing-path-in-a-matrix/


Given an `m x n` integers `matrix`, return _the length of the longest increasing path in_ `matrix`.

From each cell, you can either move in four directions: left, right, up, or down. You **may not** move **diagonally** or move **outside the boundary** (i.e., wrap-around is not allowed).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg)
```
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg)
```
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
```

**Example 3:**

```
Input: matrix = [[1]]
Output: 1
```

**Constraints:**

-   `m == matrix.length`
-   `n == matrix[i].length`
-   `1 <= m, n <= 200`
-   `0 <= matrix[i][j] <= 231 - 1`

---

### 118. Distinct Subsequences · 困难

**链接（CN）：** https://leetcode.cn/problems/distinct-subsequences/description/  
**链接（EN）：** https://leetcode.com/problems/distinct-subsequences/


Given two strings s and t, return _the number of distinct_ **_subsequences_** _of_ s _which equals_ t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

**Example 1:**

```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
```

**Example 2:**

```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
```

**Constraints:**

-   `1 <= s.length, t.length <= 1000`
-   `s` and `t` consist of English letters.

---

### 119. Edit Distance · 中等

**链接（CN）：** https://leetcode.cn/problems/edit-distance/description/  
**链接（EN）：** https://leetcode.com/problems/edit-distance/

给你两个单词 `word1` 和 `word2`， _请返回将 `word1` 转换成 `word2` 所使用的最少操作数_  。

你可以对一个单词进行如下三种操作：

-   插入一个字符
-   删除一个字符
-   替换一个字符

**示例 1：**

```
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
```

**示例 2：**

```
输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')
```

**提示：**

-   `0 <= word1.length, word2.length <= 500`
-   `word1` 和 `word2` 由小写英文字母组成

---

### 120. Burst Balloons · 困难

**链接（CN）：** https://leetcode.cn/problems/burst-balloons/description/  
**链接（EN）：** https://leetcode.com/problems/burst-balloons/

有 `n` 个气球，编号为`0` 到 `n - 1`，每个气球上都标有一个数字，这些数字存在数组 `nums` 中。

现在要求你戳破所有的气球。戳破第 `i` 个气球，你可以获得 `nums[i - 1] * nums[i] * nums[i + 1]` 枚硬币。 这里的 `i - 1` 和 `i + 1` 代表和 `i` 相邻的两个气球的序号。如果 `i - 1`或 `i + 1` 超出了数组的边界，那么就当它是一个数字为 `1` 的气球。

求所能获得硬币的最大数量。

**示例 1：**
```
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
```

**示例 2：**

```
输入：nums = [1,5]
输出：10
```

**提示：**

-   `n == nums.length`
-   `1 <= n <= 300`
-   `0 <= nums[i] <= 100`

---

### 121. Regular Expression Matching · 困难

**链接（CN）：** https://leetcode.cn/problems/regular-expression-matching/description/  
**链接（EN）：** https://leetcode.com/problems/regular-expression-matching/


Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

-   `'.'` Matches any single character.​​​​
-   `'*'` Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).

**Example 1:**

```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2:**

```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

**Example 3:**

```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

**Constraints:**

-   `1 <= s.length <= 20`
-   `1 <= p.length <= 20`
-   `s` contains only lowercase English letters.
-   `p` contains only lowercase English letters, `'.'`, and `'*'`.
-   It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.

---


## Greedy

### 122. Maximum Subarray · 中等

**链接（CN）：** https://leetcode.cn/problems/maximum-subarray/description/  
**链接（EN）：** https://leetcode.com/problems/maximum-subarray/

给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**子数组** 是数组中的一个连续部分。

**示例 1：**

```
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
```

**示例 2：**

```
输入：nums = [1]
输出：1
```

**示例 3：**

```
输入：nums = [5,4,-1,7,8]
输出：23
```

**提示：**

-   `1 <= nums.length <= 105`
-   `-104 <= nums[i] <= 104`

**进阶：**如果你已经实现复杂度为 `O(n)` 的解法，尝试使用更为精妙的 **分治法** 求解。

---

### 123. Jump Game · 中等

**链接（CN）：** https://leetcode.cn/problems/jump-game/description/  
**链接（EN）：** https://leetcode.com/problems/jump-game/

给你一个非负整数数组 `nums` ，你最初位于数组的 **第一个下标** 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 `true` ；否则，返回 `false` 。

**示例 1：**

```
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
```

**示例 2：**

```
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
```

**提示：**

-   `1 <= nums.length <= 104`
-   `0 <= nums[i] <= 105`

---

### 124. Jump Game II · 中等

**链接（CN）：** https://leetcode.cn/problems/jump-game-ii/description/  
**链接（EN）：** https://leetcode.com/problems/jump-game-ii/

给定一个长度为 `n` 的 **0 索引**整数数组 `nums`。初始位置在下标 0。

每个元素 `nums[i]` 表示从索引 `i` 向后跳转的最大长度。换句话说，如果你在索引 `i` 处，你可以跳转到任意 `(i + j)` 处：

-   `0 <= j <= nums[i]` 且
-   `i + j < n`

返回到达 `n - 1` 的最小跳跃次数。测试用例保证可以到达 `n - 1`。

**示例 1:**

```
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
```

**示例 2:**

```
输入: nums = [2,3,0,1,4]
输出: 2
```

**提示:**

-   `1 <= nums.length <= 104`
-   `0 <= nums[i] <= 1000`
-   题目保证可以到达 `n - 1`

---

### 125. Gas Station · 中等

**链接（CN）：** https://leetcode.cn/problems/gas-station/description/  
**链接（EN）：** https://leetcode.com/problems/gas-station/

在一条环路上有 `n` 个加油站，其中第 `i` 个加油站有汽油 `gas[i]` 升。

你有一辆油箱容量无限的的汽车，从第 `i` 个加油站开往第 `i+1` 个加油站需要消耗汽油 `cost[i]` 升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 `gas` 和 `cost` ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 `-1` 。如果存在解，则 **保证** 它是 **唯一** 的。

**示例 1:**

```
输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
```

**示例 2:**

```
输入: gas = [2,3,4], cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。
```

**提示:**

-   `n == gas.length == cost.length`
-   `1 <= n <= 105`
-   `0 <= gas[i], cost[i] <= 104`
-   输入保证答案唯一。

---

### 126. Hand of Straights · 中等

**链接（CN）：** https://leetcode.cn/problems/hand-of-straights/description/  
**链接（EN）：** https://leetcode.com/problems/hand-of-straights/


Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

Given an integer array `hand` where `hand[i]` is the value written on the `ith` card and an integer `groupSize`, return `true` if she can rearrange the cards, or `false` otherwise.

**Example 1:**

```
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
```

**Example 2:**

```
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.
```

**Constraints:**

-   `1 <= hand.length <= 104`
-   `0 <= hand[i] <= 109`
-   `1 <= groupSize <= hand.length`

**Note:** This question is the same as 1296: [https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/)

---

### 127. Merge Triplets to Form Target Triplet · 中等

**链接（CN）：** https://leetcode.cn/problems/merge-triplets-to-form-target-triplet/description/  
**链接（EN）：** https://leetcode.com/problems/merge-triplets-to-form-target-triplet/


A **triplet** is an array of three integers. You are given a 2D integer array `triplets`, where `triplets[i] = [ai, bi, ci]` describes the `ith` **triplet**. You are also given an integer array `target = [x, y, z]` that describes the **triplet** you want to obtain.

To obtain `target`, you may apply the following operation on `triplets` **any number** of times (possibly **zero**):

-   Choose two indices (**0-indexed**) `i` and `j` (`i != j`) and **update** `triplets[j]` to become `[max(ai, aj), max(bi, bj), max(ci, cj)]`.
    -   For example, if `triplets[i] = [2, 5, 3]` and `triplets[j] = [1, 7, 5]`, `triplets[j]` will be updated to `[max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5]`.

Return `true` _if it is possible to obtain the_ `target` _**triplet**_ `[x, y, z]` _as an **element** of_ `triplets`_, or_ `false` _otherwise_.

**Example 1:**

```
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],[2,7,5]]
The target triplet [2,7,5] is now an element of triplets.
```

**Example 2:**

```
Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.
```

**Example 3:**

```
Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
The target triplet [5,5,5] is now an element of triplets.
```

**Constraints:**

-   `1 <= triplets.length <= 105`
-   `triplets[i].length == target.length == 3`
-   `1 <= ai, bi, ci, x, y, z <= 1000`

---

### 128. Partition Labels · 中等

**链接（CN）：** https://leetcode.cn/problems/partition-labels/description/  
**链接（EN）：** https://leetcode.com/problems/partition-labels/


You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string `"ababcc"` can be partitioned into `["abab", "cc"]`, but partitions such as `["aba", "bcc"]` or `["ab", "ab", "cc"]` are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return _a list of integers representing the size of these parts_.

**Example 1:**

```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
```

**Example 2:**

```
Input: s = "eccbbbbdec"
Output: [10]
```

**Constraints:**

-   `1 <= s.length <= 500`
-   `s` consists of lowercase English letters.

---

### 129. Valid Parenthesis String · 中等

**链接（CN）：** https://leetcode.cn/problems/valid-parenthesis-string/description/  
**链接（EN）：** https://leetcode.com/problems/valid-parenthesis-string/


Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` _if_ `s` _is **valid**_.

The following rules define a **valid** string:

-   Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
-   Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
-   Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
-   `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

**Example 1:**

```
Input: s = "()"
Output: true
```

**Example 2:**

```
Input: s = "(*)"
Output: true
```

**Example 3:**

```
Input: s = "(*))"
Output: true
```

**Constraints:**

-   `1 <= s.length <= 100`
-   `s[i]` is `'('`, `')'` or `'*'`.

---


## Intervals

### 130. Insert Interval · 中等

**链接（CN）：** https://leetcode.cn/problems/insert-interval/description/  
**链接（EN）：** https://leetcode.com/problems/insert-interval/

给你一个 **无重叠的** _，_按照区间起始端点排序的区间列表 `intervals`，其中 `intervals[i] = [starti, endi]` 表示第 `i` 个区间的开始和结束，并且 `intervals` 按照 `starti` 升序排列。同样给定一个区间 `newInterval = [start, end]` 表示另一个区间的开始和结束。

在 `intervals` 中插入区间 `newInterval`，使得 `intervals` 依然按照 `starti` 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。

返回插入之后的 `intervals`。

**注意** 你不需要原地修改 `intervals`。你可以创建一个新数组然后返回它。

**示例 1：**

```
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
```

**示例 2：**

```
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
```

**提示：**

-   `0 <= intervals.length <= 104`
-   `intervals[i].length == 2`
-   `0 <= starti <= endi <= 105`
-   `intervals` 根据 `starti` 按 **升序** 排列
-   `newInterval.length == 2`
-   `0 <= start <= end <= 105`

---

### 131. Merge Intervals · 中等

**链接（CN）：** https://leetcode.cn/problems/merge-intervals/description/  
**链接（EN）：** https://leetcode.com/problems/merge-intervals/  
**面经出现：** 陌陌 - 全栈开发笔试

以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [starti, endi]` 。请你合并所有重叠的区间，并返回 _一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间_ 。

**示例 1：**

```
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
```

**示例 2：**

```
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
```

**示例 3：**

```
输入：intervals = [[4,7],[1,4]]
输出：[[1,7]]
解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。
```

**提示：**

-   `1 <= intervals.length <= 104`
-   `intervals[i].length == 2`
-   `0 <= starti <= endi <= 104`

---

### 132. Non Overlapping Intervals · 中等

**链接（CN）：** https://leetcode.cn/problems/non-overlapping-intervals/description/  
**链接（EN）：** https://leetcode.com/problems/non-overlapping-intervals/

给定一个区间的集合 `intervals` ，其中 `intervals[i] = [starti, endi]` 。返回 _需要移除区间的最小数量，使剩余区间互不重叠_ 。

**注意** 只在一点上接触的区间是 **不重叠的**。例如 `[1, 2]` 和 `[2, 3]` 是不重叠的。

**示例 1:**

```
输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
```

**示例 2:**

```
输入: intervals = [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
```

**示例 3:**

```
输入: intervals = [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
```

**提示:**

-   `1 <= intervals.length <= 105`
-   `intervals[i].length == 2`
-   `-5 * 104 <= starti < endi <= 5 * 104`

---

### 133. Meeting Rooms · 简单

**链接（CN）：** https://leetcode.cn/problems/meeting-rooms/description/  
**链接（EN）：** https://leetcode.com/problems/meeting-rooms/


(无题干)

---

### 134. Meeting Rooms II · 中等

**链接（CN）：** https://leetcode.cn/problems/meeting-rooms-ii/description/  
**链接（EN）：** https://leetcode.com/problems/meeting-rooms-ii/


(无题干)

---

### 135. Minimum Interval to Include Each Query · 困难

**链接（CN）：** https://leetcode.cn/problems/minimum-interval-to-include-each-query/description/  
**链接（EN）：** https://leetcode.com/problems/minimum-interval-to-include-each-query/

给你一个二维整数数组 `intervals` ，其中 `intervals[i] = [lefti, righti]` 表示第 `i` 个区间开始于 `lefti` 、结束于 `righti`（包含两侧取值，**闭区间**）。区间的 **长度** 定义为区间中包含的整数数目，更正式地表达是 `righti - lefti + 1` 。

再给你一个整数数组 `queries` 。第 `j` 个查询的答案是满足 `lefti <= queries[j] <= righti` 的 **长度最小区间 `i` 的长度** 。如果不存在这样的区间，那么答案是 `-1` 。

以数组形式返回对应查询的所有答案。

**示例 1：**

```
输入：intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
输出：[3,3,1,4]
解释：查询处理如下：
- Query = 2 ：区间 [2,4] 是包含 2 的最小区间，答案为 4 - 2 + 1 = 3 。
- Query = 3 ：区间 [2,4] 是包含 3 的最小区间，答案为 4 - 2 + 1 = 3 。
- Query = 4 ：区间 [4,4] 是包含 4 的最小区间，答案为 4 - 4 + 1 = 1 。
- Query = 5 ：区间 [3,6] 是包含 5 的最小区间，答案为 6 - 3 + 1 = 4 。
```

**示例 2：**

```
输入：intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
输出：[2,-1,4,6]
解释：查询处理如下：
- Query = 2 ：区间 [2,3] 是包含 2 的最小区间，答案为 3 - 2 + 1 = 2 。
- Query = 19：不存在包含 19 的区间，答案为 -1 。
- Query = 5 ：区间 [2,5] 是包含 5 的最小区间，答案为 5 - 2 + 1 = 4 。
- Query = 22：区间 [20,25] 是包含 22 的最小区间，答案为 25 - 20 + 1 = 6 。
```

**提示：**

-   `1 <= intervals.length <= 105`
-   `1 <= queries.length <= 105`
-   `intervals[i].length == 2`
-   `1 <= lefti <= righti <= 107`
-   `1 <= queries[j] <= 107`

---


## Math & Geometry

### 136. Rotate Image · 中等

**链接（CN）：** https://leetcode.cn/problems/rotate-image/description/  
**链接（EN）：** https://leetcode.com/problems/rotate-image/

给定一个 _n_ × _n_ 的二维矩阵 `matrix` 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 **[原地](https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)** 旋转图像，这意味着你需要直接修改输入的二维矩阵。**请不要** 使用另一个矩阵来旋转图像。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)
```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)
```
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

**提示：**

-   `n == matrix.length == matrix[i].length`
-   `1 <= n <= 20`
-   `-1000 <= matrix[i][j] <= 1000`

---

### 137. Spiral Matrix · 中等

**链接（CN）：** https://leetcode.cn/problems/spiral-matrix/description/  
**链接（EN）：** https://leetcode.com/problems/spiral-matrix/

给你一个 `m` 行 `n` 列的矩阵 `matrix` ，请按照 **顺时针螺旋顺序** ，返回矩阵中的所有元素。

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg)
```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg)
```
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
```

**提示：**

-   `m == matrix.length`
-   `n == matrix[i].length`
-   `1 <= m, n <= 10`
-   `-100 <= matrix[i][j] <= 100`

---

### 138. Set Matrix Zeroes · 中等

**链接（CN）：** https://leetcode.cn/problems/set-matrix-zeroes/description/  
**链接（EN）：** https://leetcode.com/problems/set-matrix-zeroes/

给定一个 `_m_ x _n_` 的矩阵，如果一个元素为 **0** ，则将其所在行和列的所有元素都设为 **0** 。请使用 **[原地](http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95)** 算法**。**

**示例 1：**

![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)
```
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)
```
输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

**提示：**

-   `m == matrix.length`
-   `n == matrix[0].length`
-   `1 <= m, n <= 200`
-   `-231 <= matrix[i][j] <= 231 - 1`

**进阶：**

-   一个直观的解决方案是使用  `O(_m__n_)` 的额外空间，但这并不是一个好的解决方案。
-   一个简单的改进方案是使用 `O(_m_ + _n_)` 的额外空间，但这仍然不是最好的解决方案。
-   你能想出一个仅使用常量空间的解决方案吗？

---

### 139. Happy Number · 简单

**链接（CN）：** https://leetcode.cn/problems/happy-number/description/  
**链接（EN）：** https://leetcode.com/problems/happy-number/

编写一个算法来判断一个数 `n` 是不是快乐数。

**「快乐数」** 定义为：

-   对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
-   然后重复这个过程直到这个数变为 1，也可能是 **无限循环** 但始终变不到 1。
-   如果这个过程 **结果为** 1，那么这个数就是快乐数。

如果 `n` 是 _快乐数_ 就返回 `true` ；不是，则返回 `false` 。

**示例 1：**

```
输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

**示例 2：**

```
输入：n = 2
输出：false
```

**提示：**

-   `1 <= n <= 231 - 1`

---

### 140. Plus One · 简单

**链接（CN）：** https://leetcode.cn/problems/plus-one/description/  
**链接（EN）：** https://leetcode.com/problems/plus-one/

给定一个表示 **大整数** 的整数数组 `digits`，其中 `digits[i]` 是整数的第 `i` 位数字。这些数字按从左到右，从最高位到最低位排列。这个大整数不包含任何前导 `0`。

将大整数加 1，并返回结果的数字数组。

**示例 1：**

```
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
加 1 后得到 123 + 1 = 124。
因此，结果应该是 [1,2,4]。
```

**示例 2：**

```
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
加 1 后得到 4321 + 1 = 4322。
因此，结果应该是 [4,3,2,2]。
```

**示例 3：**

```
输入：digits = [9]
输出：[1,0]
解释：输入数组表示数字 9。
加 1 得到了 9 + 1 = 10。
因此，结果应该是 [1,0]。
```

**提示：**

-   `1 <= digits.length <= 100`
-   `0 <= digits[i] <= 9`
-   `digits` 不包含任何前导 `0`。

---

### 141. Pow(x, n) · 中等

**链接（CN）：** https://leetcode.cn/problems/powx-n/description/  
**链接（EN）：** https://leetcode.com/problems/powx-n/

实现 [pow(_x_, _n_)](https://www.cplusplus.com/reference/valarray/pow/) ，即计算 `x` 的整数 `n` 次幂函数（即，`xn` ）。

**示例 1：**

```
输入：x = 2.00000, n = 10
输出：1024.00000
```

**示例 2：**

```
输入：x = 2.10000, n = 3
输出：9.26100
```

**示例 3：**

```
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
```

**提示：**

-   `-100.0 < x < 100.0`
-   `-231 <= n <= 231-1`
-   `n` 是一个整数
-   要么 `x` 不为零，要么 `n > 0` 。
-   `-104 <= xn <= 104`

---

### 142. Multiply Strings · 中等

**链接（CN）：** https://leetcode.cn/problems/multiply-strings/description/  
**链接（EN）：** https://leetcode.com/problems/multiply-strings/

给定两个以字符串形式表示的非负整数 `num1` 和 `num2`，返回 `num1` 和 `num2` 的乘积，它们的乘积也表示为字符串形式。

**注意：**不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

**示例 1:**

```
输入: num1 = "2", num2 = "3"
输出: "6"
```

**示例 2:**

```
输入: num1 = "123", num2 = "456"
输出: "56088"
```

**提示：**

-   `1 <= num1.length, num2.length <= 200`
-   `num1` 和 `num2` 只能由数字组成。
-   `num1` 和 `num2` 都不包含任何前导零，除了数字0本身。

---

### 143. Detect Squares · 中等

**链接（CN）：** https://leetcode.cn/problems/detect-squares/description/  
**链接（EN）：** https://leetcode.com/problems/detect-squares/


You are given a stream of points on the X-Y plane. Design an algorithm that:

-   **Adds** new points from the stream into a data structure. **Duplicate** points are allowed and should be treated as different points.
-   Given a query point, **counts** the number of ways to choose three points from the data structure such that the three points and the query point form an **axis-aligned square** with **positive area**.

An **axis-aligned square** is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the `DetectSquares` class:

-   `DetectSquares()` Initializes the object with an empty data structure.
-   `void add(int[] point)` Adds a new point `point = [x, y]` to the data structure.
-   `int count(int[] point)` Counts the number of ways to form **axis-aligned squares** with point `point = [x, y]` as described above.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/09/01/image.png)
```
Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points
```

**Constraints:**

-   `point.length == 2`
-   `0 <= x, y <= 1000`
-   At most `3000` calls **in total** will be made to `add` and `count`.

---


## Bit Manipulation

### 144. Single Number · 简单

**链接（CN）：** https://leetcode.cn/problems/single-number/description/  
**链接（EN）：** https://leetcode.com/problems/single-number/

给你一个 **非空** 整数数组 `nums` ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

**示例 1 ：**

**输入：**nums = \[2,2,1\]

**输出：**1

**示例 2 ：**

**输入：**nums = \[4,1,2,1,2\]

**输出：**4

**示例 3 ：**

**输入：**nums = \[1\]

**输出：**1

**提示：**

-   `1 <= nums.length <= 3 * 104`
-   `-3 * 104 <= nums[i] <= 3 * 104`
-   除了某个元素只出现一次以外，其余每个元素均出现两次。

---

### 145. Number of 1 Bits · 简单

**链接（CN）：** https://leetcode.cn/problems/number-of-1-bits/description/  
**链接（EN）：** https://leetcode.com/problems/number-of-1-bits/

给定一个正整数 `n`，编写一个函数，获取一个正整数的二进制形式并返回其二进制表达式中 设置位 的个数（也被称为[汉明重量](https://baike.baidu.com/item/%E6%B1%89%E6%98%8E%E9%87%8D%E9%87%8F)）。

**示例 1：**

```
输入：n = 11
输出：3
解释：输入的二进制串 1011 中，共有 3 个设置位。
```

**示例 2：**

```
输入：n = 128
输出：1
解释：输入的二进制串 10000000 中，共有 1 个设置位。
```

**示例 3：**

```
输入：n = 2147483645
输出：30
解释：输入的二进制串 1111111111111111111111111111101 中，共有 30 个设置位。
```

**提示：**

-   `1 <= n <= 231 - 1`

**进阶**：

-   如果多次调用这个函数，你将如何优化你的算法？

---

### 146. Counting Bits · 简单

**链接（CN）：** https://leetcode.cn/problems/counting-bits/description/  
**链接（EN）：** https://leetcode.com/problems/counting-bits/

给你一个整数 `n` ，对于 `0 <= i <= n` 中的每个 `i` ，计算其二进制表示中 **`1` 的个数** ，返回一个长度为 `n + 1` 的数组 `ans` 作为答案。

**示例 1：**

```
输入：n = 2
输出：[0,1,1]
解释：
0 --> 0
1 --> 1
2 --> 10
```

**示例 2：**

```
输入：n = 5
输出：[0,1,1,2,1,2]
解释：
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

**提示：**

-   `0 <= n <= 105`

**进阶：**

-   很容易就能实现时间复杂度为 `O(n log n)` 的解决方案，你可以在线性时间复杂度 `O(n)` 内用一趟扫描解决此问题吗？
-   你能不使用任何内置函数解决此问题吗？（如，C++ 中的 `__builtin_popcount` ）

---

### 147. Reverse Bits · 简单

**链接（CN）：** https://leetcode.cn/problems/reverse-bits/description/  
**链接（EN）：** https://leetcode.com/problems/reverse-bits/

颠倒给定的 32 位有符号整数的二进制位。

**示例 1：**

**输入：**n = 43261596

**输出：**964176192

**解释：**

整数

二进制

43261596

00000010100101000001111010011100

964176192

00111001011110000010100101000000

**示例 2：**

**输入：**n = 2147483644

**输出：**1073741822

**解释：**

整数

二进制

2147483644

01111111111111111111111111111100

1073741822

00111111111111111111111111111110

**提示：**

-   `0 <= n <= 231 - 2`
-   `n` 为偶数

**进阶**: 如果多次调用这个函数，你将如何优化你的算法？

---

### 148. Missing Number · 简单

**链接（CN）：** https://leetcode.cn/problems/missing-number/description/  
**链接（EN）：** https://leetcode.com/problems/missing-number/

给定一个包含 `[0, n]` 中 `n` 个数的数组 `nums` ，找出 `[0, n]` 这个范围内没有出现在数组中的那个数。

**示例 1：**

**输入：**nums = \[3,0,1\]

**输出：**2

**解释：**`n = 3`，因为有 3 个数字，所以所有的数字都在范围 `[0,3]` 内。2 是丢失的数字，因为它没有出现在 `nums` 中。

**示例 2：**

**输入：**nums = \[0,1\]

**输出：**2

**解释：**`n = 2`，因为有 2 个数字，所以所有的数字都在范围 `[0,2]` 内。2 是丢失的数字，因为它没有出现在 `nums` 中。

**示例 3：**

**输入：**nums = \[9,6,4,2,3,5,7,0,1\]

**输出：**8

**解释：**`n = 9`，因为有 9 个数字，所以所有的数字都在范围 `[0,9]` 内。8 是丢失的数字，因为它没有出现在 `nums` 中。

**提示：**

-   `n == nums.length`
-   `1 <= n <= 104`
-   `0 <= nums[i] <= n`
-   `nums` 中的所有数字都 **独一无二**

**进阶：**你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?

---

### 149. Sum of Two Integers · 中等

**链接（CN）：** https://leetcode.cn/problems/sum-of-two-integers/description/  
**链接（EN）：** https://leetcode.com/problems/sum-of-two-integers/

给你两个整数 `a` 和 `b` ，**不使用** 运算符 `+` 和 `-` ​​​​​​​，计算并返回两整数之和。

**示例 1：**

```
输入：a = 1, b = 2
输出：3
```

**示例 2：**

```
输入：a = 2, b = 3
输出：5
```

**提示：**

-   `-1000 <= a, b <= 1000`

---

### 150. Reverse Integer · 中等

**链接（CN）：** https://leetcode.cn/problems/reverse-integer/description/  
**链接（EN）：** https://leetcode.com/problems/reverse-integer/

给你一个 32 位的有符号整数 `x` ，返回将 `x` 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 `[−231,  231 − 1]` ，就返回 0。

**假设环境不允许存储 64 位整数（有符号或无符号）。**

**示例 1：**

```
输入：x = 123
输出：321
```

**示例 2：**

```
输入：x = -123
输出：-321
```

**示例 3：**

```
输入：x = 120
输出：21
```

**示例 4：**

```
输入：x = 0
输出：0
```

**提示：**

-   `-231 <= x <= 231 - 1`

---
