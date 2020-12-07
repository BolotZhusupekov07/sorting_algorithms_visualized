import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def bubble_sort(list_):
    if len(list_) == 1:
        return
    yield list_
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list_)-1):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
                swapped = True
            yield list_


def insertion_sort(list_):
    for i in range(1, len(list_)):
        insert_number = list_[i]
        j = i - 1
        while j >= 0 and list_[j] > insert_number:
            list_[j+1] = list_[j]
            j -= 1
            yield list_
        list_[j + 1] = insert_number
        yield list_


def selection_sort(list_):
    for i in range(len(list_)):
        lowest_value_index = i
        yield list_
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[lowest_value_index]:
                lowest_value_index = j
                yield list_
        list_[i], list_[lowest_value_index] = list_[lowest_value_index], list_[i]
        yield list_


def merge_sort(list_, left_index, right_index):
    if left_index >= right_index:
        return
    middle = (left_index + right_index) // 2
    yield from merge_sort(list_, left_index, middle)
    yield from merge_sort(list_, middle + 1, right_index)
    yield from merge(list_, left_index, right_index, middle)
    yield list_


def merge(list_, left_index, right_index, middle):
    left_copy = list_[left_index:middle + 1]
    right_copy = list_[middle + 1:right_index + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            list_[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1

        else:
            list_[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
        sorted_index += 1
        yield list_
    while left_copy_index < len(left_copy):
        list_[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1
        yield list_
    while right_copy_index < len(right_copy):
        list_[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1
        yield list_

        
def quick_sort(list_):                                             
    quick_sort2(list_, 0, len(list_) - 1)                          
                                                                   
                                                                   
def quick_sort2(list_, low, high):                                 
    if low < high:                                                 
        split_index = partition(list_, low, high)                  
        yield from quick_sort2(list_, low, split_index)            
        yield from quick_sort2(list_, split_index + 1, high)       
                                                                   
                                                                   
def partition(list_, low, high):                                   
    pivot = A[(low + high) // 2]                                   
    i = low - 1                                                    
    j = high + 1                                                   
    while True:                                                    
        i += 1                                                     
        while list_[i] < pivot:                                    
            i += 1                                                 
                                                                   
        j -= 1                                                     
        while A[j] > pivot:                                        
            j -= 1                                                 
                                                                   
        if i >= j:                                                 
            return j                                               
                                                                   
        list_[i], list_[j] = list_[j], list_[i]                    
        yield list_                                                

        
if __name__ == "__main__":

    try:
        Range = int(input('Write range: '))
        Algorithm = input('Pick sorting algorithm:''\n'
                          'B for Bubble sort''\n'
                          'S for Selection sort''\n'
                          'M for Merge sort''\n'
                          'I for Insertion sort''\n')
        A = [x for x in range(Range)]

        random.shuffle(A)

        if Algorithm == 'B':
            title = 'Bubble sort'
            generator = bubble_sort(A)
        elif Algorithm == 'I':
            title = 'Insertion sort'
            generator = insertion_sort(A)
        elif Algorithm == 'S':
            title = 'Selection sort'
            generator = selection_sort(A)
        elif Algorithm == 'M':
            title = 'Merge sort'
            generator = merge_sort(A, 0, len(A) - 1)

        fig, ax = plt.subplots()

        bar_rects = ax.bar(range(len(A)), A, align='edge')

        ax.set_xlim(0, Range)
        ax.set_ylim(0, int(1.05 * Range))

        iterations = [0]


        def update_fig(list_, rects, iteration):
            for rect, val in zip(rects, list_):
                rect.set_height(val)
            iteration[0] += 1


        anim = animation.FuncAnimation(fig, func=update_fig,
                                       fargs=(bar_rects, iterations),
                                       frames=generator, interval=1,
                                       repeat=False)
        plt.show()

    except ValueError:
        print('Please enter valid input')
    except NameError:
        print('Please enter valid sorting algorithm')
