import time
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
            

def merge_sort(list_, left_index, right_index):
    if left_index>=right_index:
        return 
    middle = (left_index + right_index)//2
    yield from merge_sort(list_, left_index, middle)
    yield from merge_sort(list_, middle+1, right_index)
    yield from merge(list_, left_index, right_index, middle)
    yield list_
    
def merge(list_, left_index, right_index, middle):
    left_copy = list_[left_index:middle+1]
    right_copy = list_[middle+1:right_index+1]
    
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_index_index]:
            list_[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
            
        else:
            list_[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
        sorted_index += 1
        yield list_
    while left_copy_index == len(left_copy):
        list_[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1
        yield list_
    while right_copy_index == len(right_copy):
        list_[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1
        yield list_
              
Range = int(input())
Algorigthm = input()


list_ = [x +1 for x in range(Range)]
random.seed(time.time())
random.shuffle(list_)


bar_rects = ax.bar(range(len(list_), list_, align = 'edge')
                   


fig, ax = plt.subplots()
ax.title(title)

