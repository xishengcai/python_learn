#!/usr/bin/python


def insert(arr):
    '''
    last situation is [0,1,2,3,4,5....len-2] , [len-1]
    :param arr: array of wait to sort
    :return:
    '''
    l = len(arr) - 1
    for i in range(l):
        k = i+1
        while k > 0:
            if arr[k] < arr[k-1]:
                arr[k], arr[k-1] = arr[k-1], arr[k]
                k -= 1
            else:
                break


if __name__ == '__main__':
    import random
    arr = []
    for i in range(100000):
        arr.append(random.randrange(-100, 100))
    # print arr
    insert(arr)
    print arr[:100]
