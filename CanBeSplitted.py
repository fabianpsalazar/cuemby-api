def canBeSplitted(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return -1
    for i in range(len(arr)):
        if sum(arr[:i+1]) == sum(arr[i+1:]):
            return 1
    return -1
