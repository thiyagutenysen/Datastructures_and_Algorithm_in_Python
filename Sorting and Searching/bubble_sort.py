array = [9, 2, 5, 4, 7, 6, 1, 3, 8, 0]


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return array


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array = swap(array, j, j+1)
    return array


print("Sorted array =", bubble_sort(array))
