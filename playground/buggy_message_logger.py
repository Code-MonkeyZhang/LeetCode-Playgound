"""
Buggy Message Logger

一个聊天应用的消息持久化系统。消息逐条追加到内存数组，在某些时机执行 flush
将"新增消息"写入磁盘。系统维护一个 savedPtr 标记已写入的边界。

正确的 flush: 写入 messages[savedPtr:]，然后 savedPtr = len(messages)
Buggy flush:  写入 messages[savedPtr:]，但 savedPtr 始终为 0（声明为 const）

给定操作序列，求总共执行了多少次消息写入。

操作:
  "msg"   — 追加一条消息
  "flush" — 执行一次 flush（带有 bug）

示例:
  ops = ["msg", "msg", "flush", "msg", "flush"]
  输出: 5  (2 + 3)

  ops = ["msg", "flush"]
  输出: 1  (单次 flush 不产生重复)
"""

from typing import List


class Solution:
    def totalWrites(self, ops: List[str]) -> int:
        """
        模拟 buggy logger，返回总写入次数。

        因为 savedPtr 始终为 0，每次 flush 写入的消息数 = 当时 messages 数组的长度。
        所以只需要维护一个计数器，flush 时把当前消息总数加到结果里。

        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        msg_count = 0
        total = 0
        for op in ops:
            if op == "msg":
                msg_count += 1
            elif op == "flush":
                total += msg_count
        return total

    def totalWritesCorrect(self, ops: List[str]) -> int:
        """
        正确实现（savedPtr 会更新），返回总写入次数。
        每条消息恰好写入一次，所以结果 = "msg" 操作的数量。
        """
        return ops.count("msg")

    def wasteRatio(self, ops: List[str]) -> float:
        """
        返回浪费比例: (buggy写入次数 - 正确写入次数) / buggy写入次数
        """
        buggy = self.totalWrites(ops)
        correct = self.totalWritesCorrect(ops)
        if buggy == 0:
            return 0.0
        return (buggy - correct) / buggy


class BuggyLogger:
    """
    完整模拟版：跟踪每条消息被写入磁盘的次数。

    用于直观理解 bug 的影响——越早的消息被重复写入的次数越多。
    """

    def __init__(self):
        self.messages: List[str] = []
        self.disk: List[str] = []  # 磁盘上的所有写入（含重复）

    def add_message(self, content: str) -> None:
        self.messages.append(content)

    def flush(self) -> int:
        """执行一次 buggy flush，返回本次写入的消息数。"""
        written = 0
        for msg in self.messages:  # bug: 从 index 0 开始，不是从 savedPtr
            self.disk.append(msg)
            written += 1
        return written

    def message_frequency(self) -> dict:
        """统计磁盘上每条消息出现的次数。"""
        freq = {}
        for msg in self.disk:
            freq[msg] = freq.get(msg, 0) + 1
        return freq


# ============================================================
# 测试
# ============================================================

def test_solution():
    s = Solution()

    # 示例 1: 两次 flush，第二次全量重复
    assert s.totalWrites(["msg", "msg", "flush", "msg", "flush"]) == 5

    # 示例 2: 单次 flush，无重复
    assert s.totalWrites(["msg", "flush"]) == 1

    # 示例 3: 多次 flush
    ops = ["msg", "msg", "msg", "flush", "msg", "flush", "msg", "flush", "flush"]
    # 3 + 4 + 5 + 5 = 17
    assert s.totalWrites(ops) == 17

    # 正确实现的写入次数 = msg 操作数
    assert s.totalWritesCorrect(ops) == 5

    # 没有 flush
    assert s.totalWrites(["msg", "msg", "msg"]) == 0

    # 空 flush（没有消息时 flush）
    assert s.totalWrites(["flush", "flush"]) == 0

    print("All Solution tests passed!")


def test_logger_simulation():
    """模拟真实场景：用户发消息 + agent 多步处理触发多次 flush"""

    logger = BuggyLogger()

    # 模拟一次对话：用户消息 + agent 两步（工具调用 + 文字回复）
    logger.add_message("用户: 给我放首歌吧")       # step 0: 用户消息
    logger.flush()                                   # flush 1 (step_start)
    logger.add_message("assistant: [调用 show_pose]")  # step 1: 工具调用
    logger.add_message("assistant: [调用 play_music]") # step 1: 工具调用
    logger.flush()                                   # flush 2 (step_start of step 2)
    logger.add_message("assistant: 好的，正在播放～")   # step 2: 文字回复
    logger.flush()                                   # flush 3 (loop end)

    freq = logger.message_frequency()

    print(f"磁盘总写入次数: {len(logger.disk)}")
    print(f"实际唯一消息数: {len(logger.messages)}")
    print(f"浪费比例: {(len(logger.disk) - len(logger.messages)) / len(logger.disk) * 100:.1f}%")
    print()
    print("每条消息的重复次数:")
    for msg, count in freq.items():
        print(f"  {count}x  {msg}")

    # 验证: 用户消息出现 3 次（3 次 flush）
    assert freq["用户: 给我放首歌吧"] == 3
    # 验证: 最后的文字回复只出现 1 次（只在最后一次 flush 时才存在于 messages 中）
    assert freq["assistant: 好的，正在播放～"] == 1

    print("\nLogger simulation test passed!")


def test_real_world_scenario():
    """
    模拟真实数据中的 "你看看游戏媒体比如IGN吧" 出现 9 次的场景。
    说明那轮对话经历了 9 次 flush（agent 调了很多次工具）。
    """
    s = Solution()

    # 9 次 flush 意味着 agent 经历了约 8-9 个 step
    # 假设每次 step 产生 1-3 条新消息
    ops = ["msg"]                      # 用户消息
    ops += ["msg"] + ["flush"]         # step 1: 1 new msg, flush
    ops += ["msg", "msg"] + ["flush"]  # step 2: 2 new msgs, flush
    ops += ["msg"] + ["flush"]         # step 3: 1 new msg, flush
    ops += ["msg", "msg"] + ["flush"]  # step 4: 2 new msgs, flush
    ops += ["msg"] + ["flush"]         # step 5: 1 new msg, flush
    ops += ["msg", "msg"] + ["flush"]  # step 6: 2 new msgs, flush
    ops += ["msg"] + ["flush"]         # step 7: 1 new msg, flush
    ops += ["msg"] + ["flush"]         # step 8: 1 new msg, flush
    ops += ["msg"] + ["flush"]         # step 9: 1 new msg, flush (final)

    total_writes = s.totalWrites(ops)
    actual_msgs = s.totalWritesCorrect(ops)

    print(f"真实场景模拟 (9 步对话):")
    print(f"  实际消息数: {actual_msgs}")
    print(f"  磁盘写入数: {total_writes}")
    print(f"  用户消息重复次数: 9 (等于 flush 次数)")
    print(f"  浪费比例: {s.wasteRatio(ops) * 100:.1f}%")

    assert total_writes == 72  # 2+4+5+7+8+10+11+12+13
    assert actual_msgs == 13

    print(f"\n  (修正) 实际消息数: {actual_msgs}, 磁盘写入数: {total_writes}")
    print("\nReal world scenario test passed!")


if __name__ == "__main__":
    test_solution()
    print()
    test_logger_simulation()
    print()
    test_real_world_scenario()
