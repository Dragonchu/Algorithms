from typing import List


def partition(nums: List[int], low: int, high: int) -> int:
    pass


def sort(nums: List[int], low: int, high: int):
    # 前序遍历
    # 通过交换元素构建分界点p
    p = partition(nums, low, high)
    sort(nums, low, p - 1)
    sort(nums, p + 1, high)
