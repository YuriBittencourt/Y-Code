def mergesort(lst):
    if(len(lst)<=1):
        return lst
    a = mergesort(lst[:int(len(lst)/2)])
    b = mergesort(lst[int(len(lst)/2):])
    merged = __merge(a,b)
    return merged


def __merge(arr1, arr2):
    merged = []
    while(arr1!=[] and arr2!=[]):
        if(arr1[0] <= arr2[0]):
            merged.append(arr1.pop(0))
        else:
            merged.append(arr2.pop(0))
    return merged + arr1 + arr2

#testar corretude
if __name__ == "__main__":
    from random import random
    case = 1000
    while(case):
        case-=1
        arr = [i*random() for i in range(0, case)]
        arr_sorted = sorted(arr)
        assert mergesort(arr) == arr_sorted

