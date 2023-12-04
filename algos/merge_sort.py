# Merge sort algorithm

# Time Complexity: O(n log n) (n = len(lst))
def merge_sort(lst, key=lambda x: x):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid], key)
    right_half = merge_sort(lst[mid:], key)

    return merge(left_half, right_half, key)

# Time Complexity: O(n) (n = len(left) + len(right))
def merge(left, right, key):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if key(left[left_index]) > key(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged