def insertionsort(lst):
    sorted=[lst[0]]
    for item in lst:
        for i in sorted:
            if item < i:
                sorted.insert(sorted.index(i)-1,item)