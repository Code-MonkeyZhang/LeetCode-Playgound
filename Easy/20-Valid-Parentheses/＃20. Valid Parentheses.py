# LeetCode 20 — 有效的括号
#
# 题目描述：给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判断字符串是否有效。
# 有效字符串需满足：左括号必须用相同类型的右括号闭合，左括号必须以正确的顺序闭合，每个右括号都有一个对应的相同类型的左括号。
#
# 示例 1：输入: s = "()" → 输出: true
# 示例 2：输入: s = "()[]{}" → 输出: true
# 示例 3：输入: s = "(]" → 输出: false

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            # 如果是左括号
            if char not in mapping:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if mapping[char] != top:
                    return False

        return len(stack) == 0


def run_tests():
    solution = Solution()
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "(((",
        ")))",
        ""
    ]

    for i, case in enumerate(test_cases, 1):
        result = solution.isValid(case)
        print(f"Test case {i}: '{case}' -> {'Valid' if result else 'Invalid'}")


# Run the tests
if __name__ == "__main__":
    run_tests()
