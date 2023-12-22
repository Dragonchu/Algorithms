# 递归遍历数组
from typing import List


def traverse(arr: List[int], i: int):
    if i == len(arr):
        print("遍历完最后一个元素")
        return
    # 前序位置
    print(f"前序: {arr[i]}->")
    traverse(arr, i + 1)
    # 后序位置
    print(f"后序: {arr[i]}->")


if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5]
    traverse(test_arr, 0)
