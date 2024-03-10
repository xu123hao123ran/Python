def shell_sort(alist):
    n = len(alist)
    gap = n//2
    i = 1
    if alist[i] < alist[i-gap]:
        alist[i], alist[i-1] = alist[i-1], alist[i]
    else:
        print('1')