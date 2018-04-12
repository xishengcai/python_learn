#!/usr/bin/python

def choice(arr):
    l = len(arr)
    j = 0
    for i in range(l):
	j = i+1
        for k in range(j, l):
	    if arr[i] > arr[k]:
		arr[i], arr[k] = arr[k], arr[i]


if __name__ == '__main__':
    a = [1,2,-3,-4,-2,10,11]
    print a
    choice(a)
    print a
