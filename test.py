import unittest
import random


def bubble_sort(arr):
    if len(arr) == 1:
        return
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True


def insertion_sort(arr):
    for i in range(len(arr)):
        insert_num = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > insert_num:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = insert_num


def selection_sort(arr):
    for i in range(len(arr)):
        lowest_value_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_value_index]:
                lowest_value_index = j
        arr[i], arr[lowest_value_index] = arr[lowest_value_index], arr[i]


def merge(arr, left_index, right_index, middle):
    left_copy = arr[left_index:middle + 1]
    right_copy = arr[middle + 1: right_index + 1]

    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            arr[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        else:
            arr[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
        sorted_index += 1
    while left_copy_index < len(left_copy):
        arr[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1
    while right_copy_index < len(right_copy):
        arr[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1


def merge_sort(arr, left_index, right_index):
    if left_index >= right_index:
        return
    middle = (right_index + left_index) // 2
    merge_sort(arr, left_index, middle)
    merge_sort(arr, middle + 1, right_index)
    merge(arr, left_index, right_index, middle)


def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - 1] > temp:
                arr[j] = arr[j - 1]
                j -= 1
            arr[j] = temp
        gap //= 2


def odd_even_sort(arr):
    is_sorted = 0
    while is_sorted == 0:
        is_sorted = 1
        for i in range(0, len(arr) - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = 0
        for i in range(1, len(arr) - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = 0
    return


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
        heapify(list_, heap_size, largest)


def heap_sort(list_):
    heap_size = len(list_)
    for i in range(heap_size, -1, -1):
        heapify(list_, heap_size, i)
    for i in range(heap_size - 1, 0, -1):
        list_[0], list_[i] = list_[i], list_[0]
        heapify(list_, i, 0)


test_list_1 = [x for x in range(10)]
test_list_2 = [x for x in range(10)]
test_list_3 = [x for x in range(10)]
test_list_4 = [x for x in range(10)]
test_list_5 = [x for x in range(10)]
test_list_6 = [x for x in range(10)]
test_list_7 = [x for x in range(10)]


random.shuffle(test_list_1)
random.shuffle(test_list_2)
random.shuffle(test_list_3)
random.shuffle(test_list_4)
random.shuffle(test_list_5)
random.shuffle(test_list_6)
random.shuffle(test_list_7)


bubble_sort(test_list_1)
insertion_sort(test_list_2)
selection_sort(test_list_3)
merge_sort(test_list_4, 0, len(test_list_4) - 1)
shell_sort(test_list_5)
heap_sort(test_list_6)
odd_even_sort(test_list_7)


class Test(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertListEqual(test_list_1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_insertion_sort(self):
        self.assertListEqual(test_list_2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_selection_sort(self):
        self.assertListEqual(test_list_3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_merge_sort(self):
        self.assertListEqual(test_list_4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_shell_sort(self):
        self.assertListEqual(test_list_5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_heap_sort(self):
        self.assertListEqual(test_list_6, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_odd_even_sort(self):
        self.assertListEqual(test_list_7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()
