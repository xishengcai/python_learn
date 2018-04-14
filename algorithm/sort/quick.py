# coding=utf-8
import random
import time


def quick_sort(arr, l, r):
    if l < r:
        # 随机在arr[l...r]的范围中, 选择一个数值作为标定点pivot
        # random_index = random.randrange(l, r)
        # arr[l], arr[random_index] = arr[random_index], arr[l]
        i, j = l+1, r
        v = arr[l]
        while True:
            while arr[i] <= v and i < r:
                i += 1
            while arr[j] >= v and j > l:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                # arr[j] < v
                # 得到3个部分  v, <v arr[j],  >v
                break
        if l >= j:
            quick_sort(arr, j+1, r)
        else:
            arr[l], arr[j] = arr[j], arr[l]
            quick_sort(arr, l, j-1)
            quick_sort(arr, j+1, r)


if __name__ == '__main__':
    a = []
    for i in range(1000000):
        a.append(random.randrange(-10000, 100))
    # print "sort_before: ", a
    # a = [100,5,5,5,5,-1,-100,10,11,12,13]
    t = time.time()
    quick_sort(a, 0, len(a)-1)
    print time.time() - t
    print a[:10]



