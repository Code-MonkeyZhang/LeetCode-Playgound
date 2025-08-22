from typing import List, Tuple

"""
题目简述：
给定两个字符串 s 和 t，'#' 表示退格（删除前一个字符）。
把 s 和 t 分别输入到空白编辑器后，判断两者得到的最终字符串是否相等。

示例：
s = "ab#c", t = "ad#c"  -> True   (两者都变成 "ac")
s = "ab##", t = "c#d#"  -> True   (两者都变成 "")
s = "a#c",  t = "b"     -> False  (分别变成 "c" 和 "b")
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # TODO: 在这里写你的解法（不要使用额外数组也是可选的进阶要求）
        # 要求：返回布尔值，表示最终是否相等
        result_1 = []
        result_2 = []

        s_length = len(s)
        t_length = len(t)

        for i in range(s_length):
            if s[i] == '#':
                if bool(result_1):
                    result_1.pop()
                continue
            result_1.append(s[i])

        for j in range(t_length):
            if t[j] == '#':
                if bool(result_2):
                    result_2.pop()
                continue
            result_2.append(t[j])

        return result_1 == result_2



# ------------------- 测试环境 -------------------
def run_tests():
    sol = Solution()

    # 预置的多组测试用例（已包含期望答案）
    # 为了避免“泄露思路”，这里不做期望值的计算，只给出硬编码的 expected
    tests: List[Tuple[str, str, bool, str]] = [
        # 来自题目示例
        ("ab#c", "ad#c", True, "示例1：两者都变为 'ac'"),
        ("ab##", "c#d#", True, "示例2：两者都变为 ''"),
        ("a#c",  "b",    False, "示例3：分别为 'c' 与 'b'"),

        # 基础与边界
        ("a##", "#", True, "都变为空"),
        ("#", "#", True, "都为空"),
        ("####", "##", True, "连续退格，仍为空"),
        ("abc", "abc", True, "无退格，完全相同"),
        ("abc", "ab", False, "无退格，长度不同"),

        # 退格相互抵消
        ("xy#z", "xz#z", True, "都变成 'xzz'"),
        ("xy#z#", "x#",  True, "都变成 'x' 然后退格为空"),

        # 前缀退格
        ("##a#b#c", "c", True, "前缀退格后只剩 'c'"),
        ("##abc#", "ab", True, "退格掉末尾 'c'"),

        # 更复杂交错
        ("a#b#c#d#e#f#g#h#", "", True, "交替添加并退格，最后为空"),
        ("nzp#o#g", "b#nzp#o#g", True, "头部插入并退格后相同"),
        ("bbbextm", "bbb#extm", False, "一个退格删掉 'b'，另一个没有"),

        # 极端/长退格块
        ("abc########", "####", True, "超量退格也不会变成负数，结果都空"),
        ("", "", True, "空串对空串（虽然实际输入保证长度>=1，此为健壮性检查）"),
    ]

    ok_cnt = 0
    for i, (s, t, expected, note) in enumerate(tests, 1):
        try:
            got = sol.backspaceCompare(s, t)
        except Exception as e:
            got = f"抛出异常: {repr(e)}"

        correct = (got == expected)
        if correct:
            ok_cnt += 1

        print(f"\nTest Case {i}: {note}")
        print(f"输入 s = {s!r}, t = {t!r}")
        print(f"期待值: {expected}")
        print(f"你的输出: {got}")
        print("结果:", "✅ 正确" if correct else "❌ 错误")

    print(f"\n通过情况：{ok_cnt}/{len(tests)} ✅")


if __name__ == "__main__":
    run_tests()
