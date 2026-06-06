# LeetCode 202 — 快乐数
#
# 题目描述：编写一个算法来判断一个数 n 是不是快乐数。
# 「快乐数」定义为：对于一个正整数，每次将该数替换为它每个位置上的数字的平方和，
# 然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
#
# 示例 1：输入: n = 19 → 输出: true（1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1）
# 示例 2：输入: n = 2 → 输出: false

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        product = n
        while product not in seen:
            seen.append(product)

            digits = []
            while product != 0:
                digits.append(product % 10)
                product = product//10
            print(digits)

            for i in range(len(digits)):
                digits[i] = digits[i]**2

            product = sum(digits)
            if product == 1:
                return True

        return False

# 测试用例


def test_solution():
    sol = Solution()

    assert sol.isHappy(7) == False, "Test case 2 failed"

    # 测试用例 1
    assert sol.isHappy(19) == True, "Test case 1 failed"

    # 测试用例 2
    assert sol.isHappy(2) == False, "Test case 2 failed"

    # 可以添加更多测试用例

    print("All test cases passed!")


# 运行测试
test_solution()
