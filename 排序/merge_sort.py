def merge_sort(alist):
    """
    归并排序
    :param alist: 混乱列表
    :return: 有序列表
    """
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


if __name__ == '__main__':
    li = [90, 12, 34, 23, 41, 56, 14, 75, 68]
    print(li)
    print(merge_sort(li))
