def bubble_sort(lst):
    arr_sorted = lst.copy()
    while(True):
        swapped=False
        for i in range(1,len(arr_sorted)):
            if(arr_sorted[i-1]>arr_sorted[i]):
                aux=arr_sorted.pop(i)
                arr_sorted.insert(i-1,aux)
                swapped=True
        if not swapped:
            return arr_sorted