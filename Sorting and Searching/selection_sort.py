array = [9, 2, 5, 4, 7, 6, 1, 3, 8, 0]


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return array


def selection_sort(array):
    for i in range(len(array)):
        min = array[i]
        min_index = i
        for j in range(i, len(array)):
            if min > array[j]:
                min = array[j]
                min_index = j
        if min_index != i:
            array = swap(array, i, min_index)
    return array


print("Sorted array =", selection_sort(array))
