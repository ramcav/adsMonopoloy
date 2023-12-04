import random

# Time Complexity: O(n) (n = len(arr))
def fisher_yates_shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr