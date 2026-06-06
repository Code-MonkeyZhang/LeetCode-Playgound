# LeetCode 125 — 验证回文串
#
# 题目描述：给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1：输入: s = "A man, a plan, a canal: Panama" → 输出: true
# 示例 2：输入: s = "race a car" → 输出: false

"""
LeetCode 125: Valid Palindrome

Problem (brief):
Given a string s, return True if, after converting all uppercase letters to lowercase
and removing all non-alphanumeric characters, it reads the same forward and backward;
otherwise return False.

Simple Examples:
1) s = "A man, a plan, a canal: Panama"  -> True
2) s = "race a car"                      -> False
3) s = " "                               -> True   (becomes "" after cleanup)
"""

from typing import Any


# === Your solution goes here ===
# Paste your Solution class below. Keep the class name and method signature.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TODO: Implement your solution.

        """
        思路:
        - 两个指正一头一尾, 互相比较之后向中间靠拢
        - 停止条件: left < right
        """
        # amanaplanacanalpanama

        """
        edge cases:
        - 空的直接返回True
        """
        s = "".join(ch.lower() for ch in s if ch.isalnum())

        if s == "":
            return True


# === Test runner ===

_total = 0
_passed = 0


def _print_case_header(title: str, s_in: str, expected: bool) -> None:
    print("=" * 64)
    print(title)
    print("-" * 64)
    print(f"Input s: {repr(s_in)}")
    print(f"Expected: {expected}")


def _print_case_result(actual: Any, ok: bool) -> None:
    print(f"Actual:   {actual}")
    print(f"Correct:  {ok}")


def run_test_case(title: str, s_in: str, expected: bool) -> None:
    global _total, _passed
    _total += 1

    _print_case_header(title, s_in, expected)

    try:
        result = Solution().isPalindrome(s_in)
        ok = result == expected
        _print_case_result(result, ok)
        if ok:
            _passed += 1
    except Exception as e:
        _print_case_result(f"<raised {type(e).__name__}: {e}>", False)


def print_summary() -> None:
    print("=" * 64)
    print(f"Passed: {_passed}/{_total} tests")
    if _passed == _total and _total > 0:
        print("All green! 🎉 Great job — on to the next one!")
    elif _passed == 0:
        print("No worries — set a breakpoint on a case, step through, and try again.")
    else:
        print("Nice progress! Review the failing cases and iterate.")


if __name__ == "__main__":
    # --- Separate test cases (not packed into a single array) ---
    # Put breakpoints on individual run_test_case calls as needed.

    # Case 1: Example from prompt
    run_test_case(
        title="Case 1: Classic phrase with punctuation and spaces",
        s_in="A man, a plan, a canal: Panama",
        expected=True,
    )

    # Case 2: Example from prompt
    run_test_case(
        title="Case 2: Not a palindrome after cleanup",
        s_in="race a car",
        expected=False,
    )

    # Case 3: Example from prompt (whitespace only)
    run_test_case(
        title="Case 3: Only spaces",
        s_in=" ",
        expected=True,
    )

    # Case 4: Mixed letters and digits, palindromic after cleanup
    run_test_case(
        title="Case 4: Alphanumeric mix",
        s_in="No 'x' in Nixon 20202",
        expected=True,
    )

    # Case 5: Non-palindrome with symbols
    run_test_case(
        title="Case 5: Symbols scattered, not palindrome",
        s_in="(ab@c) d c!b a?",
        expected=False,
    )

    # Case 6: Single character
    run_test_case(
        title="Case 6: Single character",
        s_in="Z",
        expected=True,
    )

    # Case 7: Long string with only non-alphanumerics
    run_test_case(
        title="Case 7: All punctuation",
        s_in="!@#$%^&*()_+[]{}|;:',.<>/?`~",
        expected=True,
    )

    # Case 8: Even length palindrome
    run_test_case(
        title="Case 8: Even-length",
        s_in="abBA",
        expected=True,
    )

    # Case 9: Uneven with trailing punctuation
    run_test_case(
        title="Case 9: Trailing punctuation",
        s_in="Red rum, sir, is murder!!!",
        expected=True,
    )

    # Case 10: Clearly not palindrome after cleanup
    run_test_case(
        title="Case 10: Straightforward non-palindrome",
        s_in="leetcode",
        expected=False,
    )

    # Print final summary
    print_summary()
