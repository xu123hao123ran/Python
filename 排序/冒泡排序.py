def bubble_sort(alist):
    n = len(alist)
    for j in range(0, n - 1):
        for i in range(0, n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


if __name__ == '__main__':
    li = [90, 12, 34, 23, 41, 56, 14, 75, 68]
    print(li)
    bubble_sort(li)
    print(li)
