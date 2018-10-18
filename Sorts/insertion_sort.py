def insertion_sort(lst):
    arr_sorted = lst.copy()
    for i in range(1, len(arr_sorted)):
        value = arr_sorted[i]
        j = i
        while j > 0 and value < arr_sorted[j - 1]:
            arr_sorted[j] = arr_sorted[j - 1]
            j-=1
        arr_sorted[j] = value
    return arr_sorted