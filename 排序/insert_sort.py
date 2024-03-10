def insert_sort(alist):
    for j in range(1, len(alist)):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


if __name__ == '__main__':
    li = [94, 12, 34, 45, 16, 54, 68, 36, 76]
    print(li)
    insert_sort(li)
    print(li)