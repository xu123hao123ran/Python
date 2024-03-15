def quick_sort(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # high游标左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        # low的游标右移
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    # 对low左边的元素进行排序
    quick_sort(alist, first, low - 1)
    # 对low右边的元素进行排序
    quick_sort(alist, low + 1, last)


if __name__ == '__main__':
    li = [90, 12, 34, 23, 41, 56, 14, 75, 68]
    print(li)
    n = len(li)
    quick_sort(li, 0, len(li)-1)
    print(li)
