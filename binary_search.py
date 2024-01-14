#! /usr/bin/python
# coding:utf-8
# Author:zhangjunyi
# date:2024/1/14

from typing import List


def binary_search_(array: List, target: int) -> any:
    left, right = 0, len(array)-1
    mid = left + (right-left)//2
    while left <= right:
        if arr[mid] == target:
            right = mid
        elif arr[mid] < target:
            left = mid
        elif arr[mid] > target:
            return mid
        mid = left + (right-left) // 2
    return -1


def get_ordered_arrays():
    array1 = [1, 3, 5, 7, 9]
    array2 = [2, 4, 6, 8, 10]
    array3 = [11, 13, 15, 17, 19]
    return [array1, array2, array3]


if __name__ == '__main__':
    # 调用函数获取有序数组列表
    ordered_arrays = get_ordered_arrays()
    # 输出每个有序数组
    for i, arr in enumerate(ordered_arrays, start=1):
        print(binary_search_(arr, 7))
        # print(binary_search_(arr, 8))
        # print(binary_search_(arr, 15))
