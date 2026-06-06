"""
题目描述：
给定一个整数数组，请你实现冒泡排序，将数组按升序排序。

冒泡排序思路：
- 从左到右，依次比较相邻的两个元素，如果前者大于后者，则交换它们。
- 每一轮“冒泡”操作会把当前未排序部分中最大的元素移动到末尾。
- 重复 n-1 轮，直到数组有序。

示例：
输入: [5, 1, 4, 2, 8]
输出: [1, 2, 4, 5, 8]

输入: [3, 2, 1]
输出: [1, 2, 3]
"""

# ========== 你的函数 ========== #
def bubble_sort(arr):
    # TODO: 在这里实现冒泡排序

    n = len(arr)
    for i in range(n):
        for j in range(0,n-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr


# ========== 测试环境 ========== #
def run_test_case(test_input, expected):
    print("输入：", test_input)
    output = bubble_sort(test_input[:])  # 用切片避免修改原始输入
    print("期望输出：", expected)
    print("实际输出：", output)
    print("是否正确：", output == expected)
    print("-" * 40)


if __name__ == "__main__":
    # 每个测试用例单独列出，方便断点调试
    run_test_case([5, 1, 4, 2, 8], [1, 2, 4, 5, 8])
    run_test_case([3, 2, 1], [1, 2, 3])
    run_test_case([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    run_test_case([], [])
    run_test_case([10], [10])
    run_test_case([2, 2, 1, 1], [1, 1, 2, 2])
