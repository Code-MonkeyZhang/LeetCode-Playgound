"""
题目描述：
给定一个整数数组，请你实现快速排序，将数组按升序排序。

快速排序思路：
- 选择一个“基准值”（pivot）。
- 将数组分成两部分：比 pivot 小的，和比 pivot 大的。
- 递归地对这两部分分别排序，再合并。

示例：
输入: [3, 6, 8, 10, 1, 2, 1]
输出: [1, 1, 2, 3, 6, 8, 10]

输入: [5, 2, 9, 1, 5, 6]
输出: [1, 2, 5, 5, 6, 9]
"""

# ========== 你的函数 ========== #
def quick_sort(arr):
    # TODO: 在这里实现快速排序
    return arr


# ========== 测试环境 ========== #
def run_test_case(test_input, expected):
    print("输入：", test_input)
    output = quick_sort(test_input[:])  # 用切片避免修改原始输入
    print("期望输出：", expected)
    print("实际输出：", output)
    print("是否正确：", output == expected)
    print("-" * 40)


if __name__ == "__main__":
    # 每个测试用例单独列出，方便断点调试
    run_test_case([3, 6, 8, 10, 1, 2, 1], [1, 1, 2, 3, 6, 8, 10])
    run_test_case([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9])
    run_test_case([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    run_test_case([], [])
    run_test_case([10], [10])
    run_test_case([2, 2, 1, 1], [1, 1, 2, 2])
