# coding = utf-8
import random
import time


def shift_down(arr, index):
    """
    :param arr:
    :param index:
    :return:
    """
    l = len(arr)
    left_child = arr[2*index+1]

    if 2*index+2 < l and left_child < arr[2*index+2]:
        max_child = 2*index+2
    else:
        max_child = 2*index+1
    if arr[max_child] > arr[index]:
        arr[index], arr[max_child] = arr[max_child], arr[index]


def heap_sort(arr):
    """
    :param arr: list wait to sort
    :return sorted_arr: sorted_array
    """
    temp_arr = arr
    sorted_arr = []
    while len(temp_arr) >= 1:
        start = len(temp_arr)/2 - 1
        for i in range(start, -1, -1):
            shift_down(temp_arr, i)
        sorted_arr.append(temp_arr[0])
        temp_arr[0] = temp_arr[-1]
        del temp_arr[-1]
    return sorted_arr


if __name__ == '__main__':
    a = []
    for i in range(1000):
        a.append(random.randrange(-10000, 100))
    t = time.time()
    print heap_sort(a)[:100]
    print time.time() - t

