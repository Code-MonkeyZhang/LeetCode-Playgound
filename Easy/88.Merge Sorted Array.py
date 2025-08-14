"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

 
示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

示例 2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。

示例 3：
输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。
"""


class Solution:
    def merge(self, nums1, m, nums2, n):

        """
        直观解法是这样的, 
        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        先把nums2拼接到nums1后面,然后sort nums1.
        但是这样的做法效率不够高,排序至少需要O((m+n)log(m+n))
        
        更好的方法是用双指针将nums1填充,这样只需要遍历一次 复杂度是 O(m+n)
        """

        """ 直观解法 """
        # nums2_index = 0
        
        # for index in range(m,len(nums1)):
        #     nums1[index] = nums2[nums2_index]
        #     nums2_index += 1

        # nums1 = nums1.sort() # 注意这里不能用sorted(nums1)



        """ 双指针写法 """
        p1 = m - 1
        p2 = n - 1
        p = len(nums1) - 1

        """下面这个写法会导致p1是-1是仍然被访问,会造成问题"""
        # while p2 >= 0:
        #     if p1 >= 0 and nums1[p1] <= nums2[p2]:
        #         nums1[p] = nums2[p2]
        #         p2 -= 1
        #     else:
        #         nums1[p] = nums1[p1]
        #         p1 -= 1
            
        #     p -= 1

        """Best Answer"""
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            
            p -= 1
            
        




def test_merge_sorted_array():
    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(f"Test case 1: {nums1}")

    # Test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    print(f"Test case 2: {nums1}")

    # Test case 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(f"Test case 3: {nums1}")

    # Test case 3
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(f"Test case 3: {nums1}")


# Run the tests
test_merge_sorted_array()
