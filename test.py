import unittest


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
    while left_copy_index < len(left_copy) and right_copy_index < len(right_index):
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
    merge_sort(arr, left_index, middle + 1)
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


test_list_1 = [5, 8, 7, 1, 2, 3, 5, 6, 2, 1, 0, 5, 9, 3, 2, 3]
bubble_sort(test_list_1)
test_list_2 = [78, 9, 52, 1, 5, 9, 8, 9, 86, 2, 3, 4, 5, 7, 2, 3, 6]
insertion_sort(test_list_2)
test_list_3 = [9, 4, 5, 6, 3, 1, 4, 8, 7, 89, 12, 36, 10, 15, 7, 0]
selection_sort(test_list_3)


class Test(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertListEqual(test_list_1, [0, 1, 1, 2, 2, 2, 3, 3, 3, 5, 5, 5, 6, 7, 8, 9])

    def test_insertion_sort(self):
        self.assertListEqual(test_list_2, [1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 9, 52, 78, 86])

    def test_selection_sort(self):
        self.assertListEqual(test_list_3, [0, 1, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10, 12, 15, 36, 89])


if __name__ == '__main__':
    unittest.main()
