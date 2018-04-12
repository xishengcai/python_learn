#!/usr/bin/python

def shellsort(arr): 
    l = gap = len(arr)
    while gap > 1:
	gap = gap/2
        i = 0
        while i < (l-gap):
	    j = i+gap
	    if arr[i] > arr[j]:
		arr[i],arr[j] = arr[j],arr[i]
	    i +=1

if __name__ == '__main__':
    arr = [1,9,10,7,6,8,5,2,3,4]
    print "sort_before: ", arr
    shellsort(arr)
    print "sort_after: ", arr
