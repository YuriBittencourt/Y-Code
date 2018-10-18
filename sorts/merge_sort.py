def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    a = merge_sort(lst[:int(len(lst)/2)])
    b = merge_sort(lst[int(len(lst)/2):])
    merged = __merge(a, b)
    return merged


def __merge(arr1, arr2):
    merged = []
    while arr1 != [] and arr2 != []:
        if arr1[0] <= arr2[0]:
            merged.append(arr1.pop(0))
        else:
            merged.append(arr2.pop(0))
    return merged + arr1 + arr2
