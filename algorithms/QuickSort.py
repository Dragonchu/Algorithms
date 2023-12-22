from typing import List


def partition(nums: List[int], low: int, high: int) -> int:
    pass


def sort(nums: List[int], low: int, high: int):
    print("QuickSort start")
    # 前序遍历
    # 通过交换元素构建分界点p
    p = partition(nums, low, high)
    sort(nums, low, p - 1)
    sort(nums, p + 1, high)
    print("QuickSort end")


if __name__ == '__main__':
    sort([1, 2, 3], 0, 3)
