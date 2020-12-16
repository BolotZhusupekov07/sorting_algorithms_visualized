import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import *
from tkinter import ttk


def bubble_sort(list_):
    if len(list_) == 1:
        return
    yield list_
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list_) - 1):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
                swapped = True
            yield list_


def insertion_sort(list_):
    for i in range(1, len(list_)):
        insert_number = list_[i]
        j = i - 1
        while j >= 0 and list_[j] > insert_number:
            list_[j + 1] = list_[j]
            j -= 1
            yield list_
        list_[j + 1] = insert_number
        yield list_


def shell_sort(list_):
    n = len(list_)
    gap = n // 2
    yield list_
    while gap > 0:
        for i in range(gap, n):
            temp = list_[i]
            j = i
            while j >= gap and list_[j - 1] > temp:
                list_[j] = list_[j - 1]
                yield list_
                j -= 1
            list_[j] = temp
            yield list_
        gap //= 2


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


def odd_even_sort(list_):
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        for i in range(0, len(list_) - 1, 2):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
                isSorted = 0
                yield list_
        for i in range(1, len(list_) - 1, 2):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
                isSorted = 0
                yield list_
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


def heapify(list_, heap_size, index):
    largest = index
    left = index * 2 + 1
    right = index * 2 + 2

    if left < heap_size and list_[largest] < list_[left]:
        largest = left
    if right < heap_size and list_[largest] < list_[right]:
        largest = right

    if largest != index:
        list_[index], list_[largest] = list_[largest], list_[index]
        yield list_
        yield from heapify(list_, heap_size, largest)


def heap_sort(list_):
    heap_size = len(list_)
    for i in range(heap_size, -1, -1):
        yield from heapify(list_, heap_size, i)
    for i in range(heap_size - 1, 0, -1):
        list_[0], list_[i] = list_[i], list_[0]
        yield from heapify(list_, i, 0)
        yield list_


class getRange:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x400')
        self.root.title('Visualize')
        self.root.resizable(0, 0)
        self.alg = StringVar()
        self.var_size = StringVar()
        self.label_size = Label(self.root, textvariable=self.var_size)
        self.var_size.set('Choose the size:')
        self.label_size.place(x=35, y=8)
        self.size_tuple = (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                           30, 40, 50, 60, 70, 80, 90, 100)
        self.size_ = IntVar()
        self.size_box = ttk.Combobox(self.root, width=15,
                                     textvariable=self.size_,
                                     state='readonly',
                                     height=12)
        self.size_box['values'] = self.size_tuple
        self.size_box.place(x=35, y=30)
        self.size_box.bind('<<ComboboxSelected>>', self.size)

        self.var_alg = StringVar()
        self.label_alg = Label(self.root, textvariable=self.var_alg)
        self.label_alg.place(x=198, y=8)
        self.var_alg.set('Choose the algorithm:')
        self.box2 = ttk.Combobox(self.root, width=20, textvariable=self.alg,
                                 state='readonly', height=8)

        self.box_values = ('Bubble Sort', 'Insertion Sort', 'Selection Sort',
                           'Merge Sort', 'Shell Sort', 'Heap Sort',
                           'Odd-Even Sort')
        self.box2['values'] = self.box_values
        self.box2.bind('<<ComboboxSelected>>', self.sort_alg)
        self.box2.place(x=200, y=30, width=150)
        self.butt = Button(self.root, text='Animate', command=self.Entry, relief=GROOVE)
        self.butt.place(x=240, y=350, width=60, height=25)
        self.butt2 = Button(self.root, text='Cancel', command=self.root.destroy, relief=GROOVE)
        self.butt2.place(x=310, y=350, width=60, height=25)

        self.Algorithm = None
        self.temp = None
        self.Range = None
        self.root.mainloop()

    def sort_alg(self, event):
        self.Algorithm = self.box2.get()

    def size(self, event):
        self.temp = self.size_box.get()
        self.Range = int(self.temp)

    def Entry(self):
        try:
            self.animate()
        except TypeError:
            pass

    def animate(self):
        A = [x for x in range(self.Range)]
        random.shuffle(A)
        if self.Algorithm == 'Bubble Sort':
            title = 'Bubble Sort'
            generator = bubble_sort(A)
        elif self.Algorithm == 'Insertion Sort':
            title = 'Insertion Sort'
            generator = insertion_sort(A)
        elif self.Algorithm == 'Selection Sort':
            title = 'Selection Sort'
            generator = selection_sort(A)
        elif self.Algorithm == 'Merge Sort':
            title = 'Merge Sort'
            generator = merge_sort(A, 0, len(A) - 1)
        elif self.Algorithm == 'Heap Sort':
            title = 'Heap Sort'
            generator = heap_sort(A)
        elif self.Algorithm == 'Shell Sort':
            title = 'Shell Sort'
            generator = shell_sort(A)
        elif self.Algorithm == 'Odd-Even Sort':
            title = 'Odd-Even Sort'
            generator = odd_even_sort(A)

        fig, ax = plt.subplots()
        title_ = plt.title(title)
        bar_ = ax.bar(range(len(A)), A, align='edge', color='green')
        ax.set_xlim(0, self.Range)
        ax.set_ylim(0, int(1.05 * self.Range))

        iterations = [0]

        def update_fig(list_, rect, iteration):
            for bar_rect, val in zip(rect, list_):
                bar_rect.set_height(val)
            iteration[0] += 1

        anim = animation.FuncAnimation(fig, func=update_fig,
                                       fargs=(bar_, iterations),
                                       frames=generator, interval=5,
                                       repeat=False)
        plt.show()


getRange()
