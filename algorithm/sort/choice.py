#!/usr/bin/python
import time
import random


def choice(arr):
    l = len(arr)
    j = 0
    for i in range(l):
        j = i+1
        for k in range(j, l):
            if arr[i] > arr[k]:
                arr[i], arr[k] = arr[k], arr[i]


if __name__ == '__main__':
    a =[]
    for i in range(100000):
        a.append(random.randrange(-100, 200))
    t = time.time()
    choice(a)
    print time.time() - t
