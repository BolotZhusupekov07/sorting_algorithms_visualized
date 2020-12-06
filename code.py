def bubble_sort(list_):
    if len(list_):
        return
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list_)):
            if list_[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list_[i]
                swapped = True
            yield list_
            
            
            
