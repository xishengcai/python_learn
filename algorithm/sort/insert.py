#!/usr/bin/python

def insert(arr):
    l = len(arr) - 1
    j = 0
    for i in range(l):
	j = i+i
        for k in range(i):
	    if arr[j] <  arr[k]:
		arr[j], arr[k] = arr[k], arr[j]

if __name__ == '__main__':
    import random
    arr = []
    for i in range(100):
	arr.append(random.randint(100))
    print arr
    insert(arr)
    print arr
