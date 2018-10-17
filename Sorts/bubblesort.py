def bubblesort(lst):
    n = len(lst)
    while(True):
        swapped=False
        for i in range(1,n):
            if(lst[i-1]>lst[i]):
                aux=lst.pop(i)
                lst.insert(i-1,aux)
                swapped=True
        if not swapped:
            return lst
