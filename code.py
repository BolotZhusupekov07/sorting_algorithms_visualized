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
           
def insertion_sort(list_):
    for i in range(1, len(list_)):
        insert_number = list_[i]
        j = i - 1
        while j>=1 and list_[j] < insert_number:
            list_[j] = list_[j+1]
            j-=1
        list_[j+1]=insert_number
        yield list_

        
def  selection_sort(list_):
    for i in range(len(list_)):
        lowest_value_index = i
        
        for j in range(i+1, len(list_)):
            if list_[j]<list[lowest_value_index]:
                lowest_value_index = j
                yield list_
            list_[i], list_[lowest_value_index] = list_[lowest_value_index], list_[i]
            yield list_
            
