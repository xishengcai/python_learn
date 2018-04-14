# coding=utf-8
import random
import time


def sort_merge(arr):
    """
    Merge Sort是我们学习的第一个O(nlogn)复杂度的算法
    可以在1秒之内轻松处理100万数量级的数据
    注意：不要轻易尝试使用SelectionSort, InsertionSort或者BubbleSort处理100万级的数据
    否则，你就见识了O(n^2)的算法和O(nlogn)算法的本质差异：）
    :param arr:
    :return:
    """
    if len(arr) <= 1:
        return arr
    len_ = len(arr)
    mid = len_ / 2
    left = sort_merge(arr[:mid])
    right = sort_merge(arr[mid:])
    return merge(left, right)


def merge(left, right):
    arr = []
    i = j = 0   # i is left's index, j is right's index
    while i < len(left) or j < len(right):
        if i == len(left):
            arr.append(right[j])
            j += 1
        elif j == len(right):
            arr.append(left[i])
            i += 1
        elif left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
    return arr


if __name__ == '__main__':
    a = []
    for i in range(10000000):
        a.append(random.randrange(1, 100))
    # print "sort_before: ", a
    # a = [100,5,5,5,5,-1,-100,10,11,12,13]
    t = time.time()
    print sort_merge(a)[:100]
    print time.time() - t
