from sorts.merge_sort import merge_sort as test_sort
#testar corretude
if __name__ == "__main__":
    print("-" * 50, "\nRunning the empty list test case")
    try:
        assert test_sort([]) == []
        print("Passed!")
    except:
        print("Failed!")
    print("-" * 50, "\nRunning the unitary list test case")
    try:
        assert test_sort([0]) == [0]
        print("Passed!")
    except:
        print("Failed!")
    print("-" * 50, "\nRunning the already sorted list test case")
    try:
        assert test_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        print("Passed!")
    except:
        print("Failed!")
    print("-" * 50, "\nTesting if the sort is not altering the original list")
    try:
        lst = [5, 4, 3, 2, 1]
        assert not test_sort(lst) == lst
        print("Passed!")
    except:
        print("Failed!")
    print("-" * 50)
    from random import random
    case = 1000
    failed=0
    i = 1
    print("Running  ", case, "test cases randomly:")
    while(i<case):
        arr = [i*random() for i in range(0, case)]
        arr_sorted = sorted(arr)
        i+=1
        try:
            assert test_sort(arr) == arr_sorted
        except:
            failed+=1
    print("Passed on", case-failed, "tests!")
    print("-" * 50)