def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap = gap // 2
