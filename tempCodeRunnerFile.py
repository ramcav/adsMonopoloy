mid = len(lst) // 2
    left_half = merge_sort(lst[:mid], key)
    right_half = merge_sort(lst[mid:], key)

    return merge(left_half, right_half, key)