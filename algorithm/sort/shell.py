# coding=utf-8


def shellsort(arr): 
    l = gap = len(arr)
    while gap > 1:
        gap = gap/2   # 希尔增量
        for k in range(gap):   # 循环gap次
            for i in range(k+gap, l-k, gap):
                # 对arr[i] arr[i+gap*1]  arr[i+gap*2] arr[i+gap*3] 序列使用插入排序
                for j in range(i, k, -gap):
                    if arr[j] < arr[j-gap]:
                        arr[j], arr[j-gap] = arr[j-gap], arr[j]
                    else:
                        break


if __name__ == '__main__':
    import random
    a = []
    for i in range(100000):
        a.append(random.randrange(-10000, 20000))
    import time
    print time.time()
    shellsort(a)
    print time.time()
    print a[:1000]

